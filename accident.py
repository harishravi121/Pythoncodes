import random
#no of vehicles=n
n=random.randint(10,100)
#p=accidentprobability is p
p=0.01
accident=1-(1-p)**n
print(n,accident)


'''

72 0.5150086297258372
Sample output


'''
