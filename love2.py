import pyttsx3
import random
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while 1:
    engine.setProperty('rate',random.randint(150,260))
    y=' I love you'


    engine.say(y)
    engine.runAndWait()
    z=['Missing your handsome face already.','You make me feel like the most special woman on earth.','You are everything I could want in a man.','I would marry you all over again, just so you know.','Every single morning I thank God for you.','I love you. Whatever comes our way and whatever happens, we’re in this together.','Your heart is so full of love, and I am lucky enough to find a place there. Love you, honey.']

    z2=random.choice(z)
    engine.say(z2)
    engine.runAndWait()
