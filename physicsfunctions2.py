import numpy as np

def densityair(T):
    M=28.97e-3
    R=8.314
    P=1.01e5
    rho=P*M/R/T
    print(rho, ' kg/m**3')
    
densityair(300)


def Range1(u,theta):

    thetarad=theta*np.pi/180
    g=9.81
    R=u**2*np.sin(2*thetarad)/g
    Rkm=R/1e3
    print(R, ' m',Rkm,'km')
    H=u**2*(np.sin(thetarad))*2/g/2
    Hkm=H/1000
    print(H,'m',Hkm,'km')

Range1(1.25e3,45)

def surfaceenergy(N,R): #Breaking 1 drop to N
    r=R/N**0.33
    delA=4*np.pi*r**2*N-4*np.pi*R**2
    S=0.075 #N/m
    delU=delA*S
    print(delU,' J')

surfaceenergy(100,1)

def sun(T):
    Sig=5.67e-8 #Wm-2K-4
    R=696340e3
    A=4*np.pi*R**2
    T=6000
    Power=A*Sig*T**4/1e25
    print(Power,'e25 W')

sun(6000)
    
