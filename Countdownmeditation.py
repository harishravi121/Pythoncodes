#Meditation timer

import time
import random
import winsound
t=30 #Meditaion set time in seconds
for i in range(10):
    a=t*(1+random.random()) #Random time upto double the t
    print(a)
    time.sleep(a) #Random inspection time
    print('Done')
    winsound.Beep(int(500+500*random.random()),int(500+500*random.random())) #Beeps with varying frequency and time
