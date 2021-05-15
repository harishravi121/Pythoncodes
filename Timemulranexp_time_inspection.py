import time
import random
for i in range(10):
    a=random.random()*30 
    print(a)
    time.sleep(a) #Random inspection time
    a=input()
    start=time.time()
    b=input()
    stop=time.time()
    t=(stop-start) #Timer between start and stop
    print(t,'seconds')
    print((2**(stop-start))*100*random.random())
