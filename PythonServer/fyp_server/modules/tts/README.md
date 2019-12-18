<h2 align="center">Text-to-speech Module (TTS)</h2>

We used this module to convert text into speech. If the user does not know how to pronounce a word, he can enter that word into the system and can hear the pronunciation by clicking volume button. This volume button is shown in the web interface as below.

<figure>  
<img align=center src="https://github.com/maneeshaindrachapa/Thesaurus/blob/master/WorkInProgress/Docs/images/tts.jpg?raw=true"  alt="Working system interfaces for the language identifier"  style="width:100%">  
<figcaption align=center>TTS implementation in the system</figcaption>  
</figure>

As this is not relevant to our research area, we used Google Text To Speech (gTTS) API to implement this. In here, gTTS is converting the text into voice. gTTS takes 2 parameters as text and language of the text to execute the convert process.

If a word is pronounced for the first time, then it will save to a new mp3 file in the server and system will play it. That file is named as the text + .mp3 extension. As an example, if a user submits the word ‘අම්මා’ then the mp3 file is saved as ‘අම්මා.mp3’. This mp3 file will only be created if there is not such an mp3 file already exists. Therefore, there exists only one mp3 file for a particular word in the server. Whenever user interact with the pronunciation of a word, this process will happen. That is how user hear the pronunciation of the word. This is working for both Sinhala and English language.




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NzEzOTcwMzNdfQ==
-->