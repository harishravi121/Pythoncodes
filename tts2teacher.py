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

    
    a=random.randint(0,10)
    b=random.randint(0,10)
    c=a+b
    say=str(a)+' plus '+str(b)+' equals '+str(c)
    engine.say(say)
    engine.runAndWait()
    time.sleep(random.random())
