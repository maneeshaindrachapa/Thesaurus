<h2 align="center">Similar Word Cluster Generator Module</h2>

### Optimized FastText Word Embedding Model

#### Introduction

We didn’t get results as expected by using the Fasttext model which we created by collecting data from Sinhala monolingual corpus available on WMT19 (World Machine Translation 2019). It gave us less synonyms while giving more contextual words. It is because, this text corpus did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sites. Therefore, we fed synonyms sets to the Fasttext model.

Data sources like Sinhala textbooks (Ordinary Level) include some number of synonyms, but not considerable number of synonymsing pre-processing the  raine aat mon cl dataset.  tid t oin l ih  asext. er that  the synonym tacti e sed ensim tol a the  etor a odelling o a thesaurus. Therefore, we investigated synonyms rich data sources such as Madhura online dictionary and Concise dictionary.

As the synonym datasets for the system we crawled Sinhala synonym sets from Madhura dictionary by submitt Fasttext model en  actd the snony wo from etra model aed on the cone tae of the o etorith wr cunt theol ad iat eold agr e#### Literature Review

Word embeddings an English dataset to the Madhura application URL and extract the similar meaning word from the response. These synonym sets were not enough to feed the model. So, we used the Concise dictionary to extract furthermore synonym sets.

There are lot of issues in the data. Therefore, we fixed those issues before feeding synonym setl. The synonym sets which we crawled from the Madura online dictionary contained related synonyms as well as unrelated words. Therefore, we had to mre word representation, most common usage building continuous word vectors based on their contexts in a large corpus. Fasttext is one of lightweight approaches which used to build vector representation for large corpus data without any language dependency. Fasttext can used to build the vector model based on the character level with n-grams or word levels with word n-grams based on the purpose of the model building.  As researchers of the Facebook identified model building with character n-grams are important to identify the morphological variations of the word and the anually look someogy of those words and fix them. Also, Concise dictionary contained lot of garbage data and Unicode errors. Therefore, we had to write script to clean those data and fix Unicode errors. Generally, a dictionary is providing both synonyms and definitions for the words. Therefore, we had to filter synonyms from the Concise dictionary when extracting the data. All the synonyms and definitions for a particular word is separated by ‘;’ sign. Thus, we split each of these phrases by ‘;’ at first. Then if a corresponding phrase has less than 3 words, we assumed it as a synonym of that word. Otherwise we assumed it as a definition.

#### Literature Review

A web crawler is a program or automated script which browses the World Wide Web in an automated methodological manner. This process is known as we are crawling. People can crawl lot of data from the internet by using crawlers without applying much effort. In modern world, crawling become very straight forward with the help of advanced programming concepts.

When training a Fasttext model under a text corpus, there are a lot of parameters need to be adjusted in order to optimize the model. This procedure will help to find the most appropriate parameters set that provide the best results for a given Fasttext model.

#### Data Preparation & Pre-processing

The synonym sets which we crawled from Madhura dictionary doesn’t need any pre-processing work. But the synonym sets which we extracted from Concise dictionary needed fair amount of data pre-processing work. It is because the conversion of the dictionary pdf file format to word/txt format dictionary had a lot of unwanted data for our model training including numbers, special characters, emojis and etc. Therefore, we had to pre-process andclean data and Unicode errors. As the first thing we had to clean this data set using pre-processing script. Then we trained a Fasttext model using this cleaned dataset. But it did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sitesand correct the data sets and then we wrote a python script to clean this dictionary data and extract synonyms sets. But we had to fix some errors by manually, because there are some unidentifiable errors using scripts. After extracting synonyms sets from Concise dictionary, we feed all of these synonyms sets to the Fasttext model.

#### Model Training

In this phase we mainly used Fasttext tool as our main model building tool. With the Fasttext model we can to build athe vector mode with 100 - 300 dimensions. As we mentioned in previous topics Fasttext is very light weight tool for word embedding model training. In our model training followed Fasttext documentation as the reference for tune-up the parameters of the tool. In Fasttext model training there are few parameters we can tune-up to get the model asl. We used Fasttext model training parameters as given in below.

Here we only have changed the dataset by adding synonyms sets which we expetracted. With our dataset we followed unsupervised training approach with Fasttext.

When our model training, we used few parameter changes related to our model building on the dataset. We tried different types of model training by changing the parameter values of the model training. Then we evaluate the model given word results with word extractio from Madhura and Concise dictionaries to the dataset row by row. Therefore, one row will get one synonym set. The Fasttext will identify words in the same row as synonyms, because here we considered a context window size of 5. Therefore, surrounding words will obtain using python library called Gensim. Gensim is one of nearest neighbour vector extraction tools that are available for most common word embedding approaches.  With this Gensim we initially provided threshold as the 10 and extracted nearest neighbour according to cosine similarity and evaluated the built models and finally come up with the suitable model with below parameters.

After we successfully trained our model, we have identified that model gives synonyms words with contextually similar words and not related words. Therefore, we fed crawled synsets to the model to replace those unwanted words by having threshold with cosine similarity and for some words we had to feed the synsets by manually. To optimize the modelmilar vectors. Then the cosine similarity between those vectors become closer to 1. So, we can find the related synonyms more accurately by feeding synonym sets into the dataset.

After we successfully trained our model, we have identified that model gives many related synonyms words (higher percentage), while providing some contextually similar words (lower percentage).

#### Synonyms Extraction

After successfully trained the Fasttext model, we loaded model into python library called Gensim to extract the synonyms. We mainly extract the nearest vectors based on cosine distance-based approach.

After we successfully get the output from the Gensim tool then we have filtered the words based on the similarity measure to get the best synonym set for the input word. As an average value for the similarity threshold we have identified that with in cosine similarity 1 to 0.85 we can get best synonyms for the word. Therefore, we have configured the synset extractor with 0.85 similarity threshold filtering after the Gensim extract the words. This model gave us far more better results than the previous Fasttext model which we built just using the text corpus. That is because now the Fasttext model is rich with synonym sets.

#### Summary & Results

After we successfully built the model, we evaluated the model results with our previous implementations with the synset identification. Then we identified that Fasttext model gives more accurate results than all other implementations. Then we implemented the system with this Fasttext model as the primary synset identification.

With the Fasttext model we successfully retrieved synsets with some level of accuracy and after we fed the synsets for the model for optimization, then model behave more accurate than the previous and show the most similar words for an input word to the system.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwOTMyNjYwMywtNjM0MjIxODc3LDExOT
A3NTI5MzMsMTEyODUyNzQyLDEzMDAxMDkwODAsMjEwMjc0MjMy
M119
-->