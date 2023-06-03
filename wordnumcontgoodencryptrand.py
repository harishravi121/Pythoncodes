print(ord('a')-96)
print('if')
s=''
for i in range(26):
	s+= chr(i+97)+' '+str(i+1)+'  '
	
print(s)
import random	
print()
print('Decode  if its n*a+b and broken into two randoly sized chunks to add')
print()
sentance='winter is cool'

s=''
x=0
for i in range(len(sentance)):
        if(sentance[i]==' '):
                s+='   '

        else:
                x=(ord(sentance[i])-96)*137+4
                y=random.randint(0,x-1)
                z=x-y
                s+=str(y)+' '+str(z)+'  '

print(s)
	
	
