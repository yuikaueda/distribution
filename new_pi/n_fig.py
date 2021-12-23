import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize


data = np.loadtxt('data1_kb2.dat')

#x = data[:,0]
x = np.arange(1, 101, 1)
y = data[:,1]

#fig, ax = plt.subplots(1, 1)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#axe.plot(x, y, 'o', c='black')
width =0.8

plt.bar(x, y, width, color="darkblue")
plt.xlabel(r"$l_i$", fontsize=18)
plt.ylabel("Number", fontsize=18)
plt.ylim(0, 500)
plt.xlim(0, 100)

plt.show()
fig.savefig("actin_ni_10-2.png")

