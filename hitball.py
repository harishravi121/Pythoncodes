import time
spd1=5
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
for i in range(1,50):
    t=i*0.2
    x1=x1+0.2*spd1
    x2=x2-0.2*spd2


    if((x2-x1)<1&flag==0):
        spd1=-1*(spd1+spd2)
        flag=1
    if(x2>=x1):
        st3=x*int(x1)+'0'+x*int((x2-x1))+'|'
    if(x1>x2):
        st3=x*int(x2)+st+x*int((x1-x2))+st
    print('\n'*50)
    print(st3)
    time.sleep(.05)
    
    
