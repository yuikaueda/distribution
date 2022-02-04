import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('la2.dat')
data2 = np.loadtxt('la5.dat')
data3 = np.loadtxt('la10.dat')
data4 = np.loadtxt('la20.dat')

l1 = data1[:,0]
a1 = data1[:,1]

a2 = data2[:,1]

a3 = data3[:,1]

a4 = data4[:,1]

fig, ax = plt.subplots(1, 1)
ax.plot(l1, a1, 'o-', c='coral', label = r"$a/l_1=2$", markersize=3)
ax.plot(l1, a2, 's-', c='limegreen', label = r"$a/l_1=5$", markersize=3)
ax.plot(l1, a3, 'v-', c='royalblue', label = r"$a/l_1=10$", markersize=3)
ax.plot(l1, a4, 'p-', c='orchid', label = r"$a/l_1=20$", markersize=3)

plt.xlabel(r"$l_i$", fontsize=18)
plt.ylabel(r"$A_i$", fontsize=18)

ax.legend()
plt.show()
fig.savefig("a_2t5t10t20_Ai.png")
