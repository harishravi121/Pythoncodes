a=2
import random
n=0
ha=1
import time
x=0
for i in range(1,1000):
    
    print('hello world')
    while ha==1:
        
        b=random.sample((1,2,4,3,5,6),1)
        n=n+1
        print(b[0],n)
        if(b[0]==2):
            ha=0
            print(ha)
    ha=1
    x=n-x
    print('The random won at n th move ',n)
    time.sleep(3)
