import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize


data = np.loadtxt('ni08_10-3.dat')

x = data[:,0]
y = data[:,1]

fig, axe = plt.subplots(1, 1)

#axe.plot(x, y, 'o', c='black')

axe.bar(x, y)
plt.xlabel("l", fontsize=15)
plt.ylabel("n", fontsize=15)
plt.ylim(0, 30)

fig.savefig("ni2_10-3.png")

