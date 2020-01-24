import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=1-np.exp(-x)
plt.plot(x,y)
plt.show()
