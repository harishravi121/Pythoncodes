import random

start=800
Rating=200


#cost of living per day

COL=100

days=10
cash=start
for i in range(10):
    prizen=random.randint(Rating)
    cash=cash+prinzen-COL
endcash=cash
print(startcash,endcash)
'''
We can make profit when rating is greater than 200

Lets make a nice simulation.

