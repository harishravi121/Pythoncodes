print(ord('a')-96)
print('if')
s=''
for i in range(26):
	s+= chr(i+97)+' '+str(i+1)+'  '
	
print(s)
	
print()
print('Decode')
print()
sentance='is a 2016 british experimental protest film that was produced directed and shot'
n=random.randint(1,15)
s=''
for i in range(len(sentance)):
	if(sentance[i]==' '):
		s+='  '
	else:
	    s+=str(ord(sentance[i])-96+n)+' '
	    
print(s)
	
	
