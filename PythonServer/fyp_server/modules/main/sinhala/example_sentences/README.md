<h2 align="center">Word Example Extractor Module</h2>

This module is basically used to give supportive sentences for a given word. This feature is useful if a user does not have an idea about a particular word.

#### Data preparation and pre-processing

In our system implementation, we extracted the Sinhala example sentences from a text corpus. We created a separate corpus for Sinhala language which includes more than 100000 sentences for this. We collected this data from English & Sinhala monolingual corpus available on WMT19(World Machine Translation 2019). First, we cleaned this dataset by removing English characters, numbers, special characters etc. Then we fixed the Unicode errors. In this dataset, each sentence is separated by ‘.’. So, we split each sentence and then put all sentences to a list.

For English language, we extracted example sentences from the Thesaurus API because it is already existing and that is not relevant to our research area.

#### Implementation

The system is taking the user input and then find the sentences which include that word from the list. Then the system will put all those relevant sentences to another list. Then the results are sent to the frontend.

#### Results

If a user enters a word to the system, the system will search for the sentence that includes input word and then show it in the interface as shown below.

<figure>  
<img align=center src="https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/spell_correct.jpg?raw=true"  alt="Working system interfaces for the language identifier"  style="width:100%">  
<figcaption align=center>Example Sentences for a word</figcaption>  
</figure>



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk5NzU0Mjg2M119
-->