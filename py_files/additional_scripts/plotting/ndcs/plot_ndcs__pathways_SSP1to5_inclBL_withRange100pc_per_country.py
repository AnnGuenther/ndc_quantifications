# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 08/2020.
"""

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

folders_reclass = [
    'ndcs_20200628_2218_SSP1_typeCalc',
    'ndcs_20200628_2120_SSP2_typeCalc',
    'ndcs_20200628_2229_SSP3_typeCalc',
    'ndcs_20200628_2243_SSP4_typeCalc',
    'ndcs_20200628_2258_SSP5_typeCalc']
folders_reclass100 = [
    'ndcs_20200628_2221_SSP1_typeCalc_pccov100',
    'ndcs_20200628_2122_SSP2_typeCalc_pccov100',
    'ndcs_20200628_2234_SSP3_typeCalc_pccov100',
    'ndcs_20200628_2248_SSP4_typeCalc_pccov100',
    'ndcs_20200628_2301_SSP5_typeCalc_pccov100']

folders_main = [
    'ndcs_20200702_0834_SSP1_typeOrig',
    'ndcs_20200702_0829_SSP2_typeOrig',
    'ndcs_20200702_0839_SSP3_typeOrig',
    'ndcs_20200702_0844_SSP4_typeOrig',
    'ndcs_20200702_0848_SSP5_typeOrig']
folders_main100 = [
    'ndcs_20200702_0836_SSP1_typeOrig_pccov100',
    'ndcs_20200702_0830_SSP2_typeOrig_pccov100',
    'ndcs_20200702_0840_SSP3_typeOrig_pccov100',
    'ndcs_20200702_0845_SSP4_typeOrig_pccov100',
    'ndcs_20200702_0849_SSP5_typeOrig_pccov100']

folders_reclass_constant_path = [
    'ndcs_20200930_1636_SSP1_typeCalc_constEmiAfterLastTar',
    'ndcs_20200930_1625_SSP2_typeCalc_constEmiAfterLastTar',
    'ndcs_20200930_1649_SSP3_typeCalc_constEmiAfterLastTar',
    'ndcs_20200930_1705_SSP4_typeCalc_constEmiAfterLastTar',
    'ndcs_20200930_1720_SSP5_typeCalc_constEmiAfterLastTar']
folders_reclass100_constant_path = [
    'ndcs_20200628_2225_SSP1_typeCalc_pccov100_constEmiAfterLastTar',
    'ndcs_20200628_2125_SSP2_typeCalc_pccov100_constEmiAfterLastTar',
    'ndcs_20200628_2238_SSP3_typeCalc_pccov100_constEmiAfterLastTar',
    'ndcs_20200628_2253_SSP4_typeCalc_pccov100_constEmiAfterLastTar',
    'ndcs_20200628_2304_SSP5_typeCalc_pccov100_constEmiAfterLastTar']

folders_main_constant_path = [
    'ndcs_20200930_1639_SSP1_typeOrig_constEmiAfterLastTar',
    'ndcs_20200930_1628_SSP2_typeOrig_constEmiAfterLastTar',
    'ndcs_20200930_1654_SSP3_typeOrig_constEmiAfterLastTar',
    'ndcs_20200930_1709_SSP4_typeOrig_constEmiAfterLastTar',
    'ndcs_20200930_1723_SSP5_typeOrig_constEmiAfterLastTar']
folders_main100_constant_path = [
    'ndcs_20200702_0837_SSP1_typeOrig_pccov100_constEmiAfterLastTar',
    'ndcs_20200702_0831_SSP2_typeOrig_pccov100_constEmiAfterLastTar',
    'ndcs_20200702_0841_SSP3_typeOrig_pccov100_constEmiAfterLastTar',
    'ndcs_20200702_0846_SSP4_typeOrig_pccov100_constEmiAfterLastTar',
    'ndcs_20200702_0850_SSP5_typeOrig_pccov100_constEmiAfterLastTar']

folders_reclass_baselineUncondi = [
    'ndcs_20200930_1638_SSP1_typeCalc_BLForUCAboveBL',
    'ndcs_20200930_1626_SSP2_typeCalc_BLForUCAboveBL',
    'ndcs_20200930_1651_SSP3_typeCalc_BLForUCAboveBL',
    'ndcs_20200930_1707_SSP4_typeCalc_BLForUCAboveBL',
    'ndcs_20200930_1722_SSP5_typeCalc_BLForUCAboveBL']
folders_reclass100_baselineUncondi = [
    'ndcs_20200628_2227_SSP1_typeCalc_pccov100_BLForUCAboveBL',
    'ndcs_20200628_2126_SSP2_typeCalc_pccov100_BLForUCAboveBL',
    'ndcs_20200628_2241_SSP3_typeCalc_pccov100_BLForUCAboveBL',
    'ndcs_20200628_2255_SSP4_typeCalc_pccov100_BLForUCAboveBL',
    'ndcs_20200628_2306_SSP5_typeCalc_pccov100_BLForUCAboveBL']

folders_main_baselineUncondi = [
    'ndcs_20200930_1641_SSP1_typeOrig_BLForUCAboveBL',
    'ndcs_20200930_1629_SSP2_typeOrig_BLForUCAboveBL',
    'ndcs_20200930_1655_SSP3_typeOrig_BLForUCAboveBL',
    'ndcs_20200930_1711_SSP4_typeOrig_BLForUCAboveBL',
    'ndcs_20200930_1725_SSP5_typeOrig_BLForUCAboveBL']
folders_main100_baselineUncondi = [
    'ndcs_20200702_0838_SSP1_typeOrig_pccov100_BLForUCAboveBL',
    'ndcs_20200702_0832_SSP2_typeOrig_pccov100_BLForUCAboveBL',
    'ndcs_20200702_0843_SSP3_typeOrig_pccov100_BLForUCAboveBL',
    'ndcs_20200702_0847_SSP4_typeOrig_pccov100_BLForUCAboveBL',
    'ndcs_20200702_0852_SSP5_typeOrig_pccov100_BLForUCAboveBL']

folders_reclass_fao = [
    'ndcs_20200930_1642_SSP1_typeCalc_FAO',
    'ndcs_20200930_1630_SSP2_typeCalc_FAO',
    'ndcs_20200930_1657_SSP3_typeCalc_FAO',
    'ndcs_20200930_1713_SSP4_typeCalc_FAO',
    'ndcs_20200930_1726_SSP5_typeCalc_FAO']
folders_reclass100_fao = [
    'ndcs_20200706_1234_SSP1_typeCalc_pccov100_FAO',
    'ndcs_20200706_1226_SSP2_typeCalc_pccov100_FAO',
    'ndcs_20200706_1241_SSP3_typeCalc_pccov100_FAO',
    'ndcs_20200706_1249_SSP4_typeCalc_pccov100_FAO',
    'ndcs_20200706_1257_SSP5_typeCalc_pccov100_FAO']

folders_main_fao = [
    'ndcs_20200930_1644_SSP1_typeOrig_FAO',
    'ndcs_20200930_1632_SSP2_typeOrig_FAO',
    'ndcs_20200930_1658_SSP3_typeOrig_FAO',
    'ndcs_20200930_1715_SSP4_typeOrig_FAO',
    'ndcs_20200930_1727_SSP5_typeOrig_FAO']
folders_main100_fao = [
    'ndcs_20200706_1236_SSP1_typeOrig_pccov100_FAO',
    'ndcs_20200706_1228_SSP2_typeOrig_pccov100_FAO',
    'ndcs_20200706_1243_SSP3_typeOrig_pccov100_FAO',
    'ndcs_20200706_1251_SSP4_typeOrig_pccov100_FAO',
    'ndcs_20200706_1259_SSP5_typemain_pccov100_FAO']

cat = 'IPCM0EL'

# %%    
ssp1_4 = ['SSP1', 'SSP2', 'SSP3', 'SSP4']
ssp1_5 = ssp1_4 + ['SSP5']

# Read in data.
ptws = {}
for folders, what in \
    [folders_reclass, 'reclass'], [folders_reclass100, 'reclass100'], \
    [folders_main, 'main'], [folders_main100, 'main100'], \
    [folders_reclass_constant_path, 'reclass_const'], [folders_reclass100_constant_path, 'reclass100_const'], \
    [folders_main_constant_path, 'main_const'], [folders_main100_constant_path, 'main100_const'], \
    [folders_reclass_baselineUncondi, 'reclass_blUncondi'], [folders_reclass100_baselineUncondi, 'reclass100_blUncondi'], \
    [folders_main_baselineUncondi, 'main_blUncondi'], [folders_main100_baselineUncondi, 'main100_blUncondi'], \
    [folders_reclass_fao, 'reclass_fao'], [folders_reclass100_fao, 'reclass100_fao'], \
    [folders_main_fao, 'main_fao'], [folders_main100_fao, 'main100_fao']:
    
    ptws[what] = {}
    
    for folder, ssp in zip(folders, meta.ssps.scens.short):
        
        data = pd.read_csv(Path(meta.path.output, 'output_for_paper', folder, 
            'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
        ptws[what][ssp] = data

# Plotting.
colours_ssps = pd.read_csv(
    Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 
         'colours_ssps.csv'), index_col=0)
colours_ssps.index = [meta.ssps.scens.long_to_short[xx] for xx in colours_ssps.index]

years_int = range(1990, 2031)
years_str = [str(xx) for xx in years_int]

XL_emi = [2010, 2030.5]
XL_tars = [2016, 2037.5]

linewdth_all = 1.5
linestyle = {'SSP1': '--', 'SSP2': '-', 'SSP3': '--', 'SSP4': ':', 'SSP5': ':'}

yr_add = .2

colour_100pc = (0, .4, .4)
colour_estpc = (.1, .8, .4)
colour_prioNDCs = (.1, .7, .7)
colour_prioSSPs = (.4, .5, .1)

# %%
fig = plt.figure(figsize=(12, 4))

for iso3 in ['BRA']: # meta.isos.EARTH:
    
    ax_emi = fig.add_subplot(1, 2, 1)
    #inax = inset_axes(ax_emi, width="25%", height="30%", loc='upper right')
    ax_tars = fig.add_subplot(1, 2, 2)
            
    handles = {}
    
    ax_emi.set_xlim(XL_emi)
    ax_tars.set_xlim(XL_tars)
    
    txt_options = []
    for tpe, add_x0, \
        tpe_data100, tpe_const100, tpe_blUncondi100, tpe_fao100, \
        tpe_data, tpe_const, tpe_blUncondi, tpe_fao in \
        ['type_reclass', 0, 
         ptws['reclass100'], ptws['reclass100_const'], ptws['reclass100_blUncondi'], ptws['reclass100_fao'], 
         ptws['reclass'], ptws['reclass_const'], ptws['reclass_blUncondi'], ptws['reclass_fao']], \
        ['type_main', +2, 
         ptws['main100'], ptws['main100_const'], ptws['main100_blUncondi'], ptws['main100_fao'], 
         ptws['main'], ptws['main_const'], ptws['main_blUncondi'], ptws['main_fao']]:
    
        for ssp, ssp_long, add_x in \
            zip(meta.ssps.scens.short, meta.ssps.scens.long, [0, 4, 8, 12, 16]):
            
            add_xx = add_x0 + add_x
            
            colour_act = colours_ssps.loc[ssp, :].to_list()
            linewdth = linewdth_all*1.5
            
            # Vertical lines
            axa = ax_tars
            yr_plt = 2017
                        
            for opt, data_opt in \
                ['default', tpe_data100], \
                ['baseline uncondi', tpe_blUncondi100], \
                ['constant emi', tpe_const100], \
                ['LU FAO', tpe_fao100], \
                ['default (*)', tpe_data], \
                ['baseline uncondi (*)', tpe_blUncondi], \
                ['constant emi (*)', tpe_const], \
                ['LU FAO (*)', tpe_fao]:
                
                txt_options += [opt]
                data_upper2030 = data_opt[ssp]
                data_upper2030 = 1e-3 * data_upper2030.loc[
                    (data_upper2030.iso3 == iso3) & 
                    (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                    (data_upper2030.category == cat), '2030'].max()
                
                data_lower2030 = data_opt[ssp]
                data_lower2030 = 1e-3 * data_lower2030.loc[
                    (data_lower2030.iso3 == iso3) & 
                    (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                    (data_lower2030.category == cat), '2030'].min()
                
                axa.plot(
                    [yr_plt + add_xx, yr_plt + add_xx], 
                    [data_upper2030, data_lower2030], 
                    color=colour_act, linewidth=linewdth_all)
                
                yr_plt += yr_add
                
                data_act = data_opt[ssp]
                data_act = 1e-3 * data_act.loc[
                    (data_act.iso3 == iso3) & 
                    (data_act.condi.isin(['unconditional', 'conditional'])) &
                    (data_act.category == cat), '2030']
                
                axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
                
                if 'default' in opt:
                    
                    # Lines.
                    data_upper = data_opt[ssp]
                    data_upper = 1e-3 * data_upper.loc[
                        (data_upper.iso3 == iso3) & (data_upper.condi.isin(['unconditional', 'conditional'])) &
                        (data_upper.category == cat), :].reindex(columns=years_str).max()
                    
                    data_lower = data_opt[ssp]
                    data_lower = 1e-3 * data_lower.loc[
                        (data_lower.iso3 == iso3) & (data_lower.condi.isin(['unconditional', 'conditional'])) &
                        (data_lower.category == cat), :].reindex(columns=years_str).min()
                    
                    # Filled area.
                    if ssp == 'SSP2':
                        ax_emi.fill_between(years_int, data_upper[years_str], 
                            data_lower[years_str], color=colour_act, linewidth=linewdth, alpha=.2)
            
                if opt == 'LU FAO':
                    yr_plt += .2
                    
            # BAU
            data = tpe_data[ssp]
            data = 1e-3 * data.loc[
                (data.iso3 == iso3) & (data.condi == 'emi_bau') & (data.category == cat), :]. \
                reindex(columns=years_str).values[0]
            handles[ssp], = ax_emi.plot(years_int, data, color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp])
    
    YL_emi = [min([ax_emi.get_ylim()[0], ax_tars.get_ylim()[0]]),
              max([ax_emi.get_ylim()[1], ax_tars.get_ylim()[1]])*1.05]
    for axa, txt, XL in \
        [ax_emi, '(a) Baseline emissions', XL_emi], \
        [ax_tars, '(b) Target emissions (2030)', XL_tars]:
        axa.set_ylim(YL_emi)
        axa.text(XL[0] + .05*np.diff(XL), YL_emi[1] + .14*np.diff(YL_emi), 
            txt, fontweight='bold', ha='left', va='bottom')
        if axa == ax_emi:
            txt1 = '\nupper lines: prio NDCs (for type_reclass)'
            txt2 = 'lower lines: prio SSPs (for type_main)'
        else:
            txt1 = '\n'
            txt2 = '\n'
        axa.text(XL[0] + .05*np.diff(XL), YL_emi[1] + .08*np.diff(YL_emi), 
                 txt1, ha='left', va='bottom')
        axa.text(XL[0] + .05*np.diff(XL), YL_emi[1] + .02*np.diff(YL_emi), 
                 txt2, ha='left', va='bottom')
        
        if axa == ax_tars:
            yval = 2*[YL_emi[1] - .02*np.diff(YL_emi)]
            # 100% cov
            axa.plot([2016.85, 2017.65], yval, color=colour_100pc, linewidth=3)
            axa.plot([2018.85, 2019.65], yval, color=colour_100pc, linewidth=3)
            # estimated cov
            axa.plot([2017.85, 2018.65], yval, color=colour_estpc, linewidth=3)
            axa.plot([2019.85, 2020.65], yval, color=colour_estpc, linewidth=3)
            yval = 2*[YL_emi[1] - .04*np.diff(YL_emi)]
            # prio NDCs, type_reclass
            axa.plot([2016.85, 2018.65], yval, color=colour_prioNDCs, linewidth=3)
            # prio SSPs, type_main
            axa.plot([2018.85, 2020.65], yval, color=colour_prioSSPs, linewidth=3)
            # text
            axa.text(XL[0] + .05*np.diff(XL), YL_emi[1] + .08*np.diff(YL_emi), 
                     'prio NDCs, type_reclass', color=colour_prioNDCs, ha='left', va='bottom')
            axa.text(XL[0] + .05*np.diff(XL), YL_emi[1] + .02*np.diff(YL_emi), 
                     'prio SSPs, type_main', color=colour_prioSSPs, ha='left', va='bottom')
            axa.text(XL[0] + .55*np.diff(XL), YL_emi[1] + .08*np.diff(YL_emi), 
                     '100% coverage', color=colour_100pc, ha='left', va='bottom')
            axa.text(XL[0] + .55*np.diff(XL), YL_emi[1] + .02*np.diff(YL_emi), 
                     'estimated coverage', color=colour_estpc, ha='left', va='bottom')
            
            xstart = 2016.75
            for xx in np.arange(xstart, 2040, 1):
                axa.plot([xx, xx], YL_emi, 'k', linewidth=.2)
            for xx in np.arange(xstart, 2040, 2):
                axa.plot([xx, xx], YL_emi, 'k', linewidth=.4)
            for xx in np.arange(xstart, 2040, 4):
                axa.plot([xx, xx], YL_emi, 'k', linewidth=.6)
    
        axa.set_ylabel('emissions / Gt CO$_2$eq AR4', fontweight='bold')
    
    ssps_legend = meta.ssps.scens.short
    ax_emi.legend([handles[xx] for xx in ssps_legend], [f"dm{xx}" for xx in ssps_legend], loc='best')
    
    ax_emi.set_xlabel('year', fontweight='bold')
    ax_tars.xaxis.set_ticks(np.arange(2018.75, 2036, 4))
    ax_tars.set_xticklabels([f"dm{xx}" for xx in ssp1_5])
    ax_tars.yaxis.set_ticks_position('both')
    
    # Different options:
    ax_tars.text(XL[1] + .08*np.diff(XL), YL_emi[0] + .5*np.diff(YL_emi), 
        f"Quadruples:\n(1) {txt_options[0]} (2) {txt_options[1]}\n(3) {txt_options[2]} (4) {txt_options[3]}",
        ha='center', va='center', rotation=90)
    
    ax_emi.xaxis.set_ticks(range(2010, 2032, 5))
        
    fig.subplots_adjust(left=.1, right=.9, top=.8)
    path_to_plot = Path(meta.path.main, 'latex_files', #iso3, 
        f'ndc_tars_{cat}_{iso3}.png')
    plt.savefig(path_to_plot, dpi=300)
    plt.clf()

plt.close(fig)

# %%
