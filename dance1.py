import random
import time
import winsound


a=['up','right','down','left','center']
b=['up','center','down']
while 1:
    print('Leg'+' '+random.choice(a)+' '+random.choice(a))
    time.sleep(3)
    winsound.Beep(1000,200)
    print('Hand'+' '+random.choice(b)+' '+random.choice(b))
    print()
    time.sleep(3)
    winsound.Beep(1000,200)
