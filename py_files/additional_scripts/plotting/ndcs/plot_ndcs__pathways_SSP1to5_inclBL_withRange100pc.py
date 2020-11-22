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
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def plotting():
    
    ssp1_4 = ['SSP1', 'SSP2', 'SSP3', 'SSP4']
    ssp1_5 = ssp1_4 + ['SSP5']
    
    tars_all = {}
    condi_rge = ['unconditional', 'worst'], ['unconditional', 'best'], \
        ['conditional', 'worst'], ['conditional', 'best']
    for condi, rge in condi_rge:
        tars_all[f"{condi}_{rge}"] = pd.DataFrame(columns=ssp1_5, dtype='float64')
    
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
            
            data = pd.read_csv(Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
            ptws[what][ssp] = data
            
            for condi, rge in condi_rge:
                tars_all[f"{condi}_{rge}"].loc[what, ssp] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for ssps in meta.ssps.scens.short:
        
        diff = ptws['reclass'][ssps].loc[(ptws['reclass'][ssps].group == 'EARTH') & (ptws['reclass'][ssps].condi == 'emi_bau'), '2030'].values[0] - \
            ptws['main'][ssps].loc[(ptws['main'][ssps].group == 'EARTH') & (ptws['main'][ssps].condi == 'emi_bau'), '2030'].values[0]
        print(f"% Difference between bau for reclass and main {ssps}: {diff/1000 :+.1f} Gt CO2eq_AR4.")
        diff = ptws['reclass100'][ssps].loc[(ptws['reclass100'][ssps].group == 'EARTH') & (ptws['reclass100'][ssps].condi == 'emi_bau'), '2030'].values[0] - \
            ptws['main100'][ssps].loc[(ptws['main100'][ssps].group == 'EARTH') & (ptws['main100'][ssps].condi == 'emi_bau'), '2030'].values[0]
        print(f"% Difference between bau for reclass_100% and main_100% {ssps}: {diff/1000 :+.1f} Gt CO2eq_AR4.")
    
    diff_med = (tars_all['unconditional_worst']-tars_all['conditional_best'])*1e-3
    [print(f"% Difference between uncondi worst & condi best: min/max for the different options, for {xx}: " +
           f"{diff_med.loc[:, xx].min() :.1f} to {diff_med.loc[:, xx].max() :.1f} Gt CO2eq AR4") for xx in tars_all['unconditional_worst'].columns]
    
    print("\nDifference between the default 100% runs with LULUCF prio CRF, and with FAO:")
    for ssp in tars_all['unconditional_worst'].columns:
        print(f"type_reclass ({ssp}): " +
            f"unconditional worst {1e-3*(tars_all['unconditional_worst'].loc['reclass100', ssp] - tars_all['unconditional_worst'].loc['reclass100_fao', ssp]) :.1f}; " +
            f"conditional best {1e-3*(tars_all['conditional_best'].loc['reclass100', ssp] - tars_all['conditional_best'].loc['reclass100_fao', ssp]) :.1f} Gt CO2eq")
        print(f"type_main ({ssp}): " +
            f"unconditional worst {1e-3*(tars_all['unconditional_worst'].loc['main100', ssp] - tars_all['unconditional_worst'].loc['main100_fao', ssp]) :.1f}; " +
            f"conditional best {1e-3*(tars_all['conditional_best'].loc['main100', ssp] - tars_all['conditional_best'].loc['main100_fao', ssp]) :.1f} Gt CO2eq")
    
    rge_SSP2 = np.percentile(1e-3*(tars_all['unconditional_worst'].loc[:, 'SSP2'] - tars_all['conditional_best'].loc[:, 'SSP2']), [10, 50, 90])
    rge_SSP1to4 = np.percentile(1e-3*(tars_all['unconditional_worst'].loc[:, ssp1_4] - tars_all['conditional_best'].loc[:, ssp1_4]), [10, 50, 90])
    print("\n% Range for SSP2 (10, 50, 90%): " + ", ".join([f"{xx :.1f}" for xx in rge_SSP2]) + " Gt CO2eq")
    print(f"% Range for SSP1-4 (10, 50, 90%): " + ", ".join([f"{xx :.1f}" for xx in rge_SSP1to4]) + " Gt CO2eq")
    
    print("\n% Range of unconditional worst (SSP1-4, 10, 50, 90%): " + 
          ", ".join([f"{xx :.1f}" for xx in np.percentile(tars_all['unconditional_worst'].loc[:, ssp1_4]/1000, [10, 50, 90])]) + " Gt CO2 eq")
    print("% Range of unconditional best (SSP1-4, 10, 50, 90%): " +
          ", ".join([f"{xx :.1f}" for xx in np.percentile(tars_all['unconditional_best'].loc[:, ssp1_4]/1000, [10, 50, 90])]) + " Gt CO2 eq")
    print("% Range of conditional worst (SSP1-4, 10, 50, 90%): " + 
          ", ".join([f"{xx :.1f}" for xx in np.percentile(tars_all['conditional_worst'].loc[:, ssp1_4]/1000, [10, 50, 90])]) + " Gt CO2 eq")
    print("% Range of conditional best (SSP1-4, 10, 50, 90%): " +
          ", ".join([f"{xx :.1f}" for xx in np.percentile(tars_all['conditional_best'].loc[:, ssp1_4]/1000, [10, 50, 90])]) + " Gt CO2 eq")
    
    tars_SSP1to4 = np.percentile((tars_all['unconditional_worst'].loc[:, ssp1_4].values,
                                  tars_all['conditional_best'].loc[:, ssp1_4].values), [10, 50, 90])/1000
    print("\n% Range of SSP1-4 quantifications (uncondi worst and condi best): " + 
          ", ".join([f"{xx :.1f}" for xx in tars_SSP1to4]) + " Gt CO2 eq")
    
    rge_condi_SSP1to4 = np.percentile(tars_all['unconditional_worst'].loc[:, ssp1_4].add(
        -tars_all['conditional_best'].loc[:, ssp1_4]).values, [10, 50, 90])/1000
    print("\n% Range between unconditional worst and conditional best targets (SSP1-4, 10, 50, 90%): " + 
          ", ".join([f"{xx :.1f}" for xx in rge_condi_SSP1to4]) + " Gt CO2eq")
   
    tars_all['unconditional_worst'].drop(columns=['SSP5'], inplace=True)
    tars_all['conditional_best'].drop(columns=['SSP5'], inplace=True)
    tars_all['unconditional_worst'].loc[:, 'median'] = tars_all['unconditional_worst'].median(axis=1)
    tars_all['conditional_best'].loc[:, 'median'] = tars_all['conditional_best'].median(axis=1)
    
    # Plotting.
    colours_ssps = pd.read_csv(
        Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 
             'colours_ssps.csv'), index_col=0)
    colours_ssps.index = [meta.ssps.scens.long_to_short[xx] for xx in colours_ssps.index]
    
    years_int = range(1990, 2031)
    years_str = [str(xx) for xx in years_int]
    
    fig = plt.figure(figsize=(12, 10))
    ax_emi = fig.add_subplot(2, 2, 1)
    #inax = inset_axes(ax_emi, width="25%", height="30%", loc='upper right')
    ax_tars = fig.add_subplot(2, 2, 2)
    
    XL_emi = [2010, 2030.5]
    XL_tars = [2016, 2037]
    YL = [42, 70]#[40, 69]
    #for axa, XL, YL in [ax_emi, [2015, 2049.5], [43, 80]], [inax, [1989, 2030], [30, 70]]:
    
    linewdth_all = 1.5
    linestyle = {'SSP1': '--', 'SSP2': '-', 'SSP3': '--', 'SSP4': ':', 'SSP5': ':'}
            
    handles = {}
    
    yr_add = .2
    
    ax_emi.set_xlim(XL_emi)
    ax_tars.set_xlim(XL_tars)
    
    for yy in np.arange(47.5, 66, 2.5):
        ax_tars.plot([2000, 2070], [yy, yy], 'k:', linewidth=.5)
    
    txt_options = []
    txt_yloc = []
    for tpe, add_x0, \
        tpe_data100, tpe_const100, tpe_blUncondi100, tpe_fao100, \
        tpe_data, tpe_const, tpe_blUncondi, tpe_fao in \
        ['type_reclass', 0, 
         ptws['reclass100'], ptws['reclass100_const'], ptws['reclass100_blUncondi'], ptws['reclass100_fao'], 
         ptws['reclass'], ptws['reclass_const'], ptws['reclass_blUncondi'], ptws['reclass_fao']], \
        ['type_main', +2, 
         ptws['main100'], ptws['main100_const'], ptws['main100_blUncondi'], ptws['main100_fao'], 
         ptws['main'], ptws['main_const'], ptws['main_blUncondi'], ptws['main_fao']]:
    
        for ssp, add_x in zip(meta.ssps.scens.short, 
            [0, 4, 8, 12, 16]):
            
            add_xx = add_x0 + add_x                
            
            colour_act = colours_ssps.loc[ssp, :].to_list()
            linewdth = linewdth_all*1.5
            
            # 100% coverage.
            txt_options += ['default']
            data_upper = tpe_data100[ssp]
            data_upper = 1e-3 * data_upper.loc[
                (data_upper.group == 'EARTH') & (data_upper.condi.isin(['unconditional', 'conditional'])) &
                (data_upper.category == cat), :].reindex(columns=years_str).max()
            
            data_lower = tpe_data100[ssp]
            data_lower = 1e-3 * data_lower.loc[
                (data_lower.group == 'EARTH') & (data_lower.condi.isin(['unconditional', 'conditional'])) &
                (data_lower.category == cat), :].reindex(columns=years_str).min()
            
            # Filled area.
            if ssp == 'SSP2':
                ax_emi.fill_between(years_int, data_upper[years_str], 
                    data_lower[years_str], color=colour_act, linewidth=linewdth, alpha=.2)
            
            # Vertical lines
            axa = ax_tars
            
            yr_plt = 2017
            
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper['2030'], data_lower['2030']],
                color=colour_act, linewidth=linewdth_all)
            
            if (ssp == 'SSP5' and tpe == 'type_reclass'):
                axa.text(yr_plt + add_xx - .2, data_upper['2030'], 'unconditional\nworst',
                    ha='right', va='top')
                axa.text(yr_plt + add_xx - .2, data_lower['2030'], 'conditional\nbest',
                    ha='right', va='bottom')
                axa.plot([yr_plt + add_xx - .1, yr_plt + add_xx + .1], 2*[data_upper['2030']], 'k', linewidth=1)
                axa.plot([yr_plt + add_xx - .1, yr_plt + add_xx + .1], 2*[data_lower['2030']], 'k', linewidth=1)
            
            if ssp == 'SSP1':
                txt_yloc += [data_upper['2030']]
            
            data_act = tpe_data100[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            # baseline for uncondi even if condi is worse than baseline
            txt_options += ['baseline uncondi']
            data_upper2030 = tpe_blUncondi100[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_blUncondi100[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_blUncondi100[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            # constant emissions after last target year
            txt_options += ['constant emi']
            data_upper2030 = tpe_const100[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_const100[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_const100[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            # FAO
            txt_options += ['LU FAO']
            data_upper2030 = tpe_fao100[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_fao100[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_fao100[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            # estimated coverage
            txt_options += ['default (*)']
            data_upper2030 = tpe_data[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_data[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add + .2
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_data[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            # estimated coverage: lines.
            data_upper = tpe_data[ssp]
            data_upper = 1e-3 * data_upper.loc[
                (data_upper.group == 'EARTH') & (data_upper.condi.isin(['unconditional', 'conditional'])) &
                (data_upper.category == cat), :].reindex(columns=years_str).max()
            
            data_lower = tpe_data[ssp]
            data_lower = 1e-3 * data_lower.loc[
                (data_lower.group == 'EARTH') & (data_lower.condi.isin(['unconditional', 'conditional'])) &
                (data_lower.category == cat), :].reindex(columns=years_str).min()
            
            # Filled area.
            if ssp == 'SSP2':
                ax_emi.fill_between(years_int, data_upper[years_str], 
                    data_lower[years_str], color=colour_act, linewidth=linewdth, alpha=.2)
            
            if (ssp == 'SSP5' and tpe == 'type_reclass'):
                axa.text(yr_plt + add_xx, data_act.values.min()-.2, "1", ha='center', va='top', fontsize=6)
            
            # baseline for uncondi even if condi is worse than baseline
            txt_options += ['baseline uncondi (*)']
            data_upper2030 = tpe_blUncondi[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_blUncondi[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_blUncondi[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            if (ssp == 'SSP5' and tpe == 'type_reclass'):
                axa.text(yr_plt + add_xx, data_act.values.max()+.1, "2", ha='center', va='bottom', fontsize=6)
            
            # constant emissions after last target year
            txt_options += ['constant emi (*)']
            data_upper2030 = tpe_const[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_const[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_const[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            if (ssp == 'SSP5' and tpe == 'type_reclass'):
                axa.text(yr_plt + add_xx, data_act.values.min()-.2, "3", ha='center', va='top', fontsize=6)
            
            # FAO
            txt_options += ['LU FAO (*)']
            data_upper2030 = tpe_fao[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_fao[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_fao[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            if (ssp == 'SSP5' and tpe == 'type_reclass'):
                axa.text(yr_plt + add_xx, data_act.values.max()+.1, "4", ha='center', va='bottom', fontsize=6)
            
            # BAU
            data = tpe_data[ssp]
            data = 1e-3 * data.loc[
                (data.group == 'EARTH') & (data.condi == 'emi_bau') & (data.category == cat), :]. \
                reindex(columns=years_str).values[0]
            handles[ssp], = ax_emi.plot(years_int, data, color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp])
    
    for axa, txt, XL in [ax_emi, '(a) Baseline emissions', XL_emi], [ax_tars, '(b) Target emissions (2030)', XL_tars]:
        
        axa.set_ylim(YL)
        axa.yaxis.set_ticks(range(45, 70, 5))
        axa.text(XL[0] + .05*np.diff(XL), YL[1] - .05*np.diff(YL), 
            txt, fontweight='bold', ha='left', va='top')
        
        if axa == ax_emi:
            axa.text(XL[0] + .05*np.diff(XL), YL[1] - .1*np.diff(YL), 
                'upper lines: prio NDCs (for type_reclass)\nlower lines: prio SSPs (for type_main)', ha='left', va='top')
        if axa == ax_tars:            
            # text for prio NDCs / prio SSPs.
            axa.text(2017.8, txt_yloc[0] + .02*np.diff(YL), 'prio NDCs\ntype_reclass', 
                rotation=90, ha='center', va='bottom')
            axa.text(2019.8, txt_yloc[1] + .02*np.diff(YL), 'prio SSPs\ntype_main', 
                rotation=90, ha='center', va='bottom')
            # text for 100\% cov, estimated cov.
            axa.text(2017.4, YL[0] + .01*np.diff(YL), '100% cov.', 
                rotation=90, ha='center', va='bottom')
            axa.text(2018.4, YL[0] + .01*np.diff(YL), 'estim. cov.', 
                rotation=90, ha='center', va='bottom')
            axa.text(2019.4, YL[0] + .01*np.diff(YL), '100% cov.', 
                rotation=90, ha='center', va='bottom')
            axa.text(2020.4, YL[0] + .01*np.diff(YL), 'estim. cov.', 
                rotation=90, ha='center', va='bottom')
            axa.plot([2016.8, 2016.8], [42, 65], 'k:', linewidth=.7)
            axa.plot([2017.8, 2017.8], [42, 57.5], 'k:', linewidth=.7)
            axa.plot([2018.8, 2018.8], [42, 65], 'k:', linewidth=.7)
            axa.plot([2019.8, 2019.8], [42, 55], 'k:', linewidth=.7)
            axa.plot([2020.8, 2020.8], [42, 65], 'k:', linewidth=.7)
    
        axa.set_ylabel('emissions / Gt CO$_2$eq AR4', fontweight='bold')
    
    ssps_legend = meta.ssps.scens.short
    ax_emi.legend([handles[xx] for xx in ssps_legend], [f"dm{xx}" for xx in ssps_legend], loc='center left', bbox_to_anchor=(0, .55))
    
    ax_emi.set_xlabel('year', fontweight='bold')
    ax_tars.xaxis.set_ticks(np.arange(2018.75, 2036, 4))
    ax_tars.set_xticklabels([f"dm{xx}" for xx in ssp1_5])
    ax_tars.yaxis.set_ticks_position('both')
    
    # Different options:
    ax_tars.text(XL[1] - .01*np.diff(XL), YL[0] + .01*np.diff(YL), 
        f"Quadruples:\n(1) {txt_options[0]}\n(2) {txt_options[1]}\n(3) {txt_options[2]}\n(4) {txt_options[3]}",
        ha='right', va='bottom')
    
    ax_emi.xaxis.set_ticks(range(2010, 2032, 5))
    
    ###
    linestyle = {'SSP1BLIMAGE': '--', 'SSP2BLMESGB': '-', 'SSP3BLAIMCGE': '--', 'SSP4BLGCAM4': ':', 'SSP5BLREMMP': ':'}
    
    ax_pop = fig.add_subplot(2, 2, 3)
    ax_gdp = fig.add_subplot(2, 2, 4)
    #inax_pop = inset_axes(ax_pop, loc='upper left', width="100%", height="100%", bbox_to_anchor=(.1, .5, .4, .5), bbox_transform=ax_pop.transAxes)
    #inax_gdp = inset_axes(ax_gdp, loc='upper left', width="100%", height="100%", bbox_to_anchor=(.1, .5, .4, .5), bbox_transform=ax_gdp.transAxes)
    
    years = range(1990, 2031)
    
    ssps = meta.ssps.scens.long
    colours_ssps = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
        'colours', 'colours_ssps.csv'), index_col=0)
    
    ax_p = ax_pop
    ax_g = ax_gdp
    XL = XL_emi
    YL_p = [6.8e9, 8.75e9]
    YL_g = [80e12, 220e12]
    #for ax_p, ax_g, XL, YL_p, YL_g in ax_pop, ax_gdp, [2015, 2031], [7.25e9, 8.75e9], [100e12, 220e12]:
        # [inax_pop, inax_gdp, [1989, 2031], [0, 8.75e9], [0, 220e12]]:
        
    for ssp, count, add_x in zip(ssps + [ssps[1]], range(len(ssps + [ssps[1]])), [-.2, -.1, 0, .1, .2]):
        
        linewdth = linewdth_all*1.5
        colour_act = colours_ssps.loc[ssp, :].to_list()
        
        ax_p.plot(pop_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
            color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp], label=(f"dm{ssp}" if count != 5 else '__nolegend__'))
        
        ax_g.plot(gdp_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
            color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp], label=(f"dm{ssp}" if count != 5 else '__nolegend__'))
    
    if ax_p == ax_pop:
        
        ax_p.set_xlabel('year', fontweight='bold')
        ax_g.set_xlabel('year', fontweight='bold')
        ax_p.set_ylabel('population / Pers', fontweight='bold')
        ax_g.set_ylabel('GDP (PPP) / 2011 GK$', fontweight='bold')
                    
        for axa, txt, YL in zip([ax_p, ax_g], ['(c) Population', '(d) GDP (PPP)'], [YL_p, YL_g]):
            
            axa.xaxis.set_ticks(range(2010, 2031, 5))
            axa.yaxis.set_ticks_position('both')
            axa.text(XL[0] + .05*np.diff(XL), YL[1] - .05*np.diff(YL), txt, fontweight='bold', ha='left', va='top')
            axa.set_xlim(XL)
            axa.set_ylim(YL)
    
    hpf.set_ticks_scientific_notation(ax_p, 'y')
    hpf.set_ticks_scientific_notation(ax_g, 'y')
    
    ax_p.set_xlim(XL)
    ax_g.set_xlim(XL)
    
    if annotate:
        axa.text(XL[0], YL[0] - .22*np.diff(YL), annotation + 
            "\n'100% coverage': assumed 100% coverage for all countries. 'estimated coverage': quantifications with estimated coverages shown for 2030." +
            "\n'constant emi': quantification with constant emissions after the last target year (no GHG-target: baseline emissions; with '100% coverage')." +
            "\n'baseline uncondi': baseline emissions used as unconditional pathway even if it is better than the conditional pathway (with '100% coverage')." +
            "\n'LU FAO': LULUCF data prioritising FAO as first data source (with '100% coverage').", 
            fontsize=8, ha='left', va='top')
    
    #fig.subplots_adjust(left=.1, right=.9)
    plt.savefig(path_to_plot, dpi=300)
    path_to_pdf = str(path_to_plot).replace('.png', '.pdf')
    plt.savefig(path_to_pdf, dpi=300)
    hpf.crop_pdf(path_to_pdf)
    plt.clf()
    plt.close(fig)

# %%
meta = setup_metadata()

# %%

folders_reclass = [
 'ndcs_20201122_1037_SSP1_typeReclass',
 'ndcs_20201122_1114_SSP2_typeReclass',
 'ndcs_20201122_1154_SSP3_typeReclass',
 'ndcs_20201122_1221_SSP4_typeReclass',
 'ndcs_20201122_1312_SSP5_typeReclass']
folders_reclass100 = [
 'ndcs_20201122_1044_SSP1_typeReclass_pccov100',
 'ndcs_20201122_1122_SSP2_typeReclass_pccov100',
 'ndcs_20201122_1208_SSP3_typeReclass_pccov100',
 'ndcs_20201122_1230_SSP4_typeReclass_pccov100',
 'ndcs_20201122_1322_SSP5_typeReclass_pccov100']

folders_main = [
 'ndcs_20201122_1013_SSP1_typeMain',
 'ndcs_20201122_1054_SSP2_typeMain',
 'ndcs_20201122_1131_SSP3_typeMain',
 'ndcs_20201122_1237_SSP4_typeMain',
 'ndcs_20201122_1254_SSP5_typeMain']
folders_main100 = [
 'ndcs_20201122_1029_SSP1_typeMain_pccov100',
 'ndcs_20201122_1103_SSP2_typeMain_pccov100',
 'ndcs_20201122_1141_SSP3_typeMain_pccov100',
 'ndcs_20201122_1245_SSP4_typeMain_pccov100',
 'ndcs_20201122_1303_SSP5_typeMain_pccov100']

folders_reclass_constant_path = [
 'ndcs_20201122_1043_SSP1_typeReclass_constEmiAfterLastTar',
 'ndcs_20201122_1120_SSP2_typeReclass_constEmiAfterLastTar',
 'ndcs_20201122_1206_SSP3_typeReclass_constEmiAfterLastTar',
 'ndcs_20201122_1228_SSP4_typeReclass_constEmiAfterLastTar',
 'ndcs_20201122_1320_SSP5_typeReclass_constEmiAfterLastTar']
folders_reclass100_constant_path = [
 'ndcs_20201122_1052_SSP1_typeReclass_pccov100_constEmiAfterLastTar',
 'ndcs_20201122_1130_SSP2_typeReclass_pccov100_constEmiAfterLastTar',
 'ndcs_20201122_1220_SSP3_typeReclass_pccov100_constEmiAfterLastTar',
 'ndcs_20201122_1236_SSP4_typeReclass_pccov100_constEmiAfterLastTar',
 'ndcs_20201122_1331_SSP5_typeReclass_pccov100_constEmiAfterLastTar']

folders_main_constant_path = [
 'ndcs_20201122_1028_SSP1_typeMain_constEmiAfterLastTar',
 'ndcs_20201122_1102_SSP2_typeMain_constEmiAfterLastTar',
 'ndcs_20201122_1139_SSP3_typeMain_constEmiAfterLastTar',
 'ndcs_20201122_1244_SSP4_typeMain_constEmiAfterLastTar',
 'ndcs_20201122_1301_SSP5_typeMain_constEmiAfterLastTar']
folders_main100_constant_path = [
 'ndcs_20201122_1035_SSP1_typeMain_pccov100_constEmiAfterLastTar',
 'ndcs_20201122_1112_SSP2_typeMain_pccov100_constEmiAfterLastTar',
 'ndcs_20201122_1151_SSP3_typeMain_pccov100_constEmiAfterLastTar',
 'ndcs_20201122_1252_SSP4_typeMain_pccov100_constEmiAfterLastTar',
 'ndcs_20201122_1310_SSP5_typeMain_pccov100_constEmiAfterLastTar']

folders_reclass_baselineUncondi = [
 'ndcs_20201122_1041_SSP1_typeReclass_BLForUCAboveBL',
 'ndcs_20201122_1119_SSP2_typeReclass_BLForUCAboveBL',
 'ndcs_20201122_1203_SSP3_typeReclass_BLForUCAboveBL',
 'ndcs_20201122_1227_SSP4_typeReclass_BLForUCAboveBL',
 'ndcs_20201122_1318_SSP5_typeReclass_BLForUCAboveBL']
folders_reclass100_baselineUncondi = [
 'ndcs_20201122_1050_SSP1_typeReclass_pccov100_BLForUCAboveBL',
 'ndcs_20201122_1128_SSP2_typeReclass_pccov100_BLForUCAboveBL',
 'ndcs_20201122_1217_SSP3_typeReclass_pccov100_BLForUCAboveBL',
 'ndcs_20201122_1234_SSP4_typeReclass_pccov100_BLForUCAboveBL',
 'ndcs_20201122_1329_SSP5_typeReclass_pccov100_BLForUCAboveBL']

folders_main_baselineUncondi = [
 'ndcs_20201122_1026_SSP1_typeMain_BLForUCAboveBL',
 'ndcs_20201122_1100_SSP2_typeMain_BLForUCAboveBL',
 'ndcs_20201122_1137_SSP3_typeMain_BLForUCAboveBL',
 'ndcs_20201122_1242_SSP4_typeMain_BLForUCAboveBL',
 'ndcs_20201122_1259_SSP5_typeMain_BLForUCAboveBL']
folders_main100_baselineUncondi = [
 'ndcs_20201122_1033_SSP1_typeMain_pccov100_BLForUCAboveBL',
 'ndcs_20201122_1110_SSP2_typeMain_pccov100_BLForUCAboveBL',
 'ndcs_20201122_1148_SSP3_typeMain_pccov100_BLForUCAboveBL',
 'ndcs_20201122_1251_SSP4_typeMain_pccov100_BLForUCAboveBL',
 'ndcs_20201122_1308_SSP5_typeMain_pccov100_BLForUCAboveBL']

folders_reclass_fao = [
 'ndcs_20201122_1037_SSP1_typeReclass_FAO',
 'ndcs_20201122_1114_SSP2_typeReclass_FAO',
 'ndcs_20201122_1154_SSP3_typeReclass_FAO',
 'ndcs_20201122_1221_SSP4_typeReclass_FAO',
 'ndcs_20201122_1312_SSP5_typeReclass_FAO']
folders_reclass100_fao = [
 'ndcs_20201122_1044_SSP1_typeReclass_pccov100_FAO',
 'ndcs_20201122_1122_SSP2_typeReclass_pccov100_FAO',
 'ndcs_20201122_1208_SSP3_typeReclass_pccov100_FAO',
 'ndcs_20201122_1230_SSP4_typeReclass_pccov100_FAO',
 'ndcs_20201122_1322_SSP5_typeReclass_pccov100_FAO']

folders_main_fao = [
 'ndcs_20201122_1013_SSP1_typeMain_FAO',
 'ndcs_20201122_1054_SSP2_typeMain_FAO',
 'ndcs_20201122_1131_SSP3_typeMain_FAO',
 'ndcs_20201122_1237_SSP4_typeMain_FAO',
 'ndcs_20201122_1254_SSP5_typeMain_FAO']
folders_main100_fao = [
 'ndcs_20201122_1029_SSP1_typeMain_pccov100_FAO',
 'ndcs_20201122_1103_SSP2_typeMain_pccov100_FAO',
 'ndcs_20201122_1141_SSP3_typeMain_pccov100_FAO',
 'ndcs_20201122_1245_SSP4_typeMain_pccov100_FAO',
 'ndcs_20201122_1303_SSP5_typeMain_pccov100_FAO']

# %%
annotation = 'Baseline emissions (SSP1 to SSP5 marker scenarios): solid lines.' + \
    '\nShaded area: worst and best pathways for SSP2.'

cat = 'IPCM0EL'

pop_filled = {}
gdp_filled = {}

for ssp in meta.ssps.scens.long:
    
    pop_filled[ssp] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f'POP_DEMOGR_TOTAL_NET_{ssp}FILLED_PMSSPBIEMISC.csv'))
    
    gdp_filled[ssp] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f'GDPPPP_ECO_TOTAL_NET_{ssp}FILLED_PMSSPBIEMISC.csv'))

annotate = False
numbers_diff = True

path_to_plot = Path(meta.path.main, 'plots', 'ndc_quantifications', 
    'comparison_of_ssps', f'ndcs_comparison_ssps_prioReclassAndMain_{cat}_onePlot_diff.png')

plotting()

# %%
