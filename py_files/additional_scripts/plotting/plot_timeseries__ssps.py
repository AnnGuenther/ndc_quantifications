# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
"""
Plot time series of global emissions, population and GDP, for the SSP1 to SSP5.
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()
ssps = meta.ssps.scens.long

colours_ssps = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
    'colours', 'colours_ssps.csv'), index_col=0)

emi_filled = {}
emi_orig = {}
pop_filled = {}
pop_orig = {}
gdp_filled = {}
gdp_orig = {}

for ssp in ssps:
    
    emi_filled[ssp] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f'KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp}FILLED_PMSSPBIE.csv'))
    
    pop_filled[ssp] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f'POP_DEMOGR_TOTAL_NET_{ssp}FILLED_PMSSPBIEMISC.csv'))
    
    gdp_filled[ssp] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f'GDPPPP_ECO_TOTAL_NET_{ssp}FILLED_PMSSPBIEMISC.csv'))

# %%
linewdth_all = 1.5

fig = plt.figure(figsize=(12, 4))
ax_emi = fig.add_subplot(1, 3, 1)
ax_pop = fig.add_subplot(1, 3, 2)
ax_gdp = fig.add_subplot(1, 3, 3)

years = range(1990, 2031)

for ssp, count, add_x in zip(ssps + [ssps[1]], range(len(ssps + [ssps[1]])), [-.2, -.1, 0, .1, .2]):
    
    linestyle = ('--' if 'SSP4' in ssp else '-')
    
    linewdth = linewdth_all#(linewdth_all * 1.5 if count in [1, 5] else linewdth_all)
    colour_act = colours_ssps.loc[ssp, :].to_list()
    
    ax_emi.plot(1e-3 * emi_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
        color=colour_act, linewidth=linewdth, linestyle=linestyle, label=(ssp if count != 5 else '__nolegend__'))
    
    ax_pop.plot(pop_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
        color=colour_act, linewidth=linewdth, linestyle=linestyle, label=(ssp if count != 5 else '__nolegend__'))
    
    ax_gdp.plot(gdp_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
        color=colour_act, linewidth=linewdth, linestyle=linestyle, label=(ssp if count != 5 else '__nolegend__'))

XL = [1989, 2031]
for axa in [ax_emi, ax_pop, ax_gdp]:
    axa.set_xlabel('year', fontweight='bold')
    #axa.set_ylim([0, axa.get_ylim()[-1]])
    axa.set_xlim(XL)

ax_gdp.legend(loc='upper left')

ax_emi.set_ylabel('emissions / Gg CO$_2$eq AR4', fontweight='bold')
ax_pop.set_ylabel('population / Pers', fontweight='bold')
ax_gdp.set_ylabel('GDP (PPP) / 2011 US$', fontweight='bold')

YL = ax_emi.get_ylim()
ax_emi.text(XL[0] - .15*np.diff(XL), YL[0] - .23*np.diff(YL), 
    "Global pathways based on SSP marker scenarios, down-scaled to country-level " +
    "(Gütschow et al., 2020) and 'filled' for missing values / countries.")

for axa in [ax_pop, ax_gdp]:
    hpf.set_ticks_scientific_notation(axa, 'y')

fig.subplots_adjust(wspace=.3, bottom=.2)
path_to_png = Path(meta.path.main, 'plots', 'time_series', 'time_series_ssps.png')
plt.savefig(path_to_png, dpi=300)
path_to_pdf = str(path_to_png).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
# Only plot population and GDP, witout legend and annotation (for paper).
linewdth_all = 1.5
linestyle = {'SSP1BLIMAGE': '-.', 'SSP2BLMESGB': '-', 'SSP3BLAIMCGE': '--', 'SSP4BLGCAM4': ':', 'SSP5BLREMMP': (0, (3, 5, 1, 5))}

fig = plt.figure(figsize=(13, 5))
ax_pop = fig.add_subplot(1, 2, 1)
ax_gdp = fig.add_subplot(1, 2, 2)

years = range(1990, 2031)

for ssp, count, add_x in zip(ssps + [ssps[1]], range(len(ssps + [ssps[1]])), [-.2, -.1, 0, .1, .2]):
        
    linewdth = linewdth_all#(linewdth_all * 1.5 if count in [1, 5] else linewdth_all)
    colour_act = colours_ssps.loc[ssp, :].to_list()
    
    ax_pop.plot(pop_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
        color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp], label=(ssp if count != 5 else '__nolegend__'))
    
    ax_gdp.plot(gdp_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
        color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp], label=(ssp if count != 5 else '__nolegend__'))

XL = [1989, 2031.5]
for axa in [ax_pop, ax_gdp]:
    axa.set_xlabel('year', fontweight='bold')
    #axa.set_ylim([0, axa.get_ylim()[-1]])
    axa.set_xlim(XL)

#ax_gdp.legend(loc='center left')

ax_pop.set_ylabel('population / Pers', fontweight='bold')
ax_gdp.set_ylabel('GDP (PPP) / 2011 US$', fontweight='bold')

YL = ax_pop.get_ylim()
#ax_pop.text(XL[0] - .15*np.diff(XL), YL[0] - .23*np.diff(YL), 
#    "Global pathways based on SSP marker scenarios, down-scaled to country-level " +
#    "(Gütschow et al., 2020) and 'filled' for missing values / countries.")

for axa, txt in zip([ax_pop, ax_gdp], ['(b) Population', '(c) GDP PPP']):
    axa.xaxis.set_ticks(range(1990, 2031, 5))
    axa.yaxis.set_ticks_position('both')
    XL = axa.get_xlim()
    YL = axa.get_ylim()
    axa.text(XL[0] + .05*np.diff(XL), YL[1] - .05*np.diff(YL), txt, fontweight='bold', ha='left', va='top')
    axa.set_xlim(XL)
    axa.set_ylim(YL)
    hpf.set_ticks_scientific_notation(axa, 'y')

fig.subplots_adjust(wspace=.2, bottom=.3, left=.1, right=.99)
path_to_png = Path(meta.path.main, 'plots', 'time_series', 'time_series_ssps_pop_gdp.png')
plt.savefig(path_to_png, dpi=300)
path_to_pdf = str(path_to_png).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%