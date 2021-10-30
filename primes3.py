cnt=1500
str1=''

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
    cnt=cnt+1
    checkprime(cnt)
print('Some primes near 1500 are', str1)
