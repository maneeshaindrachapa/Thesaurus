<h2 align="center">Similar Word Cluster Generator Module</h2>

### Optimized FastText Word Embedding Model

#### Introduction

We didn’t get results as expected by using the Fasttext model which we created by collecting data from Sinhala monolingual corpus available on WMT19 (World Machine Translation 2019). It gave us less synonyms while giving more contextual words. It is because, this text corpus did not contain substantial Sinhala synonyms as we expected. The reason for that was hater in nl the wor arri  reposil ea e o h  reated  ein ta o h rsarch rt or the s detctin ote rs h ted to e a or meding me i ate os thefr e prepred this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sites. Therefore, we fed synonyms sets to the Fasttext model.

Data sources like Sinhala textbooks (Ordinary Level) include some number of synonyms, but not considerable number of synonymsing pre-processing the  raine aat mon cl dataset.  tid t oin l ih  asext. er that  the synonym tacti e sed ensim tol a the  etor a odelling o a thesaurus. Therefore, we investigated synonyms rich data sources such as Madhura online dictionary and Concise dictionary.

As the synonym datasets for the system we crawled Sinhala synonym sets from Madhura dictionary by submitt Fasttext model en  actd the snony wo from etra model aed on the cone tae of the o etorith wr cunt theol ad iat eold agr e#### Literature Review

Word embeddings an English dataset to the Madhura application URL and extract the similar meaning word from the response. These synonym sets were not enough to feed the model. So, we used the Concise dictionary to extract furthermore synonym sets.

There are lot of issues in the data. Therefore, we fixed those issues before feeding synonym sets into the Fasttext model. The synonym sets which we crawled from the Madura online dictionary contained related synonyms as well as unrelated words. Therefore, we had to mre word representation, most common usage building continuous word vectors based on their contexts in a large corpus. Fasttext is one of lightweight approaches which used to build vector representation for large corpus data without any language dependency. Fasttext can used to build the vector model based on the character level with n-grams or word levels with word n-grams based on the purpose of the model building.  As researchers of the Facebook identified model building with character n-grams are important to identify the morphological variations of the word and the anually look someogy of those words and fix them. Also, Concise dictionary contained lot of garbage data and Unicode errors. Therefore, we had to write script to clean those data and fix Unicode errors. Generally, a dictionary is providing both synonyms and definitions for the words. Therefore, we had to filter synonyms from the Concise dictionary when extracting the data. All the synonyms and definitions for a particular word is separated by ‘;’ sign. Thus, we split each of these phrases by ‘;’ at first. Then if a corresponding phrase has less than 3 words, we assumed it as a synonym of that word. Otherwise we assumed it as a definition.

#### Literature Review

<![endif]-->

A web crawler is a program or automated script which browses the World Wide Web in an automated methodological manner. This process is known as we are crawling. People can c. But in our requirement of vector modelling is extract the meaningfully similarity or contextual similarity from text corpus. Therefore, the word n-gram (word window) is more important than the character level to get the contextual related properties of the words. Then using Fasttext we build the vector space model on corpus with word n-grams by tuning the parameter of the Fasttext. After successfully build the vector space model we can use the different types of approaches to get the similarity measure as Cosine Similarity, Euclidean distance. With the cosine similarity we can get the bounded similarity values with 0-1 range and with these values we can get the similarity threshold to filter out the unrelated words in the results of the synonym extraction than the Euclidean distance approach.

After we successfully build the vector space model next thing is defining the approach to get the synonyms-based cosine similarity. Gensim is a Naturawl lot of data from the internet by using crawlers without applying much effort. In modern world, crawling become very straight forward with the help of advanced programming concepts.

When training a Fasttext model under a text corpus, there are a lot of parameters need to be adjusted in order to optimize the model. ThiLanguage Processing package that does ‘Topic Modelling for Humans’. It is a leading and a state-of-the-art package for processing texts, working with word vector models (such as Word2Vec, Fasttext etc) and for building topic models. Here Gensim is mainly used to load the vector space model and get the similarity words pfrocedure will help to find the most appropriate parameters set that provide the best results for a given Fasttextm vector space using cosine similarity. Then we can extract the word synonyms by inserting the word count threshold value to the Gensim modulel.

#### Data Preparation & Pre-processing

Mainly used a text corpus which we created by collecting data from Sinhala monolingual corpus available on WMT19 (World Machine Translation 2019) to train the Fasttext model. It contained approximately 110M words. This dataset had a lot of unwanted data for our model training including numbers, special characters, emojis and etc. Therefore, we had to pre-process and clean this dataset using pre-processing script. Then we trained a Fasttext model using this cleaned dataset. But it did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sites.

#### Model Training

<![endif]-->

In this phase we mainly used Fasttext tool as our main model building tool. With the Fasttext model we can build a vector mode with 100 - 300 dimensions. As we mentioned in previous topics Fasttext is very light weight tool for word embedding model training. In our model training followed Fasttext documentation as the reference for tune-up the parameters of the tool. In Fasttext model training there are few parameters we can tune-up to get the model as we expected. With our dataset we followed unsupervised training approach with Fasttext.

When our model training, we used few parameter changes related to our model building on the dataset. We tried different types of model training by changing the parameter values of the model training. Then we evaluate the model given word results with word extraction using python library called Gensim. Gensim is one of nearest neighbour vector extraction tools that are available for most common word embedding approaches.  With this Gensim we initially provided threshold as the 10 and extracted nearest neighbour according to cosine similarity and evaluated the built models and finally come up with the suitable model with below parameters.

After we successfully trained our model, we have identified that model gives synonyms words with contextually similar words and not related words. Therefore, we fed crawled synsets to the model to replace those unwanted words by having threshold with cosine similarity and for some words we had to feed the synsets by manually. To optimize the model.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEyODUyNzQyLDEzMDAxMDkwODAsMjEwMj
c0MjMyM119
-->