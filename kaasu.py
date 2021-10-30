#Cashier Problem

import random

bill=random.randint(5,1000)
print(bill)
bill2=bill
cash=[500,100,50,10,5,2,1]
print(cash)
n=[0]*len(cash)
for i in range(len(n)):
    n[i]=random.randint(1,10)
Breakup=[0]*len(cash)

for i in range(len(Breakup)):
    Breakup[i]=(bill-bill%cash[i])/cash[i]
    bill=bill-Breakup[i]*cash[i]

print(Breakup)
