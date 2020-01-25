import random

s=['S','R','G','M','P','D','N','S.']

c=['C','D','E','F','G','A','B']

app=['#','#m','M','m']



for i in range(1,20):

     print(random.sample(s,4))

     chord=random.sample(c,1)+random.sample(app,1)+random.sample(c,1)+random.sample(app,1)

     print(chord)

     print()
