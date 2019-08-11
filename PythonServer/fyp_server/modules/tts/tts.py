import os
from gtts import gTTS

entries = os.listdir('audio_db/')

def tts(Text, language):
    TTS = gTTS(text=Text, lang=language)
    file_path = Text + ".mp3"
    if (file_path not in entries):
        TTS.save("audio_db/" + file_path)        # Save to mp3 in current dir.


tts("cat", 'en')
