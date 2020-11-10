import main
import CV2_func
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21,None, np.int32)
y = np.zeros(21, np.double)
y[0] = main.errorPercent

plt.figure()
plt.xticks(x)
plt.ylim(0,100)
plt.plot(x,y)
plt.show()