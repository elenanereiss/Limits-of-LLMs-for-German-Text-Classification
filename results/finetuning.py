llama_finetuning = {
    "covid19": {
        "informativeness": {
            "Informative": {
                "precision": 0.9222222222222223,
                "recall": 0.9540229885057471,
                "f1-score": 0.9378531073446328,
                "support": 87.0
            },
            "Personal_Experience": {
                "precision": 0.3333333333333333,
                "recall": 0.5714285714285714,
                "f1-score": 0.4210526315789474,
                "support": 7.0
            },
            "none": {
                "precision": 0.8518518518518519,
                "recall": 0.6571428571428571,
                "f1-score": 0.7419354838709677,
                "support": 35.0
            },
            "accuracy": 0.8527131782945736,
            "macro avg": {
                "precision": 0.7024691358024692,
                "recall": 0.7275314723590585,
                "f1-score": 0.7002804075981827,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.8711742750502439,
                "recall": 0.8527131782945736,
                "f1-score": 0.8566537263218571,
                "support": 129.0
            }
        },
        "topic": {
            "Case_Report": {
                "precision": 0.8717948717948718,
                "recall": 0.918918918918919,
                "f1-score": 0.8947368421052632,
                "support": 37.0
            },
            "Consequences": {
                "precision": 0.6666666666666666,
                "recall": 0.3333333333333333,
                "f1-score": 0.4444444444444444,
                "support": 6.0
            },
            "Governm_Decisions": {
                "precision": 0.7647058823529411,
                "recall": 0.5909090909090909,
                "f1-score": 0.6666666666666667,
                "support": 22.0
            },
            "Risk_Reduction": {
                "precision": 0.6666666666666666,
                "recall": 0.6666666666666666,
                "f1-score": 0.6666666666666666,
                "support": 3.0
            },
            "Vaccination": {
                "precision": 0.6666666666666666,
                "recall": 0.7368421052631579,
                "f1-score": 0.7,
                "support": 19.0
            },
            "none": {
                "precision": 0.6304347826086957,
                "recall": 0.6904761904761905,
                "f1-score": 0.6590909090909092,
                "support": 42.0
            },
            "accuracy": 0.7286821705426356,
            "macro avg": {
                "precision": 0.7111559227927513,
                "recall": 0.6561910509278931,
                "f1-score": 0.6719342548289916,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.7304253271659445,
                "recall": 0.7286821705426356,
                "f1-score": 0.7241892610313663,
                "support": 129.0
            }
        },
        "credibility": {
            "credible": {
                "precision": 0.8405797101449275,
                "recall": 0.7435897435897436,
                "f1-score": 0.7891156462585034,
                "support": 78.0
            },
            "non-credible": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "none": {
                "precision": 0.65,
                "recall": 0.8125,
                "f1-score": 0.7222222222222223,
                "support": 48.0
            },
            "accuracy": 0.751937984496124,
            "macro avg": {
                "precision": 0.49685990338164254,
                "recall": 0.5186965811965812,
                "f1-score": 0.5037792894935752,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.7501179642736772,
                "recall": 0.751937984496124,
                "f1-score": 0.745873543215736,
                "support": 129.0
            }
        }
    },
    "speech_acts_coarse": {
        "coarse labels": {
            "ASSERTIVE": {
                "precision": 0.7205882352941176,
                "recall": 0.7153284671532847,
                "f1-score": 0.7179487179487181,
                "support": 137.0
            },
            "COMMISSIVE": {
                "precision": 0.4,
                "recall": 0.5,
                "f1-score": 0.4444444444444445,
                "support": 4.0
            },
            "DIRECTIVE": {
                "precision": 0.9396551724137931,
                "recall": 0.8582677165354331,
                "f1-score": 0.8971193415637861,
                "support": 127.0
            },
            "EXPRESSIVE": {
                "precision": 0.6619718309859155,
                "recall": 0.5875,
                "f1-score": 0.6225165562913908,
                "support": 80.0
            },
            "OTHER": {
                "precision": 0.8666666666666667,
                "recall": 0.9285714285714286,
                "f1-score": 0.896551724137931,
                "support": 14.0
            },
            "UNSURE": {
                "precision": 0.2653061224489796,
                "recall": 0.43333333333333335,
                "f1-score": 0.3291139240506329,
                "support": 30.0
            },
            "accuracy": 0.7193877551020408,
            "macro avg": {
                "precision": 0.6423646713015788,
                "recall": 0.6705001575989132,
                "f1-score": 0.6512824514061506,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.7467016801467393,
                "recall": 0.7193877551020408,
                "f1-score": 0.7303504461176384,
                "support": 392.0
            }
        }
    },
    "speech_acts_fine": {
        "fine labels": {
            "ADDRESS": {
                "precision": 0.9866666666666667,
                "recall": 0.9866666666666667,
                "f1-score": 0.9866666666666668,
                "support": 75.0
            },
            "AGREE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "ASSERT": {
                "precision": 0.6145833333333334,
                "recall": 0.5,
                "f1-score": 0.5514018691588785,
                "support": 118.0
            },
            "COMMISSIVE": {
                "precision": 0.25,
                "recall": 0.75,
                "f1-score": 0.375,
                "support": 4.0
            },
            "COMPLAIN": {
                "precision": 0.42,
                "recall": 0.4117647058823529,
                "f1-score": 0.41584158415841577,
                "support": 51.0
            },
            "EXCLUDED": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "GUESS": {
                "precision": 0.2727272727272727,
                "recall": 0.6,
                "f1-score": 0.37499999999999994,
                "support": 5.0
            },
            "OTHER": {
                "precision": 0.75,
                "recall": 0.8,
                "f1-score": 0.7741935483870969,
                "support": 15.0
            },
            "PREDICT": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 7.0
            },
            "REJOICE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "REQUEST": {
                "precision": 0.8518518518518519,
                "recall": 0.696969696969697,
                "f1-score": 0.7666666666666667,
                "support": 33.0
            },
            "REQUIRE": {
                "precision": 0.2857142857142857,
                "recall": 0.375,
                "f1-score": 0.3243243243243243,
                "support": 16.0
            },
            "SUGGEST": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "SUSTAIN": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "UNSURE": {
                "precision": 0.16071428571428573,
                "recall": 0.3,
                "f1-score": 0.20930232558139533,
                "support": 30.0
            },
            "WISH": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 2.0
            },
            "expressEMOJI": {
                "precision": 0.9545454545454546,
                "recall": 1.0,
                "f1-score": 0.9767441860465117,
                "support": 21.0
            },
            "accuracy": 0.5892857142857143,
            "macro avg": {
                "precision": 0.32628253826783243,
                "recall": 0.37767065114815984,
                "f1-score": 0.3385377159405857,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.6099589094295728,
                "recall": 0.5892857142857143,
                "f1-score": 0.5932171720465335,
                "support": 392.0
            }
        }
    },
    "hasoc2020": {
        "coarse labels": {
            "HOF": {
                "precision": 0.6045197740112994,
                "recall": 0.7985074626865671,
                "f1-score": 0.6881028938906752,
                "support": 134.0
            },
            "NOT": {
                "precision": 0.9226361031518625,
                "recall": 0.8214285714285714,
                "f1-score": 0.8690958164642375,
                "support": 392.0
            },
            "accuracy": 0.8155893536121673,
            "macro avg": {
                "precision": 0.763577938581581,
                "recall": 0.8099680170575693,
                "f1-score": 0.7785993551774564,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.8415950611274605,
                "recall": 0.8155893536121673,
                "f1-score": 0.8229873532991094,
                "support": 526.0
            }
        },
        "fine labels": {
            "HATE": {
                "precision": 0.16470588235294117,
                "recall": 0.5833333333333334,
                "f1-score": 0.25688073394495414,
                "support": 24.0
            },
            "NONE": {
                "precision": 0.934931506849315,
                "recall": 0.7222222222222222,
                "f1-score": 0.8149253731343283,
                "support": 378.0
            },
            "OFFN": {
                "precision": 0.2727272727272727,
                "recall": 0.25,
                "f1-score": 0.2608695652173913,
                "support": 36.0
            },
            "PRFN": {
                "precision": 0.5948275862068966,
                "recall": 0.7840909090909091,
                "f1-score": 0.6764705882352942,
                "support": 88.0
            },
            "accuracy": 0.6939163498098859,
            "macro avg": {
                "precision": 0.49179806203410636,
                "recall": 0.5849116161616161,
                "f1-score": 0.502286565132992,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.7975666543154,
                "recall": 0.6939163498098859,
                "f1-score": 0.7283795527984543,
                "support": 526.0
            }
        }
    },
    "germeval2019_task12": {
        "coarse labels": {
            "OFFENSE": {
                "precision": 0.6663395485770363,
                "recall": 0.7,
                "f1-score": 0.6827551533433885,
                "support": 970.0
            },
            "OTHER": {
                "precision": 0.8553677932405567,
                "recall": 0.8350315380883067,
                "f1-score": 0.8450773385710779,
                "support": 2061.0
            },
            "accuracy": 0.791817881887166,
            "macro avg": {
                "precision": 0.7608536709087965,
                "recall": 0.7675157690441533,
                "f1-score": 0.7639162459572333,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.7948737657500867,
                "recall": 0.791817881887166,
                "f1-score": 0.7931299549779209,
                "support": 3031.0
            }
        },
        "fine labels": {
            "ABUSE": {
                "precision": 0.36347517730496454,
                "recall": 0.5125,
                "f1-score": 0.4253112033195021,
                "support": 400.0
            },
            "INSULT": {
                "precision": 0.30407124681933845,
                "recall": 0.5206971677559913,
                "f1-score": 0.38393574297188754,
                "support": 459.0
            },
            "OTHER": {
                "precision": 0.8803471791692499,
                "recall": 0.6889859291606016,
                "f1-score": 0.772999455634186,
                "support": 2061.0
            },
            "PROFANITY": {
                "precision": 0.14705882352941177,
                "recall": 0.09009009009009009,
                "f1-score": 0.111731843575419,
                "support": 111.0
            },
            "accuracy": 0.6182777961068954,
            "macro avg": {
                "precision": 0.42373810670574114,
                "recall": 0.4530682967516707,
                "f1-score": 0.42349456137524866,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.6980131438111682,
                "recall": 0.6182777961068954,
                "f1-score": 0.6439805674862508,
                "support": 3031.0
            }
        }
    },
    "germeval2019_task3": {
        "offensive labels": {
            "EXPLICIT": {
                "precision": 0.9405099150141643,
                "recall": 0.8341708542713567,
                "f1-score": 0.8841544607190411,
                "support": 796.0
            },
            "IMPLICIT": {
                "precision": 0.4107142857142857,
                "recall": 0.6865671641791045,
                "f1-score": 0.5139664804469273,
                "support": 134.0
            },
            "accuracy": 0.8129032258064516,
            "macro avg": {
                "precision": 0.675612100364225,
                "recall": 0.7603690092252307,
                "f1-score": 0.6990604705829842,
                "support": 930.0
            },
            "weighted avg": {
                "precision": 0.8641737705774076,
                "recall": 0.8129032258064516,
                "f1-score": 0.8308155474325216,
                "support": 930.0
            }
        }
    },
    "germeval2021": {
        "toxic": {
            "0": {
                "precision": 0.7670753064798599,
                "recall": 0.7373737373737373,
                "f1-score": 0.7519313304721029,
                "support": 594.0
            },
            "1": {
                "precision": 0.5817694369973191,
                "recall": 0.62,
                "f1-score": 0.6002766251728907,
                "support": 350.0
            },
            "accuracy": 0.6938559322033898,
            "macro avg": {
                "precision": 0.6744223717385895,
                "recall": 0.6786868686868687,
                "f1-score": 0.6761039778224969,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.6983707997861213,
                "recall": 0.6938559322033898,
                "f1-score": 0.6957034206683697,
                "support": 944.0
            }
        },
        "engaging": {
            "0": {
                "precision": 0.8413461538461539,
                "recall": 0.7597684515195369,
                "f1-score": 0.7984790874524714,
                "support": 691.0
            },
            "1": {
                "precision": 0.48125,
                "recall": 0.6086956521739131,
                "f1-score": 0.537521815008726,
                "support": 253.0
            },
            "accuracy": 0.7192796610169492,
            "macro avg": {
                "precision": 0.661298076923077,
                "recall": 0.684232051846725,
                "f1-score": 0.6680004512305987,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7448373329530639,
                "recall": 0.7192796610169492,
                "f1-score": 0.7285403269352387,
                "support": 944.0
            }
        },
        "factClaiming": {
            "0": {
                "precision": 0.8432601880877743,
                "recall": 0.8539682539682539,
                "f1-score": 0.8485804416403785,
                "support": 630.0
            },
            "1": {
                "precision": 0.6993464052287581,
                "recall": 0.6815286624203821,
                "f1-score": 0.6903225806451613,
                "support": 314.0
            },
            "accuracy": 0.7966101694915254,
            "macro avg": {
                "precision": 0.7713032966582662,
                "recall": 0.767748458194318,
                "f1-score": 0.7694515111427699,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7953905611622116,
                "recall": 0.7966101694915254,
                "f1-score": 0.7959395853347659,
                "support": 944.0
            }
        }
    }
}

