from modules.formatter import formatter
import modules.tts.tts as tts
import modules.translator.translator as translator
import modules.main.sinhala.example_sentences.example_sentences as example_sentences
import modules.main.sinhala.synonyms.synonyms as synonyms
import modules.main.sinhala.definitions.definitions as definitions
import modules.display_error.display_error as display_error
import modules.main.sinhala.pos_tag.pos_tagger as pos_tagger


# word pos tag identification
def getPosTag(word):
    try:
        tagged = pos_tagger.get_sinhala_pos(word)[0]
        return tagged['tag']
    except:
        return 'NONE'

    # get word definitions


def getDefinition(word):
    return definitions.definition(word)


# get synset
def getSynset(word):
    return synonyms.getSynset(word, 18, 0.85)


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
        code, translated = translator.translate([input_word.replace('_', ' ')], 'si', 'en')

        # generate audio with tts
        tts.audio_gen(input_word.replace('_', ' '), 'si')

        # format data and return
        return 200, formatter.mainDataFormat(input_word, 'si', pos_tag, definition, syn_set, example_sentences,
                                             translated[0])
    except TypeError:
        display_error.print_error(404, "No thesaurus results")
        return 404, "No thesaurus results"
    except KeyError:
        display_error.print_error(404, "No thesaurus results")
        return 404, "No thesaurus results"
