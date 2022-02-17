import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize



data0 = np.loadtxt('fig16_kkb0.1_f01e-12.dat')
data1 = np.loadtxt('fig16_kkb0.1_f01e+1.dat')

x = np.arange(1, 101, 1)
y0 = data0[:,1]
y1 = data1[:,1]

fig, axe = plt.subplots(1, 1)

width = 0.8
#axe.plot(x, y, 'o', c='black')

axe.bar(x, y0, width, color="deepskyblue", alpha=0.4, label=r"$f_0=1e^{-12}$")
axe.bar(x, y1, width, color="orangered", alpha=0.5, label=r"$f_0=1e^1$")
plt.xlabel(r"$l_i$", fontsize=18)
plt.ylabel("Number", fontsize=18)
plt.ylim(0, 200)
plt.xlim(0, 100)

axe.legend()
plt.show()
fig.savefig("kkb0.1_fe-12ande1.png")

