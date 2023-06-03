print(ord('அ')-2948)
print('if')
s=''
for i in range(98):
	s+=chr(i+2949)+' '+str(i+1)+'  '

print(s)
import random	
print()
print('Decode')
print()
sentance='எனக்கு உணவு மிகவும் பிடிக்கும்'

s=''

n=2#random.randint(1,15)
n1=0
n2=0
n3=0
s=''
for i in range(len(sentance)):
        if(sentance[i]==' '):
                s+='   '

        else:
                n1=ord(sentance[i])-2948+n
                n2=random.randint(0,n1-1)
                n3=n1-n2
                s+=str(n2)+' '+str(n3)+'  '	
print(s)
