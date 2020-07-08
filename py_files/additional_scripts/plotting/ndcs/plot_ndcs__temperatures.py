# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from setup_metadata import setup_metadata
import helpers_functions as hpf

# %%
meta = setup_metadata()

# %%
temps = pd.read_csv(
    Path(meta.path.main, 'data', 'other', 'magicc_temperatures_ndcs_20200630.csv'))
colours = pd.read_csv(
    Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_ssps.csv'), index_col=0)

# %%
YL = [2.25, 4.75]
XL = [-1, 5]

fig = plt.figure(figsize=(8, 6))
axa = fig.add_subplot(1, 1, 1)
for temp in np.arange(2, 5, .25):
    axa.plot([-1, 5], [temp, temp], 'k:', linewidth=.2)
for xx in np.arange(-.5, 7, 1):
    axa.plot([xx, xx], YL, 'k:', linewidth=.2)

count = 0
for ssp in meta.ssps.scens.short:
    colour_ssp = tuple(colours.loc[meta.ssps.scens.short_to_long[ssp], :])
    for tpe, x_add_all, x_add in ['type_calc', -.3, -.1], ['type_orig', .1, .3]:
        
        pccov = 'pccov_100'
        yvals = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_median' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0]
        axa.plot([count + x_add_all, count + x_add_all], [min(yvals), max(yvals)], color=colour_ssp)
        yval = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            'BAU_68_percent_median'].values[0]
        axa.plot([count + x_add_all - .1, count + x_add_all + .1], [yval, yval], color=colour_ssp)
        axa.scatter([count + x_add_all]*4, temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_median' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0], marker='.', color=colour_ssp)
        
        pccov = 'pccov_real'
        yvals = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_median' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0]
        axa.plot([count + x_add, count + x_add], [min(yvals), max(yvals)], color=colour_ssp)
        yval = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            'BAU_68_percent_median'].values[0]
        axa.plot([count + x_add - .1, count + x_add + .1], [yval, yval], color=colour_ssp)
        axa.scatter([count + x_add]*4, temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_median' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0], marker='.', color=colour_ssp)
   
    count += 1

axa.set_xlim(XL)
axa.set_ylim(YL)
axa.text(1-.3, YL[1] - .02*np.diff(YL), 'prio NDCs (100%)', rotation=90, ha='center', va='top', fontweight='bold')
axa.text(1-.1, YL[1] - .02*np.diff(YL), 'prio NDCs (estimated %)', rotation=90, ha='center', va='top', fontweight='bold')
axa.text(1+.1, YL[1] - .02*np.diff(YL), 'prio SSPs (100%)', rotation=90, ha='center', va='top', fontweight='bold')
axa.text(1+.3, YL[1] - .02*np.diff(YL), 'prio SSPs (estimated %)', rotation=90, ha='center', va='top', fontweight='bold')

axa.set_ylabel('temperature rise compared to\npre-industrial times / C°', fontweight='bold')

axa.set_xticks(range(len(meta.ssps.scens.short)))
axa.set_xticklabels(meta.ssps.scens.short, fontweight='bold')
axa.yaxis.set_ticks_position('both')

fig.subplots_adjust(left=.2)
path_to_png = Path(meta.path.main, 'plots', 'ndc_quantifications', 'temperatures_2100_overview.png')
plt.savefig(path_to_png, dpi=300)
path_to_pdf = str(path_to_png).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
YL = [1.5, 7]
XL = [-.5, 3.5]

fig = plt.figure(figsize=(8, 6))
axa = fig.add_subplot(1, 1, 1)
for temp in np.arange(YL[0], YL[1]+1, .25):
    axa.plot([-1, 5], [temp, temp], 'k:', linewidth=.2)
for xx in np.arange(-.5, XL[1]+1, 1):
    axa.plot([xx, xx], YL, 'k:', linewidth=.2)

count = 0
for ssp in meta.ssps.scens.short[:-1]:
    colour_ssp = tuple(colours.loc[meta.ssps.scens.short_to_long[ssp], :])
    for tpe, x_add_all, x_add in ['type_calc', -.3, -.1], ['type_orig', .1, .3]:
        
        pccov = 'pccov_100'
        
        yval_low = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            'BAU_68_percent_low'].values[0]
        yval_high = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            'BAU_68_percent_high'].values[0]
        axa.fill_between([count + x_add_all - .1, count + x_add_all + .1], 
                         [yval_low, yval_low], [yval_high, yval_high], color=colour_ssp, alpha=.2)
        yval = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            'BAU_68_percent_median'].values[0]
        axa.plot([count + x_add_all - .1, count + x_add_all + .1], [yval, yval], color=colour_ssp)
        print(f"% {ssp} {tpe} {pccov} BAU (median): {yval :.1f}°C.")
        
        yvals_low = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_low' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0]
        yvals_high = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_high' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0]
        axa.fill_between([count + x_add_all - .05, count + x_add_all + .05], [min(yvals_low), min(yvals_low)], 
                         [max(yvals_high), max(yvals_high)], color=colour_ssp, alpha=.4)
        
        yvals = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_median' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0]
        axa.plot([count + x_add_all, count + x_add_all], [min(yvals), max(yvals)], color=colour_ssp)
        print(f"% {ssp} {tpe} {pccov} targets (median): {min(yvals) :.1f} - {max(yvals) :.1f}°C.")
        
        axa.scatter([count + x_add_all]*4, temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_median' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0], marker='.', color=colour_ssp)
        
        pccov = 'pccov_real'
        
        yval_low = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            'BAU_68_percent_low'].values[0]
        yval_high = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            'BAU_68_percent_high'].values[0]
        axa.fill_between([count + x_add - .1, count + x_add + .1], 
                         [yval_low, yval_low], [yval_high, yval_high], color=colour_ssp, alpha=.2)
        yval = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            'BAU_68_percent_median'].values[0]
        axa.plot([count + x_add - .1, count + x_add + .1], [yval, yval], color=colour_ssp)
        
        yvals_low = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_low' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0]
        yvals_high = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_high' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0]
        axa.fill_between([count + x_add - .05, count + x_add + .05], [min(yvals_low), min(yvals_low)], 
                         [max(yvals_high), max(yvals_high)], color=colour_ssp, alpha=.4)
        
        yvals = temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_median' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0]
        axa.plot([count + x_add, count + x_add], [min(yvals), max(yvals)], color=colour_ssp)
        print(f"% {ssp} {tpe} {pccov} targets (median): {min(yvals) :.1f} - {max(yvals) :.1f}°C.")
        
        axa.scatter([count + x_add]*4, temps.loc[(temps.SSP == ssp) & (temps.type == tpe) & (temps.pccov == pccov), 
            [f'NDC{xx}_68_percent_median' for xx in ['UCW', 'UCB', 'CW', 'CB']]].values[0], marker='.', color=colour_ssp)
   
    count += 1

