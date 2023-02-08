import pyttsx3
import random
import time

from google_speech import Speech
from googletrans import Translator
translator = Translator()

srclang='en'
destlang='kn'
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',random.randint(150,260))


for i in range(10):
    engine.setProperty('rate',random.randint(150,260))
    k=str(random.randint(0,1000))
    translated = translator.translate(k, src=srclang, dest=destlang)
    speech = Speech(translated.text, destlang)
    speech.play()
    print(i)
    print(k)

    time.sleep(.1)
