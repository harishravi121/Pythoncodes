print(ord('ಅ')-3204)
print('if')
for i in range(98):
	print(i+1, chr(i+3205))
	
print()
print('Decode')
print()
sentance='ಕರ್ನಾಟಕ ಒಂದು ಮೋಜಿನ ರಾಜ್ಯ'
for i in range(len(sentance)):
	if(sentance[i]==' '):
		print()
	else:
	    print(ord(sentance[i])-3204)
	
	