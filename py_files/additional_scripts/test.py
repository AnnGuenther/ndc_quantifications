# %%
import pandas as pd
import numpy as np
from pathlib import Path
import os
from copy import deepcopy
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata
meta = setup_metadata()

# %%
fig = plt.figure(figsize=(5, 5))
axa = fig.add_subplot(1, 1, 1)

test = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'isipedia',
    'data', 'quantiles_example.csv'), index_col=0)
test.columns = [int(xx) for xx in test.columns]
test = test.drop(columns=[2015])

ndcs = pd.Series(index=test.columns, dtype='float')
ndcs[np.arange(1990, 2031, 10)] = \
    test.loc['scen1', [1990, 2000, 2010]].tolist() + [48, 50]

quantiles = test.quantile(np.arange(0, 1, .01))

for scen in test.index:
    lbl = ('__nolegend__' if scen != test.index[0] else 'scenarios from database')
    axa.plot(test.columns, test.loc[scen, :].values, color=[0, 0, 1], alpha=.5, linewidth=1, label=lbl)

for quantile in quantiles.index:
    lbl = ('__nolegend__' if quantile != quantiles.index[0] else 'quantiles (0%, 1%, 2%, etc.)')
    axa.plot(quantiles.columns, quantiles.loc[quantile, :].values, color='c', alpha=.5, linewidth=.5, label=lbl)

quantiles_2030 = quantiles.loc[:, 2030]
quantile_chosen = 0.45 # more or less
ndcs_path = pd.Series(index=ndcs.index, dtype='float')
ndcs_path[np.arange(1990, 2031, 10)] = ndcs[np.arange(1990, 2031, 10)]

ndcs_path[np.arange(2040, 2101, 10)] = quantiles.loc[quantile_chosen, np.arange(2040, 2101, 10)]

plt_yrs = np.arange(1990, 2031, 10)
axa.plot(plt_yrs, ndcs_path.loc[plt_yrs], 'k', linewidth=3, label='NDC pathway up to 2030')
plt_yrs = np.arange(2030, 2101, 10)
axa.plot(plt_yrs, ndcs_path.loc[plt_yrs], 'r', linewidth=3, label='NDC pathway extension')

XL = [1989, 2101]
YL = axa.get_ylim()

axa.set_xlim(XL)
axa.set_ylim(YL)

# bottom to top
axa.text(XL[1] + .03*np.diff(XL), ndcs_path.loc[2100]-4, '45%', rotation=90, fontweight='bold', color='r',
    ha='center', va='top')
axa.text(XL[1] + .03*np.diff(XL), ndcs_path.loc[2100], '--', fontweight='bold', color='r',
    ha='center', va='center')
axa.text(XL[1] + .03*np.diff(XL), ndcs_path.loc[2100]+4, '55%', rotation=90, fontweight='bold', color='r',
    ha='center', va='bottom')

axa.text(2030, ndcs_path.loc[2030], 'x', color='k', fontweight='bold', ha='center', va='center', fontsize=20)
axa.text(2030, ndcs_path.loc[2030], 'x', color='r', fontweight='bold', ha='center', va='center', fontsize=15)
axa.text(1995, YL[0] + .1*np.diff(YL), 
    'NDC value in 2030\nequals the 45th quantile\nof the scenarios', color='r', fontweight='bold')

axa.legend()

axa.set_xlabel('years', fontweight='bold')
axa.set_ylabel('emissions', fontweight='bold')

#fig.subplots_adjust(left=.1, right=.9)
plt.savefig(Path(meta.path.py_files, 'additional_scripts', 'isipedia', 'plots', 'quantiles.png'), dpi=300)
plt.savefig(Path(meta.path.py_files, 'additional_scripts', 'isipedia', 'plots', 'quantiles.svg'), dpi=300)
plt.clf()
plt.close(fig)

# %%