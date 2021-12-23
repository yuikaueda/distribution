import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize



data0 = np.loadtxt('kkb1e-1_f0_1e-12_l080.dat')
data1 = np.loadtxt('kkb1e-1_f0_1e-0_l080.dat')

x = np.arange(1, 101, 1)
y0 = data0[:,1]
y1 = data1[:,1]

fig, axe = plt.subplots(1, 1)

width = 0.8
#axe.plot(x, y, 'o', c='black')

axe.bar(x, y0, width, color="deepskyblue", alpha=0.4, label=r"$f_0=1e^{-12}$")
axe.bar(x, y1, width, color="orangered", alpha=0.5, label=r"$f_0=1e^0$")
plt.xlabel(r"$l_i$", fontsize=18)
plt.ylabel("Number", fontsize=18)
plt.ylim(0, 30)
plt.xlim(0, 100)

axe.legend()
plt.show()
fig.savefig("2data_y30kkb1e-1_f0_1e-12ande-0_l080.png")

