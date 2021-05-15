import random
s=''
for i in range(10):
    a=random.randint(1,100000)
    b=random.randint(0,a)
    c=random.randint(0,b)
    d=random.randint(0,c)
    s=s+str(d)+', '
print(s)
