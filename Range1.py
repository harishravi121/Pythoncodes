import numpy as np
u=1.25e3
theta=45
thetarad=theta*np.pi/180
g=9.81
R=u**2*np.sin(2*thetarad)/g
Rkm=R/1e3
print(R, ' m',Rkm,'km')
H=u**2*(np.sin(thetarad))*2/g/2
Hkm=H/1000
print(H,'m',Hkm,'km')
