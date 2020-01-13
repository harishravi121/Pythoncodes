import time
import numpy as np
spd1=25
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
xbat1=100
ybat1=0
xbat2=100
ybat2=20
omega=1e-1
flag2=0
for i in range(1,50):
    t=(i-k)*0.2
    ybat2=20-20*np.cos(omega*i*0.2)
    xbat2=100-20*np.sin(omega*i*0.2)
    st4=x*int(xbat2)+'*'
    

    
    x1=x1+0.2*spd1
    st3=x*int(x1)+'0'
    y=y0+u*t-0.5*g*t**2
    print('\n'*50)
    a=int(abs((y-20)*(x1-xbat2)/-(y-ybat2)*(x1-100)))

    if(a==0&flag2==0):  #Hit by the bat
        flag2=1
        print(flag2)
        
        u=spd1/4
        spd1=-spd1
        y0=y
        
        k=i
       
    
    for j in range(1,22):  #priting of the motion
        j1=int(22-y)
        j2=int(22-ybat2)

        if(j==j2):
            print(st4)
        if(j==j1):
            print(st3)
        if(j!=j1|j!=j2):
            print('\n')
            
        if(int(y)<1&flag==0):
            u=g*t
            y0=0
            k=i
            flag=1
   
    print(x1,y)
    time.sleep(.05)
    
#x1 y1 and x2 y2 interlieve them well and then invoke angular rotation equation
#Then check if they touch on the line joining them, then invoke the velocities and then implement the motion after reflection
