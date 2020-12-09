import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize


data = np.loadtxt('ni_10-2.dat')

x = np.arange(1, 11, 0.1)
y = data[:,1]

fig, axe = plt.subplots(1, 1)

width = 0.08
#axe.plot(x, y, 'o', c='black')

axe.bar(x, y, width)
plt.xlabel("l", fontsize=15)
plt.ylabel("n", fontsize=15)
plt.ylim(0, 500)
plt.xlim(0, 11)

fig.savefig("ni_2_10-2.png")

