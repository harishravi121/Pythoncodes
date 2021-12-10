import random
print('Relativistic length contraction. Velocity in m/s initial length and contracted length are given. Things contract on Moving')
for i in range(5):
    velocity=random.randint(1,100)*1e6 #in m/s
    c=3e8

    lengthinit=random.random()*100

    lengthcontr=lengthinit*(1-velocity**2/c**2)**.5

    print('v lo l ',velocity, round(lengthinit,2),round(lengthcontr,2))

'''
Relativistic length contraction. Velocity in m/s initial length and contracted length are given
v lo l  91000000.0 41.53 39.57
v lo l  86000000.0 68.97 66.08
v lo l  8000000.0 79.1 79.07
v lo l  5000000.0 30.89 30.89
v lo l  79000000.0 51.2 49.39

-Dr. Harish Extremeadventureinc

'''
