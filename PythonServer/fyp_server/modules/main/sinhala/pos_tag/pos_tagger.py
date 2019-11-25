import nltk
from modules.main.sinhala.pos_tag.util.preprocessing_sin import addCharInformation as addCharSinhala, addCasingInformation as addCasingSinhala, createMatrices as createSinhala
from modules.main.sinhala.pos_tag.neuralnets.BiLSTM import BiLSTM

sinhala_pos = BiLSTM.loadModel('modules/main/sinhala/pos_tag/model/sinhala_pos.h5')

pos_dic = {'NNC': 'Noun', 'PRP': 'Noun', 'QUE': 'Noun',
           'QBE': 'Noun', 'NDT': 'Noun', 'VNN': 'Verb', 'VFM': 'Verb', 'VNF': 'Verb',
           'VP': 'Verb', 'AUX': 'Verb', 'NCV': 'Verb', 'JCV': 'Verb',
           'RPCV': 'Verb','SVCV': 'Verb','JJ': 'Adjective', 'NNJ': 'Adjective',
           'RB': 'Adverb', 'POST': 'Nipathana', 'CC': 'Nipathana', 'RP': 'Nipathana',
           'UH': 'Nipathana','NIP': 'Nipathana','DET': 'Other', 'CM': 'Other','NVB': 'Other',
           'NUM': 'Other', 'ABB': 'Other', 'FS': 'Other', 'PUNC': 'Other', 'FRW': 'Other', 'UNK': 'Unknown'}

def get_sinhala_pos(text):
    sentences = [{'tokens': nltk.word_tokenize(
        text)}]
    addCharSinhala(sentences)
    addCasingSinhala(sentences)
    dataMatrix = createSinhala(sentences, sinhala_pos.mappings, True)
    tags = sinhala_pos.tagSentences(dataMatrix)
    for sentenceIdx in range(len(sentences)):
        tokens = sentences[sentenceIdx]['tokens']
        data = []
        for tokenIdx in range(len(tokens)):
            tokenTags = []
            for modelName in sorted(tags.keys()):
                tokenTags.append(tags[modelName][sentenceIdx][tokenIdx])
            data.append({'token': tokens[tokenIdx], 'tag': pos_dic[tokenTags[0]]})
    return data

get_sinhala_pos('අම්මා')