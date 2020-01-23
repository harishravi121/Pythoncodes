import numpy as np
Sig=5.67e-8 #Wm-2K-4
R=696340e3
A=4*np.pi*R**2
T=6000
Power=A*Sig*T**4/1e25
print(Power,'e25 W')
