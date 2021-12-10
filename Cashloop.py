import random

start=800
Rating=200


#cost of living per day

COL=100

days=10
cash=start
for i in range(3): #Going to competition 3 times with 10 rounds.
    for i in range(10):
        prizen=random.randint(10,Rating)
        cash=cash+prizen-COL
    endcash=cash
    print(start,endcash)

print('Start cash end cash Means you enjoyed the tournament and have some cash left')



'''
800 806
800 1372
800 1709

Means you enjoyed the tournament and have some cash left
We can make profit when rating is greater than 200

Lets make a nice simulation.

'''
