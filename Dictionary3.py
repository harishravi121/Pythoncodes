import random

from PyDictionary import PyDictionary
dictionary=PyDictionary()
with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
file.close()
for i in range(3):
  
    # Open the file in read mode

      
    # print random string
    a=random.choice(words)
    print(a)
    print (dictionary.meaning(a))
    print()
    print ('Synonyms ' , dictionary.synonym(a))
    print()
    print ('Antonyms ', dictionary.antonym(a))
    print()
    print()
