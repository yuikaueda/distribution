import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize


data = np.loadtxt('fig7_kkb0.1_l020.dat')

x = np.arange(1, 101, 1)
y = data[:,1]

fig, axe = plt.subplots(1, 1)

width = 0.8
#axe.plot(x, y, 'o', c='black')

axe.bar(x, y, width, color="green")
plt.xlabel(r"$l_i$", fontsize=18)
plt.ylabel("Number", fontsize=18)
plt.ylim(0, 50)
plt.xlim(0, 100)

plt.show()
fig.savefig("fig7_kkb0.1_l020.png")

