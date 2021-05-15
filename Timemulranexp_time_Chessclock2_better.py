#chess clock

import time
import random

tz=0
Tot=60 #Total time
Tot2=50+random.random()*10 #Total time with a fun variable
tz2=0
tx=time.time()
print(Tot-tz,Tot2-tz2,'seconds')
a=input()
for i in range(10):
    a=input()
    ty=time.time()
    tz+=ty-tx
    print(Tot-tz,Tot2-tz2,'seconds') #Printing time
    b=input()
    tx=time.time()
    tz2+=tx-ty
    print(Tot-tz,Tot2-tz2,'seconds')
    print((2**(tz))*100*random.random(),(2**(tz2))*100*random.random())
