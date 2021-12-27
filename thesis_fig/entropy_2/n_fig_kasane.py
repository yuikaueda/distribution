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

axe.bar(x, y0, width, color="green", alpha=0.4, label=r"$l_0=20$")
axe.bar(x, y1, width, color="fuchsia", alpha=0.3, label=r"$l_0=80$")
plt.xlabel(r"$l_i$", fontsize=18)
plt.ylabel("Number", fontsize=18)
plt.ylim(0, 15)
plt.xlim(0, 100)

axe.legend()
plt.show()
fig.savefig("2data_y15_f0_1e-4_l020and80.png")

