import random
s=''
for i in range(10):
    a=random.random()
    b=random.randint(1,10)
    c=b**a
    d=random.randint(1,20)
    e=d**c
    for j in range(random.randint(1,5)):
        s=s+str(round(e,2))+', '
print(s)
