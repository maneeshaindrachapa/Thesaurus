<h2 align="center">Language Identifier Module</h2>

The objective of developing this module is to identify the language that users interact with the system. The languages used in the system are Sinhala and English. When a word is entered to the system, the system needs to automatically recognize the language of the word entered the application itself because Sinhala words and English words are communicating with 2 separate methods of generating thesaurus data. Therefore, proper language identification is necessary for our system.

At first, we tried to identify the language of a word just by looking at the Unicode values. We took the Unicode range of the Sinhala and English characters separately and then if characters of a word are belonging to a above range and calculated the percentages of that input word belong to Sinhala, English and any other language. After calculating the percentage of world for all languages then we get the most scored language as the input word language.

Then we used the deep learning-based approach to detect the language because of the higher accuracy with the neural network-based approach. Here we used the character sequence properties of words to detect the languages. After we trained the model and we compared the both methodologies and with the final implementation we choose the most accurate technique with implementation.

### Unicode Based Approach

Unicode is a character encoding standard that uses with all the language that represent in the computers. For each letter or symbol in a language has different Unicode values which can be used to identify those in the computers. In this approach we mainly used those Unicode values to clearly identify the Sinhala and English languages separately.

Here we get input word and considered each character in the word and get the Unicode value of that character. Then considering the Unicode ranges of Sinhala and English language classified the that character to the related language. Then with the character language identification calculate the character combined word relatedness to the Sinhala, English or other languages. Then based on this relatedness score identify the high score valued language as the input word language.

### Deep learning Based Approach
#### Data Preparation & Pre-processing
<![endif]-->

The main problem with the neural network approach is it’s required large data as the training dataset. Therefore, as the first step we find large Sinhala and English data to train the neural network model. Then, we prepared a dataset by extracting a Sinhala and English dataset from the Wikipedia articles using the Python Wikipedia library and collected data from English & Sinhala monolingual corpus available on WMT19(World Machine Translation 2019). Also when we are collecting the data we had to prepare the same size of data set for both Sinhala and English languages to avoid the model bias on one language.

After preparing data set, we had to remove all the unwanted things in the data set. Then we had to decode the Unicode’s data into ascii and for the Sinhala data that unidecode to Singlish form to convert all the data only in English alphabet to get both languages in one feature set. For this unidecode execution we mainly used python unidecode library directly and successfully unidecode all the words in the corpus.

(Example: අම්මා => amma, බල්ලා => ballaa)

Then we had to only select words only with English alphabetic characters. For filter this we used regular expression ‘a-zA-Z’. This also avoid the numerical characters in the data set and return the pure word text data. With the unidecode process we can get all the word with alphabetic characters and we can get those English alphabet characters as the features when we create the word embeddings to feed the neural network.

One-hot vector encoding is an approach mostly used with the machine learning data pre-processing to convert categorical data to numerical data which computer can understand. With this approach we can feed neural networks without losing data properties. Here mainly have a vocabulary as the dimensions(features) of the vector. This vocabulary only includes unique data that can be used to categorize the whole data set. When data set encoding if data is related to that one of category then algorithm create a vector with length equal to length of vocabulary space by putting only 1 on related category and others are 0.

In this scenario, when creating the one-hot vector approach because we can create that easily on English letter word by using the alphabet as the vector vocabulary. Then we created a one-hot vectors for each letter in single word with length of 26(length of English alphabet). After creating all the one hot vectors for a word, algorithm combines all the one hot vector and create single multi-hot vector for that word. But one problem we have to solve here is we need to have the same length multi-hot vector while we are feeding data to the neural network. To solve this, we post-padded our multi hot vectors into same length by initially declaring max word length for the words. Then we padded words with lower length than the max word length by putting 26*(max length - word length) times 0’s into the word. (26 0’s for each letter) Also we avoided all the word which length is greater than the declared max word length.

In our implementation we put maximum word length as 30 and created multi hot vectors with length of 780(30*max_word_length). That vector represents the character properties for a particular word.

<figure>  
<img align=center src="https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/multi-hot%20vector.png?raw=true"  alt="Trulli"  style="width:100%">  
<figcaption align=center>Multi-hot vector example</figcaption>  
</figure>

Model Training

After we have done all the pre-processing required to train the model, we have divided our data set into training and test data sets(x_train,x_test) as 85% of the dataset is training data and 15% of the data is test data. In this language classifier for Sinhala & English languages, we used a supervised learning approach with Keras 5-layer neural network model. Here we used Sequential neural network approach in Keras model with initially defining 200 neurons for the input layer with 26*max_word_length input dimension. Then process the input data with different 3 internal layers and finally converted the output layer with 2 neurons (for two languages Sinhala & English). Every hidden layer in the neural network used ‘sigmoid’ function as the activation function. Also, we used MSE (Mean Squared Error) as the error calculating approach and 100 epochs with batch size of 1000 for our model training. After we trained our model, we have saved model weights into a file called “weights.hdf5” for use the model again without training again. Also, the as the intermediate state of the complete process we have saved multi-hot vectors in csv file as the backfile for data preparation and pre-processing.

<figure>  
<img align=center src="https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/Language%20Identifier.png?raw=true"  alt="Trulli"  style="width:100%">  
<figcaption align=center>Language identifier model complete architecture </figcaption>  
</figure>

#### Results Evaluation

After successfully implemented the Language identifier with both Unicode and Deep Learning based approaches we had to evaluate both the approaches. Then we had to select the best approach to implement into the final system.

For the evaluation process we tested the approaches with already tagged English & Sinhala data sets (Appendix 01 & 02). For the Deep Learning based approach, we observed the following accuracy and error from the neural network model.

Accuracy: 92.97% (for 50 epochs)

Mean Squared Error (MSE): 0.0652


Here we used data set only includes 110,270,445 words for each Sinhala and English languages as the training data set. If we use more data and train the model with optimal number of epochs, we can increase the accuracy of this neural network model.

Then we tested the Unicode based language identification approach with same test dataset and we get the accuracy of the classification as 98%. Then with the comparison of the accuracy levels of both approaches discussed in above we selected the high accuracy approach to implement with the final system. The identification of the language in the final system is shown as below in the client side of the application.


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNjg1NjM2MDksLTEzMjYwMDg5MzksMT
Q4ODQ2ODQ3MiwtMTgwODk1NDYxNiwzMDAwMDAzNTAsLTIwODg3
NDY2MTIsNzMwOTk4MTE2XX0=
-->