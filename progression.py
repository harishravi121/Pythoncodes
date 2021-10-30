import random
d=random.randint(2,10)
a=random.randint(1,100)
st1=''
tn=a
st1=st1+str(tn)+' '
for i in range(10):
    tn=tn+d
    st1=st1+str(tn)+' '

print('A progression is ', st1)
