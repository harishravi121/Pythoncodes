import random


a=['Harish','Nandini','Sunay','Yogesh','Ravi','Adarsh'] # array
print('Before sorting')
print(a)
for j in range(len(a)-1,0,-1):
 for i in range(j):
    if(ord(a[i][0])<ord(a[i+1][0])):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
print('Descending order sort')
print(a)

#Before sorting
#['Harish', 'Nandini', 'Sunay', 'Yogesh', 'Ravi', 'Adarsh']
#Descending order sort
#['Yogesh', 'Sunay', 'Ravi', 'Nandini', 'Harish', 'Adarsh']
