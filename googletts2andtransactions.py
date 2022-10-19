from google_speech import Speech
from googletrans import Translator
import random
lang='te'
a=["Do excercise","Pray to god"," Bathe","Eat well","Sleep well","Work well","Grow well","Play well","Apply to jobs","Take medicenes"]
for i in range(20):
    sent=random.choice(a)
    
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)

    speech = Speech(translated.text, lang)


    speech.play()
