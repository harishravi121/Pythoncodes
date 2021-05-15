import pyttsx3
import random
import time
import winsound
import numpy as np
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices') 
volume = engine.getProperty('volume')
engine.say('I am random calculations trainer.')
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
    a=round(1000**random.random(),1)
    b=round(1000**random.random(),1)
    d=round(a-b,1)
    
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))
    say=str(a)+' minus '+str(b)+' equals '+str(d)
    engine.say(say)
    engine.runAndWait()
    time.sleep(random.random())
    a=round(1000**random.random(),1)
    b=round(1000**random.random(),1)
    e=round(a*b,1)
    
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))
    say=str(a)+' multiplied by'+str(b)+' equals '+str(e)
    engine.say(say)
    engine.runAndWait()
    time.sleep(random.random())
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))
    a=round(1000**random.random(),1)
    b=round(1000**random.random(),1)
    f=round(a/b,1)
    say=str(a)+' divided by '+str(b)+' equals '+str(f)
    engine.say(say)
    engine.runAndWait()
    time.sleep(random.random())
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))

    a=round(1000**random.random(),1)
    b=round(1000**random.random(),1)
    f=round(np.exp(a),1)
    say=' Exponential '+ str(a)+' equals '+str(f)
    engine.say(say)
    engine.runAndWait()
    time.sleep(random.random())
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))
