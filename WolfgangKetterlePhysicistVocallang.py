import pyttsx3
import random
import time
from google_speech import Speech
from googletrans import Translator


srclang='en'
destlang='kn'
translator = Translator()

responses1=['Physics is great and fun','Ground state of Hydrogen is -13.6eV','BEC is Bose Einstein Condensate at nano kelvin','h=6e-34 Js and c=3e8 m/s']
responses2=['FInd the divergence of r^2cos(\\ theta) er','E=mc^2 and \gamma=1/\sqrt(v^2-c^2)','EMF of a line is Blv','Power radiated by a hot black body is AesigmaT^4']
responses3=['We have to go to conferences and publish in journals like nature, science and EJPD']
responses4=['Life is prokaryotes and Eukaryotes','Heart has 4 chambers and couples to body and respiratory system','Brain has a billion neurons','Eat 1900 calories a day and atleast 60 g of protein']
responses5=['Love all serve all','Help ever hurt never','Patience is a virtue','There should be deva chintana',' Observe a path of devotion']
responses6=['Compound interest is (1+r/100)^n','As prices increase demand decreases','Stocks, mutual funds and real estate are good investment vehicles']

responses=responses1+responses2+responses3+responses4+responses5+responses6
while 1:
    a=input()
    z2=random.choice(responses)
    #print('Ketterle the physicist : ' ,random.choice(responses))
    translated = translator.translate(z2, src=srclang, dest=destlang)
    speech = Speech(translated.text, destlang)
    speech.play()
