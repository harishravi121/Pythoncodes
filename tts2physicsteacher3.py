import pyttsx3
import random
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices') 
volume = engine.getProperty('volume')

engine.say('For 1 mole in 1 meter cube, ')
for i in range(10):
    #Randomizing volume and other speech properties
    engine.setProperty('rate',random.randint(100,200))
    engine.setProperty('volume',.5+.5*random.random())
    k=random.randint(0,1)
    engine.setProperty('voice', voices[k].id)

    
    T=round(500**random.random(),1)
    V=1
    
    R=8.314
    n=1
    p=round(n*R*T/V,1)
    
    say='If temperature is '+str(T)+' kelvin, the pressure is '+str(p)+' pascals.'
    engine.say(say)
    engine.runAndWait()
    time.sleep(random.random())
