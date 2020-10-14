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
def plotting_together_types_onePlot_diff():
    
    # Get data.
    ptws_calc = {}
    ptws_orig = {}
    ptws_calc_const = {}
    ptws_orig_const = {}
    ptws_calc_blUncondi= {}
    ptws_orig_blUncondi= {}
    ptws_calc_fao = {}
    ptws_orig_fao = {}
    ptws_calc_unfccc = {}
    ptws_orig_unfccc = {}
    
    median_upper = pd.DataFrame(columns=['SSP1', 'SSP2', 'SSP3', 'SSP4'], dtype='float64')
    median_lower = pd.DataFrame(columns=['SSP1', 'SSP2', 'SSP3', 'SSP4'], dtype='float64')
    
    for folder, folder100, ssps in zip(folders_calc, folders_calc100, meta.ssps.scens.short):
        
        ptws_calc[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        ptws_calc[f"{ssps}_100pc"] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder100, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_calc[ssps]
            median_upper.loc['calc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['calc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
            data = ptws_calc[f"{ssps}_100pc"]
            median_upper.loc['calc_100pc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['calc_100pc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for folder, folder100, ssps in zip(folders_orig, folders_orig100, meta.ssps.scens.short):
        
        ptws_orig[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        ptws_orig[f"{ssps}_100pc"] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder100, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_orig[ssps]
            median_upper.loc['orig', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['orig', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
            data = ptws_orig[f"{ssps}_100pc"]
            median_upper.loc['orig_100pc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['orig_100pc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for ssps in meta.ssps.scens.short:
        
        diff = ptws_calc[ssps].loc[(ptws_calc[ssps].group == 'EARTH') & (ptws_calc[ssps].condi == 'emi_bau'), '2030'].values[0] - \
            ptws_orig[ssps].loc[(ptws_orig[ssps].group == 'EARTH') & (ptws_orig[ssps].condi == 'emi_bau'), '2030'].values[0]
        print(f"% Difference between bau for calc and orig {ssps}: {diff/1000 :+.1f} Gt CO2eq_AR4.")
        diff = ptws_calc[f"{ssps}_100pc"].loc[(ptws_calc[f"{ssps}_100pc"].group == 'EARTH') & (ptws_calc[f"{ssps}_100pc"].condi == 'emi_bau'), '2030'].values[0] - \
            ptws_orig[f"{ssps}_100pc"].loc[(ptws_orig[f"{ssps}_100pc"].group == 'EARTH') & (ptws_orig[f"{ssps}_100pc"].condi == 'emi_bau'), '2030'].values[0]
        print(f"% Difference between bau for calc_100% and orig_100% {ssps}: {diff/1000 :+.1f} Gt CO2eq_AR4.")
    
    for folder, ssps in zip(folders_calc_constant_path, meta.ssps.scens.short):
        
        ptws_calc_const[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_calc_const[ssps]
            median_upper.loc['calc_const', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['calc_const', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for folder, ssps in zip(folders_orig_constant_path, meta.ssps.scens.short):
        
        ptws_orig_const[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_orig_const[ssps]
            median_upper.loc['orig_const', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['orig_const', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for folder, ssps in zip(folders_calc_baselineUncondi, meta.ssps.scens.short):
        
        ptws_calc_blUncondi[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_calc_blUncondi[ssps]
            median_upper.loc['calc_blUncondi', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['calc_blUncondi', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for folder, ssps in zip(folders_orig_baselineUncondi, meta.ssps.scens.short):
        
        ptws_orig_blUncondi[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_orig_blUncondi[ssps]
            median_upper.loc['orig_blUncondi', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['orig_blUncondi', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for folder, ssps in zip(folders_calc_fao, meta.ssps.scens.short):
        
        ptws_calc_fao[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_calc_fao[ssps]
            median_upper.loc['calc_fao', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['calc_fao', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for folder, ssps in zip(folders_calc_unfccc, meta.ssps.scens.short):
        
        ptws_calc_unfccc[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_calc_unfccc[ssps]
            median_upper.loc['calc_unfccc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['calc_unfccc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for folder, ssps in zip(folders_orig_fao, meta.ssps.scens.short):
        
        ptws_orig_fao[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_orig_fao[ssps]
            median_upper.loc['orig_fao', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['orig_fao', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    for folder, ssps in zip(folders_orig_unfccc, meta.ssps.scens.short):
        
        ptws_orig_unfccc[ssps] = pd.read_csv(
            Path(meta.path.output, 'output_for_paper', folder, 'ndc_targets_pathways_per_group.csv'))
        
        if ssps != 'SSP5':
            data = ptws_orig_unfccc[ssps]
            median_upper.loc['orig_unfccc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].max()
            median_lower.loc['orig_unfccc', ssps] = data.loc[(data.group == 'EARTH') & (data.condi.isin(['unconditional', 'conditional'])), '2030'].min()
    
    median_upper.loc[:, 'median'] = median_upper.median(axis=1)
    median_lower.loc[:, 'median'] = median_lower.median(axis=1)
    
    # Plotting.
    colours_ssps = pd.read_csv(
        Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 
             'colours_ssps.csv'), index_col=0)
    colours_ssps.index = [meta.ssps.scens.long_to_short[xx] for xx in colours_ssps.index]
    
    years_int = range(1990, 2031)
    years_str = [str(xx) for xx in years_int]
    
    fig = plt.figure(figsize=(10, 7))
    axa = fig.add_subplot(1, 1, 1)
    
    XL = [1989, 2049.5]
    
    linewdth_all = 1
    # linestyle = {'SSP1': '-.', 'SSP2': '-', 'SSP3': '--', 'SSP4': ':', 'SSP5': (0, (3, 5, 1, 5))}
    linestyle = {'SSP1': '--', 'SSP2': '-', 'SSP3': '--', 'SSP4': ':', 'SSP5': ':'}
    
    ylim_max = 0
    
    handles = {}
    
    yr_add = .3
    
    axa.set_xlim(XL)
    for yy in np.arange(47.5, 66, 2.5):
        axa.plot([2031, 2070], [yy, yy], 'k:', linewidth=.2)

    for tpe, tpe_data, add_x0, tpe_const, tpe_blUncondi, tpe_unfccc, tpe_fao in \
        ['type_calc', ptws_calc, 0, ptws_calc_const, ptws_calc_blUncondi, ptws_calc_unfccc, ptws_calc_fao], \
        ['type_orig', ptws_orig, +2, ptws_orig_const, ptws_orig_blUncondi, ptws_orig_unfccc, ptws_orig_fao]:
        
        for ssp, add_x in zip(meta.ssps.scens.short, 
                              [-1, 3, 7, 11, 15]):
            add_xx = add_x0 + add_x
            
            colour_act = colours_ssps.loc[ssp, :].to_list()
            linewdth = linewdth_all*1.5#(linewdth_all*1.5 if ssp == 'SSP2' else linewdth_all)
            
            # 100% coverage.
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
                axa.fill_between(years_int, data_upper[years_str], 
                    data_lower[years_str], color=colour_act, linewidth=linewdth, alpha=.2)
            
            # Vertical lines
            
            yr_plt = 2033
            axa.plot([yr_plt + add_xx, yr_plt + add_xx], [data_upper['2030'], data_lower['2030']],
                color=colour_act, linewidth=linewdth_all)
            
            # estimated coverage
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
            
            # constant emissions after last target year
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
            
            # baseline for uncondi even if condi is worse than baseline
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
            
            # UNFCCC
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
            
            # FAO
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
            
            # BAU
            data = tpe_data[ssp]
            data = 1e-3 * data.loc[
                (data.group == 'EARTH') & (data.condi == 'emi_bau') & (data.category == cat), :]. \
                reindex(columns=years_str).values[0]
            handles[ssp], = axa.plot(years_int, data, color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp])
        
        ylim_max = max([ylim_max, axa.get_ylim()[-1]])
    
    #YL = [0, ylim_max]
    YL = [axa.get_ylim()[0], ylim_max*1.1]
    
    axa.set_ylabel('emissions / Gt CO$_2$eq AR4', fontweight='bold')
    axa.xaxis.set_ticks(range(1990, 2031, 5))
    axa.yaxis.set_ticks(range(20, 90, 5))
    axa.yaxis.set_ticks_position('both')
    axa.tick_params(labeltop=False, labelright=True)
    axa.set_ylim(YL)
    axa.set_xlabel('year', fontweight='bold')
    axa.text(XL[0] + .05*np.diff(XL), YL[1] - .05*np.diff(YL), 
        '(a) Emissions', fontweight='bold', ha='left', va='top')
    axa.text(XL[0] + .05*np.diff(XL), YL[1] - .1*np.diff(YL), 
        'upper lines: prio NDCs (type_reclass)\nlower lines: prio SSPs (type_main)', ha='left', va='top')
    
    axa.text(2032.9, YL[1] - .02*np.diff(YL), 'prio NDCs', rotation=90, ha='center', va='top', fontweight='bold')
    axa.text(2034.9, YL[1] - .02*np.diff(YL), 'prio SSPs', rotation=90, ha='center', va='top', fontweight='bold')
    
    axa.plot([2031, 2031], axa.get_ylim(), 'k:', linewidth=.2)
    
    txt_y = YL[0] + .02*np.diff(YL)
    # txt_y2 = YL[1] + .1*np.diff(YL)
    # txt_y3 = YL[1] + .2*np.diff(YL)
    
    # median_default_uncondi_worst = median_upper.loc['calc_100pc', 'median']/1000
    # median_default_condi_best = median_lower.loc['calc_100pc', 'median']/1000
    
    yr_txt = 2037
    for txt in ['100% coverage', 'estimated coverage', 'constant emi', 'baseline uncondi', 'LULUCF UNFCCC', 'LULUCF FAO']:
        yr_txt += 1.5
        axa.text(yr_txt, txt_y, txt, rotation=90, ha='center', va='bottom')
    
    ssps_legend = meta.ssps.scens.short
    axa.legend([handles[xx] for xx in ssps_legend], ssps_legend, loc='center left')
    
    XL = [XL[0], XL[1] + 3]
    axa.set_xlim(XL)
    
    if annotate:
        axa.text(XL[0], YL[0] - .22*np.diff(YL), annotation + 
            "\n'100% coverage': assumed 100% coverage for all countries. 'estimated coverage': quantifications with estimated coverages shown for 2030." +
            "\n'constant emi': quantification with constant emissions after the last target year (no GHG-target: baseline emissions; with '100% coverage')." +
            "\n'baseline uncondi': baseline emissions used as unconditional pathway even if it is better than the conditional pathway (with '100% coverage')." +
            "\n'LULUCF UNFCCC & FAO': LULUCF data prioritising UNFCCC or FAO as first data source (with '100% coverage').", 
            fontsize=8, ha='left', va='top')
    
    fig.subplots_adjust(bottom=.3, left=.1, right=.9)
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

annotate = False
numbers_diff = True

path_to_plot = Path(meta.path.main, 'plots', 'ndc_quantifications', 
    'comparison_of_ssps', f'ndcs_comparison_ssps_prioCalcAndOrig_{cat}_onePlot_diff2.png')

plotting_together_types_onePlot_diff()

# %%