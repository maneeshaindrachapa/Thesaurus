import env_data

def formatData(word, pos_tag, definition, synset, example_sentences, translated):
    formatted = {"word": word, "pos": pos_tag, "definition": definition, "synonyms": synset,
                 "exampleSentences": example_sentences, "translated": translated, "audio": (env_data.BASE_API_URL+"/readword?word="+word)}
    return formatted
