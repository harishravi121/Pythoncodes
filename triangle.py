import random
import numpy as np

a=random.randint(1,10)
b=random.randint(2,12)
angl=random.random()*3.14

c=(a**2+b**2-2*a*b*np.cos(angl))**.5
print('A triangle is ', a,b,round(c,3))
