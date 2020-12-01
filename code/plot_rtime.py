import main
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(1, 5,None, np.int32)
y = np.zeros(4, np.double)

it = 0
for i in main.runtimes:
    y[it] = i
    it += 1

plt.figure()
plt.xticks(x)
plt.xlabel("Sets")
plt.ylim(0,math.ceil(max(y)))
plt.ylabel("Adverage Runtime (Milliseconds)")
plt.bar(x,y)
plt.show()
