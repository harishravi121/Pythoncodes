import random
cho=['Read 2 books ','Do coursera 5 mins','Do NPTEL 5 mins',' Solve rubiks cube 1 side','See Amazon prime 10 mins','See youtube','See insta','Play a 1 min game of chess or 4 in a row','Apply to one university or company','Rewrite a bit of code','Rewrite thesis','Read sai inspires or other religious materials','Do tri dumbell workout']

while 1:
    a=input()
    print('Congrats')
    print(random.choice(cho)+' or '+random.choice(cho))
