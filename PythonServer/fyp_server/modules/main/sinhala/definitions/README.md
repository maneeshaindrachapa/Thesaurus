<h2 align="center">Word Definition Extractor Module</h2>

This module is to provide definitions for a user input word. We cannot implement a method to automatically extract definitions of a word from a text corpus. Therefore, we used a dictionary look-up approach to provide definitions of a word. For Sinhala language, we extract definitions by using the data which we collected from the Concise Dictionary. For English language, we extracted definitions from the Thesaurus API because it is already existing and that is not relevant to our research area.

#### Data preparation and pre-processing

In our system implementation, we extracted the Sinhala example sentences from a text corpus. We created a separate corpus for Sinhala language, we extracted definitions from the Thesaurus API because it is already existing and that is not relevant to our research area.

#### Data preparation and pre-processing

The main prohich includes more than 100000 sentences for this. We collected this data from English & Sinhala monolingual corpus availablem of providing definition of a wn WMT19(World is finding a dataset whiMach include word and its definition. There are no such available tools exist to provide definitions for Sinhala words properly. Therefore, we used Concise dictionary to extract definitions for Sinhala we Translation 2019). First, we cleaned this dataset by removing English characters, numbers, special characters etc. Then we fixed the Unicode errords. It had a lot of garbage data which we don’t need. Therefore, we wrote a python script to remove unwanted data and clean this dataset. After that we put each of Sinhala word and its corresponding definitions to a list. In here, we had to consider both synonyms and definitions, because this data is obtained from a dictionary. So, we assume that if a phrase has more than 3 words, we consider it as a definition of the considered word. Otherwise, it is a synonym of considered wordn this dataset, each sentence is separated by ‘.’. So, we split each sentence and then put all sentences to a list.

For English language, we extracted example sentences from the Thesaurus API because it is already existing and that is not relevant to our research area.

#### Implementation

The system is taking the user input and then find the corresponding definition for that word from sentences which include that word from the list. Then the system will put all those relevant sentences to another list. Then the results are sent to the frontend.

#### Results

If a user entereds a word, definition of that word is to the system, the system will search for the sentence that includes input word and then shown it in the web application asinterface as shown below.

<figure>  
<img align=center src="https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/def.jpg?raw=true" style="width:100%">  
<figcaption align=center>Word definitions</figcaption>  
</figure>
Example Sentences for a word</figcaption>  
</figure>

For English language, we extracted example sentences from the Thesaurus API because it is already existing and that is not relevant to our research area.



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NDE1MTY2OTUsMjkwNjc0OTMyLC0xMz
c4NzY4NDY0XX0=
-->