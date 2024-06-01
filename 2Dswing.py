# This is a code written by Harish from Exinc in 2020s. All the best
# Its about swing of a bat with stars as a straight line in a screen getting updated.

import time
arbitan3030=1
spd1=10
spd2=2
accel=2
deccel=1
x=' '
st='*'
x1=0
x2=50
m1=1
m2=1

flag=0
g=1
y0=20
u=0;
k=0
for i in range(1,50):
    t=(i-k)*0.2
    x1=x1+0.2*spd1
    st3=x*int(x1)+'0'
    y=y0+u*t-0.5*g*t**2
    print('\n'*50)
    for j in range(1,22):
        j1=int(22-y)

        if(j==j1):
            print(st3)
        if(j!=j1):
            print('\n')
            
        if(int(y)<1&flag==0):
            u=g*t
            y0=0
            k=i
            flag=1
   
    
    time.sleep(.05)
    
    
