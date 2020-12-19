import random
import time
start=time.time()
flag=0
#Array of words


def convert(lst): 
    return (lst[0].split()) 
  
# Driver code 
lst =  ["Success comes from hard work."] 
print( convert(lst))
a= convert(lst)
def sentancify(s): #Given an array of characters, it makes the word
    s2=''
    for i in range(len(s)):
        s2=s2+s[i]+' '
    return s2

def wordify(w): #Given an array of characters, it makes the word
    c=''
    for i in range(len(w)):
        c=c+w[i]
    return c

print('The scrambled words are given enter the correct word')
for i in range(1):
    b=random.sample(a,len(a)) #sample the word array randomly
    #print(sentancify(b))
    for i in range(2):
        s3=''
        for i in range(len(a)): #5 Words scrambled
       
            word=b[i]
            c=random.sample(word,len(word)) #sample the word array randomly
            f=wordify(c) #It makes the word
            s3=s3+f
            s3=s3+' '

        print(s3)
        
