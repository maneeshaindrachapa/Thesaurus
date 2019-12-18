<h2 align="center">Spell Checker Module</h2>

This module is developed by our parallel NLP research group. We integrated this module for our system to check the spellings of the input word (Sinhala) by developing a custom API layer for the other group Sinhala spell checker application. With this implementation user can check whether the entered word is correct or wrong. When user typing the Sinhala word in the search box it’s real time check the user input word is with correct or incorrect spellings. If the word is incorrect, then the system will give an error hint to the user by displaying error as below.

<figure>  
<img align=center src="https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/spell_incorrect.jpg?raw=true"  alt="Working system interfaces for the l_ietermulti-hotvector.png?raw=true"  alt="Multi-hot vector example"  style="width:100%">  
<figcaption align=center>orrect spellings indicator </figcaption>  
</figure>

Although there exists an error, the user can search for incorrect word in the system. But the system will not display results if it’s not in the model. In the spellings incorrect scenario, we provided search functionality because there can be correct spellings that spell checker system may not identifiable. If the word spellings are correct, then the system will give a hint to the user as below.

<figure>  
<img align=center src="https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/spell_correct.jpg?raw=true"  alt="Working system interfaces for the language identifier"  style="width:100%">  
<figcaption align=center>Correct spellings indicator</figcaption>  
</figure>


<!--stackedit_data:
eyJoaXN0b3J5IjpbMzUzODY0MjAyLC0yODM2OTIzNTYsOTQ0Nj
YxODYsNTU4NzMxNTg5XX0=
-->