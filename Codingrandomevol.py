import random
import time

t=time.time()
a=random.randint(999,10000)
t2=time.time()
print(a)
print(t2-t,'secs')

a=1234
b=1
e=1

print('choose mid 4 its done after squaring. Clearly its random')

   
def harirand():
    global b,a,e
    b=a**2
    c=str(b)
    d=c[2:6]
    e=int(d)
    a=e
    print(e)

t=time.time()
harirand()
t2=time.time()

print(t2-t,'secs')   
'''

choose mid 4 its done after squaring. Clearly its random
9187
0.0 secs
choose mid 4 its done after squaring. Clearly its random
2275
0.0049495697021484375 secs
'''
