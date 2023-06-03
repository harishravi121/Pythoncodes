print(ord('അ')-3332)
print('if')
s=''
for i in range(98):
	s+=chr(i+3333)+' '+str(i+1)+'  '

print(s)
	
print()
print('Decode')
print()
sentance='ഞാൻ നിന്നെ സ്നേഹിക്കുന്നു'

s=''
for i in range(len(sentance)):
	if(sentance[i]==' '):
		s+='  '
	else:
	    s+=str(ord(sentance[i])-3332)+' '
	
print(s)