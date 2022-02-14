import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize


data = np.loadtxt('fig6_kkb10.dat')

x = data[:,2]
y = data[:,3]

fig, axe = plt.subplots(1, 1)

width = 0.8
#axe.plot(x, y, 'o', c='black')

axe.plot(x, y, width, color="darkblue")
plt.xlabel(r"$ln(l_i)$", fontsize=18)
plt.ylabel(r"$ln(n_i)$", fontsize=18)
plt.ylim(0, 10)
plt.xlim(0, 5)

plt.show()
fig.savefig("fig10_kkb10.png")

