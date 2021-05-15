import random
s=''
for i in range(10):
    a=random.random()
    b=random.randint(1,10)
    c=b**a
    d=random.randint(1,20)
    e=d**c
    for j in range(random.randint(2,6)):
        s=s+str(round(e+random.random(),2))+', '
print(s)
