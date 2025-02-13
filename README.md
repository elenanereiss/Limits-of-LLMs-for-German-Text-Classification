# Limits of LLMs for German Text Classification

This repo is dedicated to an analysis of the LLMs performance as text classifiers on five German datasets from social media covering 13 tasks. We investigate zero- (ZSC) and few-shot classification (FSC) approaches with various LLMs.

## Experiment setup
### Approaches

- zero-shot prompting
- few-shot prompting
- peft fine-tuning using qlora

### Datasets


| Dataset                     | Citation                                                | Task                                                   | Size |
|-----------------------------|---------------------------------------------------------|--------------------------------------------------------|------|
| **German COVID-19 Twitter** | submitted                                               | informativeness, topic, credibility                    | 643  |
| **[German Speech Act Dataset](https://github.com/MelinaPl/speech-act-analysis)**      | Plakidis and Rehm (2022)                                | coarse and fine classification                         | 1959 |
| **[German HASOC2020](https://hasocfire.github.io/hasoc/2020/index.html)**              | Mandl, Modha, Kumar M, and Chakravarthi (2021)          | coarse and fine classification                         | 2899 |
| **[GermEval 2019 Subtask 2: The Shared Task on Identification of Offensive Language](https://fz.h-da.de/iggsa/data)**           | Struß, Siegel, Ruppenhofer, Wiegand, and Klenner (2019) | coarse and fine classification                         | 7026 |
|                             |                                                         | classification of implicit/explicit offensive language | 2888 |
| **[GermEval 2021: The Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments](https://germeval2021toxic.github.io/SharedTask/)**           | Risch, Stoll, Wilms, and Wiegand (2021)                 | toxic, engaging, fact claming comment classification   | 4188 |


For further information please see [datasets description](https://github.com/elenanereiss/Limits-of-LLMs-for-German-Text-Classification/blob/main/Datasets.md).

### Models

#### Instruct LLMs for prompting

- [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
- [EuroLLM-9B-Instruct](https://huggingface.co/utter-project/EuroLLM-9B-Instruct)
- [Teuken-7B-instruct-research-v0.4](https://huggingface.co/openGPT-X/Teuken-7B-instruct-research-v0.4)

Further information about datasets can be found here []().

#### Base LLMs for fine-tuning

- [Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B)
- [EuroLLM-9B](https://huggingface.co/utter-project/EuroLLM-9B)
- Teuken-7B-base (is available on request contact@opengpt-x.de)
- [BübleLM-2B](https://huggingface.co/flair/bueble-lm-2b)

## Results

Results per class can be found [here](https://github.com/elenanereiss/Limits-of-LLMs-for-German-Text-Classification/blob/main/Results.md#results-per-class).

| dataset             | task             | approach   |   Llama-3.2-3B precision |   Llama-3.2-3B recall |   Llama-3.2-3B f1-score |   EuroLLM-9B precision |   EuroLLM-9B recall |   EuroLLM-9B f1-score |   Teuken-7B precision |   Teuken-7B recall |   Teuken-7B f1-score |   BübleLM precision |   BübleLM recall |   BübleLM f1-score |
|:--------------------|:-----------------|:-----------|-------------------------:|----------------------:|------------------------:|-----------------------:|--------------------:|----------------------:|----------------------:|-------------------:|---------------------:|--------------------:|-----------------:|-------------------:|
| covid19             | informativeness  | zs         |                 0.838542 |              0.612808 |               0.590435  |              0.519048  |           0.338807  |             0.34519   |             0.673893  |           0.533333 |            0.491977  |                     |                  |                    |
| covid19             |                  | fs         |                 0.500978 |              0.565298 |               0.517766  |              0.748605  |           0.57121   |             0.628054  |             0.680037  |           0.634154 |            0.653288  |                     |                  |                    |
| covid19             |                  | t          |                 0.702469 |              0.727531 |               0.70028   |              0.769749  |           0.792228  |             0.779943  |             0.647741  |           0.677942 |            0.647627  |            0.728136 |         0.7237   |           0.722761 |
| covid19             | topic            | zs         |                 0.233333 |              0.229532 |               0.175309  |              0.305958  |           0.169514  |             0.198914  |             0.460917  |           0.37115  |            0.294857  |                     |                  |                    |
| covid19             |                  | fs         |                 0.50591  |              0.442207 |               0.39872   |              0.239926  |           0.241133  |             0.165348  |             0.620837  |           0.376286 |            0.31353   |                     |                  |                    |
| covid19             |                  | t          |                 0.711156 |              0.656191 |               0.671934  |              0.515     |           0.532677  |             0.502289  |             0.541453  |           0.614297 |            0.560508  |            0.609117 |         0.571011 |           0.575528 |
| covid19             | credibility      | zs         |                 0.332515 |              0.172543 |               0.0970674 |              0.466667  |           0.0352564 |             0.0653179 |             0.411425  |           0.388889 |            0.381033  |                     |                  |                    |
| covid19             |                  | fs         |                 0.537415 |              0.357906 |               0.412675  |              0.484538  |           0.494124  |             0.36923   |             0.557854  |           0.50641  |            0.443985  |                     |                  |                    |
| covid19             |                  | t          |                 0.49686  |              0.518697 |               0.503779  |              0.541085  |           0.564637  |             0.541822  |             0.46875   |           0.48344  |            0.469064  |            0.506623 |         0.517628 |           0.51011  |
| speech_acts_coarse  | coarse labels    | zs         |                 0.296795 |              0.221922 |               0.142433  |              0.192914  |           0.224964  |             0.170898  |             0.253561  |           0.184994 |            0.115082  |                     |                  |                    |
| speech_acts_coarse  |                  | fs         |                 0.418397 |              0.321895 |               0.287129  |              0.208346  |           0.205111  |             0.174202  |             0.187965  |           0.237892 |            0.191404  |                     |                  |                    |
| speech_acts_coarse  |                  | t          |                 0.642365 |              0.6705   |               0.651282  |              0.690719  |           0.562598  |             0.587731  |             0.579138  |           0.602185 |            0.560238  |            0.479687 |         0.5356   |           0.48655  |
| speech_acts_fine    | fine labels      | zs         |                 0.134167 |              0.11147  |               0.100505  |              0.156891  |           0.126369  |             0.116417  |             0.0338756 |           0.106085 |            0.0308676 |                     |                  |                    |
| speech_acts_fine    |                  | fs         |                 0.277995 |              0.200424 |               0.171971  |              0.0980564 |           0.116942  |             0.0688366 |             0.106574  |           0.169794 |            0.095387  |                     |                  |                    |
| speech_acts_fine    |                  | t          |                 0.326283 |              0.377671 |               0.338538  |              0.33945   |           0.321864  |             0.311157  |             0.39955   |           0.425345 |            0.389196  |            0.274877 |         0.312568 |           0.282974 |
| hasoc2020           | coarse labels    | zs         |                 0.660604 |              0.619175 |               0.59467   |              0.598585  |           0.354497  |             0.374718  |             0.628846  |           0.507653 |            0.219968  |                     |                  |                    |
| hasoc2020           |                  | fs         |                 0.699169 |              0.491776 |               0.552692  |              0.633367  |           0.609351  |             0.598656  |             0.630604  |           0.516582 |            0.239209  |                     |                  |                    |
| hasoc2020           |                  | t          |                 0.763578 |              0.809968 |               0.778599  |              0.745536  |           0.791121  |             0.759394  |             0.776941  |           0.805437 |            0.788603  |            0.784705 |         0.784705 |           0.784705 |
| hasoc2020           | fine labels      | zs         |                 0.378451 |              0.37751  |               0.285505  |              0.320071  |           0.264144  |             0.16715   |             0.259561  |           0.268519 |            0.0682963 |                     |                  |                    |
| hasoc2020           |                  | fs         |                 0.391596 |              0.303541 |               0.294458  |              0.368866  |           0.304278  |             0.23011   |             0.229322  |           0.284392 |            0.252714  |                     |                  |                    |
| hasoc2020           |                  | t          |                 0.491798 |              0.584912 |               0.502287  |              0.48436   |           0.558487  |             0.506802  |             0.462343  |           0.58918  |            0.484178  |            0.489711 |         0.538976 |           0.505654 |
| germeval2019_task12 | coarse labels    | zs         |                 0.661932 |              0.621493 |               0.560364  |              0.65009   |           0.600811  |             0.544879  |             0.160013  |           0.5      |            0.242439  |                     |                  |                    |
| germeval2019_task12 |                  | fs         |                 0.651538 |              0.499429 |               0.33963   |              0.673643  |           0.669198  |             0.64088   |             0.160013  |           0.5      |            0.242439  |                     |                  |                    |
| germeval2019_task12 |                  | t          |                 0.760854 |              0.767516 |               0.763916  |              0.756021  |           0.777762  |             0.763213  |             0.731868  |           0.755838 |            0.738039  |            0.734029 |         0.763871 |           0.738084 |
| germeval2019_task12 | fine labels      | zs         |                 0.363981 |              0.367897 |               0.356866  |              0.336127  |           0.301235  |             0.216257  |             0.29213   |           0.317321 |            0.206944  |                     |                  |                    |
| germeval2019_task12 |                  | fs         |                 0.408201 |              0.26014  |               0.278312  |              0.332255  |           0.291256  |             0.226164  |             0.401785  |           0.292394 |            0.113368  |                     |                  |                    |
| germeval2019_task12 |                  | t          |                 0.423738 |              0.453068 |               0.423495  |              0.39717   |           0.44684   |             0.403367  |             0.436117  |           0.478363 |            0.439623  |            0.404853 |         0.463122 |           0.413066 |
| germeval2019_task3  | offensive labels | zs         |                 0.535016 |              0.533076 |               0.260397  |              0.501231  |           0.391435  |             0.262656  |             0.427957  |           0.5      |            0.461182  |                     |                  |                    |
| germeval2019_task3  |                  | fs         |                 0.573144 |              0.508794 |               0.144903  |              0.533797  |           0.487203  |             0.357176  |             0.595238  |           0.50495  |            0.474751  |                     |                  |                    |
| germeval2019_task3  |                  | t          |                 0.675612 |              0.760369 |               0.69906   |              0.683015  |           0.707174  |             0.693609  |             0.671447  |           0.738056 |            0.692673  |            0.653832 |         0.733546 |           0.673448 |
| germeval2021        | toxic            | zs         |                 0.604357 |              0.600298 |               0.600887  |              0.56586   |           0.480808  |             0.39625   |             0.61499   |           0.531679 |            0.364985  |                     |                  |                    |
| germeval2021        |                  | fs         |                 0.591849 |              0.598389 |               0.586313  |              0.558338  |           0.486989  |             0.516932  |             0.62038   |           0.562848 |            0.436605  |                     |                  |                    |
| germeval2021        |                  | t          |                 0.674422 |              0.678687 |               0.676104  |              0.697029  |           0.688071  |             0.691462  |             0.701477  |           0.705012 |            0.703014  |            0.677823 |         0.663454 |           0.667712 |
| germeval2021        | engaging         | zs         |                 0.547461 |              0.543707 |               0.530494  |              0.558139  |           0.492092  |             0.463812  |             0.556836  |           0.522897 |            0.327142  |                     |                  |                    |
| germeval2021        |                  | fs         |                 0.510722 |              0.412091 |               0.429085  |              0.531076  |           0.423963  |             0.469485  |             0.586691  |           0.549032 |            0.352616  |                     |                  |                    |
| germeval2021        |                  | t          |                 0.661298 |              0.684232 |               0.668     |              0.662149  |           0.678552  |             0.668114  |             0.638046  |           0.659544 |            0.643219  |            0.667417 |         0.679859 |           0.672466 |
| germeval2021        | factClaiming     | zs         |                 0.625586 |              0.610889 |               0.528285  |              0.57138   |           0.479916  |             0.34391   |             0.666667  |           0.501582 |            0.25611   |                     |                  |                    |
| germeval2021        |                  | fs         |                 0.605958 |              0.61931  |               0.593268  |              0.584566  |           0.499019  |             0.538398  |             0.597159  |           0.547523 |            0.389737  |                     |                  |                    |
| germeval2021        |                  | t          |                 0.771303 |              0.767748 |               0.769452  |              0.752389  |           0.760641  |             0.755994  |             0.72104   |           0.722435 |            0.721721  |            0.715776 |         0.713669 |           0.714685 |

## Use

### Prompting

Depending on the model run:
```
python prompting_llama.py

python prompting_eurollm.py

python prompting_teuken.py
```

## Fine-tuning

First get access to LLama 3.2 and EuroLLM on HuggingFace and log in with command `huggingface-cli login`. Then, to fine-tune a LLM run, e.g.:

```
python finetuning.py meta-llama/Llama-3.2-3B
```