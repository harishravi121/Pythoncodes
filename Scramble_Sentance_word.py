import random
import time
start=time.time()
flag=0
#Array of words
a=['I','ate','a','Banana']
def sentancify(s): #Given an array of characters, it makes the word
    s2=''
    for i in range(len(s)):
        s2=s2+s[i]+' '
    return s2
print('The scrambled words are given enter the correct word')
for i in range(3):
    b=random.sample(a,len(a)) #sample the word array randomly
    print(sentancify(b))
        
