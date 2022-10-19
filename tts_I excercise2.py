import pyttsx3
import random
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',random.randint(150,260))

engine.say('Lets do Jumping jacks')

for i in range(5):
    engine.setProperty('rate',random.randint(150,260))
    
    engine.say(str(i+1))
    engine.runAndWait()
engine.say('Lets do pushups')

for i in range(5):
    engine.setProperty('rate',random.randint(150,260))
    
    engine.say(str(i+1))
    engine.runAndWait()
    #time.sleep(random.random())



engine.say('Lets do wall situps')

for i in range(5):
    engine.setProperty('rate',random.randint(150,260))
    
    engine.say(str(i+1))
    engine.runAndWait()
engine.say('Lets do Ab crunches')

for i in range(5):
    engine.setProperty('rate',random.randint(150,260))
    
    engine.say(str(i+1))
    engine.runAndWait()


