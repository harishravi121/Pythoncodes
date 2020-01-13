import time
spd=5
accel=2
deccel=1
x=' '
st='*'
x1=0
x2=0
for i in range(1,50):
    t=i*0.2
    st2=x*int(t*spd)+st
    x1=x1+0.2*(spd+accel*t)
    x2=x2+0.2*(spd-deccel*t)
    
    st3=x*int(x1)+st
    st4=x*int(x2)+st
    print('\n'*50)
    print(st2)
    print('\n')
    print(st3)
    print('\n')
    print(st4)
    
    time.sleep(.05)
    
    
