import time
import random
for i in range(10):
    a=input()
    start=time.time()
    b=input()
    stop=time.time()
    print((stop-start)*1000*random.random())
