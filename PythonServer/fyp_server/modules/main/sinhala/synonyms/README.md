<h2 align="center">Similar Word Cluster Generator Module</h2>

### Optimized FastText Word Embedding Model

#### Introduction

We didn’t get results as expected by using the Fasttext model which we created by collecting data from Sinhala monolingual corpus available on WMT19 (World Machine Translation 2019). It gave us less synonyms while giving more contextual words. It is because, this text corpus did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sites. Therefore, we fed synonyms sets to the Fasttext model.

Data sources like Sinhala textbooks (Ordinary Level) include some number of synonyms, but not considerable number of synonyms for a thesaurus. Therefore, we investigated synonyms rich data sources such as Madhura online dictionary and Concise dictionary.

As the synonym datasets for the system we crawled Sinhala synonym sets from Madhura dictionary by submitting an English dataset to the Madhura application URL and extract the similar meaning word from the response. These synonym sets were not enough to feed the model. So, we used the Concise dictionary to extract furthermore synonym sets.

There are lot of issues in the data. Therefore, we fixed those issues before feeding synonym sets into the Fasttext model. The synonym sets which we crawled from the Madura online dictionary contained related synonyms as well as unrelated words. Therefore, we had to manually look some of those words and fix them. Also, Concise dictionary contained lot of garbage data and Unicode errors. Therefore, we had to write script to clean those data and fix Unicode errors. Generally, a dictionary is providing both synonyms and definitions for the words. Therefore, we had to filter synonyms from the Concise dictionary when extracting the data. All the synonyms and definitions for a particular word is separated by ‘;’ sign. Thus, we split each of these phrases by ‘;’ at first. Then if a corresponding phrase has less than 3 words, we assumed it as a synonym of that word. Otherwise we assumed it as a definition.

#### Literature Review

<![endif]-->

A web crawler is a program or automated script which browses the World Wide Web in an automated methodological manner. This process is known as we are crawling. People can crawl lot of data from the internet by using crawlers without applying much effort. In modern world, crawling become very straight forward with the help of advanced programming concepts.

When training a Fasttext model under a text corpus, there are a lot of parameters need to be adjusted in order to optimize the model. This procedure will help to find the most appropriate parameters set that provide the best results for a given Fasttext model.

#### Data Preparation & Pre-processing

Mainly used a text corpus which we created by collecting data from Sinhala monolingual corpus available on WMT19 (World Machine Translation 2019) to train the Fasttext model. It contained approximately 110M words. This dataset had a lot of unwanted data for our model training including numbers, special characters, emojis and etc. Therefore, we had to pre-process and clean this dataset using pre-processing script. Then we trained a Fasttext model using this cleaned dataset. But it did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sites.

#### Model Training

In this phase we mainly used Fasttext tool as our main model building tool. With the Fasttext model we can build a vector mode with 100 - 300 dimensions. As we mentioned in previous topics Fasttext is very light weight tool for word embedding model training. In our model training followed Fasttext documentation as the reference for tune-up the parameters of the tool. In Fasttext model training there are few parameters we can tune-up to get the model as we expected. With our dataset we followed unsupervised training approach with Fasttext.

When our model training, we used few parameter changes related to our model building on the dataset. We tried different types of model training by changing the parameter values of the model training. Then we evaluate the model given word results with word extraction using python library called Gensim. Gensim is one of nearest neighbour vector extraction tools that are available for most common word embedding approaches.  With this Gensim we initially provided threshold as the 10 and extracted nearest neighbour according to cosine similarity and evaluated the built models and finally come up with the suitable model with below parameters.

After we successfully trained our model, we have identified that model gives synonyms words with contextually similar words and not related words. Therefore, we fed crawled synsets to the model to replace those unwanted words by having threshold with cosine similarity and for some words we had to feed the synsets by manually. To optimize the model.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMwMDEwOTA4MCwyMTAyNzQyMzIzXX0=
-->