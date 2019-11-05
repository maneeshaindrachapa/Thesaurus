import pandas as pd
synonyms = pd.read_excel('modules/main/sinhala/definitions/def_data.xlsx')

# Load data to the dictionary
dictionary = {}
for i in range(synonyms['Word'].size):
    word = str(synonyms.loc[i]['Word'])
    definition = synonyms.loc[i]['Def1']
    if (word!='' and definition!=''):
        dictionary[word] = definition

# vacab list for dictionary
vocab = list(dictionary.keys())

# extract definitions
def definition(word):
    for vocab_word in vocab:
        if word in vocab_word:
            return dictionary.get(vocab_word)
    return ''

