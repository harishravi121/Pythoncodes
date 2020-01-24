import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,1,100)
y=np.sqrt(1-x**2)
plt.plot(x,y,x,-y)
plt.show()
