from gensim.models import KeyedVectors
from gensim.models.wrappers import FastText

model = KeyedVectors.load_word2vec_format('modules/main/sinhala/synonyms/tr.cc.si.300.vec')

def getSynset(word,n):
    similar = model.most_similar(positive=[word], topn=n)
    out = []
    for word in similar:
        syn = {"term": word[0], "similarity": word[1]}
        out.append(syn)
    return out
