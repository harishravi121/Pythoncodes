import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,96,.5)
y=500*np.exp(-x/12)
weekly=(7*y-7*y%125)/7
plt.plot(x,y,x,weekly)
plt.xlabel('months')
plt.ylabel('Daily dosage with weekly average and then monthly average')
plt.show()

