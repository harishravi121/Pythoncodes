def translate(seq): 
       
    table = { 
        'E':'€','P':'£','Y':'¥','S':'$','N':'₦','R':'₹','B':'₿','M':'ɱ','W':'₩','T':'৳',
        'G':'₾','A':'A','C':'¢','D':'D','F':'F','H':'H','I':'I','J':'J','K':'K','N':'N','O':'O',
        'Q':'Q','U':'U','V':'V','X':'X','Z':'Z',' ':' ','L':'L','.':'.',',':','
    } 
    physics ="" 
   
    for i in range(0, len(seq)): 
        
        physics+= table[seq[i]] 
    return physics 


curr='INTERNATIONAL MONETARY FUND IS GREATEST ' #EDIT WHAT STATEMENT YOU WANT CURRENCIFIED
p2=translate(curr)
print(p2)

'''

>>> 
================== RESTART: C:\Businesspython\Cashtext.py.txt ==================
₿I৳¢OIN I$ ₾₹€A৳
>>> 
================== RESTART: C:\Businesspython\Cashtext.py.txt ==================
₹U₿IK$ ¢U₿IN₾ I$ ₾₹€A৳
>>> 
================== RESTART: C:\Businesspython\Cashtext.py.txt ==================
NI₾H৳ DI$¢U$$ION I$ ₾₹€A৳
>>> 
================== RESTART: C:\Businesspython\Cashtext.py.txt ==================
৳A¥LO₹ $₩IF৳ I$ ₾₹€A৳
>>> 
================== RESTART: C:\Businesspython\Cashtext.py.txt ==================
¢NN I$ ₾₹€A৳
>>> 
================== RESTART: C:\Businesspython\Cashtext.py.txt ==================
¢NN I$ ₾₹€A৳ AɱAZIN₾ $৳UNNIN₾


=================== RESTART: C:/Businesspython/Cashtext33.py ===================
$৳A৳€ ₿ANK OF INDIA I$ ৳H€ ₾₹€A৳€$৳
>>> 
=================== RESTART: C:/Businesspython/Cashtext33.py ===================
IN৳€₹NA৳IONAL ɱON€৳A₹¥ FUND I$ ₾₹€A৳€$৳ 
>>> 
=================== RESTART: C:/Businesspython/Cashtext33.py ===================
IN৳€₹NA৳IONAL ɱON€৳A₹¥ FUND I$ ₾₹€A৳€$৳ 

Code for sale 1000 $

Dr. Harish Ravi
Contact for giving.

IF microsoft wants it it can take use it and pay later if they sell it better its good too. I will also use it. And anyone buying it can pay and use it.
All codes are like this.

'''
