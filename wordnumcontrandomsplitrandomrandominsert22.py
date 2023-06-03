print(ord('a')-96)
print('if')
s=''
for i in range(26):
	s+= chr(i+97)+' '+str(i+1)+'  '
	
print(s)

a=['hi ','how ','bye ','cow ','dog ','going ','well ','this ','that ']

import random	
print()
print('Decode if encrypted with n+2 and a random bo inbetween summing extremes')
print()
sentance='time squared proportional to radius cubed'

n=2
n1=0
n2=0
n3=0
s=''
for i in range(len(sentance)):
        if(sentance[i]==' '):
                s+='   '

        else:
                n1=ord(sentance[i])-96+n
                n2=random.randint(0,n1-1)
                n3=n1-n2
                s+=str(n2)+' '+str(random.randint(1,9))+' '+str(n3)+'  '
	    
print(s)
	
	
