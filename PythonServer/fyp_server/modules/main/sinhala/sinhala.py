from modules.formatter import formatter
import modules.tts.tts as tts
import modules.translator.translator_v2 as translator
import modules.main.sinhala.example_sentences.example_sentences as example_sentences
import modules.main.sinhala.synonyms.synonyms as synonyms
import modules.main.sinhala.definitions.definitions as definitions

# word pos tag identification
def getPosTag(word):
    return "Pos tag"


# get word definitions
def getDefinition(word):
    print(definitions.definition(word))
    return definitions.definition(word)


# get synset
def getSynset(word):
    return synonyms.getSynset(word, 15)


# get example sentences
def getExampleSentences(word):
    sentences = example_sentences.get_sentences(word)
    return sentences


# main method for get data
def getData(input_word):
    try:
        # get data
        pos_tag = getPosTag(input_word)
        definition = getDefinition(input_word)
        syn_set = getSynset(input_word)
        example_sentences = getExampleSentences(input_word)

        # translate word
        translated = translator.translate([input_word], 'si', 'en')[0]

        # generate audio with tts
        tts.audio_gen(input_word.replace('_', ' '), 'si')

        # format data and return
        return 200, formatter.mainDataFormat(input_word, 'si', pos_tag, definition, syn_set, example_sentences, translated)
    except TypeError:
        return 404, "No thesaurus results"
    except KeyError:
        return 404, "No thesaurus results"
