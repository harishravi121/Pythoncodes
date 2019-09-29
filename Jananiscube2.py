from numpy import genfromtxt
from copy import copy, deepcopy
cube=genfromtxt('Jananiscube.csv',delimiter=',');
cube2=genfromtxt('Jananiscube.csv',delimiter=',');
print(c)

# or 8+12 * 12 = 240 lines of code

print('12 moves x=0,1,2,3,4,5,6,7,8,9,10,11,12 F F- B B- U U- D D- L L- R R-')
def changeedge(jx,jy,j1x,j1y,ix,iy,i1x,i1y) :
    cube2[ix][iy]=cube[jx][jy];
    cube2[i1x][i1y]=cube[j1x][j1y];

def changecorner(jx,jy,j1x,j1y,j2x,j2y,ix,iy,i1x,i1y,i2x,i2y) :
    cube2[ix][iy]=cube[jx][jy];
    cube2[i1x][i1y]=cube[j1x][j1y];
    cube2[i2x][i2y]=cube[j2x][j2y];

    
def rotateclockwise(ax,ay,a1x,a1y,a2x,a2y,bx,by,b1x,b1y,cx,cy,c1x,c1y,c2x,c2y,dx,dy,d1x,d1y,ex,ey,e1x,e1y,e2x,e2y,fx,,fy,f1x,f1y,gx,gy,g1x,g1y,g2x,g2y,hx,hy,h1x,h1y) :
    changecorner(gx,gy,g1x,g1y,g2x,g2y,ax,ay,a1x,a1y,a2x,a2y);
    changeedge(hx,hy,h1x,h1y,bx,by,b1x,b1y,);
    chagecorner(ax,ay,a1x,a1y,a2x,a2y,cx,cy,c1x,c1y,c2x,c2y);
    changeedge(bx,by,b1x,b1y,dx,dy,d1x,d1y);
    chagnecorner(cx,cy,c1x,c1y,c2x,c2y,

    
def moves(x):
    cube=deepcopy(cube2) 
    if x==0:  # Front


    if x==1:  # Front'



    if x==2:  # Back


    if x==3: #Back'

    if x==4:  # Up
        # edges


    if x==5: #Up'
        1
    if x==6:  # Down
        # edges


    if x==7: #Down'    
        1
    if x==8:  # Right
        # edges


    if x==9: #Right'
        1                
    if x==10:  # Left
        # edges


    if x==11: #Left'         
        1

    print(c2)
 

while 1:
    move=input()
     
    moves(int(move[0]))



import numpy as np
solution=np.zeros(100)


