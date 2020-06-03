import matplotlib.pyplot as plt
import json 

plt.style.use('plotstyle.mplstyle')
fig, ax = plt.subplots(2,2, constrained_layout=True)

ax = ax.flatten()

with open('rvplot.json') as file: dat = json.load(file)

for i, dist in enumerate(dat):
    l, x, y = dat[dist].values()
    if len(y) < len(x):
        for yi,li in zip(y,l): ax[i].plot(x, yi, label=li)
    else: ax[i].plot(x,y,label=l)

    ax[i].set_title(dist)
    ax[i].xaxis.set_ticklabels([])
    ax[i].yaxis.set_ticklabels([])
    ax[i].legend()

path = '..\\docs\\common\\user_manual\\usage\\desktop\\figures\\'

fig.savefig(path+'rvplot.png')
