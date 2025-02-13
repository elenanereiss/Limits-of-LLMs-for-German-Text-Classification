**Table of contents**
1. [German Twitter COVID-19 Dataset](http://localhost:8888/notebooks/Documents/GitHub/LLMs-fails/German%20Datasets.ipynb#German-Twitter-COVID-19-Dataset:-Topic-based-Credibility-Annotations)
2. [German Speech Act Dataset](http://localhost:8888/notebooks/Documents/GitHub/LLMs-fails/German%20Datasets.ipynb#German-Speech-Act-Dataset)
3. [German HASOC2020](http://localhost:8888/notebooks/Documents/GitHub/LLMs-fails/German%20Datasets.ipynb#HASOC-2020:-Hate-Speech-and-Offensive-Content-Identification-in-Indo-European-Languages-(German))
4. [GermEval 2019 Subtask 2: The Shared Task on Identification of Offensive Language](http://localhost:8888/notebooks/Documents/GitHub/LLMs-fails/German%20Datasets.ipynb#GermEval-2019-Subtask-2:-The-Shared-Task-on-Identification-of-Offensive-Language)
5. [GermEval 2021: The Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments](http://localhost:8888/notebooks/Documents/GitHub/LLMs-fails/German%20Datasets.ipynb#GermEval-2021:-The-Shared-Task-on-the-Identification-of-Toxic,-Engaging,-and-Fact-Claiming-Comments)


**Overview**

| Dataset                     | Task              | Number of classes | Size | Min instances per class |
|-----------------------------|-------------------|-------------------|------|-------------------------|
| **German COVID-19 Twitter** | _Informativeness_ | 3                 | 643  | 55                      |
|                             | _Topic_           | 6                 | 643  | 15                      |
|                             | _Credibility_     | 3                 | 643  | 10                      |
| **German Speech Acts**      | _Coarse_          | 6                 | 1959 | 20                      |
|                             | _Fine_            | 17                | 1959 | 11                      |
| **HASOC 2020**              | _Coarse_          | 2                 | 2899 | 907                     |
|                             | _Fine_            | 4                 | 2899 | 170                     |
| **GermEval 2019**           | _Coarse_          | 2                 | 7026 | 2257                    |
|                             | _Fine_            | 4                 | 7026 | 263                     |
|                             | _Offensive_       | 2                 | 2888 | 393                     |
| **GermEval 2021**           | _Toxic_           | 2                 | 4188 | 1472                    |
|                             | _Engaging_        | 2                 | 4188 | 1118                    |
|                             | _Fact claiming_   | 2                 | 4188 | 1417                    |

# German Twitter COVID-19 Dataset: Topic-based Credibility Annotations

## Description

*The description of the dataset, subtasks and classes is taken from the official site:  [https://anonymous.4open.science/r/Twitter_COVID19-0924/README.md](https://anonymous.4open.science/r/Twitter_COVID19-0924/README.md)*

The dataset includes 643 tweets extracted during the pandemic (from 2020-03-01 to 2022-09-01). The Topic-based Credibility Annotations include three annotation layers: 

- *Informativeness*: the goal is to filter tweets that do not primarily provide covid-related information, e.g. because they are humorous or sarcastic comments or contain personal opinions or attacks (including tweets with vulgar or offensive language).
  - **Personal_Experience**: The tweet is informative and reports personal experience (personal or reported personal experiences with the disease/vaccination/side effects etc.).
  - **None**: The tweet is not related to the COVID-19 or the tweet is related to COVID-19 but does not contain any information, e.g. it is a personal statements (opinion) without an informative background, or if it is a humorous/sarcastic comment. 
  - **Informative**: The tweet is informative and states general information. It should be somewhat related to COVID-19.

- *Topics*
  - **Case_Report**: Case reports/statistics
  - **Consequences**: Consequences of a Covid infection (long-covid, psychological aspects, etc.)
  - **Governm_Decisions**: Measures and decisions by the federal government and its impact on people, countries, and the economy
  - **Origin**: The origin of the virus; its sources
  - **Risk_Reduction**: Ways of mitigating the risk of infection
  - **Treatment**: Treatments of an infection
  - **Vaccination**: Vaccination: general information about the vaccine, availability, side-effects
  - **None**: The tweet is not about any of the above topics, or it is unclear what topic is, e.g. because the context is missing or because the content only indicates what it is about.

- *Credibility*
  - **credible**: The tweet and its content seems to be to some extent credible.
  - **non-credible**: The tweet and its content seems to be non-credible and it is highly questionable whether it can be trusted.
  - **None**: Based on the tweet, it is not possible to decide if the content is credible or not.


## Dataset

Due to Twitter's content redistribution policy, we are unable to publish the full dataset, but provide annotations and tweet IDs on request.

## Distribution


### Informativeness

|                     |   train |   test |
|:--------------------|--------:|-------:|
| Informative         |     331 |     87 |
| None                |     135 |     35 |
| Personal_Experience |      48 |      7 |
| total               |     514 |    129 |

### Topic

|                   |   train |   test |
|:------------------|--------:|-------:|
| None              |     169 |     42 |
| Case_Report       |     145 |     37 |
| Governm_Decisions |      88 |     22 |
| Vaccination       |      76 |     19 |
| Consequences      |      24 |      6 |
| Risk_Reduction    |      12 |      3 |
| total             |     514 |    129 |

### Credibility
|              |   train |   test |
|:-------------|--------:|-------:|
| credible     |     316 |     78 |
| None         |     191 |     48 |
| non-credible |       7 |      3 |
| total        |     514 |    129 |

## References

Preprint: submitted

# German Speech Act Dataset

## Description

*The description of the dataset, subtasks and classes is taken from the official site:  [https://github.com/MelinaPl/speech-act-analysis](https://github.com/MelinaPl/speech-act-analysis)*

German Speech Act Dataset consists of a subset of 600 tweets taken from GermEval 2019. Tweets were split into sentences and annotated with coarse- and fine-grained speech acts.

- *Coarse-grained speech acts* consist of 6 classes
  - Assertive: Making statements about the world.
  - Expressive: Expressing an attitude or feeling.
  - Directive: Trying to get people to do something.
  - Commissive: Committing oneself to do something.
  - Unsure: Used when an utterance in a tweet cannot be classified due to missing or insufficient context.
  - Other: Used for speech acts not represented in this annotation scheme.

- *Fine-grained speech acts* consist of 23 classes
  - *Assertive speech acts*:
    - Assert: to assert something.
    - Sustain: to sustain an assertion with arguments.
    - Guess: to weaken an assertion by introducing probability/possiblity of the assertion
    - Predict: an assertion that refers to the future.
    - Agree: agreeing with something/someone.
    - Disagree: disagreeing with something/someone.
  - *Expressive speech acts*: 
    - Rejoice: Expressing a positive attitude towards someone/something.
    - Complain: To complain, e.g. expressing a negative attitude towards something/someone.
    - Wish: Wishing for something.
    - Apologize: Apologizing to someone for something.
    - Thank: Thanking someone.
    - expressEmoji: Used for an emoji or series of emojis.
  - *Directive speech acts*: 
    - Require: (Strongly) requiring someone to do something. Usually used for imperatives.
    - Request: Requesting someone to do something. Usually used for questions.
    - Suggest: Suggesting something to someone. Might be used both with positive and negative intentions.
    - Greet: Greeting someone.
    - Address: Addressing someone. Used for mentions (@xyz).
  - *Commissive speech acts*: 
    - Engage: Committing oneself to do something.
    - Accept: Accepting something based on a previous utterance.
    - Refuse: Refusing something based on a previous utterance.
    - Threat: Threatening someone.
  - Unsure
  - Other

## Dataset

You can find the dataset on the GitHub at [https://github.com/MelinaPl/speech-act-analysis](https://github.com/MelinaPl/speech-act-analysis).

## Distribution

## Coarse-grained labels

|            |   train |   test |
|:-----------|--------:|-------:|
| ASSERTIVE  |     546 |    137 |
| DIRECTIVE  |     506 |    127 |
| EXPRESSIVE |     320 |     80 |
| UNSURE     |     120 |     30 |
| OTHER      |      59 |     14 |
| COMMISSIVE |      16 |      4 |
| total      |    1567 |    392 |

## Fine-grained labels

Due to sparse occurrences of some fine-grained classes, only classes which occur more than ten times were included. Disagree, apologize, thank, greet were united in a class excluded. As for the coarse-grained class commissive, we have decided not to divide into fine-grained classes. Thus, the number of fine-grained speech acts was reduced from 23 to a 17.

|              |   train |   test |
|:-------------|--------:|-------:|
| ASSERT       |     472 |    118 |
| ADDRESS      |     300 |     75 |
| COMPLAIN     |     206 |     51 |
| REQUEST      |     130 |     33 |
| UNSURE       |     120 |     30 |
| expressEMOJI |      85 |     21 |
| REQUIRE      |      62 |     16 |
| OTHER        |      58 |     15 |
| PREDICT      |      27 |      7 |
| GUESS        |      22 |      5 |
| COMMISSIVE   |      16 |      4 |
| REJOICE      |      14 |      3 |
| EXCLUDED     |      13 |      3 |
| SUGGEST      |      13 |      3 |
| AGREE        |      10 |      3 |
| SUSTAIN      |      10 |      3 |
| WISH         |       9 |      2 |
| total        |    1567 |    392 |

## References

Plakidis, M., & Rehm, G. (2022, June). [A dataset of offensive German language tweets annotated for speech acts](https://aclanthology.org/2022.lrec-1.513.pdf). In *Proceedings of the Thirteenth Language Resources and Evaluation Conference* (pp. 4799-4807).

# HASOC 2020: Hate Speech and Offensive Content Identification in Indo-European Languages (German)

## Description

*The description of the dataset, subtasks and classes is taken from the official site:  [https://hasocfire.github.io/hasoc/2020/index.html](https://hasocfire.github.io/hasoc/2020/index.html)*

HASOC provides a forum and a data challenge for multilingual research on the identification of problematic content. In 2020, the organizers offer again English, German and Hindi with 2 sub-tasks (alltogether over 10.000 annotated tweets from Twitter): 

- *Subtask A - Identifying Hate, offensive and profane content* is coarse-grained binary classification in which participating system are required to classify tweets into two class:
  - **HOF** Hate and Offensive - this post contains Hate, offensive, and profane content.
  - **NOT** Non- Hate and offensive - this post does not contain any Hate speech, profane, offensive content.

- *Subtask B - Discrimination between Hate, profane and offensive posts* is a fine-grained classification offered for English, German, Hindi. Hate-speech and offensive posts from the subtask A are further classified into three categories:
  - **HATE** Hate speech - posts under this class contain Hate speech content.
  - **OFFN** Offenive - posts under this class contain offensive content.
  - **PRFN** Profane - these posts contain profane words.

## Dataset

You can find the dataset on the official website at [https://hasocfire.github.io/hasoc/2020/dataset.html](https://hasocfire.github.io/hasoc/2020/dataset.html).

## Distribution

## Subtask A

|       |   train |   test |
|:------|--------:|-------:|
| NOT   |    1700 |    392 |
| HOF   |     673 |    134 |
| total |    2373 |    526 |

## Subtask B

|       |   train |   test |
|:------|--------:|-------:|
| NONE  |    1700 |    378 |
| PRFN  |     387 |     88 |
| HATE  |     146 |     24 |
| OFFN  |     140 |     36 |
| total |    2373 |    526 |

## References

Mandl, T., Modha, S., Kumar M, A., & Chakravarthi, B. R. (2020, December). [Overview of the hasoc track at fire 2020: Hate speech and offensive language identification in tamil, malayalam, hindi, english and german.](https://arxiv.org/pdf/2108.05927) In *Proceedings of the 12th annual meeting of the forum for information retrieval evaluation* (pp. 29-32).

# GermEval 2019 Subtask 2: The Shared Task on Identification of Offensive Language 

## Description

The description of the dataset, subtasks and classes is taken from the official site:  [https://fz.h-da.de/iggsa/](https://fz.h-da.de/iggsa/). The dataset is available at [https://fz.h-da.de/iggsa/data](https://fz.h-da.de/iggsa/data).

- *Subtask I — Binary classification of offensive language*
  - The task is to decide whether a tweet includes some form of offensive language (**OFFENSE**) or not (**OTHER**).
- *Subtask II — Fine-grained classification of offensive language*
  - **PROFANITY**: usage of profane words, however, the tweet clearly does not want to insult anyone.
  - **INSULT**: unlike PROFANITY the tweet clearly wants to offend someone.
  - **ABUSE**: unlike INSULT, the tweet does not just insult a person but represents the stronger form of abusive language
- *Subtask III – Classification of explicit and implicit offensive language*
  - **EXPLICIT**: an offensive tweet which directly expresses hate, condemnation, superiority towards an explicitly or implicitly given target
  - **IMPLICIT**:  an offensive tweet where the expression of hate, condemnation, superiority etc. as directed towards an explicitly or implicitly given target has to be inferred from the ascription of (hypothesized) target properties that are insulting, degrading, offending, humiliating etc.

## Statistics

### Subtask I — Binary classification

|         |   train |   test |
|:--------|--------:|-------:|
| OTHER   |    2708 |   2061 |
| OFFENSE |    1287 |    970 |
| total   |    3995 |   3031 |

### Subtask II — Fine-grained classification

|           |   train |   test |
|:----------|--------:|-------:|
| OTHER     |    2708 |   2061 |
| INSULT    |     625 |    459 |
| ABUSE     |     510 |    400 |
| PROFANITY |     152 |    111 |
| total     |    3995 |   3031 |

### Subtask III — Classification of explicit and implicit offensive language

|          |   train |   test |
|:---------|--------:|-------:|
| EXPLICIT |    1699 |    796 |
| IMPLICIT |     259 |    134 |
| total    |    1958 |    930 |

## References

Struß, J. M., Siegel, M., Ruppenhofer, J., Wiegand, M., & Klenner, M. (2019). [Overview of germeval task 2, 2019 shared task on the identification of offensive language.](https://corpora.linguistik.uni-erlangen.de/data/konvens/proceedings/papers/germeval/GermEvalSharedTask2019Iggsa.pdf)

<!--
## Subtask I — Binary classification

The task is to decide whether a tweet includes a) some form of offensive language (OFFENSE) or b) or not (OTHER).


**OFFENSE**:

`Juhu, das morgige Wetter passt zum Tag SCHEIßWETTER`

`@KarlLagerfeld ist in meinen Augen strunzdumm wie ein Knäckebrot.`

`Für mich ist die #katholische #Kirche nur ein Sammelbecken von #Verbrechern #Kinderschändern und #Kriminellen #Lokalzeit`

**OTHER**:

`@Sakoelabo @Padit1337 @SawsanChebli Nicht alle Staatssekretäre kann man ernst nehmen.`

`Endlich hat Kurz einen Verbündeten aus Frankreich, der auch die |LBR| ungesetzliche Einwanderung von jungen Afrikanern unterbinden will.`

`Die Türkei führt einen Angriffskrieg und die @spdde inkl. @sigmargabriel rüstet noch ihre Panzer auf.`



## Subtask II — Fine-grained classification

In addition to detecting abusive language tweets, we distinguish between 3 subcategories:

**PROFANITY**: usage of profane words, however, the tweet clearly does not want to insult anyone.

`Juhu, das morgige Wetter passt zum Tag SCHEIßWETTER`

`@TiffanyAngelx zu anbeissen ,dein geiler Arsch`

`Als SPD wäre ich jetzt maximal angepisst.`

**INSULT**: unlike PROFANITY the tweet clearly wants to offend someone.

`ein #Tatort mit der Presswurst #Saalfeld geht gar nicht #ARD`

`@KarlLagerfeld ist in meinen Augen strunzdumm wie ein Knäckebrot.`

`Wo ist #Kubicki heute? Ist er schon besoffen im Puff?`

**ABUSE**: unlike INSULT, the tweet does not just insult a person but represents the stronger form of abusive language. (For a concise definition, please consult the above annotation guidelines).

`was mich stört ist wenn am frühen Morgen im #Morgenmagazin schon strunzdumme #Migranten moderieren`

`ich würde auch nicht mit einer schwarzen #Schwuchtel zusammenarbeiten #Tatort`

`Ich persönlich scheisse auf die grüne Kinderfickerpartei`

**OTHER**: same as in Subtask I

## Subtask III — Classification of explicit and implicit offensive language

In addition to detecting offensive language tweets, we distinguish between 2 subcategories:

**EXPLICIT**: an offensive tweet which directly expresses hate, condemnation, superiority towards an explicitly or implicitly given target.

`SPD verseuchtes Nazipack heisst jetzt ANTIFA`

**IMPLICIT**: an offensive tweet where the expression of hate, condemnation, superiority etc. as directed towards an explicitly or implicitly given target has to be inferred from the ascription of (hypothesized) target properties that are insulting, degrading, offending, humiliating etc.

`Dem Kommentar entnehme ich das auch ihre Schaukel als Kind zu nahe an der Wand gestanden hat.`

`Flüchtlinge fliehen nach Deutschland parallel dazu lassen sie ihre Familien in der Heimat sterben sehr ehrenhaft ....`

Subtask III is cast as a two-way classification task where a tweet either is explicit offensive (EXPLICIT) or implicit offensive (IMPLICIT).
-->

# GermEval 2021: The Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments

## Description

*The description of the dataset, subtasks and classes is taken from the official site:  [https://germeval2021toxic.github.io/SharedTask/](https://germeval2021toxic.github.io/SharedTask/)*

The organizers of the shared task provide an annotated dataset of over 4,000 Facebook user comments. The dataset is drawn from the Facebook page of a political talk show of a German television broadcaster, including user discussions from February till July 2019. The dataset is provided in anonymized form. User information and comment IDs are not shared. Links to users are replaced by @USER. Links to the show are replaced by @MEDIUM, and links zu the moderator of the show are replacd by @MODERATOR. 

The Shared Task consists of three subtasks. Each subtask is defined as a binary classification problem with classes 0 and 1:
- *Subtask 1 - Toxic Comment Classification*
  - The detection of toxic content in online discussions remains challenging and new approaches are constantly being demanded and developed. With this subtask we aim to continue the series of previous GermEval Shared Tasks on Offensive Language Identification.

- *Subtask 2 - Engaging Comment Classification*
  - In addition to the detection of toxic language, community managers and moderators increasingly express interest in identifying particularly valuable user content, for example, to highlight them and to give them more visibility. That includes rational, respectful, and reciprocal comments that can encourage readers to join the discussion, increase positive perceptions of discussion providers, and can enhance more fruitful and less violent exchange.

- *Subtask 3 - Fact-Claiming Comment Classification*
  - Beyond the challenge to ensure non-hostile debates, platforms and moderators are under pressure to act due to the rapid spread of misinformation and fake news. Platforms need to review and verify posted information to meet their responsibility as information providers and distributors. As a result, there is an increasing demand for systems that automatically identify comments that should be fact-checked manually. Note that this subtask is not about the fact-checking itself or the identification of fake news. However, the identification of fact-claiming comments is a pre-processing step for manual fact-checking.



## Dataset

You can find the dataset on the official website at [https://github.com/germeval2021toxic/SharedTask/tree/main/Data%20Sets](https://github.com/germeval2021toxic/SharedTask/tree/main/Data%20Sets)

## Statistics

### Subtask 1 - Toxic Comment Classification

|       |   train |   test |
|:------|--------:|-------:|
| 0     |    2122 |    594 |
| 1     |    1122 |    350 |
| total |    3244 |    944 |

### Subtask 2 - Engaging Comment Classification

|       |   train |   test |
|:------|--------:|-------:|
| 0     |    2379 |    691 |
| 1     |     865 |    253 |
| total |    3244 |    944 |

### Subtask 3 - Fact-Claiming Comment Classification

|       |   train |   test |
|:------|--------:|-------:|
| 0     |    2141 |    630 |
| 1     |    1103 |    314 |
| total |    3244 |    944 |

## References

Risch, J., Stoll, A., Wilms, L., & Wiegand, M. (2021). [Overview of the GermEval 2021 Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments.](https://aclanthology.org/2021.germeval-1.1.pdf) In *Proceedings of the GermEval 2021 Shared Task on the Identification of Toxic, Engaging, and Fact-Claiming Comments* (pp. 1–12). Association for Computational Linguistics.
