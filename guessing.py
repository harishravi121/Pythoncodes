import random

a=random.randint(1,100)

for i in range(5):
    b=input()
    if(a==b):
        print('Cracked')
    else:
        print('Try again')
print('It was',a)
