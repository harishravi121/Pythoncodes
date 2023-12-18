import random
n=10
a=[0]*n

#Generating an array of random nos
for j in range(n):
    a[j]=random.randint(1,100)

    
print(a)

#Shuffling and sorting in a loop
while 1:
    random.shuffle(a)
    a.sort()

