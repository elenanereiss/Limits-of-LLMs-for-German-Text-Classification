llama_few = {
    "covid19": {
        "informativeness": {
            "Informative": {
                "precision": 0.9315068493150684,
                "recall": 0.7816091954022989,
                "f1-score": 0.85,
                "support": 87.0
            },
            "Personal_Experience": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 7.0
            },
            "none": {
                "precision": 0.5714285714285714,
                "recall": 0.9142857142857143,
                "f1-score": 0.7032967032967034,
                "support": 35.0
            },
            "accuracy": 0.7751937984496124,
            "macro avg": {
                "precision": 0.5009784735812133,
                "recall": 0.5652983032293377,
                "f1-score": 0.5177655677655678,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.783264309227992,
                "recall": 0.7751937984496124,
                "f1-score": 0.7640727489564699,
                "support": 129.0
            }
        },
        "topic": {
            "Case_Report": {
                "precision": 0.8095238095238095,
                "recall": 0.4594594594594595,
                "f1-score": 0.5862068965517241,
                "support": 37.0
            },
            "Consequences": {
                "precision": 0.16129032258064516,
                "recall": 0.8333333333333334,
                "f1-score": 0.2702702702702703,
                "support": 6.0
            },
            "Governm_Decisions": {
                "precision": 0.6666666666666666,
                "recall": 0.2727272727272727,
                "f1-score": 0.3870967741935484,
                "support": 22.0
            },
            "Risk_Reduction": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "Vaccination": {
                "precision": 0.8888888888888888,
                "recall": 0.42105263157894735,
                "f1-score": 0.5714285714285714,
                "support": 19.0
            },
            "none": {
                "precision": 0.509090909090909,
                "recall": 0.6666666666666666,
                "f1-score": 0.5773195876288659,
                "support": 42.0
            },
            "micro avg": {
                "precision": 0.5079365079365079,
                "recall": 0.49612403100775193,
                "f1-score": 0.5019607843137255,
                "support": 129.0
            },
            "macro avg": {
                "precision": 0.5059100994584865,
                "recall": 0.44220656062761327,
                "f1-score": 0.3987203500121634,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.6500581133739423,
                "recall": 0.49612403100775193,
                "f1-score": 0.5188524911926256,
                "support": 129.0
            }
        },
        "credibility": {
            "credible": {
                "precision": 1.0,
                "recall": 0.44871794871794873,
                "f1-score": 0.6194690265486725,
                "support": 78.0
            },
            "non-credible": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "none": {
                "precision": 0.6122448979591837,
                "recall": 0.625,
                "f1-score": 0.6185567010309279,
                "support": 48.0
            },
            "micro avg": {
                "precision": 0.6565656565656566,
                "recall": 0.5038759689922481,
                "f1-score": 0.5701754385964912,
                "support": 129.0
            },
            "macro avg": {
                "precision": 0.5374149659863946,
                "recall": 0.3579059829059829,
                "f1-score": 0.4126752425265335,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.8324632178452777,
                "recall": 0.5038759689922481,
                "f1-score": 0.604723300157217,
                "support": 129.0
            }
        }
    },
    "speech_acts_coarse": {
        "coarse labels": {
            "ASSERTIVE": {
                "precision": 0.5227272727272727,
                "recall": 0.3357664233576642,
                "f1-score": 0.4088888888888889,
                "support": 137.0
            },
            "COMMISSIVE": {
                "precision": 0.3333333333333333,
                "recall": 0.25,
                "f1-score": 0.2857142857142857,
                "support": 4.0
            },
            "DIRECTIVE": {
                "precision": 0.5614035087719298,
                "recall": 0.5039370078740157,
                "f1-score": 0.5311203319502075,
                "support": 127.0
            },
            "EXPRESSIVE": {
                "precision": 0.8571428571428571,
                "recall": 0.075,
                "f1-score": 0.13793103448275862,
                "support": 80.0
            },
            "OTHER": {
                "precision": 0.17073170731707318,
                "recall": 0.5,
                "f1-score": 0.2545454545454545,
                "support": 14.0
            },
            "UNSURE": {
                "precision": 0.06504065040650407,
                "recall": 0.26666666666666666,
                "f1-score": 0.10457516339869281,
                "support": 30.0
            },
            "micro avg": {
                "precision": 0.35106382978723405,
                "recall": 0.336734693877551,
                "f1-score": 0.34375,
                "support": 392.0
            },
            "macro avg": {
                "precision": 0.41839655494982836,
                "recall": 0.3218950163163911,
                "f1-score": 0.2871291931633814,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.5539747635129271,
                "recall": 0.336734693877551,
                "f1-score": 0.36313339566971714,
                "support": 392.0
            }
        }
    },
    "speech_acts_fine": {
        "fine labels": {
            "ADDRESS": {
                "precision": 1.0,
                "recall": 0.5733333333333334,
                "f1-score": 0.7288135593220338,
                "support": 75.0
            },
            "AGREE": {
                "precision": 0.02702702702702703,
                "recall": 0.6666666666666666,
                "f1-score": 0.05194805194805195,
                "support": 3.0
            },
            "ASSERT": {
                "precision": 0.5625,
                "recall": 0.07627118644067797,
                "f1-score": 0.13432835820895522,
                "support": 118.0
            },
            "COMMISSIVE": {
                "precision": 1.0,
                "recall": 0.25,
                "f1-score": 0.4,
                "support": 4.0
            },
            "COMPLAIN": {
                "precision": 0.3559322033898305,
                "recall": 0.4117647058823529,
                "f1-score": 0.38181818181818183,
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
                "precision": 0.45,
                "recall": 0.6,
                "f1-score": 0.5142857142857142,
                "support": 15.0
            },
            "PREDICT": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 7.0
            },
            "REJOICE": {
                "precision": 0.019230769230769232,
                "recall": 0.3333333333333333,
                "f1-score": 0.03636363636363636,
                "support": 3.0
            },
            "REQUEST": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 33.0
            },
            "REQUIRE": {
                "precision": 0.25,
                "recall": 0.0625,
                "f1-score": 0.1,
                "support": 16.0
            },
            "SUGGEST": {
                "precision": 1.0,
                "recall": 0.3333333333333333,
                "f1-score": 0.5,
                "support": 3.0
            },
            "SUSTAIN": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "UNSURE": {
                "precision": 0.061224489795918366,
                "recall": 0.1,
                "f1-score": 0.0759493670886076,
                "support": 30.0
            },
            "WISH": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 2.0
            },
            "expressEMOJI": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 21.0
            },
            "micro avg": {
                "precision": 0.23393316195372751,
                "recall": 0.23214285714285715,
                "f1-score": 0.2330345710627401,
                "support": 392.0
            },
            "macro avg": {
                "precision": 0.27799496996726736,
                "recall": 0.20042367994057045,
                "f1-score": 0.17197099229618712,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.4572781899375824,
                "recall": 0.23214285714285715,
                "f1-score": 0.26770967418983554,
                "support": 392.0
            }
        }
    },
    "hasoc2020": {
        "coarse labels": {
            "HOF": {
                "precision": 0.48344370860927155,
                "recall": 0.5447761194029851,
                "f1-score": 0.512280701754386,
                "support": 134.0
            },
            "NOT": {
                "precision": 0.9148936170212766,
                "recall": 0.4387755102040816,
                "f1-score": 0.593103448275862,
                "support": 392.0
            },
            "micro avg": {
                "precision": 0.7227138643067846,
                "recall": 0.46577946768060835,
                "f1-score": 0.5664739884393064,
                "support": 526.0
            },
            "macro avg": {
                "precision": 0.699168662815274,
                "recall": 0.4917758148035334,
                "f1-score": 0.5526920750151241,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.8049805224828571,
                "recall": 0.46577946768060835,
                "f1-score": 0.5725136231163985,
                "support": 526.0
            }
        },
        "fine labels": {
            "HATE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 24.0
            },
            "NONE": {
                "precision": 0.9682539682539683,
                "recall": 0.32275132275132273,
                "f1-score": 0.48412698412698413,
                "support": 378.0
            },
            "OFFN": {
                "precision": 0.09345794392523364,
                "recall": 0.2777777777777778,
                "f1-score": 0.13986013986013987,
                "support": 36.0
            },
            "PRFN": {
                "precision": 0.5046728971962616,
                "recall": 0.6136363636363636,
                "f1-score": 0.5538461538461539,
                "support": 88.0
            },
            "micro avg": {
                "precision": 0.5360230547550432,
                "recall": 0.35361216730038025,
                "f1-score": 0.4261168384879725,
                "support": 526.0
            },
            "macro avg": {
                "precision": 0.39159620234386583,
                "recall": 0.30354136604136606,
                "f1-score": 0.29445831945831946,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.7866458192672613,
                "recall": 0.35361216730038025,
                "f1-score": 0.45013959424605815,
                "support": 526.0
            }
        }
    },
    "germeval2019_task12": {
        "coarse labels": {
            "OFFENSE": {
                "precision": 0.36759220886862826,
                "recall": 0.9144329896907216,
                "f1-score": 0.5243866390777416,
                "support": 970.0
            },
            "OTHER": {
                "precision": 0.9354838709677419,
                "recall": 0.08442503639010189,
                "f1-score": 0.1548731642189586,
                "support": 2061.0
            },
            "micro avg": {
                "precision": 0.4082339361292805,
                "recall": 0.3500494886176179,
                "f1-score": 0.37690941385435167,
                "support": 3031.0
            },
            "macro avg": {
                "precision": 0.651538039918185,
                "recall": 0.49942901304041176,
                "f1-score": 0.3396299016483501,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.7537435502035913,
                "recall": 0.3500494886176179,
                "f1-score": 0.2731272290863356,
                "support": 3031.0
            }
        },
        "fine labels": {
            "PROFANITY": {
                "precision": 0.0981012658227848,
                "recall": 0.27927927927927926,
                "f1-score": 0.1451990632318501,
                "support": 111.0
            },
            "INSULT": {
                "precision": 0.39215686274509803,
                "recall": 0.2178649237472767,
                "f1-score": 0.2801120448179272,
                "support": 459.0
            },
            "ABUSE": {
                "precision": 0.325,
                "recall": 0.0325,
                "f1-score": 0.05909090909090909,
                "support": 400.0
            },
            "OTHER": {
                "precision": 0.8175465838509317,
                "recall": 0.5109170305676856,
                "f1-score": 0.6288444311734847,
                "support": 2061.0
            },
            "micro avg": {
                "precision": 0.6303317535545023,
                "recall": 0.394919168591224,
                "f1-score": 0.48559837728194727,
                "support": 3031.0
            },
            "macro avg": {
                "precision": 0.40820117810470363,
                "recall": 0.2601403083985604,
                "f1-score": 0.27831161207854277,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.6617791982260308,
                "recall": 0.394919168591224,
                "f1-score": 0.48313205571596146,
                "support": 3031.0
            }
        }
    },
    "germeval2019_task3": {
        "offensive labels": {
            "EXPLICIT": {
                "precision": 1.0,
                "recall": 0.017587939698492462,
                "f1-score": 0.0345679012345679,
                "support": 796.0
            },
            "IMPLICIT": {
                "precision": 0.1462882096069869,
                "recall": 1.0,
                "f1-score": 0.25523809523809526,
                "support": 134.0
            },
            "accuracy": 0.15913978494623657,
            "macro avg": {
                "precision": 0.5731441048034934,
                "recall": 0.5087939698492462,
                "f1-score": 0.14490299823633157,
                "support": 930.0
            },
            "weighted avg": {
                "precision": 0.876992064610039,
                "recall": 0.15913978494623657,
                "f1-score": 0.06636339155335572,
                "support": 930.0
            }
        }
    },
    "germeval2021": {
        "toxic": {
            "0": {
                "precision": 0.7193347193347194,
                "recall": 0.5824915824915825,
                "f1-score": 0.6437209302325582,
                "support": 594.0
            },
            "1": {
                "precision": 0.46436285097192226,
                "recall": 0.6142857142857143,
                "f1-score": 0.5289052890528906,
                "support": 350.0
            },
            "accuracy": 0.5942796610169492,
            "macro avg": {
                "precision": 0.5918487851533208,
                "recall": 0.5983886483886485,
                "f1-score": 0.5863131096427243,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.6248006579713942,
                "recall": 0.5942796610169492,
                "f1-score": 0.601151571744334,
                "support": 944.0
            }
        },
        "engaging": {
            "0": {
                "precision": 0.7446808510638298,
                "recall": 0.40520984081041966,
                "f1-score": 0.5248359887535146,
                "support": 691.0
            },
            "1": {
                "precision": 0.27676240208877284,
                "recall": 0.4189723320158103,
                "f1-score": 0.3333333333333333,
                "support": 253.0
            },
            "micro avg": {
                "precision": 0.5085638998682477,
                "recall": 0.4088983050847458,
                "f1-score": 0.4533176746917205,
                "support": 944.0
            },
            "macro avg": {
                "precision": 0.5107216265763013,
                "recall": 0.412091086413115,
                "f1-score": 0.4290846610434239,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.61927474132793,
                "recall": 0.4088983050847458,
                "f1-score": 0.47351165419704644,
                "support": 944.0
            }
        },
        "factClaiming": {
            "0": {
                "precision": 0.7746781115879828,
                "recall": 0.573015873015873,
                "f1-score": 0.6587591240875912,
                "support": 630.0
            },
            "1": {
                "precision": 0.4372384937238494,
                "recall": 0.6656050955414012,
                "f1-score": 0.5277777777777778,
                "support": 314.0
            },
            "accuracy": 0.6038135593220338,
            "macro avg": {
                "precision": 0.6059583026559161,
                "recall": 0.6193104842786371,
                "f1-score": 0.5932684509326844,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.6624365437814808,
                "recall": 0.6038135593220338,
                "f1-score": 0.6151911762684372,
                "support": 944.0
            }
        }
    }
}

