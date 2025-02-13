import sys
import csv
import json
import pandas as pd
import torch
from somajo import SoMaJo
from datetime import datetime as t
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from sklearn.metrics import classification_report
from description import datasets


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


# to get equal number of examples per labels (default 8)
def sample_dataset(dataset, task, num_samples_per_label: int = 8, seed: int = 42):

    df = dataset.groupby(task)

    # sample num_samples, or at least as much as possible
    df = df.apply(
        lambda x: x.sample(min(num_samples_per_label, len(x)), random_state=seed)
    )
    df = df.reset_index(drop=True)

    return df


german_tokenizer = SoMaJo("de_CMC", split_camel_case=True)

# Input model name
model_id = "meta-llama/Llama-3.2-3B-Instruct"

for approach in ['zero', 'few']:
    
    # collect results of all tasks
    results = {}

    for dataset in datasets.keys():

        results[dataset] = {}

        for task in datasets[dataset]["tasks"]:

            print('\nPrompting of {} on {} dataset, task {}: {}-shot classification'.format(model_id.split("/")[-1]), dataset, task, approach))

            results[dataset][task] = {}


            df_test=read_dataset(datasets[dataset]["file"]["test"])
            df_test.columns = datasets[dataset]["columns"]


            # create a prompt
            # add examples
            shot = ''
            if approach != 'zero':
                # Read the dataset
                train=read_dataset(datasets[dataset]["file"]["train"])
                train.columns = datasets[dataset]["columns"]
                few_shot=sample_dataset(train, task)

                shot += "Hier sind einige Beispiele von Kategorien, die von Experten zugewiesen wurden:\n"
                for index, row in few_shot.iterrows(): 
                    shot += "Beispiel: {}\nKategorie: {}\n".format(row['text'], row[task])
                    
            # add definitions of labels
            definitions = 'Bitte klassifiziere den Text. '
            labels = list(datasets[dataset]["definitions"][task].keys())
            if approach != 'few-': 
                definitions += 'Die Kategorien sind folgend definiert:\n'
                for label in labels:
                    definitions += '- {}: {}\n'.format(label, datasets[dataset]["definitions"][task][label])
            definitions = definitions + shot

            # add question
            question = datasets[dataset]["questions"][task].format('\n- '.join(labels))


            # initialize a model
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


            model = AutoModelForCausalLM.from_pretrained(
                model_id,
                trust_remote_code=True,
                torch_dtype=torch.bfloat16,
            )
            model = model.to(device).eval()
            tokenizer = AutoTokenizer.from_pretrained(
                model_id,
                use_fast=False,
                trust_remote_code=True,
            )
            
            if tokenizer.pad_token is None:
                tokenizer.pad_token = tokenizer.eos_token


            predicted_labels = []
            output = []
            
            for i in df_test["text"]:
                
                content = "{}{}Text: {}\nAntwort:".format(definitions, question, i)
                messages = [
                    {"role": "system", "content": "You are a system for text classification in German"},
                    {"role": "user", "content": content},
                ]

                prompt = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

                prediction = model.generate(
                    prompt.to(model.device),
                    pad_token_id=tokenizer.pad_token_id,
                    max_new_tokens=256,
                    num_return_sequences=1,
                )
    
                answer=tokenizer.decode(prediction[0], skip_special_tokens=True).split("Antwort:assistant\n\n")[-1]
                output.append(answer)
                
                # tokenize an answer
                paragraphs = answer.split('\n')
                sentences = german_tokenizer.tokenize_text(paragraphs)
                tokens = []
                categories = []
                for sentence in sentences:
                    for token in sentence:
                        tokens.append(token.text)
                for token in tokens:
                    for label in labels:
                            if token.lower()==label.lower():
                                if label not in categories: categories.append(label)
                if len(categories) == 1: answer = categories[0]
                # collect all answers
                predicted_labels.append(answer)


            # classification report only for defined labels in gold data
            true_labels = df_test[task].tolist()
            converted_true_labels=[]
            for l in true_labels:
                if l==0: converted_true_labels.append('0')
                elif l==1: converted_true_labels.append('1')
                else: converted_true_labels.append(l)
            if len(converted_true_labels)==len(predicted_labels):
                print(classification_report(converted_true_labels, predicted_labels, labels=labels, zero_division=0, digits=4,))
                results[dataset][task] = classification_report(converted_true_labels, predicted_labels, labels=labels, zero_division=0, digits=4, output_dict=True)
            else: print("Error: Number of true labels and number of predicted labels are not equal")


    scores = open("results/prompting_{}_{}.json".format(approach, model_id.split("/")[-1]), "a", encoding="utf-8")
    scores.write("'{}' = {}\n\n".format(str(t.now()), json.dumps(results, indent=4)))
    scores.close()
