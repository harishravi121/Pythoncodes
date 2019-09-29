from numpy import genfromtxt
chessboard=genfromtxt('prakchess.csv',delimiter=',');
print('Row starts from 0 and column from 0 at topleft for moves where you type four numbers for two from start and two to end position, white being bottom and black with 0.1 at top')
print(chessboard)


while 1:
    move=input() #1.1 would be shite and the input should be rowcolumn move rowcolum
    temp=chessboard[int(move[2])][int(move[3])];
    chessboard[int(move[2])][int(move[3])]=chessboard[int(move[0])][int(move[1])]
    chessboard[int(move[0])][int(move[1])]=temp;
    print(chessboard)

#The computing engine should have the rules and then calculate from the other person's perspective and then do the best move with say 9 calculations
