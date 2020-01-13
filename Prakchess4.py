
import random

chessboard=[[  5.2,   3.4 ,  3.5,   9.1 ,  10.1,    3.6 ,  3.7 ,  5.4],
 [  1.10  ,  1.10  , 1.10,    1.10,    1.10,    1.10,   1.10,    1.10 ],
 [  0.00  ,   0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00,     0.00  ],
 [  0.00  ,   0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00,     0.00  ],
 [  0.00  ,   0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00,     0.00  ],
 [  0.00  ,   0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00,     0.00  ],
 [  1.00,     1.00,    1.00,     1.00,     1.00,     1.00,     1.00,    1.00,  ],
 [  5.0,     3.0,   3.1 , 9.00  , 10.00,     3.2 , 3.3 ,  5.1],
            [  'A',     'B',  'C' , 'D'  ,' E',   ' F' ,'G' ,  'H']];
print('Standard chess notation white being bottom and black with 0.1 at top')
for i in range(0,9):
    print(chessboard[i])


#The computing engine should have the rules and then calculate from the other person's perspective and then do the best move with say 9 calculations

haha=1;
while haha:
    print('SS,PS,<3')
    c=random.sample(['A','B','C','D','E','F','G','H'],2);
    d=random.sample(range(1,8),2);

    move=c[0]+str(d[0])+c[1]+str(d[1])
    print(move)
    chessboard[8-int(move[3])][ord(move[2])-65]=chessboard[8-int(move[1])][ord(move[0])-65]
    chessboard[8-int(move[1])][ord(move[0])-65]=0;
    for i in range(0,9):
        print(chessboard[i])
    print('')
    for i in range(0,10000):
        for j in range(0,500):
            1
        
#Put example demo of how to play the game or even you can't play it
