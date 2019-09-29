from sympy import *
x,g,q=symbols('x g q')
g=400*(0.86-3.42*x+6.7*x*x-6.34*x*x*x+2.28*x*x*x*x);
rho=1000;
C=4200;
T=g/rho/C
