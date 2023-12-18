import random
n=10
a=[0]*n
while 1:
        
    for j in range(n):
        a[j]=random.randint(1,100)

    a.sort()
print(a)
