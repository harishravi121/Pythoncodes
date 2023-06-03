print(ord('अ')-2308)
print('if')
s=''
for i in range(98):
	s+=chr(i+2309)+' '+str(i+1)+'  '

print(s)
	
print()
print('Decode')
print()
sentance='मैं इस दुनिया से प्यार करता हूँ'
s=''
for i in range(len(sentance)):
	if(sentance[i]==' '):
		s+='  '
	else:
	    s+=str(ord(sentance[i])-2308)+' '
	
print(s)