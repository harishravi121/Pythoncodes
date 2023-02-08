import pyttsx3
import random
import time
from google_speech import Speech
from googletrans import Translator

srclang='en'
destlang='ta'
engine = pyttsx3.init()

translator = Translator()


sent1='Lets Excercise'
translated = translator.translate(sent1, src=srclang, dest=destlang)
speech = Speech(translated.text, destlang)
speech.play()
engine.runAndWait()
for i in range(10):
    engine.setProperty('rate',random.randint(150,260))
    a=random.randint(0,2)
    if(a==0):
        sent1=str(random.randint(2,5))+' kicks'
        translated = translator.translate(sent1, src=srclang, dest=destlang)
        speech = Speech(translated.text, destlang)
        speech.play()

    if(a==1):
        sent1=str(random.randint(2,5))+' dumbells'
        translated = translator.translate(sent1, src=srclang, dest=destlang)
        speech = Speech(translated.text, destlang)
        speech.play()
    if(a==2):
        sent1=str(random.randint(2,5))+' catches'
        translated = translator.translate(sent1, src=srclang, dest=destlang)
        speech = Speech(translated.text, destlang)
        speech.play()
    time.sleep(30)
