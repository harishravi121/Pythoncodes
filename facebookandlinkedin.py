import random
import pyperclip
names=['kaumudi','vikram srinivas','Daniel brooks','Neil','Ketan Rathod','Srikanth Tenneti','Pinaki Abhilash','Shashanka Ala']
names2=['Janani Ravi','Punnai','Sunder','Mangesh','Ananth','Samhita','Sriman Chinnadurai','Sritama Bose','Navaneetha','Manmohan Kandukuri','Shriharsh Tendulkar']
        
names3=names+names2
nam=random.choice(names3)
print(nam)
pyperclip.copy(nam)
