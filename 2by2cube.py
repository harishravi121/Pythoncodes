cube2=[[0 for j in range(8)] for i in range(6)]
cube=[[0 for j in range(8)] for i in range(6)]
def cubecopy():
    for i in range(6):
        for j in range(8):
            cube2[i][j]=cube[i][j];

for i in range(6):
    print(cube[i])
print()

for i in range(2):
    for j in range(2):
        cube[i][j+2]=1
        cube[i+2][j]=2
        cube[i+2][j+2]=3
        cube[i+2][j+4]=4
        cube[i+2][j+6]=5
        cube[i+4][j+2]=6

cubecopy();


for i in range(6):
    print(cube2[i])    
