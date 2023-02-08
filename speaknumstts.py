import pyttsx3
import random
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',random.randint(150,260))


for i in range(10):
    engine.setProperty('rate',random.randint(150,260))
    k=str(random.randint(0,1000))
    print(i)
    print(k)
    engine.say(k)
    engine.runAndWait()
    

    time.sleep(.1)
