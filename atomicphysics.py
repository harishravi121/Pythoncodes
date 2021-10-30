import random

str1=''
for i in range(5):
    n=random.randint(1,20)
    En=round(-13.6/n/n,4)
    str1=str1+str(n)+' '+str(En)+' eV '
print('Random atomic numbers and energy')
print(str1)