eurollm_finetuning = {
    "covid19": {
        "informativeness": {
            "Informative": {
                "precision": 0.9195402298850575,
                "recall": 0.9195402298850575,
                "f1-score": 0.9195402298850575,
                "support": 87.0
            },
            "Personal_Experience": {
                "precision": 0.625,
                "recall": 0.7142857142857143,
                "f1-score": 0.6666666666666666,
                "support": 7.0
            },
            "none": {
                "precision": 0.7647058823529411,
                "recall": 0.7428571428571429,
                "f1-score": 0.7536231884057971,
                "support": 35.0
            },
            "accuracy": 0.8604651162790697,
            "macro avg": {
                "precision": 0.7697487040793328,
                "recall": 0.7922276956759715,
                "f1-score": 0.779943361652507,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.8615481076151391,
                "recall": 0.8604651162790697,
                "f1-score": 0.8608021570610044,
                "support": 129.0
            }
        },
        "topic": {
            "Case_Report": {
                "precision": 0.75,
                "recall": 0.8918918918918919,
                "f1-score": 0.8148148148148148,
                "support": 37.0
            },
            "Consequences": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 6.0
            },
            "Governm_Decisions": {
                "precision": 0.8333333333333334,
                "recall": 0.45454545454545453,
                "f1-score": 0.5882352941176471,
                "support": 22.0
            },
            "Risk_Reduction": {
                "precision": 0.3333333333333333,
                "recall": 0.6666666666666666,
                "f1-score": 0.4444444444444444,
                "support": 3.0
            },
            "Vaccination": {
                "precision": 0.5333333333333333,
                "recall": 0.42105263157894735,
                "f1-score": 0.47058823529411764,
                "support": 19.0
            },
            "none": {
                "precision": 0.64,
                "recall": 0.7619047619047619,
                "f1-score": 0.6956521739130435,
                "support": 42.0
            },
            "accuracy": 0.6589147286821705,
            "macro avg": {
                "precision": 0.515,
                "recall": 0.5326769010979537,
                "f1-score": 0.502289160430678,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.6519121447028423,
                "recall": 0.6589147286821705,
                "f1-score": 0.6401645405194247,
                "support": 129.0
            }
        },
        "credibility": {
            "credible": {
                "precision": 0.9516129032258065,
                "recall": 0.7564102564102564,
                "f1-score": 0.8428571428571429,
                "support": 78.0
            },
            "non-credible": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "none": {
                "precision": 0.6716417910447762,
                "recall": 0.9375,
                "f1-score": 0.7826086956521741,
                "support": 48.0
            },
            "accuracy": 0.8062015503875969,
            "macro avg": {
                "precision": 0.5410848980901942,
                "recall": 0.5646367521367521,
                "f1-score": 0.5418219461697723,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.8253070730369161,
                "recall": 0.8062015503875969,
                "f1-score": 0.8008377870865233,
                "support": 129.0
            }
        }
    },
    "speech_acts_coarse": {
        "coarse labels": {
            "ASSERTIVE": {
                "precision": 0.6308724832214765,
                "recall": 0.6861313868613139,
                "f1-score": 0.6573426573426574,
                "support": 137.0
            },
            "COMMISSIVE": {
                "precision": 1.0,
                "recall": 0.25,
                "f1-score": 0.4,
                "support": 4.0
            },
            "DIRECTIVE": {
                "precision": 0.9444444444444444,
                "recall": 0.8031496062992126,
                "f1-score": 0.8680851063829786,
                "support": 127.0
            },
            "EXPRESSIVE": {
                "precision": 0.550561797752809,
                "recall": 0.6125,
                "f1-score": 0.5798816568047338,
                "support": 80.0
            },
            "OTHER": {
                "precision": 0.8571428571428571,
                "recall": 0.8571428571428571,
                "f1-score": 0.8571428571428571,
                "support": 14.0
            },
            "UNSURE": {
                "precision": 0.16129032258064516,
                "recall": 0.16666666666666666,
                "f1-score": 0.16393442622950818,
                "support": 30.0
            },
            "accuracy": 0.6709183673469388,
            "macro avg": {
                "precision": 0.6907186508570388,
                "recall": 0.5625984194950084,
                "f1-score": 0.5877311173171226,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.6919837452638539,
                "recall": 0.6709183673469388,
                "f1-score": 0.6765594844332814,
                "support": 392.0
            }
        }
    },
    "speech_acts_fine": {
        "fine labels": {
            "ADDRESS": {
                "precision": 0.9866666666666667,
                "recall": 0.9866666666666667,
                "f1-score": 0.9866666666666668,
                "support": 75.0
            },
            "AGREE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "ASSERT": {
                "precision": 0.5921052631578947,
                "recall": 0.3813559322033898,
                "f1-score": 0.46391752577319584,
                "support": 118.0
            },
            "COMMISSIVE": {
                "precision": 0.3333333333333333,
                "recall": 0.25,
                "f1-score": 0.28571428571428575,
                "support": 4.0
            },
            "COMPLAIN": {
                "precision": 0.3142857142857143,
                "recall": 0.21568627450980393,
                "f1-score": 0.2558139534883721,
                "support": 51.0
            },
            "EXCLUDED": {
                "precision": 1.0,
                "recall": 0.3333333333333333,
                "f1-score": 0.5,
                "support": 3.0
            },
            "GUESS": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 5.0
            },
            "OTHER": {
                "precision": 0.8125,
                "recall": 0.8666666666666667,
                "f1-score": 0.8387096774193549,
                "support": 15.0
            },
            "PREDICT": {
                "precision": 0.07407407407407407,
                "recall": 0.2857142857142857,
                "f1-score": 0.11764705882352941,
                "support": 7.0
            },
            "REJOICE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "REQUEST": {
                "precision": 0.38095238095238093,
                "recall": 0.7272727272727273,
                "f1-score": 0.5,
                "support": 33.0
            },
            "REQUIRE": {
                "precision": 0.11764705882352941,
                "recall": 0.125,
                "f1-score": 0.12121212121212122,
                "support": 16.0
            },
            "SUGGEST": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "SUSTAIN": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "UNSURE": {
                "precision": 0.20454545454545456,
                "recall": 0.3,
                "f1-score": 0.24324324324324326,
                "support": 30.0
            },
            "WISH": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 2.0
            },
            "expressEMOJI": {
                "precision": 0.9545454545454546,
                "recall": 1.0,
                "f1-score": 0.9767441860465117,
                "support": 21.0
            },
            "accuracy": 0.5178571428571429,
            "macro avg": {
                "precision": 0.3394503176696766,
                "recall": 0.32186446390393375,
                "f1-score": 0.31115698343454595,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.5550304694578523,
                "recall": 0.5178571428571429,
                "f1-score": 0.5206227819610313,
                "support": 392.0
            }
        }
    },
    "hasoc2020": {
        "coarse labels": {
            "HOF": {
                "precision": 0.5777777777777777,
                "recall": 0.7761194029850746,
                "f1-score": 0.6624203821656051,
                "support": 134.0
            },
            "NOT": {
                "precision": 0.9132947976878613,
                "recall": 0.8061224489795918,
                "f1-score": 0.8563685636856369,
                "support": 392.0
            },
            "accuracy": 0.7984790874524715,
            "macro avg": {
                "precision": 0.7455362877328195,
                "recall": 0.7911209259823333,
                "f1-score": 0.759394472925621,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.8278208800681822,
                "recall": 0.7984790874524715,
                "f1-score": 0.8069597113592409,
                "support": 526.0
            }
        },
        "fine labels": {
            "HATE": {
                "precision": 0.2127659574468085,
                "recall": 0.4166666666666667,
                "f1-score": 0.28169014084507044,
                "support": 24.0
            },
            "NONE": {
                "precision": 0.9369085173501577,
                "recall": 0.7857142857142857,
                "f1-score": 0.8546762589928057,
                "support": 378.0
            },
            "OFFN": {
                "precision": 0.23636363636363636,
                "recall": 0.3611111111111111,
                "f1-score": 0.2857142857142857,
                "support": 36.0
            },
            "PRFN": {
                "precision": 0.5514018691588785,
                "recall": 0.6704545454545454,
                "f1-score": 0.6051282051282051,
                "support": 88.0
            },
            "accuracy": 0.720532319391635,
            "macro avg": {
                "precision": 0.48435999507987026,
                "recall": 0.5584866522366523,
                "f1-score": 0.5068022226700918,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.7914263458786219,
                "recall": 0.720532319391635,
                "f1-score": 0.7478425582063851,
                "support": 526.0
            }
        }
    },
    "germeval2019_task12": {
        "coarse labels": {
            "OFFENSE": {
                "precision": 0.6364421416234888,
                "recall": 0.7597938144329897,
                "f1-score": 0.6926691729323309,
                "support": 970.0
            },
            "OTHER": {
                "precision": 0.8756006406833956,
                "recall": 0.7957302280446386,
                "f1-score": 0.8337569903406202,
                "support": 2061.0
            },
            "accuracy": 0.7842296271857473,
            "macro avg": {
                "precision": 0.7560213911534421,
                "recall": 0.7777620212388141,
                "f1-score": 0.7632130816364755,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.7990636086516867,
                "recall": 0.7842296271857473,
                "f1-score": 0.7886051649080763,
                "support": 3031.0
            }
        },
        "fine labels": {
            "ABUSE": {
                "precision": 0.2793914246196404,
                "recall": 0.505,
                "f1-score": 0.3597506678539626,
                "support": 400.0
            },
            "INSULT": {
                "precision": 0.3101123595505618,
                "recall": 0.3006535947712418,
                "f1-score": 0.30530973451327437,
                "support": 459.0
            },
            "OTHER": {
                "precision": 0.8592592592592593,
                "recall": 0.6754002911208151,
                "f1-score": 0.756316218418908,
                "support": 2061.0
            },
            "PROFANITY": {
                "precision": 0.13991769547325103,
                "recall": 0.3063063063063063,
                "f1-score": 0.19209039548022597,
                "support": 111.0
            },
            "accuracy": 0.5826459914219729,
            "macro avg": {
                "precision": 0.3971701847256781,
                "recall": 0.44684004804959077,
                "f1-score": 0.4033667540665927,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.6732307292683696,
                "recall": 0.5826459914219729,
                "f1-score": 0.6150205197436002,
                "support": 3031.0
            }
        }
    },
    "germeval2019_task3": {
        "offensive labels": {
            "EXPLICIT": {
                "precision": 0.917312661498708,
                "recall": 0.8919597989949749,
                "f1-score": 0.9044585987261147,
                "support": 796.0
            },
            "IMPLICIT": {
                "precision": 0.44871794871794873,
                "recall": 0.5223880597014925,
                "f1-score": 0.4827586206896552,
                "support": 134.0
            },
            "accuracy": 0.8387096774193549,
            "macro avg": {
                "precision": 0.6830153051083284,
                "recall": 0.7071739293482338,
                "f1-score": 0.693608609707885,
                "support": 930.0
            },
            "weighted avg": {
                "precision": 0.8497947136356739,
                "recall": 0.8387096774193549,
                "f1-score": 0.8436975266219366,
                "support": 930.0
            }
        }
    },
    "germeval2021": {
        "toxic": {
            "0": {
                "precision": 0.7611464968152867,
                "recall": 0.8047138047138047,
                "f1-score": 0.7823240589198036,
                "support": 594.0
            },
            "1": {
                "precision": 0.6329113924050633,
                "recall": 0.5714285714285714,
                "f1-score": 0.6006006006006006,
                "support": 350.0
            },
            "accuracy": 0.7182203389830508,
            "macro avg": {
                "precision": 0.697028944610175,
                "recall": 0.6880711880711881,
                "f1-score": 0.691462329760202,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7136017017479369,
                "recall": 0.7182203389830508,
                "f1-score": 0.7149477767039973,
                "support": 944.0
            }
        },
        "engaging": {
            "0": {
                "precision": 0.8343653250773994,
                "recall": 0.7800289435600579,
                "f1-score": 0.8062827225130891,
                "support": 691.0
            },
            "1": {
                "precision": 0.4899328859060403,
                "recall": 0.5770750988142292,
                "f1-score": 0.52994555353902,
                "support": 253.0
            },
            "accuracy": 0.725635593220339,
            "macro avg": {
                "precision": 0.6621491054917198,
                "recall": 0.6785520211871436,
                "f1-score": 0.6681141380260545,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.742054512460499,
                "recall": 0.725635593220339,
                "f1-score": 0.7322220193876234,
                "support": 944.0
            }
        },
        "factClaiming": {
            "0": {
                "precision": 0.8470394736842105,
                "recall": 0.8174603174603174,
                "f1-score": 0.8319870759289176,
                "support": 630.0
            },
            "1": {
                "precision": 0.6577380952380952,
                "recall": 0.7038216560509554,
                "f1-score": 0.6799999999999999,
                "support": 314.0
            },
            "accuracy": 0.7796610169491526,
            "macro avg": {
                "precision": 0.7523887844611529,
                "recall": 0.7606409867556364,
                "f1-score": 0.7559935379644588,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7840727016163289,
                "recall": 0.7796610169491526,
                "f1-score": 0.7814320527915446,
                "support": 944.0
            }
        }
    }
}

