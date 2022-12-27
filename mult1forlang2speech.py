import  random

from google_speech import Speech
from num2words import num2words
from googletrans import Translator
lang='ta'
for i in range(5):
    a=random.randint(1,100)
    b=random.randint(1,1000)
    print('what is ',a,'*',b)
    l= 'what is '+num2words(a)+' multiplied by '+num2words(b)+' equal to?'
    sent=l
    print(sent)
    
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)
    print(translated.text)
    speech = Speech(translated.text, lang)
    speech.play()
    '''c=input()'''
    d=a*b
    print(d)

    sent=num2words(d)
    print(sent)

    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)
    print(translated.text)
    speech = Speech(translated.text, lang)
    speech.play()
    print('')
