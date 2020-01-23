import numpy as np

def densityair(T):
    M=28.97e-3
    R=8.314
    P=1.01e5
    rho=P*M/R/T
    print(rho)
    
densityair(300)


def Range1(u,theta):

    thetarad=theta*np.pi/180
    g=9.81
    R=u**2*np.sin(2*thetarad)/g
    Rkm=R/1e3
    print(R,Rkm)
    H=u**2*(np.sin(thetarad))*2/g/2
    Hkm=H/1000
    print(H,Hkm)

Range1(1.25e3,45)

def surfaceenergy(N,R): #Breaking 1 drop to N
    r=R/N**0.33
    delA=4*np.pi*r**2*N-4*np.pi*R**2
    S=0.075 #N/m
    delU=delA*S
    print(delU)

surfaceenergy(100,1)
