<h2 align="center">Similar Word Cluster Generator Module</h2>

### Optimized FastText Word Embedding Model

#### Introduction

This chapter mainly includes the work carried by responsible team member of the group related to the main task of the research project. For the synonym identification of the research here tried to develop a word embedding model with Fasttext tool. As the first step prepared the data set for the model training by pre-processing the WMT19 (World Machine Translation 2019) common crawl data set. Then trained the word embedding model with the Fasttext. After that for the synonym extraction we used Gensim tool as the VSM (Vector Space Modelling) for the Fasttext model. Then we extracted the synonym words from vector space model based on the cosine distance of the word vectors with word count threshold and similarity threshold.

POS Tagger Module</h2>#### Literature Review

Word embeddings are word representation, most common usage building continuous word vectors based on their contexts in a large corpus. Fasttext is one of lightweight approaches which used to build vector representation for large corpus data without any language dependency. Fasttext can used to build the vector model based on the character level with n-grams or word levels with word n-grams based on the purpose of the model building.  As researchers of the Facebook identified model building with character n-grams are important to identify the morphological variations of the word and the analogy of the words. But in our requirement of vector modelling is extract the meaningfully similarity or contextual similarity from text corpus. Therefore, the word n-gram (word window) is more important than the character level to get the contextual related properties of the words. Then using Fasttext we build the vector space model on corpus with word n-grams by tuning the parameter of the Fasttext. After successfully build the vector space model we can use the different types of approaches to get the similarity measure as Cosine Similarity, Euclidean distance. With the cosine similarity we can get the bounded similarity values with 0-1 range and with these values we can get the similarity threshold to filter out the unrelated words in the results of the synonym extraction than the Euclidean distance approach.

After we successfully build the vector space model next thing is defining the approach to get the synonyms-based cosine similarity. Gensim is a Natural Language Processing package that does ‘Topic Modelling for Humans’. It is a leading and a state-of-the-art package for processing texts, working with word vector models (such as Word2Vec, Fasttext etc) and for building topic models. Here Gensim is mainly used to load the vector space model and get the similarity words from vector space using cosine similarity. Then we can extract the word synonyms by inserting the word count threshold value to the Gensim module.

#### Data Preparation & Pre-processing

Mainly used a text corpus which we created by collecting data from Sinhala monolingual corpus available on WMT19 (World Machine Translation 2019) to train the Fasttext model. It contained approximately 110M words. This dataset had a lot of unwanted data for our model training including numbers, special characters, emojis and etc. Therefore, we had to pre-process and clean this dataset using pre-processing script. Then we trained a Fasttext model using this cleaned dataset. But it did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sites.

#### Model Training

In this phase we mainly used Fasttext tool as our main model building tool. With the Fasttext model we can build a vector mode with 100 - 300 dimensions. As we mentioned in previous topics Fasttext is very light weight tool for word embedding model training. In our model training followed Fasttext documentation as the reference for tune-up the parameters of the tool. In Fasttext model training there are few parameters we can tune-up to get the model as we expected. With our dataset we followed unsupervised training approach with Fasttext.

When our model training, we used few parameter changes related to our model building on the dataset. We tried different types of model training by changing the parameter values of the model training. Then we evaluate the model given word results with word extraction using python library called Gensim. Gensim is one of nearest neighbour vector extraction tools that are available for most common word embedding approaches.  With this Gensim we initially provided threshold as the 10 and extracted nearest neighbour according to cosine similarity and evaluated the built models and finally come up with the suitable model with below parameters.

After we successfully trained our model, we have identified that model gives synonyms words with contextually similar words and not related words. Therefore, we fed crawled synsets to the model to replace those unwanted words by having threshold with cosine similarity and for some words we had to feed the synsets by manually. To optimize the model.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMDMwMDA5NDUsMjEwMjc0MjMyM119
-->