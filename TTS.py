from gtts import gTTS
import os
from playsound import playsound

import gtts.lang
lang_arr = gtts.lang.tts_langs()

def TextToSpeech(text, lg):
    file_name = "speak.mp3"
    lang = list(lang_arr.keys()) [list(lang_arr.values()).index(lg)]
    tts = gTTS(text, lang=lang)
    tts.save(file_name)
    playsound(file_name, True)
    os.remove(file_name)