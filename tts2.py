import pyttsx3
import random
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
for i in range(10):
    engine.setProperty('rate',random.randint(100,200)) 
    engine.say("Aum Sri Sairam")
    engine.runAndWait()
    #time.sleep(random.random())
