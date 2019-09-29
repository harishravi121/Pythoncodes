import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

A=0.004;
P=1000;
eff=0.25;
h=6.626e-34;
freq=1e15;
nphotons=P*A/h/freq;
Is=nphotons*1.6e-19*eff;
print(Is)
V1=4.7;
Vt=0.025;
n=10;
Vs=4;
I0=1e-12;
I02=1e-12;
I=I02*(np.exp((V1-Vs)/Vt)-1);
print(I)
I=Is-I0*(np.exp(V1/n/Vt)-1);
print(I)
def curr(x):
    y=I02*(np.exp((x-Vs)/Vt)-1)-Is+I0*(np.exp(x/n/Vt)-1);
    return y

soln=fsolve(curr,4.7)
print(soln)



P=np.linspace(0,1000,100);
I2=np.linspace(0,1000,100);

nphotons=P*A/h/freq;
Is=nphotons*1.6e-19*eff;

for j in range(len(P)):
    nphotons=P[j]*A/h/freq;
    Is=nphotons*1.6e-19*eff;
    def curr(x):
        y=I02*(np.exp((x-Vs)/Vt)-1)-Is+I0*(np.exp(x/n/Vt)-1);
        return y
    soln=fsolve(curr,4.7)
    I2[j]=I02*(np.exp((soln-Vs)/Vt)-1);

plt.plot(P,I2)
plt.xlabel('Power (W/msq)')
plt.ylabel('current (A)')
plt.show()

P=1000;
nphotons=P*A/h/freq;
Is=nphotons*1.6e-19*eff;
Vs2=np.linspace(0,5,100);
I2=np.linspace(0,5,100);

for j in range(len(Vs2)):

    def curr(x):
        y=I02*(np.exp((x-Vs2[j])/Vt)-1)-Is+I0*(np.exp(x/n/Vt)-1);
        return y
    soln=fsolve(curr,Vs2[j]+0.7)
    I2[j]=I02*(np.exp((soln-Vs2[j])/Vt)-1);

plt.plot(Vs2,I2)
plt.xlabel('Voltage2 (V)')
plt.ylabel('current (A)')
plt.show()




