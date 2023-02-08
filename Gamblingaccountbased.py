Balance=1e7
import random


for i in range(10):
    print('How much percent do you wanna bet')
    a=int(input())*Balance/100
    b=random.randint(0,1)
    print('whats the bet 0 or 1')
    c=int(input())
    if(b==c):
        Balance+=a
        print('You won and balance is ',Balance)
    else:
        Balance-=a
        print('You Lost and balance is ',Balance)
