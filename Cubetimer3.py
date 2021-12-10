import time

for i in range(10):
    a=input()
    start=time.time()
    b=input()
    stop=time.time()
    cubetime=stop-start
    print('Time = ',cubetime,'Score 1= ',1000/cubetime,'Score 2= ',1e6/cubetime**2)


'''

Time =  8.144214391708374 Score 1=  122.78655152031608 Score 2=  15076.537234251236


Time =  8.615230083465576 Score 1=  116.07351055187819 Score 2=  13473.059851836979

What is the right game theory scoring sytem based on order of cube others etc. We should just self motivate for least time.

Happy to sell or gift code on github or email

Dr. Harish Ravi

Remains to see if I get self motivated to reach lowest time by sharing ocassionally and maintaining a log in a file next.


Time =  79.20972800254822 Score 1=  12.624711954165901 Score 2=  159.3833519256594
'''