teuken_finetuning = {
    "covid19": {
        "informativeness": {
            "Informative": {
                "precision": 0.8791208791208791,
                "recall": 0.9195402298850575,
                "f1-score": 0.898876404494382,
                "support": 87.0
            },
            "Personal_Experience": {
                "precision": 0.3333333333333333,
                "recall": 0.5714285714285714,
                "f1-score": 0.4210526315789474,
                "support": 7.0
            },
            "none": {
                "precision": 0.7307692307692307,
                "recall": 0.5428571428571428,
                "f1-score": 0.6229508196721311,
                "support": 35.0
            },
            "accuracy": 0.7984496124031008,
            "macro avg": {
                "precision": 0.6477411477411477,
                "recall": 0.6779419813902572,
                "f1-score": 0.6476266185818201,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.8092540534400999,
                "recall": 0.7984496124031008,
                "f1-score": 0.7980844519425462,
                "support": 129.0
            }
        },
        "topic": {
            "Case_Report": {
                "precision": 0.6666666666666666,
                "recall": 0.7567567567567568,
                "f1-score": 0.7088607594936708,
                "support": 37.0
            },
            "Consequences": {
                "precision": 0.4,
                "recall": 0.3333333333333333,
                "f1-score": 0.3636363636363636,
                "support": 6.0
            },
            "Governm_Decisions": {
                "precision": 0.6153846153846154,
                "recall": 0.7272727272727273,
                "f1-score": 0.6666666666666667,
                "support": 22.0
            },
            "Risk_Reduction": {
                "precision": 0.5,
                "recall": 1.0,
                "f1-score": 0.6666666666666666,
                "support": 3.0
            },
            "Vaccination": {
                "precision": 0.4666666666666667,
                "recall": 0.3684210526315789,
                "f1-score": 0.4117647058823529,
                "support": 19.0
            },
            "none": {
                "precision": 0.6,
                "recall": 0.5,
                "f1-score": 0.5454545454545454,
                "support": 42.0
            },
            "accuracy": 0.5968992248062015,
            "macro avg": {
                "precision": 0.5414529914529915,
                "recall": 0.6142973116657328,
                "f1-score": 0.5605082846333777,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.5904790300139138,
                "recall": 0.5968992248062015,
                "f1-score": 0.5876663044233045,
                "support": 129.0
            }
        },
        "credibility": {
            "credible": {
                "precision": 0.828125,
                "recall": 0.6794871794871795,
                "f1-score": 0.7464788732394365,
                "support": 78.0
            },
            "non-credible": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "none": {
                "precision": 0.578125,
                "recall": 0.7708333333333334,
                "f1-score": 0.6607142857142857,
                "support": 48.0
            },
            "accuracy": 0.6976744186046512,
            "macro avg": {
                "precision": 0.46875,
                "recall": 0.48344017094017094,
                "f1-score": 0.46906438631790737,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.715843023255814,
                "recall": 0.6976744186046512,
                "f1-score": 0.6972064947826493,
                "support": 129.0
            }
        }
    },
    "speech_acts_coarse": {
        "coarse labels": {
            "ASSERTIVE": {
                "precision": 0.7160493827160493,
                "recall": 0.4233576642335766,
                "f1-score": 0.5321100917431192,
                "support": 137.0
            },
            "COMMISSIVE": {
                "precision": 0.6666666666666666,
                "recall": 0.5,
                "f1-score": 0.5714285714285715,
                "support": 4.0
            },
            "DIRECTIVE": {
                "precision": 0.8666666666666667,
                "recall": 0.7165354330708661,
                "f1-score": 0.7844827586206896,
                "support": 127.0
            },
            "EXPRESSIVE": {
                "precision": 0.49473684210526314,
                "recall": 0.5875,
                "f1-score": 0.5371428571428571,
                "support": 80.0
            },
            "OTHER": {
                "precision": 0.5238095238095238,
                "recall": 0.7857142857142857,
                "f1-score": 0.6285714285714286,
                "support": 14.0
            },
            "UNSURE": {
                "precision": 0.20689655172413793,
                "recall": 0.6,
                "f1-score": 0.3076923076923077,
                "support": 30.0
            },
            "accuracy": 0.5790816326530612,
            "macro avg": {
                "precision": 0.5791376056147178,
                "recall": 0.6021845638364547,
                "f1-score": 0.5602380025331622,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.673345091884976,
                "recall": 0.5790816326530612,
                "f1-score": 0.6015722066365996,
                "support": 392.0
            }
        }
    },
    "speech_acts_fine": {
        "fine labels": {
            "ADDRESS": {
                "precision": 1.0,
                "recall": 0.9733333333333334,
                "f1-score": 0.9864864864864865,
                "support": 75.0
            },
            "AGREE": {
                "precision": 0.5,
                "recall": 0.3333333333333333,
                "f1-score": 0.4,
                "support": 3.0
            },
            "ASSERT": {
                "precision": 0.6296296296296297,
                "recall": 0.288135593220339,
                "f1-score": 0.3953488372093023,
                "support": 118.0
            },
            "COMMISSIVE": {
                "precision": 0.375,
                "recall": 0.75,
                "f1-score": 0.5,
                "support": 4.0
            },
            "COMPLAIN": {
                "precision": 0.375,
                "recall": 0.35294117647058826,
                "f1-score": 0.3636363636363636,
                "support": 51.0
            },
            "EXCLUDED": {
                "precision": 0.2,
                "recall": 0.3333333333333333,
                "f1-score": 0.25,
                "support": 3.0
            },
            "GUESS": {
                "precision": 0.3333333333333333,
                "recall": 0.2,
                "f1-score": 0.25,
                "support": 5.0
            },
            "OTHER": {
                "precision": 0.7333333333333333,
                "recall": 0.7333333333333333,
                "f1-score": 0.7333333333333333,
                "support": 15.0
            },
            "PREDICT": {
                "precision": 0.1875,
                "recall": 0.42857142857142855,
                "f1-score": 0.26086956521739124,
                "support": 7.0
            },
            "REJOICE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "REQUEST": {
                "precision": 0.5909090909090909,
                "recall": 0.7878787878787878,
                "f1-score": 0.6753246753246752,
                "support": 33.0
            },
            "REQUIRE": {
                "precision": 0.5714285714285714,
                "recall": 0.25,
                "f1-score": 0.34782608695652173,
                "support": 16.0
            },
            "SUGGEST": {
                "precision": 0.16666666666666666,
                "recall": 0.3333333333333333,
                "f1-score": 0.2222222222222222,
                "support": 3.0
            },
            "SUSTAIN": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "UNSURE": {
                "precision": 0.175,
                "recall": 0.4666666666666667,
                "f1-score": 0.2545454545454546,
                "support": 30.0
            },
            "WISH": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 2.0
            },
            "expressEMOJI": {
                "precision": 0.9545454545454546,
                "recall": 1.0,
                "f1-score": 0.9767441860465117,
                "support": 21.0
            },
            "accuracy": 0.5382653061224489,
            "macro avg": {
                "precision": 0.3995497694027106,
                "recall": 0.42534472467496925,
                "f1-score": 0.3891963065281331,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.6133642210491701,
                "recall": 0.5382653061224489,
                "f1-score": 0.545598930270883,
                "support": 392.0
            }
        }
    },
    "hasoc2020": {
        "coarse labels": {
            "HOF": {
                "precision": 0.643312101910828,
                "recall": 0.753731343283582,
                "f1-score": 0.6941580756013745,
                "support": 134.0
            },
            "NOT": {
                "precision": 0.9105691056910569,
                "recall": 0.8571428571428571,
                "f1-score": 0.8830486202365309,
                "support": 392.0
            },
            "accuracy": 0.8307984790874525,
            "macro avg": {
                "precision": 0.7769406038009424,
                "recall": 0.8054371002132196,
                "f1-score": 0.7886033479189527,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.842484621838299,
                "recall": 0.8307984790874525,
                "f1-score": 0.8349282153294758,
                "support": 526.0
            }
        },
        "fine labels": {
            "HATE": {
                "precision": 0.21212121212121213,
                "recall": 0.5833333333333334,
                "f1-score": 0.3111111111111111,
                "support": 24.0
            },
            "NONE": {
                "precision": 0.9250936329588015,
                "recall": 0.6534391534391535,
                "f1-score": 0.7658914728682171,
                "support": 378.0
            },
            "OFFN": {
                "precision": 0.22077922077922077,
                "recall": 0.4722222222222222,
                "f1-score": 0.3008849557522124,
                "support": 36.0
            },
            "PRFN": {
                "precision": 0.49137931034482757,
                "recall": 0.6477272727272727,
                "f1-score": 0.5588235294117647,
                "support": 88.0
            },
            "accuracy": 0.6368821292775665,
            "macro avg": {
                "precision": 0.4623433440510155,
                "recall": 0.5891804954304956,
                "f1-score": 0.48417776728582634,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.7717979726382753,
                "recall": 0.6368821292775665,
                "f1-score": 0.6786729513425241,
                "support": 526.0
            }
        }
    },
    "germeval2019_task12": {
        "coarse labels": {
            "OFFENSE": {
                "precision": 0.5980230642504119,
                "recall": 0.7484536082474227,
                "f1-score": 0.6648351648351648,
                "support": 970.0
            },
            "OTHER": {
                "precision": 0.8657127132636213,
                "recall": 0.7632217370208637,
                "f1-score": 0.811242908715833,
                "support": 2061.0
            },
            "accuracy": 0.7584955460244144,
            "macro avg": {
                "precision": 0.7318678887570166,
                "recall": 0.7558376726341431,
                "f1-score": 0.738039036775499,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.7800449601976981,
                "recall": 0.7584955460244144,
                "f1-score": 0.764388566398364,
                "support": 3031.0
            }
        },
        "fine labels": {
            "ABUSE": {
                "precision": 0.3374384236453202,
                "recall": 0.685,
                "f1-score": 0.4521452145214521,
                "support": 400.0
            },
            "INSULT": {
                "precision": 0.34933333333333333,
                "recall": 0.28540305010893247,
                "f1-score": 0.31414868105515587,
                "support": 459.0
            },
            "OTHER": {
                "precision": 0.8744892002335085,
                "recall": 0.7268316351285784,
                "f1-score": 0.7938526762056174,
                "support": 2061.0
            },
            "PROFANITY": {
                "precision": 0.183206106870229,
                "recall": 0.21621621621621623,
                "f1-score": 0.19834710743801653,
                "support": 111.0
            },
            "accuracy": 0.6357637743319037,
            "macro avg": {
                "precision": 0.4361167660205978,
                "recall": 0.4783627253634318,
                "f1-score": 0.4396234198050605,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.6987718538442707,
                "recall": 0.6357637743319037,
                "f1-score": 0.6543052540410078,
                "support": 3031.0
            }
        }
    },
    "germeval2019_task3": {
        "offensive labels": {
            "EXPLICIT": {
                "precision": 0.931129476584022,
                "recall": 0.8492462311557789,
                "f1-score": 0.8883048620236531,
                "support": 796.0
            },
            "IMPLICIT": {
                "precision": 0.4117647058823529,
                "recall": 0.6268656716417911,
                "f1-score": 0.4970414201183432,
                "support": 134.0
            },
            "accuracy": 0.8172043010752689,
            "macro avg": {
                "precision": 0.6714470912331875,
                "recall": 0.738055951398785,
                "f1-score": 0.6926731410709981,
                "support": 930.0
            },
            "weighted avg": {
                "precision": 0.8562962730635664,
                "recall": 0.8172043010752689,
                "f1-score": 0.831929269319017,
                "support": 930.0
            }
        }
    },
    "germeval2021": {
        "toxic": {
            "0": {
                "precision": 0.7854671280276817,
                "recall": 0.7643097643097643,
                "f1-score": 0.7747440273037544,
                "support": 594.0
            },
            "1": {
                "precision": 0.6174863387978142,
                "recall": 0.6457142857142857,
                "f1-score": 0.6312849162011174,
                "support": 350.0
            },
            "accuracy": 0.7203389830508474,
            "macro avg": {
                "precision": 0.701476733412748,
                "recall": 0.705012025012025,
                "f1-score": 0.7030144717524358,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7231861150716927,
                "recall": 0.7203389830508474,
                "f1-score": 0.7215547382296834,
                "support": 944.0
            }
        },
        "engaging": {
            "0": {
                "precision": 0.827922077922078,
                "recall": 0.7380607814761215,
                "f1-score": 0.7804131599081867,
                "support": 691.0
            },
            "1": {
                "precision": 0.4481707317073171,
                "recall": 0.5810276679841897,
                "f1-score": 0.5060240963855421,
                "support": 253.0
            },
            "accuracy": 0.6959745762711864,
            "macro avg": {
                "precision": 0.6380464048146975,
                "recall": 0.6595442247301556,
                "f1-score": 0.6432186281468644,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7261454989047744,
                "recall": 0.6959745762711864,
                "f1-score": 0.7068745655530712,
                "support": 944.0
            }
        },
        "factClaiming": {
            "0": {
                "precision": 0.8162939297124601,
                "recall": 0.8111111111111111,
                "f1-score": 0.8136942675159236,
                "support": 630.0
            },
            "1": {
                "precision": 0.6257861635220126,
                "recall": 0.6337579617834395,
                "f1-score": 0.629746835443038,
                "support": 314.0
            },
            "accuracy": 0.7521186440677966,
            "macro avg": {
                "precision": 0.7210400466172363,
                "recall": 0.7224345364472753,
                "f1-score": 0.7217205514794808,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7529258803652138,
                "recall": 0.7521186440677966,
                "f1-score": 0.7525083632035443,
                "support": 944.0
            }
        }
    }
}

