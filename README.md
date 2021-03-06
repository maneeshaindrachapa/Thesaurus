
<h6 align="center"><img align="center" src="https://github.com/maneeshaindrachapa/FYP/blob/master/AngularClient/src/assets/img/main_logo.png?raw=true"><h6>
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
 
## Key Layers in Implementation (Server-side) 

![System Architecture](https://github.com/maneeshaindrachapa/FYP/blob/master/WorkInProgress/Docs/images/FYP_Archi.png?raw=true)

There are 3 main layers in server side of the application,

**1. Data Layer**

This layer is responsible for storing the datasets and models which needed to each module of the system. All of these datasets and models are stored in the server to provide access whenever requested by a module.

**2. Data Accessing and Processing Layer**

This is the main module that responsible for return meaningful output from the system. In this layer there are separate modules which specified to execute specific tasks related to the user requests. The design diagram for this layer with separate modules as follows.

![Internal architecture of Data accessing and processing layer](https://github.com/maneeshaindrachapa/FYP/blob/master/WorkInProgress/Docs/images/System%20Diagram.png?raw=true)

 - [Language identifier module](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/lang_identifier)
 - [Spell Checker Module](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/spell_checker)
 - [Pos-tagger module](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/main/sinhala/pos_tag)
 - [Similar word cluster generator](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/main/sinhala/synonyms)
 - [Word definition extractor module](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/main/sinhala/definitions)
 - [Word example sentence extractor](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/main/sinhala/example_sentences)
 - [Language translation module](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/translator)
 - [Text-to-speech module](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/tts)
 - [Final output combiner](https://github.com/maneeshaindrachapa/FYP/tree/master/PythonServer/fyp_server/modules/formatter)
```
- Implemntation details written inside each module
```
**3. End-points Layer**

This is the layer in the server-side application which handle all the requests comes to the server in initial stage. This is the layer which responsible to initiate the server-side responsible module for the user request. In the end point layer, there are few different endpoints with different input data as below.

![Endpints of the system](https://github.com/maneeshaindrachapa/FYP/blob/master/WorkInProgress/Docs/images/end-points.jpg?raw=true)


## System Deployment
 #### Client side ([Web Client](https://github.com/maneeshaindrachapa/Thesaurus/tree/master/AngularClient))
 This client side of the application developed with [Angular CLI](https://cli.angular.io/). when we need to deploy we had to [build](https://angular.io/cli/build) the application and serve on web server. As the deployment steps,
 1. Build angular Application ([ng build](https://angular.io/cli/build))
 2. Set up apache on server ([on ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04-quickstart))
 3. Deploy app on Apache server

#### Server side ([Falsk Server](https://github.com/maneeshaindrachapa/Thesaurus/tree/master/PythonServer/fyp_server))
Server side of the application built on python [flask](http://flask.palletsprojects.com/en/1.1.x/) server as a REST Api. As the deployment steps,

 1. Setup python3 and pip3 on the server.
 2. Navigate to [PythonServer](https://github.com/maneeshaindrachapa/Thesaurus/tree/master/PythonServer) directory in the project.
 3. open the terminal and install requirements on [requirements.txt](https://github.com/maneeshaindrachapa/Thesaurus/blob/master/PythonServer/requirements.txt "requirements.txt").

 pip3 install -r requirements.txt

     
4. Add required data sets to the server.
 <br>i. Inside language identifier module we have to add trained model. <br>
 ii. Add example sentence data set to the [main/sinhala/example_sentences](https://github.com/maneeshaindrachapa/Thesaurus/tree/master/PythonServer/fyp_server/modules/main/sinhala/example_sentences) folder. <br>
iii. Add definitions data corpus to [man/sinhala/definitions](https://github.com/maneeshaindrachapa/Thesaurus/tree/master/PythonServer/fyp_server/modules/main/sinhala/definitions) folder. <br>
 iv. iii. dd pos tagger trained model to [main/sinhala/pos_tag](https://github.com/maneeshaindrachapa/Thesaurus/tree/master/PythonServer/fyp_server/modules/main/sinhala/pos_tag) folder.
 
5. Navigate to [fyp_server](https://github.com/maneeshaindrachapa/Thesaurus/tree/master/PythonServer/fyp_server) directory inside [PythonServer](https://github.com/maneeshaindrachapa/Thesaurus/tree/master/PythonServer) directory and start the flask server.

> python3 app.py

## System Up to Now


> Web Application

![Web Interface 1](https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/web_interface_1.png?raw=true)

![Web Interface 2](https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/web_interface_2.png?raw=true)

<h6 align="center"><a href="http://thesaurus.projects.uom.lk">thesaurus.projects.uom.lk</a></h6>

> Mobile Application

![Mobile Application 1](https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/mobile_interface_1.jpg?raw=true)

![Mobile Application 1](https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/mobile_interface_2.jpg?raw=true)



<!--stackedit_data:
eyJoaXN0b3J5IjpbODQ4ODA1NTY0LDc4MzAyMzgsMTcyODcxMj
M1NywtNTYxNDYwMDc3LDY5NDA2MDk5NSwtMTkyNjExMDc2LC0x
NTAwNTA1MTgxLDEwNjY1OTE1NzcsNTg0NTAyNDYwLDE3MjY0OD
A4NjEsMjQ0NDAyNDAzLDcxNDExNjkyNSw2MzIzMzIzNCw0MzE2
MzAxNzcsNzkzODY0OTg3LDc1MDY3MDYwLDc4NTYzNDkzOSwtMz
I4MDQ2Nzk1LC0yMTI1NzA2MjAxLDEzODg1NDAyNjddfQ==
-->