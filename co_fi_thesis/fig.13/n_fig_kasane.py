import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize



data0 = np.loadtxt('fig13_f01e0_nu0.2.dat')
data1 = np.loadtxt('fig13_f01e0_nu0.8.dat')

x = np.arange(1, 101, 1)
y0 = data0[:,1]
y1 = data1[:,1]

fig, axe = plt.subplots(1, 1)

width = 0.8
#axe.plot(x, y, 'o', c='black')

axe.bar(x, y0, width, color="cyan", alpha=0.4, label=r"$\lambda=0.2$")
axe.bar(x, y1, width, color="pink", alpha=0.4, label=r"$\lambda=0.8$")
axe.set_xlabel(r"$l_i$", fontsize=18)
axe.set_ylabel("Number", fontsize=18)
axe.set_ylim(0, 30)
axe.set_xlim(0, 100)

axe.legend()
plt.show()
fig.savefig("fig13_f01e0.png")

