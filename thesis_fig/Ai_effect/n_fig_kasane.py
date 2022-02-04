import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize



data0 = np.loadtxt('l_a2_kkb8e.dat')
data1 = np.loadtxt('l_a20_kkb8e.dat')

x = np.arange(1, 101, 1)
y0 = data0[:,1]
y1 = data1[:,1]

fig, axe = plt.subplots(1, 1)

width = 0.8
#axe.plot(x, y, 'o', c='black')

axe.bar(x, y0, width, color="blue", alpha=0.5, label=r"$a/l_1=2$")
axe.bar(x, y1, width, color="coral", alpha=0.5, label=r"$a/l_1=20$")
plt.xlabel(r"$l_i$", fontsize=18)
plt.ylabel("Number", fontsize=18)
plt.ylim(0, 500)
plt.xlim(0, 100)

axe.legend()
plt.show()
fig.savefig("y500_l2and20_k8.png")

