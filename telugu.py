print(ord('అ')-3076)
print('if')
for i in range(98):
	print(i+1, chr(i+3077))
	
print()
print('Decode')
print()
sentance='ఆంధ్ర గొప్ప రాష్ట్రం'
for i in range(len(sentance)):
	if(sentance[i]==' '):
		print()
	else:
	    print(ord(sentance[i])-3076)
	
	