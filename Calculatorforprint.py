
x='25;
y=input();
product=int(x[1])*int(y[1])+10*(int(x[0])*int(y[1])+int(x[1])*int(y[0]))+int(x[0])*int(y[0])*100
add=int(x[1])+int(y[1])+10*(int(x[0])+int(y[0]))
sub=int(x[1])-int(y[1])+10*(int(x[0])-int(y[0]))
print('Product ', product)
print('Sum ',add)
print('Subtraction ',sub)
print('Input single digit number to divide first')
z=input()
ha=1;
j=0;
while ha:
    
    r=int(x[1])+10*int(x[0])-j*int(z[0]);
    if(r<int(z[0])):
        ha=0;
    j=j+1;
        
j=j-1;
ha=1;
h=0;
while ha:
    
    r2=r*10-h*int(z[0]);
    if(r2<int(z[0])):
        ha=0;
    h=h+1;
h=h-1;
print('division ',j,'.',h)
print('Input 3 digit number to find the square root')
sq=input();
ha=1;
a=0;
while ha:
    luv=int(sq[0])*100+int(sq[1])*10+int(sq[2])-100*a*a;
    a=a+1;
    if luv<0:
        ha=0;

a=a-2;
ha=1;
b=0;
while ha:
    luv2=int(sq[0])*100+int(sq[1])*10+int(sq[2])-100*a*a-(20*a+b)*b;
    b=b+1;
    if luv2<0:
        ha=0;
b=b-2;

ha=1;
c=0;
while ha:
    luv3=100*(int(sq[0])*100+int(sq[1])*10+int(sq[2])-100*a*a-(20*a+b)*b)-c*(200*a+20*b+c);
    c=c+1;
    if luv3<0:
        ha=0;
c=c-2;


print('root ',10*a+b,'.',c)

n=8
def hfactorial(n):
    s=1;
    for j in range(1,n+1):
        s=s*j
    return s

def hsin(x):
    return x-x*x*x/6+x*x*x*x*x/120-x*x*x*x*x*x*x/5040;

def hcos(x):
    return 1-x*x/2+1/24*x*x*x*x-x*x*x*x*x*x/720;

def htan(x):
    return x+x*x*x/3+2/15*x*x*x*x*x+17/315*x*x*x*x*x*x*x+62/2035*x*x*x*x*x*x*x*x*x;


def h2cos(x):
    s=0.0;
    for j in range(n):
        
        s=s+(-1)**j/hfactorial(2*j)*(x**(2*j))
    return s


def h2sin(x):
    s=0.0;
    for j in range(n):
        s=s+(-1)**j/hfactorial(2*j+1)*(x**(2*j+1))
    return s

def h2sinh(x):
    s=0.0;
    for j in range(n):
        s=s+1/hfactorial(2*j+1)*(x**(2*j+1))
    return s



def h2atanh(x):
    s=0.0;
    for j in range(1,n):
        s=s+1/(2*j-1)*(x**(2*j-1))
    return s

def h2atan(x):
    s=0.0;
    for j in range(1,n):
        s=s+(-1)**(j+1)/(2*j-1)*(x**(2*j-1))
    return s

def h2ln1px(x):
    s=0.0;
    for j in range(1,n):
        s=s+(-1)**(j+1)/j*(x**(j))
    return s
def h2erf(x):
    s=0.0;
    for j in range(1,n):
        s=s+2/np.sqrt(np.pi)*(-1)**j/(2*j+1)/hfactorial(j)*(x**(2*j+1))
    return s

def h2exp(x):
    s=0.0;
    for j in range(1,n):
        s=s+1/hfactorial(j)*(x**(j))
    return s

def h2acot(x):
    s=0.0;
    for j in range(1,n):
        s=s+(-1)**j/(2*j+1)*(x**(2*j+1))
    return np.pi/2-s

def h2cosh(x):
    s=0.0;
    for j in range(1,n):
        s=s+1/hfactorial(2*j)*(x**(2*j))
    return s


print(h2cos(3.14/2),h2sin(0.1),h2sinh(0.1))





        
    



        
    










        
    
