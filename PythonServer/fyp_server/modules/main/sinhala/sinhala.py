from modules.formatter import formatter
import modules.tts.tts as tts
import modules.translator.translator_v2 as translator

# word pos tag identification
def getPosTag(word):
    return "Pos tag"


# get word definition
def getDefinition(word):
    return "Definition"


# get synset
def getSynset(word):
    return ["synset"]


# get example sentences
def getExampleSentences(word):
    return ["example sentenses"]


# main method for get data
def getData(input_word):


    # get data
    pos_tag = getPosTag(input_word)
    definition = getDefinition(input_word)
    syn_set = getSynset(input_word)
    example_sentences = getExampleSentences(input_word)

    # translate word
    translated = translator.translate([input_word], 'si', 'en')[0]

    # generate audio with tts
    tts.audio_gen(input_word, 'si')

    # format data and return
    return formatter.mainDataFormat(input_word, pos_tag, definition, syn_set, example_sentences, translated)
