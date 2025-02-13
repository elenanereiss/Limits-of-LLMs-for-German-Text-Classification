datasets={
    # "covid19": 
        # {
            # "file": 
                # {
                    # "train": "covid19_train.csv",
                    # "test": "covid19_test.csv"
                # },
            # "columns": ['title', 'text', 'informativeness', 'topic', 'credibility'],
            # "tasks": ['informativeness', 'topic', 'credibility'],
            # "definitions": 
                # {
                    # 'informativeness': 
                        # {
                            # 'Informative': 'Der Tweet ist informativ und enthält allgemeine Informationen. Er sollte einen gewissen Bezug zu COVID-19 haben.', 
                            # 'Personal_Experience': 'Der Text ist informativ und berichtet über persönliche Erfahrungen (bezüglich Krankheit, Impfung, Nebenwirkungen usw.).', 
                            # 'none': 'Der Text hat entweder keinen Bezug zu COVID-19, oder hat einen Bezug zu COVID-19, enthält aber keine Informationen, z.B. wenn es sich um eine persönliche Aussage (Meinung) ohne informativen Hintergrund handelt, oder wenn es sich um einen humorvollen oder sarkastischen Kommentar handelt.'
                        # },
                    # 'topic': 
                        # {
                            # 'Case_Report': 'Der Text ist ein Fallbericht oder im Text geht es um Statistiken.', 
                            # 'Consequences': 'Der Text berichtet über Folgen einer Covid-Infektion (Langzeit-Covid, psychologische Aspekte, etc.)', 
                            # 'Governm_Decisions': 'Der Text berichtet über Maßnahmen und Entscheidungen der Bundesregierung und ihre Auswirkungen auf Menschen, Länder und die Wirtschaft.', 
                            # 'Risk_Reduction': 'Im Text geht es um Möglichkeiten zur Minderung des Infektionsrisikos.', 
                            # 'Vaccination': 'Im Text geht es um Impfung: Allgemeine Informationen über den Impfstoff, Verfügbarkeit, Nebenwirkungen.', 
                            # 'none': 'Der Text behandelt keines der oben genannten Themen, oder es ist unklar, um welches Thema es sich handelt, z. B. weil der Kontext fehlt oder weil der Inhalt nur andeutet, worum es geht.'
                        # }, 
                    # 'credibility': 
                        # {
                            # 'credible': 'Der Text und sein Inhalt scheinen bis zu einem gewissen Grad glaubwürdig zu sein.',
                            # 'non-credible': 'Der Text und sein Inhalt scheinen nicht glaubwürdig zu sein und es ist sehr fraglich, ob man ihm trauen kann.', 
                            # 'none': 'Anhand des Textes ist es nicht möglich zu entscheiden, ob der Inhalt glaubwürdig ist oder nicht.'
                        # }
                # },
            # "questions": 
                # {
                    # 'informativeness': "Ist der Text informativ und hat der Text Bezug zu COVID-19? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n", 
                    # 'topic': "Über welches Thema wird es im Text gesprochen? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n",
                    # 'credibility': "Enthält der Text Tatsachenbehauptungen? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n"
                # }
        # },
    "speech_acts_coarse": 
        {
            "file": 
                {
                    "train": "data/speechacts_coarse_train.csv",
                    "test": "data/speechacts_coarse_test.csv"
                },
            "columns": ['text', 'coarse labels', 'fine labels'],
            "tasks": ['coarse labels'],
            "definitions": 
                {
                    'coarse labels': 
                        {
                            'ASSERTIVE': 'Der Text macht Aussagen über die Welt.', 
                            'COMMISSIVE': 'Im Text gibt es eine Verpflichtung, etwas zu tun.', 
                            'DIRECTIVE': 'Durch eine Aussage im Text wird es versucht, Menschen dazu zu bringen, etwas zu tun.', 
                            'EXPRESSIVE': 'Im Text wird es eine Haltung oder ein Gefühl ausgedrückt.', 
                            'OTHER': 'Eine Äußerung im Text kann aufgrund von fehlendem oder unzureichendem Kontext nicht eingeordnet werden.', 
                            'UNSURE': 'Der Text kann man zu keiner der oben genannten Kategorien einordnen.'
                        }
                },
            "questions": 
                {
                    'coarse labels': "Zu welcher Sprechaktkategorie gehört der Text? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n", 
                }
        },
    "speech_acts_fine": 
        {
            "file": 
                {
                    "train": "data/speechacts_fine_train.csv",
                    "test": "data/speechacts_fine_test.csv"
                },
            "columns": ['text', 'coarse labels', 'fine labels'],
            "tasks": ['fine labels'],
            "definitions": 
                {
                    'fine labels': 
                        {
                            'ADDRESS': 'Im Text wird jemand angesprochen. Es wird für Erwähnungen verwendet (z.B. @xyz).', 
                            'AGREE': 'Im Text wird es mit etwas oder mit jemandem einverstanden.', 
                            'ASSERT': 'Der Text enthält eine Behauptung.', 
                            'COMMISSIVE': 'Im Text gibt es eine Verpflichtung, etwas zu tun.', 
                            'COMPLAIN': 'Der Text enthält eine negative Einstellung zu jemandem oder zu etwas.',
                            'EXCLUDED': 'Der Text kann man zu keiner der oben genannten Kategorien einordnen.', 
                            'GUESS': 'Der Text wird eine Behauptung durch eine Wahrscheinlichkeit oder eine Möglichkeit abgeschwächt .', 
                            'OTHER': 'Eine Äußerung im Text kann aufgrund von fehlendem oder unzureichendem Kontext nicht eingeordnet werden.', 
                            'PREDICT': 'Der Text enthält eine Behauptung, die sich auf die Zukunft bezieht.',
                            'REJOICE': 'Der Text enthält eine positive Einstellung zu jemandem oder zu etwas.', 
                            'REQUEST': 'Der Text enthählt eine Bitte gegenüber jemanden, etwas zu tun. Es wird normalerweise für Fragen verwendet.', 
                            'REQUIRE': 'Der Text enthählt eine (starke) Aufforderung gegenüber jemanden, etwas zu tun. Es wird normalerweise für Imperative verwendet.', 
                            'SUGGEST': 'Im Text wird es jemandem etwas vorschlagen. Es kann sowohl mit positiven als auch mit negativen Absichten verwendet werden.', 
                            'SUSTAIN': 'Der Text enthält eine Behauptung, die argumentiert ist.', 
                            'UNSURE': 'Der Text kann man zu keiner der oben genannten Kategorien einordnen.', 
                            'WISH': 'Im Text wird es etwas gewünscht.', 
                            'expressEMOJI': 'Eine Aussage ist in Form eines Emoji oder einer Reihe von Emojis.'
                        }
                },
            "questions": 
                {
                    'fine labels': "Zu welcher Sprechaktkategorie gehört der Text? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n", 
                }
        },
    "hasoc2020":
        {
            "file": 
                {
                    "train": "https://raw.githubusercontent.com/roushan-raj/HASOC-2020/refs/heads/master/Dataset/Train%20Data/hasoc_2020_de_train.xlsx",
                    "test": "https://raw.githubusercontent.com/roushan-raj/HASOC-2020/refs/heads/master/Dataset/Test%20Data/german_test_1509.csv"
                },
            "columns": ['tweet_id', 'text', 'coarse labels', 'fine labels', 'id'],
            "tasks": ['coarse labels', 'fine labels'],
            "definitions": 
                {
                    'coarse labels': 
                        {
                            'HOF': 'Der Text enthält hasserfüllte, beleidigende und anstößige Inhalte.',
                            'NOT': 'Der Text enthält keine hasserfüllten, beleidigenden oder anstößigen Inhalte.'
                        },
                    'fine labels': 
                        {
                            'HATE': 'Der Text enthält hasserfüllte Inhalte.', 
                            'NONE': 'Der Text enthält keine hasserfüllten, beleidigenden oder anstößigen Inhalte.', 
                            'OFFN': 'Der Text enthält beleidigende Inhalte.', 
                            'PRFN': 'Der Text enthält anstößige Wörter.'
                        }
                },
            "questions": 
                {
                    'coarse labels': "Enthält der Text eine Form von beleidigender Sprache? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n", 
                    'fine labels': "Enthält der Text eine Form von beleidigender Sprache? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n"
                }, 
        },
    "germeval2019_task12": 
        {
            "file": 
                {
                    "train": "https://raw.githubusercontent.com/TharinduDR/Germeval-Task-2/refs/heads/master/data/german/germeval2019_training_subtask12.txt",
                    "test": "https://fz.h-da.de/fileadmin/Daten_ohne_Zuordnung/Dokumente_ohne_Zuordnung/germeval2019GoldLabelsSubtask1_2.txt"
                },
            "columns": ['text', 'coarse labels', 'fine labels'],
            "tasks": ['coarse labels', 'fine labels'],
            "definitions": 
                {
                    'coarse labels': 
                        {
                            'OFFENSE': 'Der Text enthält eine Form von beidigender Sprache.', 
                            'OTHER': 'Der Text enthält keine Form von beidigender Sprache.'
                        },
                    'fine labels': 
                        {
                            'PROFANITY': 'Der Text enthält Schimpfwörtern, der Text will aber eindeutig niemanden beleidigen.',
                            'INSULT': 'Im Gegensatz zu PROFANITY will der Text eindeutig jemanden beleidigen.', 
                            'ABUSE': 'Im Gegensatz zu INSULT beleidigt der Text nicht nur eine Person, sondern stellt die stärkere Form der Beleidigung dar.', 
                            'OTHER': 'Der Text enthält keine Form von beidigender Sprache.', 
                        }
                },
            "questions": 
                {
                    'coarse labels': "Enthält der Text eine Form von beleidigender Sprache? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n", 
                    'fine labels': "Enthält der Text eine Form von beleidigender Sprache? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n"
                }, 
        },
    "germeval2019_task3": 
        {
            "file": 
                {
                    "train": "https://raw.githubusercontent.com/TharinduDR/Germeval-Task-2/refs/heads/master/data/german/germeval2019.training_subtask3.txt",
                    "test": "https://fz.h-da.de/fileadmin/Daten_ohne_Zuordnung/Dokumente_ohne_Zuordnung/germeval2019GoldLabelsSubtask3.txt"
                },
            "columns": ['text', 'coarse labels', 'fine labels', 'offensive labels'],
            "tasks": ['offensive labels'],
            "definitions": 
                {
                    'offensive labels': 
                        {
                            'EXPLICIT': 'Der Text ist beleidigend und bringt zum Ausdruck eindeutig Hass, Verurteilung oder Überlegenheit gegenüber einem explizit oder implizit genannten Ziel.', 
                            'IMPLICIT': 'Der Text ist beleidigend. Der Ausdruck von Hass, Verurteilung, Überlegenheit usw. gegenüber einem explizit oder implizit genannten Ziel muss aus der Beschreibung von (angenommenen) Eigenschaften des Ziels abgeleitet werden, die beleidigend, erniedrigend, kränkend, demütigend usw. sind.'
                        }
                },
            "questions": 
                {
                    'offensive labels': "Der Text enthält eine Form von beleidigender Sprache. Geht es um eine explizite oder implizite Form von beleidigender Sprache? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n"
                }, 
        },
    "germeval2021": 
        {
            "file": 
                {
                    "train": "https://raw.githubusercontent.com/germeval2021toxic/SharedTask/refs/heads/main/Data%20Sets/GermEval21_TrainData.csv",
                    "test": "https://raw.githubusercontent.com/germeval2021toxic/SharedTask/refs/heads/main/Data%20Sets/GermEval21_TestData.csv"
                },
            "columns": ['comment_id', 'text', 'toxic', 'engaging', 'factClaiming'],
            "tasks": ['toxic', 'engaging', 'factClaiming'],
            "definitions": 
                {
                    'toxic': 
                        {
                            '0': 'Der Text enthält keine toxische Inhalte.', 
                            '1': 'Der Text enthält toxische Inhalte.'
                        }, 
                    'engaging': 
                        {
                            '0': 'Der Text enthält keine Inhalte, die die Leser dazu anregen, sich an der Diskussion zu beteiligen.', 
                            '1': 'Der Text enthält rationale, respektvolle und gegenseitige Kommentare, die die Leser dazu ermutigen können, sich an der Diskussion zu beteiligen, die positive Wahrnehmung von Diskussionsanbietern erhöhen und einen fruchtbareren und weniger gewalttätigen Austausch fördern können.'
                        },
                    'factClaiming': 
                        {
                            '0': 'Der Text enthält keine Tatsachenbehauptung.', 
                            '1': 'Der Text enthält eine Tatsachenbehauptung.'
                        }
                }, 
            "questions": 
                {
                    'toxic': "Enthält der Text toxische Inhalte? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n", 
                    'engaging': "Regt der Text Leser dazu an, sich an der Diskussion zu beteiligen? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n",
                    'factClaiming': "Enthält der Text eine Tatsachenbehauptung? Antworte bitte mit einem Wort und als Antwort verwende eine Kategorie aus dieser Liste:\n- {}\n" 
                }
        },
}