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
    
    ptws = {}
    for what in ['calc', 'orig', 'calc_const', 'orig_const',
                 'calc_blUncondi', 'orig_blUncondi', 'calc_fao', 'orig_fao',
                 'calc_unfccc', 'orig_unfccc']:
        ptws[what] = {}
    
    ssp1_4 = ['SSP1', 'SSP2', 'SSP3', 'SSP4']
    ssp1_5 = ssp1_4 + ['SSP5']
    
    tars_all = {}
    condi_rge = ['unconditional', 'worst'], ['unconditional', 'best'], \
        ['conditional', 'worst'], ['conditional', 'best']
    for condi, rge in condi_rge:
        tars_all[f"{condi}_{rge}"] = pd.DataFrame(columns=ssp1_5, dtype='float64')
    
    for folder, folder100, ssps in zip(folders_calc, folders_calc100, meta.ssps.scens.short):
        
        ptws['calc'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        ptws['calc'][f"{ssps}_100pc"] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder100, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['calc'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['calc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
                
        data = ptws['calc'][f"{ssps}_100pc"]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['calc_100pc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for folder, folder100, ssps in zip(folders_orig, folders_orig100, meta.ssps.scens.short):
        
        ptws['orig'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        ptws['orig'][f"{ssps}_100pc"] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder100, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['orig'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['orig', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
        
        data = ptws['orig'][f"{ssps}_100pc"]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['orig_100pc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for ssps in meta.ssps.scens.short:
        
        diff = ptws['calc'][ssps].loc[(ptws['calc'][ssps].group == 'EARTH') & (ptws['calc'][ssps].condi == 'emi_bau'), '2030'].values[0] - \
            ptws['orig'][ssps].loc[(ptws['orig'][ssps].group == 'EARTH') & (ptws['orig'][ssps].condi == 'emi_bau'), '2030'].values[0]
        print(f"% Difference between bau for calc and orig {ssps}: {diff/1000 :+.1f} Gt CO2eq_AR4.")
        diff = ptws['calc'][f"{ssps}_100pc"].loc[(ptws['calc'][f"{ssps}_100pc"].group == 'EARTH') & (ptws['calc'][f"{ssps}_100pc"].condi == 'emi_bau'), '2030'].values[0] - \
            ptws['orig'][f"{ssps}_100pc"].loc[(ptws['orig'][f"{ssps}_100pc"].group == 'EARTH') & (ptws['orig'][f"{ssps}_100pc"].condi == 'emi_bau'), '2030'].values[0]
        print(f"% Difference between bau for calc_100% and orig_100% {ssps}: {diff/1000 :+.1f} Gt CO2eq_AR4.")
    
    for folder, ssps in zip(folders_calc_constant_path, meta.ssps.scens.short):
        
        ptws['calc_const'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['calc_const'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['calc_const', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()

    
    for folder, ssps in zip(folders_orig_constant_path, meta.ssps.scens.short):
        
        ptws['orig_const'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['orig_const'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['orig_const', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for folder, ssps in zip(folders_calc_baselineUncondi, meta.ssps.scens.short):
        
        ptws['calc_blUncondi'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['calc_blUncondi'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['calc_blUncondi', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for folder, ssps in zip(folders_orig_baselineUncondi, meta.ssps.scens.short):
        
        ptws['orig_blUncondi'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['orig_blUncondi'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['orig_blUncondi', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for folder, ssps in zip(folders_calc_fao, meta.ssps.scens.short):
        
        ptws['calc_fao'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['calc_fao'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['calc_fao', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for folder, ssps in zip(folders_calc_unfccc, meta.ssps.scens.short):
        
        ptws['calc_unfccc'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['calc_unfccc'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['calc_unfccc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for folder, ssps in zip(folders_orig_fao, meta.ssps.scens.short):
        
        ptws['orig_fao'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['orig_fao'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['orig_fao', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    for folder, ssps in zip(folders_orig_unfccc, meta.ssps.scens.short):
        
        ptws['orig_unfccc'][ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        data = ptws['orig_unfccc'][ssps]
        for condi, rge in condi_rge:
            tars_all[f"{condi}_{rge}"].loc['orig_unfccc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), '2030'].max()
    
    diff_med = (tars_all['unconditional_worst']-tars_all['conditional_best'])*1e-3
    [print(f"% Difference between uncondi worst & condi best: min/max for the different options, for {xx}: " +
           f"{diff_med.loc[:, xx].min() :.1f} to {diff_med.loc[:, xx].max() :.1f} Gt CO2eq AR4") for xx in tars_all['unconditional_worst'].columns]
    
    print("\nDifference between the default 100% runs with LULUCF prio CRF, and with FAO:")
    for ssp in tars_all['unconditional_worst'].columns:
        print(f"type_calc ({ssp}): " +
            f"unconditional worst {1e-3*(tars_all['unconditional_worst'].loc['calc_100pc', ssp] - tars_all['unconditional_worst'].loc['calc_fao', ssp]) :.1f}; " +
            f"conditional best {1e-3*(tars_all['conditional_best'].loc['calc_100pc', ssp] - tars_all['conditional_best'].loc['calc_fao', ssp]) :.1f} Gt CO2eq")
        print(f"type_orig ({ssp}): " +
            f"unconditional worst {1e-3*(tars_all['unconditional_worst'].loc['orig_100pc', ssp] - tars_all['unconditional_worst'].loc['orig_fao', ssp]) :.1f}; " +
            f"conditional best {1e-3*(tars_all['conditional_best'].loc['orig_100pc', ssp] - tars_all['conditional_best'].loc['orig_fao', ssp]) :.1f} Gt CO2eq")
    
    rge_SSP2 = np.percentile(1e-3*(tars_all['unconditional_worst'].loc[:, 'SSP2'] - tars_all['conditional_best'].loc[:, 'SSP2']), [10, 50, 90])
    rge_SSP1to4 = np.percentile(1e-3*(tars_all['unconditional_worst'].loc[:, ssp1_4] - tars_all['conditional_best'].loc[:, ssp1_4]), [10, 50, 90])
    print(f"\n% Range for SSP2 (10, 50, 90%): {rge_SSP2} Gt CO2eq")
    print(f"% Range for SSP1-4 (10, 50, 90%): {rge_SSP1to4} Gt CO2eq")
    
    print(f"\n% Range of unconditional worst (SSP1-4, 10, 50, 90%): {np.percentile(tars_all['unconditional_worst'].loc[:, ssp1_4]/1000, [10, 50, 90])} Gt CO2 eq")
    print(f"% Range of unconditional best (SSP1-4, 10, 50, 90%): {np.percentile(tars_all['unconditional_best'].loc[:, ssp1_4]/1000, [10, 50, 90])} Gt CO2 eq")
    print(f"% Range of conditional worst (SSP1-4, 10, 50, 90%): {np.percentile(tars_all['conditional_worst'].loc[:, ssp1_4]/1000, [10, 50, 90])} Gt CO2 eq")
    print(f"% Range of conditional best (SSP1-4, 10, 50, 90%): {np.percentile(tars_all['conditional_best'].loc[:, ssp1_4]/1000, [10, 50, 90])} Gt CO2 eq")
    
    tars_SSP1to4 = np.percentile((tars_all['unconditional_worst'].loc[:, ssp1_4].values,
                                  tars_all['conditional_best'].loc[:, ssp1_4].values), [10, 50, 90])/1000
    print(f"\n% Range of SSP1-4 quantifications (uncondi worst and condi best): {tars_SSP1to4} Gt CO2 eq")
    
    rge_condi_SSP1to4 = np.percentile(tars_all['unconditional_worst'].loc[:, ssp1_4].add(
        -tars_all['conditional_best'].loc[:, ssp1_4]).values, [10, 50, 90])/1000
    print(f"\n% Range between unconditional worst and conditional best targets (SSP1-4, 10, 50, 90%): {rge_condi_SSP1to4} Gt CO2eq")
   
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
    YL = [43, 70]#[40, 69]
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
    for tpe, tpe_data, add_x0, tpe_const, tpe_blUncondi, tpe_unfccc, tpe_fao in \
        ['type_calc', ptws['calc'], 0, ptws['calc_const'], ptws['calc_blUncondi'], ptws['calc_unfccc'], ptws['calc_fao']], \
        ['type_orig', ptws['orig'], +2, ptws['orig_const'], ptws['orig_blUncondi'], ptws['orig_unfccc'], ptws['orig_fao']]:
    
        for ssp, add_x in zip(meta.ssps.scens.short, 
            [0, 4, 8, 12, 16]):
            
            add_xx = add_x0 + add_x
            
            colour_act = colours_ssps.loc[ssp, :].to_list()
            linewdth = linewdth_all*1.5
            
            # 100% coverage.
            txt_options += ['100% coverage']
            data_upper = tpe_data[f"{ssp}_100pc"]
            data_upper = 1e-3 * data_upper.loc[
                (data_upper.group == 'EARTH') & (data_upper.condi.isin(['unconditional', 'conditional'])) &
                (data_upper.category == cat), :].reindex(columns=years_str).max()
            
            data_lower = tpe_data[f"{ssp}_100pc"]
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
            if (ssp == 'SSP5' and tpe == 'type_calc'):
                axa.text(yr_plt + add_xx - .2, data_upper['2030'], 'unconditional\nworst', fontweight='bold',
                    ha='right', va='top')
                axa.text(yr_plt + add_xx - .2, data_lower['2030'], 'conditional\nbest', fontweight='bold',
                    ha='right', va='bottom')
                axa.plot([yr_plt + add_xx - .1, yr_plt + add_xx + .1], 2*[data_upper['2030']], 'k', linewidth=1)
                axa.plot([yr_plt + add_xx - .1, yr_plt + add_xx + .1], 2*[data_lower['2030']], 'k', linewidth=1)
            
            if ssp == 'SSP1':
                txt_yloc += [data_upper['2030']]
            
            data_act = tpe_data[f"{ssp}_100pc"]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            # UNFCCC
            txt_options += ['LULUCF UNFCCC']
            data_upper2030 = tpe_unfccc[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_unfccc[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_unfccc[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
            # FAO
            txt_options += ['LULUCF FAO']
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
            
            # baseline for uncondi even if condi is worse than baseline
            txt_options += ['baseline uncondi']
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
            
            # constant emissions after last target year
            txt_options += ['constant emi']
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
            
            # estimated coverage
            txt_options += ['estimated coverage (*)']
            data_upper2030 = tpe_data[ssp]
            data_upper2030 = 1e-3 * data_upper2030.loc[
                (data_upper2030.group == 'EARTH') & (data_upper2030.condi.isin(['unconditional', 'conditional'])) &
                (data_upper2030.category == cat), '2030'].max()
            
            data_lower2030 = tpe_data[ssp]
            data_lower2030 = 1e-3 * data_lower2030.loc[
                (data_lower2030.group == 'EARTH') & (data_lower2030.condi.isin(['unconditional', 'conditional'])) &
                (data_lower2030.category == cat), '2030'].min()
            
            yr_plt += yr_add
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper2030, data_lower2030], color=colour_act, linewidth=linewdth_all)
            
            data_act = tpe_data[ssp]
            data_act = 1e-3 * data_act.loc[
                (data_act.group == 'EARTH') & (data_act.condi.isin(['unconditional', 'conditional'])) &
                (data_act.category == cat), '2030']
            axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
            
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
            axa.text(2017.55, txt_yloc[0] + .02*np.diff(YL), 'prio NDCs\ntype_reclass', 
                rotation=90, ha='center', va='bottom', fontweight='bold')
            axa.text(2019.4, txt_yloc[1] + .02*np.diff(YL), 'prio SSPs\ntype_main', 
                rotation=90, ha='center', va='bottom', fontweight='bold')
    
        axa.set_ylabel('emissions / Gt CO$_2$eq AR4', fontweight='bold')
    
    ssps_legend = meta.ssps.scens.short
    ax_emi.legend([handles[xx] for xx in ssps_legend], ssps_legend, loc='center left', bbox_to_anchor=(0, .55))
    
    ax_emi.set_xlabel('year', fontweight='bold')
    ax_tars.xaxis.set_ticks(np.arange(2018.55, 2036, 4))
    ax_tars.set_xticklabels(ssp1_5)
    ax_tars.yaxis.set_ticks_position('both')
    
    txt_y = YL[0] + .02*np.diff(YL)
    yr_txt = 2032.3
    for txt in txt_options[:6]:
        yr_txt += .7
        ax_tars.text(yr_txt, txt_y, txt, rotation=90, ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax_emi.xaxis.set_ticks(range(2010, 2031, 5))
    
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
            color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp], label=(ssp if count != 5 else '__nolegend__'))
        
        ax_g.plot(gdp_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
            color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp], label=(ssp if count != 5 else '__nolegend__'))
    
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
            "\n'LULUCF UNFCCC & FAO': LULUCF data prioritising UNFCCC or FAO as first data source (with '100% coverage').", 
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

folders_calc = [
    'ndcs_20200628_2218_SSP1_typeCalc',
    'ndcs_20200628_2120_SSP2_typeCalc',
    'ndcs_20200628_2229_SSP3_typeCalc',
    'ndcs_20200628_2243_SSP4_typeCalc',
    'ndcs_20200628_2258_SSP5_typeCalc']
folders_calc100 = [
    'ndcs_20200628_2221_SSP1_typeCalc_pccov100',
    'ndcs_20200628_2122_SSP2_typeCalc_pccov100',
    'ndcs_20200628_2234_SSP3_typeCalc_pccov100',
    'ndcs_20200628_2248_SSP4_typeCalc_pccov100',
    'ndcs_20200628_2301_SSP5_typeCalc_pccov100']

folders_orig = [
    'ndcs_20200702_0834_SSP1_typeOrig',
    'ndcs_20200702_0829_SSP2_typeOrig',
    'ndcs_20200702_0839_SSP3_typeOrig',
    'ndcs_20200702_0844_SSP4_typeOrig',
    'ndcs_20200702_0848_SSP5_typeOrig']
folders_orig100 = [
    'ndcs_20200702_0836_SSP1_typeOrig_pccov100',
    'ndcs_20200702_0830_SSP2_typeOrig_pccov100',
    'ndcs_20200702_0840_SSP3_typeOrig_pccov100',
    'ndcs_20200702_0845_SSP4_typeOrig_pccov100',
    'ndcs_20200702_0849_SSP5_typeOrig_pccov100']

folders_calc_constant_path = [
    'ndcs_20200628_2225_SSP1_typeCalc_pccov100_constEmiAfterLastTar',
    'ndcs_20200628_2125_SSP2_typeCalc_pccov100_constEmiAfterLastTar',
    'ndcs_20200628_2238_SSP3_typeCalc_pccov100_constEmiAfterLastTar',
    'ndcs_20200628_2253_SSP4_typeCalc_pccov100_constEmiAfterLastTar',
    'ndcs_20200628_2304_SSP5_typeCalc_pccov100_constEmiAfterLastTar']
folders_orig_constant_path = [
    'ndcs_20200702_0837_SSP1_typeOrig_pccov100_constEmiAfterLastTar',
    'ndcs_20200702_0831_SSP2_typeOrig_pccov100_constEmiAfterLastTar',
    'ndcs_20200702_0841_SSP3_typeOrig_pccov100_constEmiAfterLastTar',
    'ndcs_20200702_0846_SSP4_typeOrig_pccov100_constEmiAfterLastTar',
    'ndcs_20200702_0850_SSP5_typeOrig_pccov100_constEmiAfterLastTar']

folders_calc_baselineUncondi = [
    'ndcs_20200628_2227_SSP1_typeCalc_pccov100_BLForUCAboveBL',
    'ndcs_20200628_2126_SSP2_typeCalc_pccov100_BLForUCAboveBL',
    'ndcs_20200628_2241_SSP3_typeCalc_pccov100_BLForUCAboveBL',
    'ndcs_20200628_2255_SSP4_typeCalc_pccov100_BLForUCAboveBL',
    'ndcs_20200628_2306_SSP5_typeCalc_pccov100_BLForUCAboveBL']
folders_orig_baselineUncondi = [
    'ndcs_20200702_0838_SSP1_typeOrig_pccov100_BLForUCAboveBL',
    'ndcs_20200702_0832_SSP2_typeOrig_pccov100_BLForUCAboveBL',
    'ndcs_20200702_0843_SSP3_typeOrig_pccov100_BLForUCAboveBL',
    'ndcs_20200702_0847_SSP4_typeOrig_pccov100_BLForUCAboveBL',
    'ndcs_20200702_0852_SSP5_typeOrig_pccov100_BLForUCAboveBL']

folders_calc_unfccc = [
    'ndcs_20200706_1234_SSP1_typeCalc_pccov100_UNFCCC',
    'ndcs_20200706_1226_SSP2_typeCalc_pccov100_UNFCCC',
    'ndcs_20200706_1241_SSP3_typeCalc_pccov100_UNFCCC',
    'ndcs_20200706_1249_SSP4_typeCalc_pccov100_UNFCCC',
    'ndcs_20200706_1257_SSP5_typeCalc_pccov100_UNFCCC']
folders_orig_unfccc = [
    'ndcs_20200706_1236_SSP1_typeOrig_pccov100_UNFCCC',
    'ndcs_20200706_1228_SSP2_typeOrig_pccov100_UNFCCC',
    'ndcs_20200706_1243_SSP3_typeOrig_pccov100_UNFCCC',
    'ndcs_20200706_1251_SSP4_typeOrig_pccov100_UNFCCC',
    'ndcs_20200706_1259_SSP5_typeOrig_pccov100_UNFCCC']

folders_calc_fao = [
    'ndcs_20200706_1234_SSP1_typeCalc_pccov100_FAO',
    'ndcs_20200706_1226_SSP2_typeCalc_pccov100_FAO',
    'ndcs_20200706_1241_SSP3_typeCalc_pccov100_FAO',
    'ndcs_20200706_1249_SSP4_typeCalc_pccov100_FAO',
    'ndcs_20200706_1257_SSP5_typeCalc_pccov100_FAO']
folders_orig_fao = [
    'ndcs_20200706_1236_SSP1_typeOrig_pccov100_FAO',
    'ndcs_20200706_1228_SSP2_typeOrig_pccov100_FAO',
    'ndcs_20200706_1243_SSP3_typeOrig_pccov100_FAO',
    'ndcs_20200706_1251_SSP4_typeOrig_pccov100_FAO',
    'ndcs_20200706_1259_SSP5_typeOrig_pccov100_FAO']

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
    'comparison_of_ssps', f'ndcs_comparison_ssps_prioCalcAndOrig_{cat}_onePlot_diff3.png')

plotting()

# %%
