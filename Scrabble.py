import random
import time
start=time.time()
flag=0
a=['word','hello','high','how','zebra','cricket','football','volleyball','tennis','master','abandon','excercise','narrate','rivet' ]
def wordify(w):
    c=''
    for i in range(len(w)):
        c=c+w[i]
    return c
print('The scrambled words are given enter the correct word')
for i in range(5):
    if flag==0:
        word=a[random.randint(0,len(a)-1)]
        b=random.sample(word,len(word))
        f=wordify(b)
        print(f)
        c=input()
        if c==word:
            print('Correct')
        else:
            print('Wrong the correct answer is ', word)
            flag=1

if flag==0:
    stop=time.time()
    timeelapsed=stop-start
    print('Your time is ',timeelapsed)
