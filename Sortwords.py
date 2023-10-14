
#This code of word sort improves our excitement for speaking and thinking language
#code by Dr. Harish to sort words like in column in Excel or Folders in OS.
import random


a=['Harish','Nandini','Sunay','Yogesh','Ravi','Adarsh'] # array of words to sort
print('Before sorting')
print(a)
for j in range(len(a)-1,0,-1): #2 for loops of sort algorithm
 for i in range(j):
    if(ord(a[i][0])<ord(a[i+1][0])):  #Look at the first alphabet and see larger to swap left   
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp  #swap if condition met
print('Descending order sort')
print(a)

#Code output

#Before sorting
#['Harish', 'Nandini', 'Sunay', 'Yogesh', 'Ravi', 'Adarsh']
#Descending order sort
#['Yogesh', 'Sunay', 'Ravi', 'Nandini', 'Harish', 'Adarsh']
