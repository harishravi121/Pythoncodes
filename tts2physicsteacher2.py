import pyttsx3
import random
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices') 
volume = engine.getProperty('volume')  
for i in range(10):
    #Randomizing volume and other speech properties
    engine.setProperty('rate',random.randint(100,200))
    engine.setProperty('volume',.5+.5*random.random())
    k=random.randint(0,1)
    engine.setProperty('voice', voices[k].id)

    
    t=round(10**random.random(),1)
    b=round(0.5*9.8*t**2,1)
    
    say='If an object free falls for '+str(t)+' seconds, it falls by '+str(b)+' meters.'
    engine.say(say)
    engine.runAndWait()
    time.sleep(random.random())
