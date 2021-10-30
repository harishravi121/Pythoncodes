cnt=10000
str1=''
import random
test=1
def checkprime(cnt):
    global str1
    global test
    test=1
    cnt2=cnt-1
    
    flag=0
    for j in range(2,cnt2):  #checking all nos below a particular value
        if(cnt%(j)==0):
            flag=1
            
    if(flag==0):
       test=cnt2
        
for i in range(100):
    cnt=random.randint(100,100000)
    checkprime(cnt)
    a=test
    checkprime(cnt)
    b=test
    key=a*b
    if(key!=1):
        print(key)
    
print('A key is 10000 are', key)
