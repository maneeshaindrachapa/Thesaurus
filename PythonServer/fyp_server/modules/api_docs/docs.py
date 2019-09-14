import env_data

endPoints = {'Thesaurus': {"method": "POST",
                           "url": env_data.BASE_API_URL + '/thesaurus',
                           "input": {'type': "JSON", 'format': {"word": "<word_here>", "language": "<lang_here>"}},
                           "output": {'type': "JSON",
                                      'format': {'response_code': "<code_here>",
                                                 "response_data": {"word": "<word_here>", "posTag": "<tag_here>",
                                                                   "definition": "<definition_here>",
                                                                   "synonyms": ['syn_1', 'syn_2', 'syn_3'],
                                                                   "exampleSentences": ['sentence_1', 'sentence_2',
                                                                                        'sentence_3'],
                                                                   "translated": "<translated_word>",
                                                                   "audio": "<audio_url_here>"}
                                                 }
                                      }
                           },

             'Language Identifier': {"method": "POST",
                                     "url": env_data.BASE_API_URL + '/language',
                                     "input": {'type': "JSON", 'format': {"word": "<word_here>"}},
                                     "output": {'type': "JSON", 'format': {"response_code": "<code_here>",
                                                                           "response_data": {
                                                                               "language": "<identified_lang_here>"
                                                                           }
                                                                           }
                                                }
                                     }
             }


def generateDoc():
    doc = {'Complete API End Points (Host: '+env_data.BASE_API_URL+")": endPoints}
    return doc