eurollm_few = {
    "covid19": {
        "informativeness": {
            "Informative": {
                "precision": 0.8191489361702128,
                "recall": 0.8850574712643678,
                "f1-score": 0.850828729281768,
                "support": 87.0
            },
            "Personal_Experience": {
                "precision": 0.6666666666666666,
                "recall": 0.2857142857142857,
                "f1-score": 0.4,
                "support": 7.0
            },
            "none": {
                "precision": 0.76,
                "recall": 0.5428571428571428,
                "f1-score": 0.6333333333333333,
                "support": 35.0
            },
            "micro avg": {
                "precision": 0.8032786885245902,
                "recall": 0.7596899224806202,
                "f1-score": 0.7808764940239044,
                "support": 129.0
            },
            "macro avg": {
                "precision": 0.7486052009456264,
                "recall": 0.5712096332785989,
                "f1-score": 0.6280540208717005,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.7948265435153115,
                "recall": 0.7596899224806202,
                "f1-score": 0.7673547760789183,
                "support": 129.0
            }
        },
        "topic": {
            "Case_Report": {
                "precision": 0.3333333333333333,
                "recall": 0.10810810810810811,
                "f1-score": 0.16326530612244897,
                "support": 37.0
            },
            "Consequences": {
                "precision": 0.0851063829787234,
                "recall": 0.6666666666666666,
                "f1-score": 0.1509433962264151,
                "support": 6.0
            },
            "Governm_Decisions": {
                "precision": 0.14285714285714285,
                "recall": 0.045454545454545456,
                "f1-score": 0.06896551724137931,
                "support": 22.0
            },
            "Risk_Reduction": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "Vaccination": {
                "precision": 0.4782608695652174,
                "recall": 0.5789473684210527,
                "f1-score": 0.5238095238095238,
                "support": 19.0
            },
            "none": {
                "precision": 0.4,
                "recall": 0.047619047619047616,
                "f1-score": 0.0851063829787234,
                "support": 42.0
            },
            "micro avg": {
                "precision": 0.2018348623853211,
                "recall": 0.17054263565891473,
                "f1-score": 0.18487394957983194,
                "support": 129.0
            },
            "macro avg": {
                "precision": 0.23992628812240283,
                "recall": 0.2411326227115701,
                "f1-score": 0.1653483543964151,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.32460298678916244,
                "recall": 0.17054263565891473,
                "f1-score": 0.17046951256346343,
                "support": 129.0
            }
        },
        "credibility": {
            "credible": {
                "precision": 0.8305084745762712,
                "recall": 0.6282051282051282,
                "f1-score": 0.7153284671532847,
                "support": 78.0
            },
            "non-credible": {
                "precision": 0.06060606060606061,
                "recall": 0.6666666666666666,
                "f1-score": 0.1111111111111111,
                "support": 3.0
            },
            "none": {
                "precision": 0.5625,
                "recall": 0.1875,
                "f1-score": 0.28125,
                "support": 48.0
            },
            "micro avg": {
                "precision": 0.5555555555555556,
                "recall": 0.46511627906976744,
                "f1-score": 0.5063291139240507,
                "support": 129.0
            },
            "macro avg": {
                "precision": 0.48453817839411056,
                "recall": 0.4941239316239316,
                "f1-score": 0.3692298594214653,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.7128796837113747,
                "recall": 0.46511627906976744,
                "f1-score": 0.5397593315603839,
                "support": 129.0
            }
        }
    },
    "speech_acts_coarse": {
        "coarse labels": {
            "ASSERTIVE": {
                "precision": 0.4266666666666667,
                "recall": 0.23357664233576642,
                "f1-score": 0.3018867924528302,
                "support": 137.0
            },
            "COMMISSIVE": {
                "precision": 0.013333333333333334,
                "recall": 0.25,
                "f1-score": 0.02531645569620253,
                "support": 4.0
            },
            "DIRECTIVE": {
                "precision": 0.3,
                "recall": 0.14173228346456693,
                "f1-score": 0.1925133689839572,
                "support": 127.0
            },
            "EXPRESSIVE": {
                "precision": 0.47435897435897434,
                "recall": 0.4625,
                "f1-score": 0.46835443037974683,
                "support": 80.0
            },
            "OTHER": {
                "precision": 0.03571428571428571,
                "recall": 0.14285714285714285,
                "f1-score": 0.05714285714285714,
                "support": 14.0
            },
            "UNSURE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 30.0
            },
            "micro avg": {
                "precision": 0.25,
                "recall": 0.22959183673469388,
                "f1-score": 0.2393617021276596,
                "support": 392.0
            },
            "macro avg": {
                "precision": 0.20834554334554334,
                "recall": 0.2051110114429127,
                "f1-score": 0.17420231744259898,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.3445290423861853,
                "recall": 0.22959183673469388,
                "f1-score": 0.26575844051062464,
                "support": 392.0
            }
        }
    },
    "speech_acts_fine": {
        "fine labels": {
            "ADDRESS": {
                "precision": 0.25,
                "recall": 0.04,
                "f1-score": 0.06896551724137931,
                "support": 75.0
            },
            "AGREE": {
                "precision": 0.047619047619047616,
                "recall": 0.3333333333333333,
                "f1-score": 0.08333333333333333,
                "support": 3.0
            },
            "ASSERT": {
                "precision": 0.4,
                "recall": 0.03389830508474576,
                "f1-score": 0.0625,
                "support": 118.0
            },
            "COMMISSIVE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 4.0
            },
            "COMPLAIN": {
                "precision": 0.25675675675675674,
                "recall": 0.37254901960784315,
                "f1-score": 0.304,
                "support": 51.0
            },
            "EXCLUDED": {
                "precision": 0.06451612903225806,
                "recall": 0.6666666666666666,
                "f1-score": 0.11764705882352941,
                "support": 3.0
            },
            "GUESS": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 5.0
            },
            "OTHER": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 15.0
            },
            "PREDICT": {
                "precision": 0.03333333333333333,
                "recall": 0.14285714285714285,
                "f1-score": 0.05405405405405406,
                "support": 7.0
            },
            "REJOICE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "REQUEST": {
                "precision": 0.08695652173913043,
                "recall": 0.06060606060606061,
                "f1-score": 0.07142857142857142,
                "support": 33.0
            },
            "REQUIRE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
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
                "precision": 0.1111111111111111,
                "recall": 0.1,
                "f1-score": 0.10526315789473684,
                "support": 30.0
            },
            "WISH": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 2.0
            },
            "expressEMOJI": {
                "precision": 0.4166666666666667,
                "recall": 0.23809523809523808,
                "f1-score": 0.30303030303030304,
                "support": 21.0
            },
            "micro avg": {
                "precision": 0.11869436201780416,
                "recall": 0.10204081632653061,
                "f1-score": 0.10973936899862825,
                "support": 392.0
            },
            "macro avg": {
                "precision": 0.0980564450740179,
                "recall": 0.11694151566182531,
                "f1-score": 0.06883658798858279,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.2412429387974655,
                "recall": 0.10204081632653061,
                "f1-score": 0.10436583496319833,
                "support": 392.0
            }
        }
    },
    "hasoc2020": {
        "coarse labels": {
            "HOF": {
                "precision": 0.41379310344827586,
                "recall": 0.6268656716417911,
                "f1-score": 0.49851632047477745,
                "support": 134.0
            },
            "NOT": {
                "precision": 0.8529411764705882,
                "recall": 0.5918367346938775,
                "f1-score": 0.6987951807228916,
                "support": 392.0
            },
            "micro avg": {
                "precision": 0.6652631578947369,
                "recall": 0.6007604562737643,
                "f1-score": 0.6313686313686314,
                "support": 526.0
            },
            "macro avg": {
                "precision": 0.6333671399594321,
                "recall": 0.6093512031678343,
                "f1-score": 0.5986557505988346,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.7410669525447519,
                "recall": 0.6007604562737643,
                "f1-score": 0.6477735699372503,
                "support": 526.0
            }
        },
        "fine labels": {
            "HATE": {
                "precision": 0.10869565217391304,
                "recall": 0.20833333333333334,
                "f1-score": 0.14285714285714285,
                "support": 24.0
            },
            "NONE": {
                "precision": 0.9306930693069307,
                "recall": 0.24867724867724866,
                "f1-score": 0.3924843423799583,
                "support": 378.0
            },
            "OFFN": {
                "precision": 0.06872852233676977,
                "recall": 0.5555555555555556,
                "f1-score": 0.12232415902140673,
                "support": 36.0
            },
            "PRFN": {
                "precision": 0.3673469387755102,
                "recall": 0.20454545454545456,
                "f1-score": 0.26277372262773724,
                "support": 88.0
            },
            "micro avg": {
                "precision": 0.2813141683778234,
                "recall": 0.26045627376425856,
                "f1-score": 0.2704837117472853,
                "support": 526.0
            },
            "macro avg": {
                "precision": 0.3688660456482809,
                "recall": 0.30427789802789806,
                "f1-score": 0.23010984172156126,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.7399456906208409,
                "recall": 0.26045627376425856,
                "f1-score": 0.34090382160495664,
                "support": 526.0
            }
        }
    },
    "germeval2019_task12": {
        "coarse labels": {
            "OFFENSE": {
                "precision": 0.482421875,
                "recall": 0.7639175257731958,
                "f1-score": 0.5913806863527534,
                "support": 970.0
            },
            "OTHER": {
                "precision": 0.8648648648648649,
                "recall": 0.5744784085395439,
                "f1-score": 0.6903790087463557,
                "support": 2061.0
            },
            "micro avg": {
                "precision": 0.6626506024096386,
                "recall": 0.6351039260969977,
                "f1-score": 0.6485849056603774,
                "support": 3031.0
            },
            "macro avg": {
                "precision": 0.6736433699324325,
                "recall": 0.6691979671563699,
                "f1-score": 0.6408798475495545,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.7424730139348356,
                "recall": 0.6351039260969977,
                "f1-score": 0.6586969326256714,
                "support": 3031.0
            }
        },
        "fine labels": {
            "PROFANITY": {
                "precision": 0.0627177700348432,
                "recall": 0.16216216216216217,
                "f1-score": 0.09045226130653267,
                "support": 111.0
            },
            "INSULT": {
                "precision": 0.16630196936542668,
                "recall": 0.49673202614379086,
                "f1-score": 0.24918032786885247,
                "support": 459.0
            },
            "ABUSE": {
                "precision": 0.23157894736842105,
                "recall": 0.33,
                "f1-score": 0.2721649484536082,
                "support": 400.0
            },
            "OTHER": {
                "precision": 0.868421052631579,
                "recall": 0.17612809315866085,
                "f1-score": 0.2928600242033078,
                "support": 2061.0
            },
            "micro avg": {
                "precision": 0.2800453514739229,
                "recall": 0.2444737710326625,
                "f1-score": 0.2610533732605249,
                "support": 3031.0
            },
            "macro avg": {
                "precision": 0.33225493485006746,
                "recall": 0.29125557036615346,
                "f1-score": 0.2261643904580753,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.6485455773123231,
                "recall": 0.2444737710326625,
                "f1-score": 0.2761017686444372,
                "support": 3031.0
            }
        }
    },
    "germeval2019_task3": {
        "offensive labels": {
            "EXPLICIT": {
                "precision": 0.9060150375939849,
                "recall": 0.3027638190954774,
                "f1-score": 0.4538606403013183,
                "support": 796.0
            },
            "IMPLICIT": {
                "precision": 0.1615798922800718,
                "recall": 0.6716417910447762,
                "f1-score": 0.26049204052098407,
                "support": 134.0
            },
            "micro avg": {
                "precision": 0.402187120291616,
                "recall": 0.35591397849462364,
                "f1-score": 0.37763833428408444,
                "support": 930.0
            },
            "macro avg": {
                "precision": 0.5337974649370284,
                "recall": 0.4872028050701268,
                "f1-score": 0.3571763404111512,
                "support": 930.0
            },
            "weighted avg": {
                "precision": 0.7987523392369265,
                "recall": 0.35591397849462364,
                "f1-score": 0.4259989280749045,
                "support": 930.0
            }
        }
    },
    "germeval2021": {
        "toxic": {
            "0": {
                "precision": 0.6807095343680709,
                "recall": 0.5168350168350169,
                "f1-score": 0.5875598086124402,
                "support": 594.0
            },
            "1": {
                "precision": 0.4359673024523161,
                "recall": 0.45714285714285713,
                "f1-score": 0.44630404463040446,
                "support": 350.0
            },
            "micro avg": {
                "precision": 0.5709046454767727,
                "recall": 0.4947033898305085,
                "f1-score": 0.5300794551645857,
                "support": 944.0
            },
            "macro avg": {
                "precision": 0.5583384184101935,
                "recall": 0.48698893698893697,
                "f1-score": 0.5169319266214223,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.589968240755238,
                "recall": 0.4947033898305085,
                "f1-score": 0.535187438491982,
                "support": 944.0
            }
        },
        "engaging": {
            "0": {
                "precision": 0.7747035573122529,
                "recall": 0.5672937771345875,
                "f1-score": 0.6549707602339181,
                "support": 691.0
            },
            "1": {
                "precision": 0.2874493927125506,
                "recall": 0.28063241106719367,
                "f1-score": 0.284,
                "support": 253.0
            },
            "micro avg": {
                "precision": 0.6148738379814077,
                "recall": 0.4904661016949153,
                "f1-score": 0.5456688273423689,
                "support": 944.0
            },
            "macro avg": {
                "precision": 0.5310764750124017,
                "recall": 0.4239630941008906,
                "f1-score": 0.46948538011695906,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.6441153119269514,
                "recall": 0.49046610169491517,
                "f1-score": 0.5555474526712261,
                "support": 944.0
            }
        },
        "factClaiming": {
            "0": {
                "precision": 0.7279549718574109,
                "recall": 0.6158730158730159,
                "f1-score": 0.6672398968185727,
                "support": 630.0
            },
            "1": {
                "precision": 0.4411764705882353,
                "recall": 0.3821656050955414,
                "f1-score": 0.40955631399317405,
                "support": 314.0
            },
            "micro avg": {
                "precision": 0.631055900621118,
                "recall": 0.538135593220339,
                "f1-score": 0.5809033733562036,
                "support": 944.0
            },
            "macro avg": {
                "precision": 0.584565721222823,
                "recall": 0.49901931048427867,
                "f1-score": 0.5383981054058733,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.6325646652911809,
                "recall": 0.538135593220339,
                "f1-score": 0.5815273491414803,
                "support": 944.0
            }
        }
    }
}

