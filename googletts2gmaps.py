from google_speech import Speech
from googletrans import Translator
import time
import winsound
import random

a=["Head south on 14th Cross Rd toward 5th Main Road","Turn right at the 1st cross street onto 5th Main Road","Turn right onto 10th Cross Rd","Turn left toward 1st Main Rd","Continue onto 1st Main Rd"," Turn right after Patanjali Store (on the right)"]

for i in range(5):
    lang='en'
    sent=random.choice(a)+' for '+str(random.randint(100,150))+'meters.'
    
    print(sent)
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)

    speech = Speech(translated.text, lang)


    speech.play()
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))
    #time.sleep(10)

    
    for j in range(5):
        print(j)
        time.sleep(8)

    
