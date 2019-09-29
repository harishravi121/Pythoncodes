from numpy import genfromtxt
from copy import copy, deepcopy
c=genfromtxt('Jananiscube.csv',delimiter=',');
c2=genfromtxt('Jananiscube.csv',delimiter=',');
print(c)

# or 8+12 * 12 = 240 lines of code

print('12 moves x=0,1,2,3,4,5,6,7,8,9,10,11,12 F F- B B- U U- D D- L L- R R-')
def moves(x):
    c=deepcopy(c2) 
    if x==0:  # Front
        # edges
        c2[3][4]=c[4][3];
        c2[2][4]=c[4][2];
        
        c2[4][5]=c[3][4];
        c2[4][6]=c[2][4];

        c2[5][4]=c[4][5];
        c2[6][4]=c[4][6];

        c2[4][3]=c[5][4];
        c2[4][2]=c[6][4];

    if x==1:  # Front'
        # edges
        c2[4][3]=c[3][4];
        c2[4][2]=c[2][4];
        
        c2[3][4]=c[4][5];
        c2[2][4]=c[4][6];

        c2[4][5]=c[5][4];
        c2[4][6]=c[6][4];

        c2[5][4]=c[4][3];
        c2[6][4]=c[4][2];

    if x==2:  # Back
        # edges
        c2[11][4]=c[12][3];
        c2[2][4]=c[4][2];
        
        c2[12][5]=c[11][4];
        c2[4][6]=c[2][4];

        c2[13][4]=c[12][5];
        c2[6][4]=c[4][6];

        c2[12][3]=c[13][4];
        c2[4][2]=c[6][4];

    if x==3: #Back'
       1 
    if x==4:  # Up
        # edges
        c2[0][4]=c[1][3];
        c2[2][4]=c[4][2];
        
        c2[1][5]=c[0][4];
        c2[4][6]=c[2][4];

        c2[2][4]=c[1][5];
        c2[6][4]=c[4][6];

        c2[1][3]=c[2][4];
        c2[4][2]=c[6][4];

    if x==5: #Up'
        1
    if x==6:  # Down
        # edges
        c2[6][4]=c[7][3];
        c2[2][4]=c[4][2];
        
        c2[7][5]=c[6][4];
        c2[4][6]=c[2][4];
        c2[8][4]=c[7][5];
        c2[6][4]=c[4][6];

        c2[7][3]=c[8][4];
        c2[4][2]=c[6][4];

    if x==7: #Down'    
        1
    if x==8:  # Right
        # edges
        c2[3][7]=c[4][6];
        c2[2][4]=c[4][2];
        
        c2[4][8]=c[3][7];
        c2[4][6]=c[2][4];

        c2[5][7]=c[4][8];
        c2[6][4]=c[4][6];

        c2[4][6]=c[5][7];
        c2[4][2]=c[6][4];

    if x==9: #Right'
        1                
    if x==10:  # Left
        # edges
        c2[3][1]=c[4][0];
        c2[2][4]=c[4][2];
        
        c2[4][2]=c[3][1];
        c2[4][6]=c[2][4];

        c2[5][1]=c[4][2];
        c2[6][4]=c[4][6];

        c2[4][0]=c[5][1];
        c2[4][2]=c[6][4];

    if x==11: #Left'         
        1

    print(c2)
 

while 1:
    move=input()
     
    moves(int(move[0]))



import numpy as np
solution=np.zeros(100)


