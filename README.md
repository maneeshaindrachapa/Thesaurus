
<h6 align="center"><img align="center" src="AngularClient/src/assets/img/main_logo.png"><h6>
<h1 align="center">Final Year Project - 2015 Batch</h1>
<h2 align="center">An Intelligent Sinhala-English Dictionary / Thesaurus / Word Look-Up Tool</h2>

<h6 align="center"><a href="http://thesaurus.projects.uom.lk">thesaurus.projects.uom.lk</a></h6>

```diff
- This project is still in Progress
```

### Supervisor : Prof. Gihan Dias

### Group Members
  - D.T.P. Jayathilaka [thilinaprasad.15@cse.mrt.ac.lk](thilinaprasad.15@cse.mrt.ac.lk)
  - R.M.M. Indrachapa [maneesh.15@cse.mrt.ac.lk](maneesh.15@cse.mrt.ac.lk)
  - W.Y.K.R. Ariyawansha [yasirurandeepa.15@cse.mrt.ac.lk](yasirurandeepa.15@cse.mrt.ac.lk)

> 

## Problem Statement


<![endif]-->

Most of the knowledge written in English. Languages like Sinhala can be rarely found from internet sources. Therefore, the people who have different mother tongues can’t access most of the knowledge available unless they know English. So, machine translation is the potential solution for giving access to the world's knowledge available in English.

Today, we can translate almost any language to another language by using google translator. This is also available for the Sinhala language. But the main issue in the Sinhala language is that the words which results after the translation is not matching properly. People are struggling when to use appropriate Sinhala words. This is because there are so many synonyms for one word in Sinhala language and they are coming from various scripts including Pali, Sanskrit, Tamil and etc. No one knows which word suitable for various kinds of situations. Even expert Sinhala professors didn’t know much about this.

As an example, if someone says, “I drink water” in English, there are several synonyms for the word “Water”. They are coming from different scripts and these words are used in different situations in Sinhala as shown in below.

- ජලය - Scientific Usage, Ex: - ජල විදුලි බලාගාරය, ජල බිල්පත
- වතුර - Normal Usage, Ex: - වතුර බොනවා, වතුර මල
- පැන් - Religious Usage (by Buddhists).
- දිය - Literature Usage.

Here we have to find the most suitable Sinhala word. So, when finding suitable Sinhala word, we have to look for other words in the sentence as well. We can translate the above sentence (I drink water) as මම වතුර බොමි, මම ජලය බොමි, මම පැන් බොමි, මම දිය බොමි. Likewise, there are a number of ways to say the same thing in Sinhala language. But in this case most suitable translation is මම වතුර බොමි. Therefore, the problem is to find the most appropriate word for the considered situation.

A thesaurus can be used to find synonyms. In general, a thesaurus is a reference work that group list of words according to their similarity of meaning. There are so many thesauri that are available online for the English language. But there is no such thing that exists for the Sinhala language. Therefore, the requirement of an intelligent tool to do this process for the Sinhala language in an automated way is essential for the Sri Lankan people. It is very important and valuable for them.

## Project Objectives

The goal of this research project is to develop an Intelligent Sinhala-English Dictionary, Thesaurus & Word-Lookup tool to translate and find the context of words in Sinhala and English languages. 
 
## System Design Diagram

![System Design Diagram]([https://raw.githubusercontent.com/maneeshaindrachapa/FYP/master/WorkInProgress/Docs/images/System%20Diagram%20(Data%20Accessing%20%26%20Processing%20Layer).png](https://raw.githubusercontent.com/maneeshaindrachapa/FYP/master/WorkInProgress/Docs/images/System%20Diagram%20(Data%20Accessing%20%26%20Processing%20Layer).png))

 - **Language identifier module**: Mainly used the Deep Learning based approch with the character level diffrent things in the both Sinhala & English languages.
 - **Spell Checker Module**: Use the spell checker module developing by parrallel research group.
 - **Pos-tagger module**: Use already exists pos tagger module for both sinhala & English languages.
 - **Language translation module**: Use Google translater only for the translation
 - **Similar word cluster generator**: This is the main module of this research project. The main task of this module is to identify a similar word cluster for a given word. For the implementation of this module, we hope to use the word embedding technique which helps to get the similar word cluster.
For the implementation, we planned to use word-to-vector based approach as the word-embedding to extract the synonym words. After we successfully build the word-vector space for out text corpus then we get the synonyms based on the k-nearest neighbor approach with the euclidean distance between word points.
![Vector spaces](https://github.com/maneeshaindrachapa/FYP/blob/master/WorkInProgress/Docs/images/vecotor_space.jpg?raw=true)
d1 & d2 distances canbe calculated with the euclidean distance based approach or cosine distance based approach. 
![Equations](https://raw.githubusercontent.com/maneeshaindrachapa/FYP/master/WorkInProgress/Docs/images/equations.jpg)
 - **Word example sentence extractor**: This module is basically used to give and supportive sentence for a given word. In our system implementation, we hope to extract the example sentence from a text corpus. We planned to extract sentences that include the user input word and which is able to give an idea about the word.

## System Upto Now
![System upto now](https://raw.githubusercontent.com/maneeshaindrachapa/FYP/master/WorkInProgress/Docs/images/screenshot.png)
<h6 align="center"><a href="http://thesaurus.projects.uom.lk">thesaurus.projects.uom.lk</a></h6>
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQzNzEyMDE4NSwxMzg4NTQwMjY3LC00NT
U0MjAxNjMsLTU5NTg4MzU5OCwtMTMyMDY3ODE5NiwtNzkwNzg5
ODcxLDE0MDEzMzU1MjQsLTQxMjQ4ODgzMSw4MjQ0NDMxNzAsMT
EyNzc3NDQ2OCwtMTY5Njc5MjA5XX0=
-->