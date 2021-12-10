import random

'''Three masses in equilateral triangle of length 1 where is com'''
m1=random.randint(45,55)
m2=random.randint(90,110)
m3=random.randint(145,160)

c1=[0,0]
c2=[1,0]
c3=[.5,3**.5/2]

COMx=m1*c1[0]+m2*c2[0]+m3*c3[0]
COMy=m1*c1[1]+m2*c2[1]+m3*c3[1]


print(round(COMx,2),round(COMy,2))

'''
Outputs

178.5 135.97

180.0 136.83

'''
