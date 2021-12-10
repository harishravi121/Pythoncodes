#code to measure acceleration due to gravity by dropping a ball from head Can be done on phones too


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
    
    print('h=5.5 ft Time = ',round(falltime,2),' s ' ,round(g,2), ' m/s^2')


'''

Can make apps, excel sheets etc

old Time =  0.3962876796722412 s g=  21.01322925251021

h=5.5 ft Time =  0.47  s  15.14  m/s^2

Next improvement is to add data analysis on 10 drops.

Will upload in Github as Gravitytimer.py hope to get 1 million follows

'''


