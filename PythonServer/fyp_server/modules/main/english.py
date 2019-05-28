import nltk
import modules.translator.translator as translator
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.tag import pos_tag, map_tag

# nltk.download('wordnet')
# nltk.download('universal_tagset')
# nltk.download('averaged_perceptron_tagger')

#Get postagger using the nltk tagger
def getPosTag(word):

    token = word_tokenize(word)
    tagged = nltk.pos_tag(token)
    simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tagged]
    return list(sum(simplifiedTags, ()))


#Get synonyms based on the wordnet corpus with universal postag and wup_simiarity score
def getSynonyms(word):
    #nltk.download('wordnet')
    temp = wn.synsets(word)
    if(temp):
        synonyms = []
        for syn in temp:
            for l in syn.lemmas():
                synTemp = getPosTag(l.name())
                # synTemp.append((translator.translate_word(l.name(), 'en', 'si')).text)
                synTemp.append(temp[0].wup_similarity(syn))
                synonyms.append(synTemp)
        return synonyms
    else:
        return "not found"


#Get definitions based on the wordnet corpus
def getDefinition(word):
    temp = wn.synsets(word)
    if(temp):
        return temp[0].definition()
    else:
        return "not found"


#Get examples based on the wordnet corpus
def getExamples(word):
    temp = wn.synsets(word)
    if(temp):
        return temp[0].examples()
    else:
        return "not found"


