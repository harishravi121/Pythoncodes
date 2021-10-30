cnt=1

def checkprime(cnt):
    cnt2=cnt-1
    
    flag=0
    for j in range(2,cnt2):  #checking all nos below a particular value
        if(cnt%(j)==0):
            flag=1
            
    if(flag==0):
        print(cnt)
        
for i in range(10):
    cnt=cnt+1
    checkprime(cnt)
