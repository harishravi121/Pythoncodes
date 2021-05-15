import random

from PyDictionary import PyDictionary
dictionary=PyDictionary()
  
# Open the file in read mode
with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
    a=random.choice(words)
    print(a)
    print (dictionary.meaning(a))
