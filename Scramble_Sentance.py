import random
import time
start=time.time()
flag=0
#Array of words
a=['Hir.','VProf.','Dr.','Harish','KelvinPasteur','Ravi']
def wordify(w): #Given an array of characters, it makes the word
    c=''
    for i in range(len(w)):
        c=c+w[i]
    return c
print('The scrambled words are given enter the correct word')
for i in range(3):
    s=''
    for i in range(len(a)): #5 Words scrambled
        if flag==0:
            word=a[i]
            b=random.sample(word,len(word)) #sample the word array randomly
            f=wordify(b) #It makes the word
            s=s+f
            s=s+' '

    print(s)
        
