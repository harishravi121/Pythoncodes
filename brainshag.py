import matplotlib.pyplot as plt
import numpy as np
speedofbrain=120/0.1;
speedtolocomotion=40/0.4;
threshold1=0.7;
deltathreshold=0.1;
bl=np.arange(1,21,1);
deltaS=200;
bloodlevel=bl/50;
threshold=threshold1+deltathreshold*bloodlevel;
speed=speedofbrain-deltaS*bloodlevel;
Ngenerations=4096;

#imagine a binary tree firing voltagee 0.7 plus noise, next neuron firing probability is relativethreshold
#n operations

prob=np.power((threshold1/threshold),12)
intelligence=prob*speed
prob2=1-np.power((threshold/threshold1),12)
intelligence=prob*speed

plt.plot(bl,intelligence)
plt.ylabel('Intelligence and stamina')
plt.xlabel('Number of shags per week')
plt.show()

#Effect of sudden removal.
