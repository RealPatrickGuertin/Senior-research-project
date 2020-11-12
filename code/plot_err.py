import main
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11,None, np.int32)
y = np.zeros(10, np.double)

it = 0
for i in main.errorPercent:
    y[it] = i
    it += 1

plt.figure()
plt.xticks(x)
plt.xlabel("Sets")
plt.ylim(0,100)
plt.ylabel("Percent Error")
plt.bar(x,y)
plt.show()
