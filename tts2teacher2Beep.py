import pyttsx3
import random
import time
import winsound
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices') 
volume = engine.getProperty('volume')
engine.say('I am an adder')
for i in range(10):
    #Randomizing volume and other speech properties
    engine.setProperty('rate',random.randint(100,200))
    engine.setProperty('volume',.5+.5*random.random())
    k=random.randint(0,1)
    engine.setProperty('voice', voices[k].id)

    
    a=round(1000**random.random(),1)
    b=round(1000**random.random(),1)
    c=round(a+b,1)
    say=str(a)+' plus '+str(b)+' equals '+str(c)
    engine.say(say)
    engine.runAndWait()
    time.sleep(random.random())
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))