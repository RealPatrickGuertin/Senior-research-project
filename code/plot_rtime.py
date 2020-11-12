import main
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(1, 6,None, np.int32)
y = np.zeros(5, np.double)

it = 0
for i in main.runtimes:
    y[it] = i
    it += 1

plt.figure()
plt.xticks(x)
plt.xlabel("Sets")
plt.ylim(0,math.ceil(max(y)))
plt.ylabel("Runtime (Seconds)")
plt.bar(x,y)
plt.show()
