import pyttsx3
import random
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',random.randint(150,260))

engine.say('Lets Excercise')
engine.runAndWait()
for i in range(10):
    engine.setProperty('rate',random.randint(150,260))
    a=random.randint(0,1)
    if(a==0):
        engine.say(str(random.randint(2,5))+' kicks')
        engine.runAndWait()
    if(a==1):
        engine.say(str(random.randint(2,5))+' dumbells')
        engine.runAndWait()
    time.sleep(30)
