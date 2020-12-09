import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize


data = np.loadtxt('data1_kb2.dat')

#x = data[:,0]
x = np.arange(1, 101)
y = data[:,1]

#fig, ax = plt.subplots(1, 1)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#axe.plot(x, y, 'o', c='black')
width =0.7

plt.bar(x, y, width)
plt.xlabel("l", fontsize=15)
plt.ylabel("n", fontsize=15)
plt.ylim(0, 100)
#plt.xlim(0, 0.001)

fig.savefig("ni_10-2.png")

