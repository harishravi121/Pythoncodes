import  random
from num2words import num2words
from googletrans import Translator
for i in range(5):
    a=random.randint(1,1000)
    b=random.randint(1,1000)
    print('what is ',a,'+',b)
    l= 'what is '+num2words(a)+' plus '+num2words(b)+' equal to?'
    sent=l
    print(sent)
    lang='de'
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)
    print(translated.text)
    '''c=input()'''
    d=a+b
    print(d)

    sent=num2words(d)
    print(sent)
    lang='de'
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)
    print(translated.text)
    print('')
