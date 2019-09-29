import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,96,.5)
y=10.0*np.exp(-x/12)*7
weekly=(y-y%1.0)/48
plt.plot(x,y/48.0,x,weekly)
plt.xlabel('months')
plt.ylabel('Daily dosage with 48 day or 7 week average')
plt.show()

