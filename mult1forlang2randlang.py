import  random
from num2words import num2words
from googletrans import Translator
lang='hi'
langs=['ta','te','kn','hi','de']
for i in range(5):
    lang=random.choice(langs)
    a=random.randint(1,100)
    b=random.randint(1,1000)
    print('what is ',a,'*',b)
    l= 'what is '+num2words(a)+' multiplied by '+num2words(b)+' equal to?'
    sent=l
    print(sent)
    
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)
    print(translated.text)
    '''c=input()'''
    d=a*b
    print(d)

    sent=num2words(d)
    print(sent)

    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)
    print(translated.text)
    print('')
