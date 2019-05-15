import os
import re
w_path = input("Enter your output file dir path: ")
path = "Sinhala\Sinhala"

files = []
for r,d,f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r,file))

for file in files:
    content = ""
    with open(file, 'r',encoding="utf8") as content_file:
        print(">>>>>>> Reading "+file+" file content <<<<<<<")
        content = content_file.read()
        content = re.sub('\n', ' ',content)
        content = re.sub(" \d+", " ", content)
        content = re.sub(r'[a-z]+', ' ', content,re.I)
        content = re.sub(' +', ' ',content)
        
    with open(w_path+'\si.txt', 'a+',encoding="utf8") as w_file:
        print(">>>>>>> Writing "+file+" file content <<<<<<<")
        w_file.write(content)

            
        
