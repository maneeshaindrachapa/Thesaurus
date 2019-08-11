import os
from gtts import gTTS

entries = os.listdir('modules/tts/audio_db/')

def audio_gen(Text, language):
    TTS = gTTS(text=Text, lang=language)
    file_path = Text + ".mp3"
    if (file_path not in entries):
        TTS.save("modules/tts/audio_db/" + file_path)        # Save to mp3 in current dir.
    return os.path.abspath("modules/tts/audio_db/" + file_path)

# audio_gen("cat", 'en')
