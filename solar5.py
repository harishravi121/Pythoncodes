import numpy as np
import scipy
import matplotlib.pyplot as plt
#solar power 1000TWh
t=60
x=np.arange(0,t,0.1)
y=(t-x)*1000
plt.ylabel('TWh')
plt.xlabel('Years')
plt.plot(x,y)
plt.show()

costperW=42

costoptimistic=6 
