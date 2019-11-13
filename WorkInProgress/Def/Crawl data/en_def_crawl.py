#!/usr/bin/env python
# coding: utf-8

# ## Crawling

# In[21]:


import requests
import pandas as pd
import numpy as np
import os 
import time
api_url = 'https://tuna.thesaurus.com/pageData/'

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"}

# filter out definitions from response
def getDefinition(response):
    try:
        return response.json()['data']['definitionData']['definitions'][0]['definition']
    except KeyError:
        return ''

# main method for get data
def getDefData(input_word):
    # Api call
    response = requests.get(api_url + input_word, headers=header)
    try:
        # filter out data
        definition = getDefinition(response)

        # format data and return
        return definition
    except TypeError:
        return ''


# ## Load Fasttext

# In[22]:


print("Loading Fasttext data ...")
f = open("../../FastText_en_si/FastText/cc.en.300.vec",'r', encoding='utf-8')
data = f.readlines()
print("Done")


# ## Execute Through the Words

# In[27]:


print('\nCrawling Starts => \n')
output_df = pd.DataFrame(data=[['','']],columns=['word','definition'])
start = int(input("start of the crawling: "))
end = int(input("end of the crawling: "))
for i in range(start,end):
    word_vector = data[i].split(" ", 1)
    word = word_vector[0]
    print('['+str(i)+'] | '+word)
#     if(not word.isalpha() or len(word)<=4):
#         continue
    definition = getDefData(word)
    print (definition)
    if(definition == ''):
        continue
    temp_df = pd.DataFrame(data=[[word,definition]],columns=['word','definition'])
    output_df = output_df.append(temp_df,ignore_index = True)
    


# In[28]:


output_df.to_excel("en_def_data.xlsx",index=False)


# In[6]:


# print("Sutting down in 60 Secs ......")
# time.sleep(60)
# os.system("shutdown /s /t 1") 


# In[7]:


# print("a",)
# print('b')


# In[ ]:




