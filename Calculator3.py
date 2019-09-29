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





        
    
