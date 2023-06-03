print(ord('அ')-2948)
print('if')
s=''
for i in range(98):
	s+=chr(i+2949)+' '+str(i+1)+'  '

print(s)
	
print()
print('Decode')
print()
sentance='எனக்கு உணவு மிகவும் பிடிக்கும்'

s=''
for i in range(len(sentance)):
	if(sentance[i]==' '):
		s+='  '
	else:
	    s+=str(ord(sentance[i])-2948)+' '
	
print(s)