bueble_finetuning = {
    "covid19": {
        "informativeness": {
            "Informative": {
                "precision": 0.8913043478260869,
                "recall": 0.9425287356321839,
                "f1-score": 0.9162011173184358,
                "support": 87.0
            },
            "Personal_Experience": {
                "precision": 0.5,
                "recall": 0.5714285714285714,
                "f1-score": 0.5333333333333333,
                "support": 7.0
            },
            "none": {
                "precision": 0.7931034482758621,
                "recall": 0.6571428571428571,
                "f1-score": 0.71875,
                "support": 35.0
            },
            "accuracy": 0.8449612403100775,
            "macro avg": {
                "precision": 0.728135932033983,
                "recall": 0.7237000547345375,
                "f1-score": 0.7227614835505897,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.8434271236474786,
                "recall": 0.8449612403100775,
                "f1-score": 0.8418533375196686,
                "support": 129.0
            }
        },
        "topic": {
            "Case_Report": {
                "precision": 0.7333333333333333,
                "recall": 0.8918918918918919,
                "f1-score": 0.8048780487804879,
                "support": 37.0
            },
            "Consequences": {
                "precision": 0.4,
                "recall": 0.3333333333333333,
                "f1-score": 0.3636363636363636,
                "support": 6.0
            },
            "Governm_Decisions": {
                "precision": 0.5,
                "recall": 0.5454545454545454,
                "f1-score": 0.5217391304347826,
                "support": 22.0
            },
            "Risk_Reduction": {
                "precision": 1.0,
                "recall": 0.6666666666666666,
                "f1-score": 0.8,
                "support": 3.0
            },
            "Vaccination": {
                "precision": 0.4444444444444444,
                "recall": 0.631578947368421,
                "f1-score": 0.5217391304347826,
                "support": 19.0
            },
            "none": {
                "precision": 0.5769230769230769,
                "recall": 0.35714285714285715,
                "f1-score": 0.4411764705882353,
                "support": 42.0
            },
            "accuracy": 0.5891472868217055,
            "macro avg": {
                "precision": 0.609116809116809,
                "recall": 0.5710113736429526,
                "f1-score": 0.5755281906457753,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.5907639302988139,
                "recall": 0.5891472868217055,
                "f1-score": 0.575837380614172,
                "support": 129.0
            }
        },
        "credibility": {
            "credible": {
                "precision": 0.8591549295774648,
                "recall": 0.782051282051282,
                "f1-score": 0.8187919463087248,
                "support": 78.0
            },
            "non-credible": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "none": {
                "precision": 0.6607142857142857,
                "recall": 0.7708333333333334,
                "f1-score": 0.7115384615384616,
                "support": 48.0
            },
            "accuracy": 0.7596899224806202,
            "macro avg": {
                "precision": 0.5066230717639169,
                "recall": 0.5176282051282052,
                "f1-score": 0.5101101359490622,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.7653362032661083,
                "recall": 0.7596899224806202,
                "f1-score": 0.7598419997358657,
                "support": 129.0
            }
        }
    },
    "speech_acts_coarse": {
        "coarse labels": {
            "ASSERTIVE": {
                "precision": 0.631578947368421,
                "recall": 0.6131386861313869,
                "f1-score": 0.6222222222222222,
                "support": 137.0
            },
            "COMMISSIVE": {
                "precision": 0.13333333333333333,
                "recall": 0.5,
                "f1-score": 0.2105263157894737,
                "support": 4.0
            },
            "DIRECTIVE": {
                "precision": 0.900990099009901,
                "recall": 0.7165354330708661,
                "f1-score": 0.7982456140350876,
                "support": 127.0
            },
            "EXPRESSIVE": {
                "precision": 0.49,
                "recall": 0.6125,
                "f1-score": 0.5444444444444445,
                "support": 80.0
            },
            "OTHER": {
                "precision": 0.5,
                "recall": 0.5714285714285714,
                "f1-score": 0.5333333333333333,
                "support": 14.0
            },
            "UNSURE": {
                "precision": 0.2222222222222222,
                "recall": 0.2,
                "f1-score": 0.2105263157894737,
                "support": 30.0
            },
            "accuracy": 0.6122448979591837,
            "macro avg": {
                "precision": 0.47968743365564626,
                "recall": 0.5356004484384708,
                "f1-score": 0.4865497076023391,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.648857291744212,
                "recall": 0.6122448979591837,
                "f1-score": 0.6244942713927677,
                "support": 392.0
            }
        }
    },
    "speech_acts_fine": {
        "fine labels": {
            "ADDRESS": {
                "precision": 0.9315068493150684,
                "recall": 0.9066666666666666,
                "f1-score": 0.918918918918919,
                "support": 75.0
            },
            "AGREE": {
                "precision": 0.5,
                "recall": 0.6666666666666666,
                "f1-score": 0.5714285714285715,
                "support": 3.0
            },
            "ASSERT": {
                "precision": 0.4861111111111111,
                "recall": 0.2966101694915254,
                "f1-score": 0.368421052631579,
                "support": 118.0
            },
            "COMMISSIVE": {
                "precision": 0.18181818181818182,
                "recall": 0.5,
                "f1-score": 0.26666666666666666,
                "support": 4.0
            },
            "COMPLAIN": {
                "precision": 0.25,
                "recall": 0.21568627450980393,
                "f1-score": 0.23157894736842105,
                "support": 51.0
            },
            "EXCLUDED": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "GUESS": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 5.0
            },
            "OTHER": {
                "precision": 0.47058823529411764,
                "recall": 0.5333333333333333,
                "f1-score": 0.5,
                "support": 15.0
            },
            "PREDICT": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 7.0
            },
            "REJOICE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "REQUEST": {
                "precision": 0.525,
                "recall": 0.6363636363636364,
                "f1-score": 0.5753424657534246,
                "support": 33.0
            },
            "REQUIRE": {
                "precision": 0.2,
                "recall": 0.125,
                "f1-score": 0.15384615384615385,
                "support": 16.0
            },
            "SUGGEST": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "SUSTAIN": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "UNSURE": {
                "precision": 0.17333333333333334,
                "recall": 0.43333333333333335,
                "f1-score": 0.24761904761904763,
                "support": 30.0
            },
            "WISH": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 2.0
            },
            "expressEMOJI": {
                "precision": 0.9545454545454546,
                "recall": 1.0,
                "f1-score": 0.9767441860465117,
                "support": 21.0
            },
            "accuracy": 0.46683673469387754,
            "macro avg": {
                "precision": 0.274876656789251,
                "recall": 0.3125682400214686,
                "f1-score": 0.28297447119289965,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.4975272337037762,
                "recall": 0.46683673469387754,
                "f1-score": 0.46906153314575694,
                "support": 392.0
            }
        }
    },
    "hasoc2020": {
        "coarse labels": {
            "HOF": {
                "precision": 0.6791044776119403,
                "recall": 0.6791044776119403,
                "f1-score": 0.6791044776119403,
                "support": 134.0
            },
            "NOT": {
                "precision": 0.8903061224489796,
                "recall": 0.8903061224489796,
                "f1-score": 0.8903061224489796,
                "support": 392.0
            },
            "accuracy": 0.8365019011406845,
            "macro avg": {
                "precision": 0.7847053000304599,
                "recall": 0.7847053000304599,
                "f1-score": 0.7847053000304599,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.8365019011406845,
                "recall": 0.8365019011406845,
                "f1-score": 0.8365019011406845,
                "support": 526.0
            }
        },
        "fine labels": {
            "HATE": {
                "precision": 0.2222222222222222,
                "recall": 0.3333333333333333,
                "f1-score": 0.26666666666666666,
                "support": 24.0
            },
            "NONE": {
                "precision": 0.8925373134328358,
                "recall": 0.791005291005291,
                "f1-score": 0.8387096774193549,
                "support": 378.0
            },
            "OFFN": {
                "precision": 0.20967741935483872,
                "recall": 0.3611111111111111,
                "f1-score": 0.2653061224489796,
                "support": 36.0
            },
            "PRFN": {
                "precision": 0.6344086021505376,
                "recall": 0.6704545454545454,
                "f1-score": 0.6519337016574586,
                "support": 88.0
            },
            "accuracy": 0.720532319391635,
            "macro avg": {
                "precision": 0.4897113892901086,
                "recall": 0.5389760702260702,
                "f1-score": 0.5056540420481149,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.772031904747085,
                "recall": 0.720532319391635,
                "f1-score": 0.7421168141036801,
                "support": 526.0
            }
        }
    },
    "germeval2019_task12": {
        "coarse labels": {
            "OFFENSE": {
                "precision": 0.5859434682964094,
                "recall": 0.790721649484536,
                "f1-score": 0.6731022378236068,
                "support": 970.0
            },
            "OTHER": {
                "precision": 0.8821138211382114,
                "recall": 0.7370208636584182,
                "f1-score": 0.803066349458102,
                "support": 2061.0
            },
            "accuracy": 0.7542065324975256,
            "macro avg": {
                "precision": 0.7340286447173103,
                "recall": 0.7638712565714771,
                "f1-score": 0.7380842936408544,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.7873314911294526,
                "recall": 0.7542065324975256,
                "f1-score": 0.761474403471477,
                "support": 3031.0
            }
        },
        "fine labels": {
            "ABUSE": {
                "precision": 0.31260229132569556,
                "recall": 0.4775,
                "f1-score": 0.37784371909000986,
                "support": 400.0
            },
            "INSULT": {
                "precision": 0.3323353293413174,
                "recall": 0.48366013071895425,
                "f1-score": 0.3939662821650399,
                "support": 459.0
            },
            "OTHER": {
                "precision": 0.862533692722372,
                "recall": 0.621057738961669,
                "f1-score": 0.7221438645980255,
                "support": 2061.0
            },
            "PROFANITY": {
                "precision": 0.11194029850746269,
                "recall": 0.2702702702702703,
                "f1-score": 0.158311345646438,
                "support": 111.0
            },
            "accuracy": 0.5684592543714946,
            "macro avg": {
                "precision": 0.4048529029742119,
                "recall": 0.4631220349877234,
                "f1-score": 0.41306630287487833,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.6821808467611613,
                "recall": 0.5684592543714946,
                "f1-score": 0.6063606319541546,
                "support": 3031.0
            }
        }
    },
    "germeval2019_task3": {
        "offensive labels": {
            "EXPLICIT": {
                "precision": 0.9326647564469914,
                "recall": 0.8178391959798995,
                "f1-score": 0.8714859437751005,
                "support": 796.0
            },
            "IMPLICIT": {
                "precision": 0.375,
                "recall": 0.6492537313432836,
                "f1-score": 0.47540983606557374,
                "support": 134.0
            },
            "accuracy": 0.7935483870967742,
            "macro avg": {
                "precision": 0.6538323782234957,
                "recall": 0.7335464636615916,
                "f1-score": 0.6734478899203371,
                "support": 930.0
            },
            "weighted avg": {
                "precision": 0.8523130603567798,
                "recall": 0.7935483870967742,
                "f1-score": 0.8144169132018999,
                "support": 930.0
            }
        }
    },
    "germeval2021": {
        "toxic": {
            "0": {
                "precision": 0.74,
                "recall": 0.8097643097643098,
                "f1-score": 0.7733118971061093,
                "support": 594.0
            },
            "1": {
                "precision": 0.6156462585034014,
                "recall": 0.5171428571428571,
                "f1-score": 0.562111801242236,
                "support": 350.0
            },
            "accuracy": 0.701271186440678,
            "macro avg": {
                "precision": 0.6778231292517007,
                "recall": 0.6634535834535835,
                "f1-score": 0.6677118491741727,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.6938942695722358,
                "recall": 0.701271186440678,
                "f1-score": 0.6950067768175969,
                "support": 944.0
            }
        },
        "engaging": {
            "0": {
                "precision": 0.8330804248861912,
                "recall": 0.7945007235890015,
                "f1-score": 0.8133333333333332,
                "support": 691.0
            },
            "1": {
                "precision": 0.5017543859649123,
                "recall": 0.5652173913043478,
                "f1-score": 0.5315985130111524,
                "support": 253.0
            },
            "accuracy": 0.7330508474576272,
            "macro avg": {
                "precision": 0.6674174054255517,
                "recall": 0.6798590574466746,
                "f1-score": 0.6724659231722427,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.744282238607501,
                "recall": 0.7330508474576272,
                "f1-score": 0.7378260139037658,
                "support": 944.0
            }
        },
        "factClaiming": {
            "0": {
                "precision": 0.8081761006289309,
                "recall": 0.8158730158730159,
                "f1-score": 0.812006319115324,
                "support": 630.0
            },
            "1": {
                "precision": 0.6233766233766234,
                "recall": 0.6114649681528662,
                "f1-score": 0.6173633440514469,
                "support": 314.0
            },
            "accuracy": 0.7478813559322034,
            "macro avg": {
                "precision": 0.7157763620027771,
                "recall": 0.7136689920129411,
                "f1-score": 0.7146848315833854,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7467067829835659,
                "recall": 0.7478813559322034,
                "f1-score": 0.7472627871555173,
                "support": 944.0
            }
        }
    }
}


