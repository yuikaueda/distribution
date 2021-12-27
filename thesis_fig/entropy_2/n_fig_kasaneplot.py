import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize



data0 = np.loadtxt('entro__f0_1e-4_l020.dat')
data1 = np.loadtxt('entro__f0_1e-4_l080.dat')

x = np.arange(1, 101, 1)
y0 = data0[:,1]
y1 = data1[:,1]

fig, axe = plt.subplots(1, 1)

width = 0.8
#axe.plot(x, y, 'o', c='black')

axe.scatter(x, y0, width, color="blue", alpha=0.9, label=r"$l_0=20$")
axe.scatter(x, y1, width, color="red", alpha=0.9, label=r"$l_0=80$")
axe.set_xlabel(r"$l_i$", fontsize=18)
axe.set_ylabel("Number", fontsize=18)
axe.set_ylim(9.8, 10.2)
axe.set_xlim(0, 100)

axe.legend()
plt.show()
fig.savefig("plot_2data_y15_f0_1e-4_l020and80.png")

