a = 2
import random

n = 0
ha = 1
import time

x = 0

print('hello world')
while ha == 1:

    b = random.sample((1, 2, 4, 3, 5, 6,7,8,9), 1)
    c= random.sample((1,2,3,4),1)
    

    s=b[0] + 10 * b[1]
    print(s)
    time.sleep(3)
    for i in range(1,20):
        print()
    a=int(input())

    if (s == a):
        print('congrats')



