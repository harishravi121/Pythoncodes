import pyttsx3
import random
import time
with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split(".")))
file.close()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
for i in range(3):
    a=random.choice(words)
    engine.setProperty('rate',random.randint(100,200)) 
    engine.say(a)
    print(a)
    engine.runAndWait()
    time.sleep(random.random())
    print(i)
