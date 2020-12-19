import random
import time
start=time.time()
flag=0
#Array of words
a=['word','hello','high','how','zebra','cricket','football','volleyball','tennis','master','abandon','excercise','narrate','rivet' ]
def wordify(w): #Given an array of characters, it makes the word
    c=''
    for i in range(len(w)):
        c=c+w[i]
    return c
print('The scrambled words are given enter the correct word')
while 1: 

    word=a[random.randint(0,len(a)-1)]
    b=random.sample(word,len(word)) #sample the word array randomly
    f=wordify(b) #It makes the word
    h=''
    while(h!=f):
        g=random.sample(f,len(f))  
        h=wordify(g)
    
