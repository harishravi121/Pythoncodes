import random

words1=['cubing','chess','Peace','Engineering', 'Physics','Mathematics']

words2=['cubing','chess','Peace','Engineering', 'Physics','Mathematics','Biology']

actors=['KamalHasan','RajiniKanth','TayNew','NarendraModi']

words=actors

sent=''
for i in range(random.randint(3,6)):

    sent=sent+'#'+random.choice(words)+' '

print(sent)

'''
Thinking a lot and using a lot of equations and making peaceful games and solving things are amazing. Sports is cool and the simulation in that is also cool. 
Best wishes :)

'''
