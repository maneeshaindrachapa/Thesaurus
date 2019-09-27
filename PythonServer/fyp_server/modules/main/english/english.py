import requests
from modules.formatter import formatter
import modules.tts.tts as tts
import modules.translator.translator_v2 as translator

api_url = 'https://tuna.thesaurus.com/pageData/'

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}


# filter out postag from response
def getPosTag(response):
    return response.json()['data']['definitionData']['definitions'][0]['pos']


# filter out definition from response
def getDefinition(response):
    return response.json()['data']['definitionData']['definitions'][0]['definition']


# filter out syn set from response
def getSynset(response):
    syn_set = []

    for synonym in response.json()['data']['definitionData']['definitions'][0]['synonyms']:
        syn = {"term": synonym["term"], "similarity": (int(synonym["similarity"])/100.0)}
        syn_set.append(syn)
    return syn_set


# filter out example sentences from response
def getExampleSentences(response):
    example_sentences = []
    for sentence in response.json()['data']['exampleSentences']:
        example_sentences.append(sentence['sentence'])
    return example_sentences


# main method for get data
def getData(input_word):
    # Api call
    response = requests.get(api_url + input_word, headers=header)
    try:
        # filter out data
        pos_tag = getPosTag(response)
        definition = getDefinition(response)
        syn_set = getSynset(response)
        example_sentences = getExampleSentences(response)

        # translate word
        translated = translator.translate([input_word], 'en', 'si')[0]

        # generate audio for tts
        tts.audio_gen(input_word, 'en')

        # format data and return
        return 200, formatter.mainDataFormat(input_word, pos_tag, definition, syn_set, example_sentences, translated)
    except TypeError:
        return 404, "No thesaurus results"
