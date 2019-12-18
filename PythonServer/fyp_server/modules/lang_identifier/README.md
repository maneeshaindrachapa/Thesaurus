<h2 align="center">Language Identifier Module</h2>

The objective of developing this module is to identify the language that users interact with the system. The languages used in the system are Sinhala and English. When a word is entered to the system, the system needs to automatically recognize the language of the word entered the application itself because Sinhala words and English words are communicating with 2 separate methods of generating thesaurus data. Therefore, proper language identification is necessary for our system.

At first, we tried to identify the language of a word just by looking at the Unicode values. We took the Unicode range of the Sinhala and English characters separately and then if characters of a word are belonging to a above range and calculated the percentages of that input word belong to Sinhala, English and any other language. After calculating the percentage of world for all languages then we get the most scored language as the input word language.

Then we used the deep learning-based approach to detect the language because of the higher accuracy with the neural network-based approach. Here we used the character sequence properties of words to detect the languages. After we trained the model and we compared the both methodologies and with the final implementation we choose the most accurate technique with implementation.

### Unicode Based Approach

Unicode is a character encoding standard that uses with all the language that represent in the computers. For each letter or symbol in a language has different Unicode values which can be used to identify those in the computers. In this approach we mainly used those Unicode values to clearly identify the Sinhala and English languages separately.

Here we get input word and considered each character in the word and get the Unicode value of that character. Then considering the Unicode ranges of Sinhala and English language classified the that character to the related language. Then with the character language identification calculate the character combined word relatedness to the Sinhala, English or other languages. Then based on this relatedness score identify the high score valued language as the input word language.

### Deep learning Based Approach

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwOTYzODc1MTksLTIwODg3NDY2MTIsNz
MwOTk4MTE2XX0=
-->