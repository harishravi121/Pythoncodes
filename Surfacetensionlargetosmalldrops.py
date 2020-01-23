import numpy as np
R=1
N=100
r=R/N**0.33
delA=4*np.pi*r**2*N-4*np.pi*R**2
S=0.075 #N/m
delU=delA*S
print(delU,' J')
