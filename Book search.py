import random
import time

s=100


c1a=1
c1b=s
c1=1
inp2='s'
while(1):

    c=input()

    if((inp2=='s')&(c=='s')):
        c1=random.randint(c1,c1b)


    if((inp2=='s')&(c=='a')):
        c1b=c1   
        c1=random.randint(c1a,c1)
        
    
    if((inp2=='a')&(c=='s')):
        c1a=c1
        c1=random.randint(c1,c1b)


    if((inp2=='a')&(c=='a')):
        c1=random.randint(c1a,c1)
          
                    
    inp2=c
    print(c1)
