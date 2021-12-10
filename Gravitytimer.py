import time
n=3
S=5.5*.3
for i in range(10):
    a=input()
    start=time.time()
    b=input()
    stop=time.time()
    falltime=stop-start
    g= 2*S/falltime**2
    
    print('h=5.5 ft Time = ',round(falltime,2),' ' ,round(g,2), ' m/s^2')


'''

Can make apps, excel sheets etc

Time =  0.3962876796722412 s g=  21.01322925251021

'''


