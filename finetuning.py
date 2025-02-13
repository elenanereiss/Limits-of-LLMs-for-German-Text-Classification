import sys
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from datetime import datetime as t
import json
import csv
import pandas as pd
import numpy as np
import torch
import torch.nn.functional as F
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import f1_score, classification_report, accuracy_score
from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model


# https://github.com/adidror005/youtube-videos/blob/main/LLAMA_3_Fine_Tuning_for_Sequence_Classification_Actual_Video.ipynb
from datasets import DatasetDict, Dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding,
    EarlyStoppingCallback
)

from description import datasets

import warnings
warnings.filterwarnings('ignore')

def main():
    class CustomTrainer(Trainer):
        def __init__(self, *args, class_weights=None, **kwargs):
            super().__init__(*args, **kwargs)
            # Ensure label_weights is a tensor
            if class_weights is not None:
                #            self.class_weights = torch.tensor(class_weights, dtype=torch.float32).to(self.args.device) # old param -> error with new version of transformers
                self.class_weights = class_weights.type(dtype=torch.float32).clone().detach().to(self.args.device)
            else:
                self.class_weights = None

        # def compute_loss(self, model, inputs, return_outputs=False): # old param -> error with new version of transformers
        def compute_loss(self, model, inputs, return_outputs=False, num_items_in_batch=None):
            # Extract labels and convert them to long type for cross_entropy
            labels = inputs.pop("labels").long()

            # Forward pass
            outputs = model(**inputs)

            # Extract logits assuming they are directly outputted by the model
            logits = outputs.get('logits')

            # Compute custom loss with class weights for imbalanced data handling
            if self.class_weights is not None:
                loss = F.cross_entropy(logits, labels, weight=self.class_weights)
            else:
                loss = F.cross_entropy(logits, labels)

            return (loss, outputs) if return_outputs else loss
    #        return (loss(logits, labels), outputs) if return_output else loss(logits, labels) # old param -> error with new version of transformers

    def llama_preprocessing_function(examples):
        # Tokenize the text
        tokenized_examples = tokenizer(examples['text'], truncation=True, max_length=MAX_LEN)

