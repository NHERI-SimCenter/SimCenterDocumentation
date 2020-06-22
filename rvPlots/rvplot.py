import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

import json


plt.style.use('plotstyle.mplstyle')
plt.rcParams['legend.title_fontsize'] = 'xx-small'


fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(11,3)
ax = [fig.add_subplot(gs[i*6:(i+1)*6-2, j]) 
         for j in [0,1,2] for i in [0,1]]

lg = [fig.add_subplot(gs[i*6+4:(i+1)*6, j]) 
         for j in [0,1,2] for i in [0,1] ]
[l.axis('off') for l in lg]


dists = [
    'Normal',
    'Lognormal',
    'Beta',
    'Uniform',
    'Weibull',
    'Gumbel']


with open('rvplot.json') as file: dat = json.load(file)

##############################################################################
# Add missing distributions

dist = 'Normal'
params = [[6.0, 0.5], [5.0, 1.0], ]
x = np.linspace(0.,10,100)

dat[dist] = {
    'l':['$\\mu={}$,\n $\\sigma={}$'.format(a[0],a[1]) for a in params],
    'x':x,
    'y':[],
}
for a in params: dat[dist]['y'].append(stats.norm.pdf(x,a[0],a[1]))


dist = 'Beta'
params = [[0.5, 0.5], [5.0, 1.0], [1.0, 3.0], [2.0, 2.0],[2.0, 5.0]]
x = np.linspace(0.,1.,100)

dat[dist] = {
    'l':['$a={}$,\n $b={}$'.format(a[0],a[1]) for a in params],
    'x':x,
    'y':[],
}
for a in params: dat[dist]['y'].append(stats.beta.pdf(x,a[0],a[1]))

##############################################################################

for i, dist in enumerate(dists):
    lines = []
    l, x, y = dat[dist].values()
    if len(y) < len(x):
        for yi,li in zip(y,l): lines += ax[i].plot(x, yi, label=li,linewidth=0.7)
    else: lines += ax[i].plot(x,y,label=l,linewidth=1.)

    ax[i].set_title(dist)
    # ax[i].xaxis.set_ticklabels([])
    # ax[i].yaxis.set_ticklabels([])
    leg = lg[i].legend(lines,l,loc='center',ncol=2, handlelength=0.7,labelspacing=0.3)
    plt.setp(leg.get_texts(), fontsize='6')

path = '..\\docs\\common\\user_manual\\usage\\desktop\\figures\\'

fig.savefig(path+'rvplot.png')
