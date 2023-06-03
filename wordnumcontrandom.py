print(ord('a')-96)
print('if')
s=''
for i in range(26):
	s+= chr(i+97)+' '+str(i+1)+'  '
	
print(s)

a=['hi ','how ','bye ','cow ','dog ',' going',' well','this ','that ']

import random	
print()
print('Decode')
print()
sentance=random.choice(a)+' '+random.choice(a)
n=random.randint(1,15)
s=''
for i in range(len(sentance)):
	if(sentance[i]==' '):
		s+='  '
	else:
	    s+=str(ord(sentance[i])-96+n)+' '
	    
print(s)
	
	
