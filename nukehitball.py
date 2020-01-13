import time
spd1=5
spd2=5
accel=2
deccel=1
E=20


ds=8;

x=' '
st='D'
st2='T'
x1=0
x2=70
m1=1
m2=1
#m1u1+m2u2=m1v1+m2v2 0.5(m1u1^2+m2u2^2)+E=0.5*(m1v1^2+m2v2^2)


flag=0
for i in range(1,50):
    t=i*0.2
    x1=x1+0.2*spd1
    x2=x2-0.2*spd2
    print(x1,x2)

    if((x2-x1)<1&flag==0):
        a=spd1
        spd1=-1*(spd2+ds)
        spd2=-1*(a+ds)
        flag=1
        st='He'
        st2='n'
        
    if(x2>=x1):
        st3=x*int(x1)+st+x*int((x2-x1))+st2
    if(x1>x2):
        st3=x*int(x2)+st+x*int((x1-x2))+st
    print('\n'*50)
    print(st3)

    time.sleep(.05)
    
    
