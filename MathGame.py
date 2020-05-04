import random
import time
start=time.time()
print('There will be 2 rounds of questions and you will be timed')
flag=0
for i in range(2):
    print('Round ', i+1)
    if flag==0:
        a=random.randint(0,99)
        b=random.randint(0,99)
        print('Sum ',a,' ',b,' equals')
        c=int(input())
        d=a+b
        if(c==d):
            print('Correct')
        else:
            print('wrong, the correct answer is ',d)
            flag=1

    if flag==0:
        a=random.randint(1,99)
        b=random.randint(1,99)
        print('Difference ',a,' ',b,' equals')
        c=int(input())
        d=a-b
        if(c==d):
            print('Correct')
        else:
            print('wrong, the correct answer is ',d)
            flag=1

    if flag==0:
        a=random.randint(1,19)
        b=random.randint(1,19)
        print('Product ',a,' ',b,' equals')
        c=int(input())
        d=a*b
        if(c==d):
            print('Correct')
        else:
            print('wrong, the correct answer is ',d)
            flag=1
    if flag==0:
        a=random.randint(1,99)
        b=random.randint(1,9)
        print('Division ',a,' ',b,'to one decimal place equals')
        c=float(input())
        d=a/b
        if(int(c*10)==int(d*10)):
            print('Correct')
        else:
            print('wrong, the correct answer is ',d)
            flag=1






if flag==0:
    stop=time.time()
    timeelapsed=stop-start
    print('Your time is ',timeelapsed)

