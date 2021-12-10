import random

start=800
timemax=200


#cost of living per day

COL=100

days=10
cash=start
for i in range(3): #Going to competition 3 times with 10 rounds.
    cash=start
    for i in range(10):
        prizen=5e4/random.randint(int(.8*timemax),timemax)
        cash=cash+prizen-COL
    endcash=cash
    print(start,endcash)

print('Start cash end cash Means you enjoyed the tournament and have some cash left')



'''
800 2506.0340032475856
800 2547.9215803903717
800 2660.4525912163217
Start cash end cash Means you enjoyed the tournament and have some cash left
Means you enjoyed the tournament and have some cash left
We can make profit when rating is greater than 200

Lets make a nice simulation.

'''
