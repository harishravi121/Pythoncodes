print('Input two double digit numbers by pressing enter')
x=input();
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


print('root ',10*a+b)

def hsin(x):
    return x










        
    
