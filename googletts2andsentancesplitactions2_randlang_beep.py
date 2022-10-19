from google_speech import Speech
from googletrans import Translator
import random
langs=['kn','ta','hi','te','en','de','zh-CN','ru']
import winsound

para='''The role of literary theory in narrative has been disputed; with some interpretations like Todorov's narrative model that views all narratives in a cyclical manner, and that each narrative is characterized by a three part structure that allows the narrative to progress. The beginning stage being an establishment of equilibrium—a state of non conflict, followed by a disruption to this state, caused by an external event, and lastly a restoration or a return to equilibrium—a conclusion that brings the narrative back to a similar space before the events of the narrative unfolded'''
a=para.split('.')
a1=["Do excercise","Pray to god"," Bathe well","Eat well","Sleep well","Work well","Grow well","Play well","Apply to jobs","Take medicenes"]
for i in range(20):
    lang=random.choice(langs)
    sent=random.choice(a)
    
    translator = Translator()
    translated = translator.translate(sent, src='en', dest=lang)

    speech = Speech(translated.text, lang)


    speech.play()
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random()))
