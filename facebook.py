import random
import pyperclip
names=['kaumudi','vikram srinivas','Daniel brooks','Neil','Ketan Rathod','Srikanth Tenneti','Pinaki Abhilash','Shashanka Ala']
names2=['Janani Ravi','Punnai','Sunder','Mangesh','Ananth','Samhita']
        
names3=names+names2
nam=random.choice(names3)
print(nam)
pyperclip.copy(nam)
