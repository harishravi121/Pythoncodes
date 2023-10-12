import random
N=10

a=[] # array

for i in range(N):
    a.append(random.randint(0,N*N))

for j in range(len(a)-1,0,-1):
 for i in range(j):
    if(a[i]<a[i+1]):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp

print(a)

b=[0]*10
b[0]=N*N
for i in range(N-1):
    b[i+1]=b[i]-random.randint(0,2*N)
print(b)

#Two sorted random numbers. First uses 2 loops but we don't see much change in art
#[99, 83, 68, 59, 54, 52, 42, 35, 33, 16]
#[100, 85, 82, 78, 58, 48, 28, 26, 9, -1]
