Balance=1e7
import random
import pickle
if(1==-0):
    file=open('Bet','wb')
    pickle.dump(Balance,file)
    file.close()


file=open('Bet','rb')
Balance=round(pickle.load(file))
file.close()
for i in range(5):
    print('How much percent do you wanna bet')
    a=round(int(input())*Balance/100)
    b=random.randint(0,1)
    print('whats the bet 0 or 1')
    c=int(input())
    if(b==c):
        Balance+=a
        print('You won and balance is ',Balance,' ₹')
    else:
        Balance-=a
        print('You Lost and balance is ',Balance,' ₹')
    file=open('Bet','wb')
    pickle.dump(Balance,file)
    file.close()

