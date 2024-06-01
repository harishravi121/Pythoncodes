# A series of MCQs keep popping up about addition.
# Made by Harish for benifit of school students or Adults for revision ocassionally.
#Such MCQ setting will be useful in Professorship to set problems for students in physics EE Cs etc changing order etc.
import random
import time



while 1:
    n1=random.randint(2,20)
    n2=random.randint(2,100)
    n3=random.randint(2,100)
    print(n1,n2,n3, 'what is sum')
    op=n1+n2+n3
    ans=[op,op+random.randint(2,10),op+random.randint(2,10),op+random.randint(2,10)]
    random.shuffle(ans)
    print(ans)
    chs=input()
    if(ans[int(chs)]==op):
        print('Correct, congrats')
    else:
        print('wrong')