#        # Map labels to numerical values
#        tokenized_examples['label'] = ClassLabels.str2int(examples[task])
        return tokenized_examples

    def compute_metrics(eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=1)
        print("\n", classification_report(labels, predictions, zero_division=0, digits=4))
        return {'accuracy': accuracy_score(predictions, labels),
                'macro f1': f1_score(predictions, labels, average="macro", zero_division=0)}

    def read_dataset(file):
        if ".csv" in file:
            data = pd.read_csv(file)
        elif ".txt" in file:
            data = pd.read_csv(file, sep='\t', header=None, quoting=csv.QUOTE_NONE)
        elif '.xlsx' in file:
            data = pd.read_excel(file)
        else:
            print('Error: unknown file format.')
            data=None
        return data



    # Input model name
    checkpoint = sys.argv[1]

    print(checkpoint)

    # collect results of all datasets and tasks
    results={}

    for dataset in datasets.keys():
        print(dataset)
        results[dataset] = {}
        for task in datasets[dataset]["tasks"]:
            print(task)
            results[dataset][task] = {}


            # Read the dataset
            train=read_dataset(datasets[dataset]["file"]["train"])
            train.columns = datasets[dataset]["columns"]
            train[task]=train[task].astype('category')
            train['target']=train[task].cat.codes
            category_map = {code: category for code, category in enumerate(train[task].cat.categories)}
            num_labels=len(train[task].cat.categories)


            df_test=read_dataset(datasets[dataset]["file"]["test"])
            df_test.columns = datasets[dataset]["columns"]
            df_test[task]=df_test[task].astype('category')
            df_test['target']=df_test[task].cat.codes

            col_to_delete = datasets[dataset]["columns"] # delete all columns except target


            # Create a validation split (10% of whole data) using scikit learn
            X=train.to_numpy()
            y=train[task].to_numpy()
            sss = StratifiedShuffleSplit(n_splits=1, test_size=0.125, random_state=0)

            new_columns=datasets[dataset]["columns"] + ["target"]
            for i, (train_index, test_index) in enumerate(sss.split(X, y)):

                df_train = pd.DataFrame(columns=new_columns)
                df_train = pd.concat([df_train, pd.DataFrame(X[train_index], columns=df_train.columns)], ignore_index=True)
                df_valid = pd.DataFrame(columns=new_columns)
                df_valid = pd.concat([df_valid, pd.DataFrame(X[test_index], columns=df_valid.columns)], ignore_index=True)

            # Converting pandas DataFrames into Hugging Face Dataset objects:
            dataset_train = Dataset.from_pandas(df_train)
            # Shuffle the training dataset
            dataset_train_shuffled = dataset_train.shuffle(seed=42)  # Using a seed for reproducibility
            dataset_val = Dataset.from_pandas(df_valid)
            dataset_test = Dataset.from_pandas(df_test)

            # Huggingface dataset object
            hf_dataset = DatasetDict({
                'train': dataset_train_shuffled,
                'val': dataset_val,
                'test': dataset_test
            })

            # calculate class weights based on inverse value counts
            class_weights=(1/df_train.target.value_counts(normalize=True).sort_index()).tolist()
            class_weights=torch.tensor(class_weights)
            class_weights=class_weights/class_weights.sum()

            quantization_config = BitsAndBytesConfig(
                load_in_4bit = True, # enable 4-bit quantization
                bnb_4bit_quant_type = 'nf4', # information theoretically optimal dtype for normally distributed weights
                bnb_4bit_use_double_quant = True, # quantize quantized weights //insert xzibit meme
                bnb_4bit_compute_dtype = torch.bfloat16 # optimized fp format for ML
            )

            lora_config = LoraConfig(
                r = 16, # the dimension of the low-rank matrices
                lora_alpha = 8, # scaling factor for LoRA activations vs pre-trained weight activations
                target_modules = ['q_proj', 'k_proj', 'v_proj', 'o_proj'],
                lora_dropout = 0.05, # dropout probability of the LoRA layers
                bias = 'none', # whether to train bias weights, set to 'none' for attention layers
                task_type = 'SEQ_CLS'
            )

            model = AutoModelForSequenceClassification.from_pretrained(
                checkpoint,
                quantization_config=quantization_config,
                num_labels=num_labels,
                cache_dir="/cache_dir"
            )

            model = prepare_model_for_kbit_training(model)
            model = get_peft_model(model, lora_config)

            tokenizer = AutoTokenizer.from_pretrained(checkpoint, add_prefix_space=True, cache_dir="/cache_dir")

            tokenizer.pad_token_id = tokenizer.eos_token_id
            tokenizer.pad_token = tokenizer.eos_token

            model.config.pad_token_id = tokenizer.pad_token_id
            model.config.use_cache = False
            model.config.pretraining_tp = 1

            MAX_LEN = 512


            tokenized_datasets = hf_dataset.map(llama_preprocessing_function, batched=True, remove_columns=col_to_delete)
            tokenized_datasets = tokenized_datasets.rename_column("target", "label")
            tokenized_datasets.set_format("torch")

            collate_fn = DataCollatorWithPadding(tokenizer=tokenizer, padding=True)

            training_args = TrainingArguments(
                output_dir = "/output", 
                learning_rate = 4e-5,
                per_device_train_batch_size = 8,
                per_device_eval_batch_size = 8,
                num_train_epochs = 20,
                eval_steps=50, #new
                save_steps=50, # new
                metric_for_best_model="eval_loss",  # new2
                weight_decay = 0.01,
                eval_strategy="steps", #new
                load_best_model_at_end = True
            )

            trainer = CustomTrainer(
                model = model,
                args = training_args,
                train_dataset = tokenized_datasets['train'],
                eval_dataset = tokenized_datasets['val'],
                processing_class = tokenizer, #arg processing_class new for transformers 4.46
                data_collator = collate_fn,
                compute_metrics = compute_metrics,
                class_weights=class_weights,
                callbacks=[EarlyStoppingCallback(early_stopping_patience=5)], #new
            )

            #train_result =
            trainer.train()

            def make_predictions(model,df_test):


                # Convert summaries to a list
                sentences = df_test.text.tolist()

                # Define the batch size
                batch_size = 32  # You can adjust this based on your system's memory capacity

                # Initialize an empty list to store the model outputs
                all_outputs = []

                # Process the sentences in batches
                for i in range(0, len(sentences), batch_size):
                    # Get the batch of sentences
                    batch_sentences = sentences[i:i + batch_size]

                    # Tokenize the batch
                    inputs = tokenizer(batch_sentences, return_tensors="pt", padding=True, truncation=True, max_length=512)

                    # Move tensors to the device where the model is (e.g., GPU or CPU)
                    inputs = {k: v.to('cuda' if torch.cuda.is_available() else 'cpu') for k, v in inputs.items()}

                    # Perform inference and store the logits
                    with torch.no_grad():
                        outputs = model(**inputs)
                        all_outputs.append(outputs['logits'])
                final_outputs = torch.cat(all_outputs, dim=0)
                df_test['predictions']=final_outputs.argmax(axis=1).cpu().numpy()
                df_test['predictions']=df_test['predictions'].apply(lambda l:category_map[l])


            make_predictions(model,df_test)
            
            valid_labels = df_test[task]
            predicted_labels = df_test['predictions']


            current_results = classification_report(valid_labels, predicted_labels, zero_division=0, digits=4, output_dict=True)
            results[dataset][task] = current_results

            print(classification_report(valid_labels, predicted_labels, zero_division=0, digits=4))


    scores = open("results/finetuning_{}.json".format(checkpoint.split("/")[-1]), "a", encoding="utf-8")
    scores.write("'{}' = {}\n\n".format(str(t.now()), json.dumps(results, indent=4)))
    scores.close()

if __name__ == "__main__":
    main()