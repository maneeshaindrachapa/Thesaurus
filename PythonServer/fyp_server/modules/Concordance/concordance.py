import re

theText2Use = "ol.txt"
with open(theText2Use, "r", encoding='utf-8') as fileToRead:
    fileRead = fileToRead.read()
    

file = re.sub(r' \d+', '', fileRead)
file = file.splitlines()
sentences = []
for i in file:
    sen = i.split('.')
    for j in sen:
        sentences.append(j)
print (len(sentences))

def concordance(word):
    length = 0
    for s in sentences:
        if word in s:
            length += 1
            if (length==6):
                break
            print (s.strip()+'\n')

word = 'පරපුර'
concordance(word)
