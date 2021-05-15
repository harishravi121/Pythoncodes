import time
import random
for i in range(10):
    a=input()
    start=time.time()
    b=input()
    stop=time.time()
    print((2**(stop-start))*100*random.random())
