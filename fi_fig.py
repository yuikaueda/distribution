import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 21, 100)
y = 7/(1+np.exp(6-x))

fig, ax = plt.subplots(1, 1)

plt.ylim([0,10])
plt.xlim([0,10])

ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])

ax.set_yticks([0,7])
ax.set_yticklabels(['0','$f_0$'], fontsize=18)
ax.set_xticks([6])
ax.set_xticklabels(['$l_0$'], fontsize=18)

plt.xlabel('l',fontsize=20)
plt.ylabel('f',fontsize=20)

ax.plot(x,y,color='black')
fig.savefig("f_fig.png",bbox_inches="tight")
