#chess clock

import time
import random
a=input()
tz=0
tz2=0
tx=time.time()
for i in range(10):
    a=input()
    ty=time.time()
    tz+=ty-tx
    print(tz,tz2,'seconds')
    b=input()
    tx=time.time()
    tz2=tx-ty
    print(tz,tz2,'seconds')
    #print((2**(stop-start))*100*random.random())
