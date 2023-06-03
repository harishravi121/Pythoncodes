print(ord('a')-96)
print('if')
s=''
for i in range(26):
	s+= chr(i+97)+' '+str(i+1)+'  '
	
print(s)
	
print()
print('Decode  if its n*a+b ')
print()
sentance='winter is cool'

s=''
for i in range(len(sentance)):
	if(sentance[i]==' '):
		s+='  '
	else:
	    s+=str((ord(sentance[i])-96)*137+4)+' '
	    
print(s)
	
	
