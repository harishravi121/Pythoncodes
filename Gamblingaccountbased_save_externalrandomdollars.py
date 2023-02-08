Balance=1e6
import random
import pickle
if(1==0):
    file=open('Betexdol','wb')
    pickle.dump(Balance,file)
    file.close()


file=open('Betexdol','rb')
Balance=round(pickle.load(file))
file.close()
for i in range(5):
    print('How much percent do you wanna bet')
    a=round(int(input())*Balance/100)
    b=random.randint(0,1)
    print('Did you win 1 or lose 0')
    c=int(input())
    if(c==1):
        Balance+=a
        print('You won and balance is ',Balance,' $')
    else:
        Balance-=a
        print('You Lost and balance is ',Balance,' $' )
    file=open('Betexdol','wb')
    pickle.dump(Balance,file)
    file.close()

