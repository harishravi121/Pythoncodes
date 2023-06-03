print(ord('a')-96)
print('if')
for i in range(26):
	print(i+1, chr(i+97))
	
print()
print('Decode')
print()
sentance='swami is my guru'
for i in range(len(sentance)):
	if(sentance[i]==' '):
		print()
	else:
	    print(ord(sentance[i])-96)
	
	