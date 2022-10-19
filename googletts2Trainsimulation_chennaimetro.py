from google_speech import Speech
from googletrans import Translator
import time
import winsound
import random

a=["Anna Nagar","Pachaiyappa","Thirumangalam","Nehru Park","Egmore "]
b="The next stop is "
c=". Doors will open on the left and close shortly afterwards. Mind the gap and alight from the train. "
d=" The doors are closing please stay away from the doors. "
for i in range(5):
    lang='ta'
    sent1=random.choice(a)
    sent=b+sent1+c
    print(sent)
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)

    speech = Speech(translated.text, lang)


    speech.play()
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))
    time.sleep(10)

    sent=d
    print(sent)
    lang='en'
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)

    speech = Speech(translated.text, lang)


    speech.play()
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))

    for j in range(20):
        print(j)
        time.sleep(8)

    
