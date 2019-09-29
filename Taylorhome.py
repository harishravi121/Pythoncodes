d=100;
import numpy as np
delta=-23.45*np.cos(360/365*(d+10))
print(delta)
tfromsunrise=6
alpha=np.pi/2-np.pi*tfromsunrise/12
height=5.5*0.3
shadow=5*0.3
theta=np.arctan(height/shadow)
betaindegrees=180-(-np.arcsin(np.sin(alpha/2)-np.sin((np.pi/2-theta)/2))+delta)*180/np.pi
Tfromhomehrs=6
phiindegrees=(Tfromhomehrs)/24*360
print(betaindegrees)
print(phiindegrees)
