
# coding: utf-8

# In[1]:


import pandas as pd 
import requests
import openpyxl
import numpy as np


# In[2]:


print('=========> Notation <=========')
print('===> [o] - Success')
print('===> [x] - Error')
print('===> [i] - Ignored')
print('==============================\n')

#Get range for crawler
print("Crwling word range add here (int vals) [end = -1 means till end of data]")
start = int(input("Start of range:"))
end = int(input("End of range:"))

#read fasttext vector
f = open("FastText/cc.en.300.vec",'r', encoding='utf-8')
data = f.readlines()
print('[o] Data loaded Successfully!')


# In[3]:


def html_to_frame(word):     
    url = 'https://www.maduraonline.com/?find='+word
    
    header = {
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"
    }
    
    r = requests.get(url, headers=header)

    dfs = pd.read_html(r.text)[0]
    if(len(dfs.columns)>1):
        dfs.drop(columns=[0],inplace=True)
        dfs.dropna(inplace=True)
        dfs[word] =dfs[2].apply(lambda x: x.replace(" ","_")) #dfs[word] = dfs[1]+dfs[2]
        dfs.drop(columns=[1,2],inplace=True)
        return dfs.T
    else:
        return dfs


# In[4]:


total_vector_count = 0
new_vecs = ''
if(end==-1):
    end = len(data)
for i in range(start,end):
    try:
        word_vector = data[i].split(" ", 1)
        if(not word_vector[0].isalpha()):
            print("["+str(i)+"][i] | Word: "+word_vector[0])
            continue
        print("["+str(i)+"][o] | Word: "+word_vector[0])
        si_words = html_to_frame(word_vector[0])
        si_words_count = len(si_words.columns)
        if(si_words_count>1):
            temp_vec = ''
            for i in list(dict.fromkeys(si_words.to_string(header=False,index=False).split())):
                total_vector_count +=1 
                temp_vec+= (i+" "+word_vector[1])      
            new_vecs+= temp_vec
        else:
            continue
    except:
        print("["+str(i)+"][x] | Word: "+str(word_vector[0]))
        continue


# In[16]:


#Write the vec file
to_write = str(total_vector_count)+" "+data[0].split()[1]+'\n'+new_vecs
writer = open("Output/tr.cc.si.300_"+str(start)+"_"+str(end)+".vec", "w", encoding="utf-8")
writer.write(to_write)
writer.close()

#Write new models to combine script
f=open("Output/new_models.txt", "a+")
f.write("tr.cc.si.300_"+str(start)+"_"+str(end)+".vec\n")
f.close()

#final
print("====> Done <====")
print("[o] Total new vectors:",total_vector_count)
print("[o] Vecors saved to 'tr.cc.si.300_"+str(start)+"_"+str(end)+".vec' file successfully.")

