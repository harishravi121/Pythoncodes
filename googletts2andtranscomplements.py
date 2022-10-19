from google_speech import Speech
from googletrans import Translator
import random
lang='ta'
a=["You look good","You smell good","You feel good","You are kind","You are benovelant","You are philanthropic"]
for i in range(20):
    sent=random.choice(a)
    
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)

    speech = Speech(translated.text, lang)


    speech.play()
