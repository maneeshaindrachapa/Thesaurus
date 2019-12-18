<h2 align="center">Similar Word Cluster Generator Module</h2>

### Optimized FastText Word Embedding Model

#### Introduction



#### Literature Review

A web crawler [30] is a program or automated script which browses the World Wide Web in an automated methodological manner. This process is known as we are crawling. People can crawl lot of data from the internet by using crawlers without applying much effort. In modern world, crawling become very straight forward with the help of advanced programming concepts.

When training a Fasttext model under a text corpus, there are a lot of parameters need to be adjusted in order to optimize the model. This procedure will help to find the most appropriate parameters set that provide the best results for a given Fasttext model.

#### Data Preparation & Pre-processing

The synonym sets which we crawled from Madhura dictionary doesn’t need any pre-processing work. But the synonym sets which we extracted from Concise dictionary needed fair amount of data pre-processing work. It is because the conversion of the dictionary pdf file format to word/txt format dictionary had a lot of unwanted data for our model training including numbers, special characters, emojis and etc. Therefore, we had to pre-process andclean data and Unicode errors. As the first thing we had to clean this data set using pre-processing script. Then we trained a Fasttext model using this cleaned dataset. But it did not contain substantial Sinhala synonyms as we expected. The reason for that was this dataset does not include Sinhala synonym data, because this dataset is crawled from a Sinhala public news websites and social media sitesand correct the data sets and then we wrote a python script to clean this dictionary data and extract synonyms sets. But we had to fix some errors by manually, because there are some unidentifiable errors using scripts. After extracting synonyms sets from Concise dictionary, we feed all of these synonyms sets to the Fasttext model.

#### Model Training

In this phase we mainly used Fasttext tool as our main model building tool to build the vector model. We used Fasttext model training parameters as before without doing any changes. Here we only have changed the dataset by adding synonyms sets which we extracted from Madhura and Concise dictionaries to the dataset row by row. Therefore, one row will get one synonym set. The Fasttext will identify words in the same row as synonyms, because here we considered a context window size of 5. Therefore, surrounding words will obtain similar vectors. Then the cosine similarity between those vectors become closer to 1. So, we can find the related synonyms more accurately by feeding synonym sets into the dataset.

After we successfully trained our model, we have identified that model gives many related synonyms words (higher percentage), while providing some contextually similar words (lower percentage).

#### Synonyms Extraction

After successfully trained the Fasttext model, we loaded model into python library called Gensim to extract the synonyms. We mainly extract the nearest vectors based on cosine distance-based approach.

After we successfully get the output from the Gensim tool then we have filtered the words based on the similarity measure to get the best synonym set for the input word. As an average value for the similarity threshold we have identified that with in cosine similarity 1 to 0.85 we can get best synonyms for the word. Therefore, we have configured the synset extractor with 0.85 similarity threshold filtering after the Gensim extract the words. This model gave us far more better results than the previous Fasttext model which we built just using the text corpus. That is because now the Fasttext model is rich with synonym sets.

#### Summary & Results

After we successfully built the model, we evaluated the model results with our previous implementations with the synset identification. Then we identified that Fasttext model gives more accurate results than all other implementations. Then we implemented the system with this Fasttext model as the primary synset identification.

With the Fasttext model we successfully retrieved synsets with some level of accuracy and after we fed the synsets for the model for optimization, then model behave more accurate than the previous and show the most similar words for an input word to the system.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyOTc2Njg3Miw3NDkzNzIyMCwtNjM0Mj
IxODc3LDExOTA3NTI5MzMsMTEyODUyNzQyLDEzMDAxMDkwODAs
MjEwMjc0MjMyM119
-->