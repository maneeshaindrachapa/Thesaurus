import env_data

endPoints = {'Thesaurus': {"method": "POST",
                           "url": env_data.BASE_API_URL + '/thesaurus',
                           "input": {'type': "JSON", 'format': {"word": "<word_here>", "language": "<lang_here>"}},
                           "output": {'type': "JSON",
                                      'format': {'response_code': "<code_here>",
                                                 "response_data": {"word": "<word_here>",
                                                                   "language": "<lang_here>",
                                                                   "posTag": "<tag_here>",
                                                                   "definitions": "<definition_here>",
                                                                   "synonyms": [
                                                                       {"term": 'syn_1', "similarity": '<val>'},
                                                                       {"term": 'syn_2', "similarity": '<val>'},
                                                                       {"term": 'syn_1', "similarity": '<val>'}],
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
                                     },
'Read word': {"method": "get",
                                     "url": env_data.BASE_API_URL + '/readword?word=<your_word>&lang=<language>',
                                     }
             }


def generateDoc():
    doc = {'Complete API End Points (Host: ' + env_data.BASE_API_URL + ")": endPoints}
    return doc
