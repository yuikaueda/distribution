import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 21, 100)
y = 7/(1+np.exp(6-x))

fig, ax = plt.subplots()

plt.ylim([0,10])
plt.xlim([0,10])

ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])

ax.set_yticks([0,7])
ax.set_yticklabels(['0','$f_0$'], fontsize=16)
ax.set_xticks([0,6,9])
ax.set_xticklabels(['0','$l_0$','$3l_0/2$'], fontsize=16)
#ax.set_xticks([12])
#ax.set_xticklabels(['$2l_0$'], fontsize=18)

ax.set_xlabel(r'$l$',fontsize=20)
ax.set_ylabel(r'$f$',fontsize=20)

plt.xlim(0,20)

ax.plot(x,y,color='black')
fig.savefig("re_f_fig.png",bbox_inches="tight")
plt.show()

