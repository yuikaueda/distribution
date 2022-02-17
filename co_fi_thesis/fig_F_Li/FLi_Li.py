import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('figF_f01e-12_l020.dat')
#data2 = np.loadtxt('Al_la5.dat')
#data3 = np.loadtxt('Al_la10.dat')
#data4 = np.loadtxt('Al_la20.dat')

l1 = data1[:,0]
a1 = data1[:,1]

#a2 = data2[:,1]

#a3 = data3[:,1]

#a4 = data4[:,1]

fig, ax = plt.subplots(1, 1)
fig.subplots_adjust(left=0.17)
ax.plot(l1, a1, 'o-', c='black', markersize=3)
#ax.plot(l1, a2, 's-', c='limegreen', label = r"$a/l_1=5$", markersize=3)
#ax.plot(l1, a3, 'v-', c='royalblue', label = r"$a/l_1=10$", markersize=3)
#ax.plot(l1, a4, 'p-', c='orchid', label = r"$a/l_1=20$", markersize=3)

plt.xlabel(r"$l_i$", fontsize=18)
plt.ylabel(r"$f_i/l_i(e^{-12})$", fontsize=18)

#ax.legend()
plt.show()
fig.savefig("fili_li_l020.png")
