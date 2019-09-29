from numpy import genfromtxt
import numpy as np
from copy import copy, deepcopy
cube=genfromtxt('Jananiscube.csv',delimiter=',');
cube2=genfromtxt('Jananiscube.csv',delimiter=',');
print(cube2)

# or 8+12 * 12 = 240 lines of code

print('12 moves F f B b U u D d R r L l')
def changeedge(j,i) :
    cube2[i[0][0]][i[0][1]]=cube[j[0][0]][j[0][1]];
    cube2[i[1][0]][i[1][1]]=cube[j[1][0]][j[1][1]];

def changecorner(j,i) :
    cube2[i[0][0]][i[0][1]]=cube[j[0][0]][j[0][1]];
    cube2[i[1][0]][i[1][1]]=cube[j[1][0]][j[1][1]];
    cube2[i[2][0]][i[2][1]]=cube[j[2][0]][j[2][1]];

    
def rotateclockwise(a,b,c,d,e,f,g,h) :
    changecorner(g,a);
    changeedge(h,b);
    changecorner(a,c);
    changeedge(b,d);
    changecorner(c,e);
    changeedge(d,f);
    changecorner(e,g);
    changeedge(f,h);

def rotatecounterclockwise(a,b,c,d,e,f,g,h) :
    changecorner(a,g);
    changeedge(b,h);
    changecorner(c,a);
    changeedge(d,b);
    changecorner(e,c);
    changeedge(f,d);
    changecorner(g,e);
    changeedge(h,f);

def cubecopy(n):
    for i in range(n):
        for j in range(n):
            cube[i][j]=cube2[i][j];
    
def moves2(x):
    
    if x=='F':  # Front
        rotateclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);
        

    if x=='f':  # Front'
        rotatecounterclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);



    if x=='B':  # Back
        rotateclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);


    if x=='b': #Back'
        rotatecounterclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);

    if x=='U':  # Up
        rotateclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);


    if x=='u': #Up'
        rotatecounterclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);

    if x=='D':  # Down
        rotateclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);


    if x=='d': #Down'    
        rotatecounterclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);

    if x=='R':  # Right
        rotateclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);


    if x=='r': #Right'
        rotatecounterclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);

    if x=='L':  # Left
        rotateclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);


    if x=='l': #Left'         
        rotatecounterclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);
    cubecopy(9)
    print(cube)
 

while 1:
    move=input()
     
    moves2(move[0])



import numpy as np
solution=np.zeros(100)


