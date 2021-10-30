import random
d=random.randint(2,10)
a=random.randint(1,100)
n=random.randint(5,10)
st1=''
tn=a
st1=st1+str(tn)+' '
for i in range(n):
    tn=tn*d
    st1=st1+str(tn)+' '

print('A geometric progression is ', st1)
