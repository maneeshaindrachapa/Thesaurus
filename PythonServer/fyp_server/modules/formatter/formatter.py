import env_data


def responseFormat(data, response_code=200):
    formatted = {"response_code": response_code, "response_data": data}
    return formatted

def mainDataFormat(word,lang, pos_tag, definition, synset, example_sentences, translated):
    formatted = {"word": word, "language": lang, "posTag": pos_tag, "definitions": definition, "synonyms": synset,
                 "exampleSentences": example_sentences, "translated": translated,
                 "audio": (env_data.BASE_API_URL + "/readword?word=" + word +"&lang=" + lang)}
    return formatted