axa.set_xlim(XL)
axa.set_ylim(YL)
axa.text(-.3, YL[1] - .02*np.diff(YL), 'prio NDCs (100%)', rotation=90, ha='center', va='top', fontweight='bold')
axa.text(-.1, YL[1] - .02*np.diff(YL), 'prio NDCs (estimated %)', rotation=90, ha='center', va='top', fontweight='bold')
axa.text(+.1, YL[1] - .02*np.diff(YL), 'prio SSPs (100%)', rotation=90, ha='center', va='top', fontweight='bold')
axa.text(+.3, YL[1] - .02*np.diff(YL), 'prio SSPs (estimated %)', rotation=90, ha='center', va='top', fontweight='bold')

axa.set_ylabel('temperature rise by 2100\ncompared to pre-industrial times\nC°', fontweight='bold')

axa.set_xticks(range(len(meta.ssps.scens.short[:-1])))
axa.set_xticklabels(meta.ssps.scens.short, fontweight='bold')
axa.yaxis.set_ticks_position('both')

fig.subplots_adjust(left=.2)
path_to_png = Path(meta.path.main, 'plots', 'ndc_quantifications', 'temperatures_2100_overview_exclSSP5.png')
plt.savefig(path_to_png, dpi=300)
path_to_pdf = str(path_to_png).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%