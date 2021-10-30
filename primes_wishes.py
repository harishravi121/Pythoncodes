cnt=10000
str1=''
import random

def checkprime(cnt):
    global str1
    cnt2=cnt-1
    
    flag=0
    for j in range(2,cnt2):  #checking all nos below a particular value
        if(cnt%(j)==0):
            flag=1
            
    if(flag==0):
       str1=str1+str(cnt)+' '
        
for i in range(100):
    cnt=random.randint(100,100000)
    checkprime(cnt)
print('Here are some primes have a good day lol', str1)