teuken_few = {
    "covid19": {
        "informativeness": {
            "Informative": {
                "precision": 0.8901098901098901,
                "recall": 0.9310344827586207,
                "f1-score": 0.9101123595505618,
                "support": 87.0
            },
            "Personal_Experience": {
                "precision": 0.4,
                "recall": 0.2857142857142857,
                "f1-score": 0.3333333333333333,
                "support": 7.0
            },
            "none": {
                "precision": 0.75,
                "recall": 0.6857142857142857,
                "f1-score": 0.7164179104477612,
                "support": 35.0
            },
            "micro avg": {
                "precision": 0.8359375,
                "recall": 0.8294573643410853,
                "f1-score": 0.8326848249027238,
                "support": 129.0
            },
            "macro avg": {
                "precision": 0.68003663003663,
                "recall": 0.6341543513957307,
                "f1-score": 0.6532878677772187,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.8255004685237243,
                "recall": 0.8294573643410853,
                "f1-score": 0.8262615153480918,
                "support": 129.0
            }
        },
        "topic": {
            "Case_Report": {
                "precision": 1.0,
                "recall": 0.02702702702702703,
                "f1-score": 0.05263157894736842,
                "support": 37.0
            },
            "Consequences": {
                "precision": 0.4,
                "recall": 0.3333333333333333,
                "f1-score": 0.36363636363636365,
                "support": 6.0
            },
            "Governm_Decisions": {
                "precision": 0.6666666666666666,
                "recall": 0.18181818181818182,
                "f1-score": 0.2857142857142857,
                "support": 22.0
            },
            "Risk_Reduction": {
                "precision": 0.03571428571428571,
                "recall": 0.6666666666666666,
                "f1-score": 0.06779661016949153,
                "support": 3.0
            },
            "Vaccination": {
                "precision": 1.0,
                "recall": 0.2631578947368421,
                "f1-score": 0.4166666666666667,
                "support": 19.0
            },
            "none": {
                "precision": 0.6226415094339622,
                "recall": 0.7857142857142857,
                "f1-score": 0.6947368421052632,
                "support": 42.0
            },
            "micro avg": {
                "precision": 0.373015873015873,
                "recall": 0.3643410852713178,
                "f1-score": 0.3686274509803922,
                "support": 129.0
            },
            "macro avg": {
                "precision": 0.6208370769691524,
                "recall": 0.3762862315493894,
                "f1-score": 0.3135303912065732,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.7699593249615189,
                "recall": 0.3643410852713178,
                "f1-score": 0.3698752306525682,
                "support": 129.0
            }
        },
        "credibility": {
            "credible": {
                "precision": 0.9130434782608695,
                "recall": 0.2692307692307692,
                "f1-score": 0.4158415841584158,
                "support": 78.0
            },
            "non-credible": {
                "precision": 0.3333333333333333,
                "recall": 0.3333333333333333,
                "f1-score": 0.3333333333333333,
                "support": 3.0
            },
            "none": {
                "precision": 0.42718446601941745,
                "recall": 0.9166666666666666,
                "f1-score": 0.5827814569536424,
                "support": 48.0
            },
            "accuracy": 0.5116279069767442,
            "macro avg": {
                "precision": 0.5578537592045402,
                "recall": 0.5064102564102564,
                "f1-score": 0.44398545814846385,
                "support": 129.0
            },
            "weighted avg": {
                "precision": 0.7187770982424796,
                "recall": 0.5116279069767442,
                "f1-score": 0.4760399495979168,
                "support": 129.0
            }
        }
    },
    "speech_acts_coarse": {
        "coarse labels": {
            "ASSERTIVE": {
                "precision": 0.41304347826086957,
                "recall": 0.8321167883211679,
                "f1-score": 0.5520581113801453,
                "support": 137.0
            },
            "COMMISSIVE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 4.0
            },
            "DIRECTIVE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 127.0
            },
            "EXPRESSIVE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 80.0
            },
            "OTHER": {
                "precision": 0.6666666666666666,
                "recall": 0.42857142857142855,
                "f1-score": 0.5217391304347826,
                "support": 14.0
            },
            "UNSURE": {
                "precision": 0.04807692307692308,
                "recall": 0.16666666666666666,
                "f1-score": 0.07462686567164178,
                "support": 30.0
            },
            "accuracy": 0.31887755102040816,
            "macro avg": {
                "precision": 0.18796451133407654,
                "recall": 0.23789248059321053,
                "f1-score": 0.1914040179144283,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.17184336109025553,
                "recall": 0.31887755102040816,
                "f1-score": 0.2172834567737656,
                "support": 392.0
            }
        }
    },
    "speech_acts_fine": {
        "fine labels": {
            "ADDRESS": {
                "precision": 0.6454545454545455,
                "recall": 0.9466666666666667,
                "f1-score": 0.7675675675675676,
                "support": 75.0
            },
            "AGREE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "ASSERT": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 118.0
            },
            "COMMISSIVE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 4.0
            },
            "COMPLAIN": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
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
                "precision": 0.06976744186046512,
                "recall": 0.4,
                "f1-score": 0.1188118811881188,
                "support": 15.0
            },
            "PREDICT": {
                "precision": 0.0472972972972973,
                "recall": 1.0,
                "f1-score": 0.09032258064516129,
                "support": 7.0
            },
            "REJOICE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 3.0
            },
            "REQUEST": {
                "precision": 0.3333333333333333,
                "recall": 0.030303030303030304,
                "f1-score": 0.05555555555555555,
                "support": 33.0
            },
            "REQUIRE": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
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
                "precision": 0.09090909090909091,
                "recall": 0.03333333333333333,
                "f1-score": 0.04878048780487805,
                "support": 30.0
            },
            "WISH": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 2.0
            },
            "expressEMOJI": {
                "precision": 0.625,
                "recall": 0.47619047619047616,
                "f1-score": 0.5405405405405406,
                "support": 21.0
            },
            "micro avg": {
                "precision": 0.24615384615384617,
                "recall": 0.24489795918367346,
                "f1-score": 0.24552429667519182,
                "support": 392.0
            },
            "macro avg": {
                "precision": 0.10657421816792542,
                "recall": 0.1697937356760886,
                "f1-score": 0.09538697725304834,
                "support": 392.0
            },
            "weighted avg": {
                "precision": 0.19550754169732576,
                "recall": 0.24489795918367346,
                "f1-score": 0.1903829162467768,
                "support": 392.0
            }
        }
    },
    "hasoc2020": {
        "coarse labels": {
            "HOF": {
                "precision": 0.26120857699805067,
                "recall": 1.0,
                "f1-score": 0.4142194744976816,
                "support": 134.0
            },
            "NOT": {
                "precision": 1.0,
                "recall": 0.03316326530612245,
                "f1-score": 0.06419753086419754,
                "support": 392.0
            },
            "accuracy": 0.279467680608365,
            "macro avg": {
                "precision": 0.6306042884990253,
                "recall": 0.5165816326530612,
                "f1-score": 0.23920850268093957,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.811790778170606,
                "recall": 0.279467680608365,
                "f1-score": 0.1533666191662638,
                "support": 526.0
            }
        },
        "fine labels": {
            "HATE": {
                "precision": 0.18181818181818182,
                "recall": 0.16666666666666666,
                "f1-score": 0.17391304347826086,
                "support": 24.0
            },
            "NONE": {
                "precision": 0.7354709418837675,
                "recall": 0.9708994708994709,
                "f1-score": 0.8369441277080958,
                "support": 378.0
            },
            "OFFN": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 36.0
            },
            "PRFN": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 88.0
            },
            "micro avg": {
                "precision": 0.7080152671755725,
                "recall": 0.7053231939163498,
                "f1-score": 0.7066666666666667,
                "support": 526.0
            },
            "macro avg": {
                "precision": 0.22932228092548734,
                "recall": 0.2843915343915344,
                "f1-score": 0.2527142927965892,
                "support": 526.0
            },
            "weighted avg": {
                "precision": 0.5368282364937271,
                "recall": 0.7053231939163498,
                "f1-score": 0.6093893409071074,
                "support": 526.0
            }
        }
    },
    "germeval2019_task12": {
        "coarse labels": {
            "OFFENSE": {
                "precision": 0.32002639392939625,
                "recall": 1.0,
                "f1-score": 0.48487878030492376,
                "support": 970.0
            },
            "OTHER": {
                "precision": 0.0,
                "recall": 0.0,
                "f1-score": 0.0,
                "support": 2061.0
            },
            "accuracy": 0.32002639392939625,
            "macro avg": {
                "precision": 0.16001319696469812,
                "recall": 0.5,
                "f1-score": 0.24243939015246188,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.10241689281145311,
                "recall": 0.32002639392939625,
                "f1-score": 0.1551740075538687,
                "support": 3031.0
            }
        },
        "fine labels": {
            "PROFANITY": {
                "precision": 0.03787506148548942,
                "recall": 0.6936936936936937,
                "f1-score": 0.07182835820895522,
                "support": 111.0
            },
            "INSULT": {
                "precision": 0.20562770562770563,
                "recall": 0.4139433551198257,
                "f1-score": 0.274765003615329,
                "support": 459.0
            },
            "ABUSE": {
                "precision": 0.36363636363636365,
                "recall": 0.06,
                "f1-score": 0.10300429184549356,
                "support": 400.0
            },
            "OTHER": {
                "precision": 1.0,
                "recall": 0.0019408054342552159,
                "f1-score": 0.00387409200968523,
                "support": 2061.0
            },
            "micro avg": {
                "precision": 0.09745622728774364,
                "recall": 0.09732761464863081,
                "f1-score": 0.09739187850775834,
                "support": 3031.0
            },
            "macro avg": {
                "precision": 0.4017847826873897,
                "recall": 0.29239446356194365,
                "f1-score": 0.11336793641986576,
                "support": 3031.0
            },
            "weighted avg": {
                "precision": 0.7604888796313269,
                "recall": 0.09732761464863081,
                "f1-score": 0.060467273108145404,
                "support": 3031.0
            }
        }
    },
    "germeval2019_task3": {
        "offensive labels": {
            "EXPLICIT": {
                "precision": 0.8571428571428571,
                "recall": 0.9949748743718593,
                "f1-score": 0.9209302325581395,
                "support": 796.0
            },
            "IMPLICIT": {
                "precision": 0.3333333333333333,
                "recall": 0.014925373134328358,
                "f1-score": 0.02857142857142857,
                "support": 134.0
            },
            "accuracy": 0.853763440860215,
            "macro avg": {
                "precision": 0.5952380952380952,
                "recall": 0.5049501237530938,
                "f1-score": 0.47475083056478407,
                "support": 930.0
            },
            "weighted avg": {
                "precision": 0.7816692268305171,
                "recall": 0.853763440860215,
                "f1-score": 0.7923538027363983,
                "support": 930.0
            }
        }
    },
    "germeval2021": {
        "toxic": {
            "0": {
                "precision": 0.835820895522388,
                "recall": 0.18855218855218855,
                "f1-score": 0.3076923076923077,
                "support": 594.0
            },
            "1": {
                "precision": 0.4049382716049383,
                "recall": 0.9371428571428572,
                "f1-score": 0.5655172413793104,
                "support": 350.0
            },
            "accuracy": 0.4661016949152542,
            "macro avg": {
                "precision": 0.6203795835636632,
                "recall": 0.5628475228475228,
                "f1-score": 0.43660477453580904,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.6760656853835031,
                "recall": 0.4661016949152542,
                "f1-score": 0.4032841792923617,
                "support": 944.0
            }
        },
        "engaging": {
            "0": {
                "precision": 0.8833333333333333,
                "recall": 0.15340086830680175,
                "f1-score": 0.26140567200986436,
                "support": 691.0
            },
            "1": {
                "precision": 0.29004854368932037,
                "recall": 0.9446640316205533,
                "f1-score": 0.4438254410399257,
                "support": 253.0
            },
            "accuracy": 0.3654661016949153,
            "macro avg": {
                "precision": 0.5866909385113268,
                "recall": 0.5490324499636775,
                "f1-score": 0.35261555652489507,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.7243279818715375,
                "recall": 0.3654661016949153,
                "f1-score": 0.3102957160401668,
                "support": 944.0
            }
        },
        "factClaiming": {
            "0": {
                "precision": 0.8376068376068376,
                "recall": 0.15555555555555556,
                "f1-score": 0.26238286479250333,
                "support": 630.0
            },
            "1": {
                "precision": 0.3567110036275695,
                "recall": 0.9394904458598726,
                "f1-score": 0.5170902716914987,
                "support": 314.0
            },
            "accuracy": 0.4163135593220339,
            "macro avg": {
                "precision": 0.5971589206172035,
                "recall": 0.5475230007077141,
                "f1-score": 0.389736568242001,
                "support": 944.0
            },
            "weighted avg": {
                "precision": 0.6776478419823777,
                "recall": 0.4163135593220339,
                "f1-score": 0.3471054556466183,
                "support": 944.0
            }
        }
    }
}