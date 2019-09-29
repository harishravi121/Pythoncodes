import numpy as np
#Bdip=mu0m/4/pi/r^3*(3cos^2(theta)+1);
polarrad=6363.806e3;
equatorialrad=6397.3e3;
magaxislat=86; # most current
magaxislong=-72.6;
Bmin=25e-6;
Bmax=65e-6;
lat=8;
long=77;
theta=90-lat;
r=polarrad*(1+(equatorialrad-polarrad)/polarrad*np.cos(theta));

mu0=4*np.pi*1e-7;

m1=Bmax/1e-7*np.power(polarrad,3)/2

m=m1*0.9;
Bmin2=1e-7/np.power(equatorialrad,3)*m;
Bmax3=1e-7/np.power(polarrad,3)*m*2;
print(Bmin2,'   ',Bmax3)

x=sin(theta)*cos(long);
y=sin(theta)*sin(long);
z=cos(theta);

#ref classical mechanics page 153

t2=acos(x*sin(90-magaxislat)*sin(magaxislong)-y*sin(90-magaxislat)*cos(magaxislong)+z*cos(90-magaxislat));

        
