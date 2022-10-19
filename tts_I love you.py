import pyttsx3
import random
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
for i in range(10):
    engine.setProperty('rate',random.randint(100,200)) 
    engine.say("I love you")
    engine.runAndWait()
    #time.sleep(random.random())
