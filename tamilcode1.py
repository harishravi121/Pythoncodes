print(ord('அ')-2948)
print('if')
for i in range(98):
	print(i+1, chr(i+2949))
	
print()
print('Decode')
print()
sentance='எனக்கு உணவு மிகவும் பிடிக்கும்'
for i in range(len(sentance)):
	if(sentance[i]==' '):
		print()
	else:
	    print(ord(sentance[i])-2948)
	
	