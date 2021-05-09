# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2021.
"""

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

# %%
pop_filled = {}
gdp_filled = {}

for ssp in meta.ssps.scens.long:
    
    pop_filled[ssp] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables_PMH21', f'POP_DEMOGR_TOTAL_NET_PMH21{ssp}FILLED_PMH21SSPBIEMISC.csv'))
    
    gdp_filled[ssp] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables_PMH21', f'GDPPPP_ECO_TOTAL_NET_PMH21{ssp}FILLED_PMH21SSPBIEMISC.csv'))
numbers_diff = True

cat = 'IPCM0EL'

ssp1_4 = ['SSP1', 'SSP2', 'SSP3', 'SSP4']
ssp1_5 = ssp1_4 + ['SSP5']

linewdth_all = 1.5
linewdth = linewdth_all*1.5

yr_add = .2

# %%
def read_emis():
    
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
        [folders_reclass_const_diff, 'reclass_constDiff'], [folders_reclass100_const_diff, 'reclass100_constDiff'], \
        [folders_main_const_diff, 'main_constDiff'], [folders_main100_const_diff, 'main100_constDiff'], \
        [folders_reclass_baselineUncondi, 'reclass_blUncondi'], [folders_reclass100_baselineUncondi, 'reclass100_blUncondi'], \
        [folders_main_baselineUncondi, 'main_blUncondi'], [folders_main100_baselineUncondi, 'main100_blUncondi'], \
        [folders_reclass_bl_tar, 'reclass_blTar'], [folders_reclass100_bl_tar, 'reclass100_blTar'], \
        [folders_main_bl_tar, 'main_blTar'], [folders_main100_bl_tar, 'main100_blTar'], \
        [folders_reclass_fao, 'reclass_fao'], [folders_reclass100_fao, 'reclass100_fao'], \
        [folders_main_fao, 'main_fao'], [folders_main100_fao, 'main100_fao'], \
        [folders_reclass_cat, 'reclass_cat'], [folders_reclass100_cat, 'reclass100_cat'], \
        [folders_main_cat, 'main_cat'], [folders_main100_cat, 'main100_cat']:
        
        ptws[what] = {}
        
        for folder, ssp in zip(folders, meta.ssps.scens.short):
            
            data = pd.read_csv(Path(path_to_output, folder, 'ndc_targets_pathways_per_group.csv'))
            ptws[what][ssp] = data
            
            for condi, rge in condi_rge:
                tars_all[f"{condi}_{rge}"].loc[what, ssp] = data.loc[(data.group == 'EARTH') & (data.condi == condi) & (data.rge == rge), tar_yrs].max()
    
    return tars_all, ptws

# %%
def plot_emis():
    
    linestyle = {'SSP1': '--', 'SSP2': '-', 'SSP3': '--', 'SSP4': ':', 'SSP5': ':'}
    
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
    
    rge_ucw_cb_per_ssp = {}
    for ssp in meta.ssps.scens.short:
        rge_ucw_cb_per_ssp[ssp] = np.percentile((tars_all['unconditional_worst'].loc[:, ssp].values,
                                                 tars_all['conditional_best'].loc[:, ssp].values), [0, 10, 50, 90, 100])/1000
        print(f"\n% Range of {ssp} quantifications (uncondi worst and condi best): " + 
              ", ".join([f"{xx :.1f}" for xx in rge_ucw_cb_per_ssp[ssp]]) + " Gt CO2 eq")
    
    rge_condi_SSP1to4 = np.percentile(tars_all['unconditional_worst'].loc[:, ssp1_4].add(
        -tars_all['conditional_best'].loc[:, ssp1_4]).values, [10, 50, 90])/1000
    print("\n% Range between unconditional worst and conditional best targets (SSP1-4, 10, 50, 90%): " + 
          ", ".join([f"{xx :.1f}" for xx in rge_condi_SSP1to4]) + " Gt CO2eq")
       
    tars_all['unconditional_worst'].drop(columns=['SSP5'], inplace=True)
    tars_all['conditional_best'].drop(columns=['SSP5'], inplace=True)
    tars_all['unconditional_worst'].loc[:, 'median'] = tars_all['unconditional_worst'].median(axis=1)
    tars_all['conditional_best'].loc[:, 'median'] = tars_all['conditional_best'].median(axis=1)
    
    for yy in np.arange(45, 66, 2.5):
        ax_emi.plot([2000, 2070], [yy, yy], 'k:', linewidth=.3)
    
    # Plotting.
    handles = {}
    
    for tpe, add_x0, \
        tpe_data100, tpe_const100, tpe_constDiff100, \
        tpe_blUncondi100, tpe_blTar100, tpe_fao100, tpe_cat100, \
        tpe_data, tpe_const, tpe_constDiff, \
        tpe_blUncondi, tpe_blTar, tpe_fao, tpe_cat in \
        ['type_reclass', 0, 
            ptws['reclass100'], ptws['reclass100_const'], ptws['reclass100_constDiff'],
            ptws['reclass100_blUncondi'], ptws['reclass100_blTar'],
            ptws['reclass100_fao'], ptws['reclass100_cat'], 
            ptws['reclass'], ptws['reclass_const'], ptws['reclass_constDiff'],
            ptws['reclass_blUncondi'], ptws['reclass_blTar'],
            ptws['reclass_fao'], ptws['reclass_cat']], \
        ['type_main', +3.5,
            ptws['main100'], ptws['main100_const'], ptws['main100_constDiff'],
            ptws['main100_blUncondi'], ptws['main100_blTar'],
            ptws['main100_fao'], ptws['main100_cat'],
            ptws['main'], ptws['main_const'], ptws['main_constDiff'],
            ptws['main_blUncondi'], ptws['main_blTar'],
            ptws['main_fao'], ptws['main_cat']]:
    
        for ssp, add_x in zip(meta.ssps.scens.short, range(0, 45, 7)):
            
            colour_act = colours_ssps.loc[ssp, :].to_list()
            
            for which_tars in [tpe_data100, tpe_data]: # 100% cov vs estim. cov
                
                data_upper = which_tars[ssp]
                data_upper = 1e-3 * data_upper.loc[
                    (data_upper.group == 'EARTH') & (data_upper.condi.isin(['unconditional', 'conditional'])) &
                    (data_upper.category == cat), :].reindex(columns=years_str).max()
                
                data_lower = which_tars[ssp]
                data_lower = 1e-3 * data_lower.loc[
                    (data_lower.group == 'EARTH') & (data_lower.condi.isin(['unconditional', 'conditional'])) &
                    (data_lower.category == cat), :].reindex(columns=years_str).min()
                
                # Filled area.
                if ssp == ssp_chosen:
                    
                    ax_emi.fill_between(years_int, data_upper[years_str], 
                        data_lower[years_str], color=colour_act, linewidth=linewdth, alpha=.2)
            
            # BAU
            data = tpe_data[ssp]
            data = 1e-3 * data.loc[
                (data.group == 'EARTH') & (data.condi == 'emi_bau') & (data.category == cat), :]. \
                reindex(columns=years_str).values[0]
            handles[ssp], = ax_emi.plot(years_int, data, color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp])
    
    # Plot the mitigated range per SSP
    for ssp, xloc in zip(meta.ssps.scens.short, np.arange(2030.4, 2031.4, .2)):
        
        ax_emi.plot([xloc]*5, rge_ucw_cb_per_ssp[ssp], '.-', color= colours_ssps.loc[ssp, :].to_list())
        
        if miti_txt:
            
            if ssp == 'SSP5':
                
                for txt, count in zip(['min', '10%', 'median', '90%', 'max'], range(5)):
                    
                    if txt == 'min':
                        ax_emi.text(2031.3, rge_ucw_cb_per_ssp[ssp][count]-.5, txt, rotation=90, ha='center', va='top')
                    
                    elif txt == 'max':
                        ax_emi.text(2031.3, rge_ucw_cb_per_ssp[ssp][count]+.5, txt, rotation=90, ha='center', va='bottom')
                    
                    else:
                        ax_emi.text(2031.4, rge_ucw_cb_per_ssp[ssp][count], txt, rotation=90, ha='left', va='center')
                    
                    ax_emi.text(2031.2, rge_ucw_cb_per_ssp[ssp][count], 'o', ha='center', va='center')
    
    XL = XL_emi
    
    YL = [39.5, 68]
    if tar_yri == 2050:
        YL[-1] = 100
    
    ax_emi.set_ylim(YL)
    ax_emi.yaxis.set_ticks(range(45, 70, 5))
    ax_emi.text(XL[0] + .05*np.diff(XL), YL[1] - .05*np.diff(YL), 
        title, fontweight='bold', ha='left', va='top')
    ax_emi.text(XL[0] + .05*np.diff(XL), YL[1] - .115*np.diff(YL), 
        explanation, ha='left', va='top')
    ax_emi.set_ylabel('emissions / Gt CO$_2$eq AR4 (1e6)', fontweight='bold')
    
    ssps_legend = meta.ssps.scens.short
    if legend:
        ax_emi.legend([handles[xx] for xx in ssps_legend],
            [f"dm{xx}" for xx in ssps_legend], loc='center left', bbox_to_anchor=(0, .55))
    
    ax_emi.set_xlabel('year', fontweight='bold')
    
    ax_emi.xaxis.set_ticks(range(2010, tar_yri+1, 5))

# %%
for tar_yri in [2030, 2050]:
    
    for ssp_chosen in meta.ssps.scens.short:
        
        colours_ssps = pd.read_csv(
            Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 
                 'colours_ssps.csv'), index_col=0)
        colours_ssps.index = [meta.ssps.scens.long_to_short[xx] for xx in colours_ssps.index]
        
        tar_yrs = str(tar_yri)
        years_int = range(1990, tar_yri+1)
        years_str = [str(xx) for xx in years_int]
        
        XL_emi = [2010, tar_yri+.5+2]
        
        path_to_plot = Path(meta.path.main, 'plots', 'ndc_quantifications', 
            'comparison_of_ssps', f'ndcs_global_bl{cat}_pop_gdp_{tar_yri}_{ssp_chosen}.png')
        
        fig = plt.figure(figsize=(14, 11)) # 12, 10
        
        # %%
        path_to_output = Path(meta.path.output, 'output_for_paper', 'first_subm_exclUSA')
        
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
        
        folders_reclass_const_diff = [
         'ndcs_20210428_0948_SSP1_typeReclass_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1003_SSP2_typeReclass_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1019_SSP3_typeReclass_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1036_SSP4_typeReclass_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1117_SSP5_typeReclass_constDiffAfterLastTar_SMD20200417_PMH21']
        folders_reclass100_const_diff = [
         'ndcs_20210428_0951_SSP1_typeReclass_pccov100_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1007_SSP2_typeReclass_pccov100_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1026_SSP3_typeReclass_pccov100_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1046_SSP4_typeReclass_pccov100_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1121_SSP5_typeReclass_pccov100_constDiffAfterLastTar_SMD20200417_PMH21']
        
        folders_main_const_diff = [
         'ndcs_20210428_0941_SSP1_typeMain_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_0955_SSP2_typeMain_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1011_SSP3_typeMain_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1054_SSP4_typeMain_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1109_SSP5_typeMain_constDiffAfterLastTar_SMD20200417_PMH21']
        folders_main100_const_diff = [
         'ndcs_20210428_0944_SSP1_typeMain_pccov100_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_0959_SSP2_typeMain_pccov100_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1015_SSP3_typeMain_pccov100_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1102_SSP4_typeMain_pccov100_constDiffAfterLastTar_SMD20200417_PMH21',
         'ndcs_20210428_1114_SSP5_typeMain_pccov100_constDiffAfterLastTar_SMD20200417_PMH21']
        
        folders_reclass_bl_tar = [
         'ndcs_20210428_1943_SSP1_typeReclass_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_1950_SSP2_typeReclass_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_1957_SSP3_typeReclass_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_2001_SSP4_typeReclass_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_2012_SSP5_typeReclass_BLForTarAboveBL_SMD20200417_PMH21']
        folders_reclass100_bl_tar = [
         'ndcs_20210428_1945_SSP1_typeReclass_pccov100_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_1952_SSP2_typeReclass_pccov100_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_1959_SSP3_typeReclass_pccov100_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_2003_SSP4_typeReclass_pccov100_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_2013_SSP5_typeReclass_pccov100_BLForTarAboveBL_SMD20200417_PMH21']
        
        folders_main_bl_tar = [
         'ndcs_20210428_1939_SSP1_typeMain_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_1947_SSP2_typeMain_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_1954_SSP3_typeMain_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_2005_SSP4_typeMain_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_2008_SSP5_typeMain_BLForTarAboveBL_SMD20200417_PMH21']
        folders_main100_bl_tar = [
         'ndcs_20210428_1941_SSP1_typeMain_pccov100_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_1948_SSP2_typeMain_pccov100_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_1955_SSP3_typeMain_pccov100_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_2006_SSP4_typeMain_pccov100_BLForTarAboveBL_SMD20200417_PMH21',
         'ndcs_20210428_2010_SSP5_typeMain_pccov100_BLForTarAboveBL_SMD20200417_PMH21']
        
        folders_reclass_cat = [
         'ndcs_20210429_0052_SSP1_typeReclass_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0101_SSP2_typeReclass_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0110_SSP3_typeReclass_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0115_SSP4_typeReclass_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0132_SSP5_typeReclass_CAT_SMD20200417_PMH21']
        folders_reclass100_cat = [
         'ndcs_20210429_0054_SSP1_typeReclass_pccov100_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0103_SSP2_typeReclass_pccov100_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0112_SSP3_typeReclass_pccov100_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0117_SSP4_typeReclass_pccov100_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0134_SSP5_typeReclass_pccov100_CAT_SMD20200417_PMH21']
        
        folders_main_cat = [
         'ndcs_20210429_0048_SSP1_typeMain_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0057_SSP2_typeMain_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0106_SSP3_typeMain_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0120_SSP4_typeMain_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0127_SSP5_typeMain_CAT_SMD20200417_PMH21']
        folders_main100_cat = [
         'ndcs_20210429_0050_SSP1_typeMain_pccov100_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0059_SSP2_typeMain_pccov100_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0108_SSP3_typeMain_pccov100_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0123_SSP4_typeMain_pccov100_CAT_SMD20200417_PMH21',
         'ndcs_20210429_0129_SSP5_typeMain_pccov100_CAT_SMD20200417_PMH21']
        
        ax_emi = fig.add_subplot(2, 2, 1)
        ax_emi.set_xlim(XL_emi)
        title = '(a) Baseline emissions'
        explanation = 'upper lines: prio NDCs (17/04/2020, for type_reclass)\nlower lines: prio SSPs (for type_main)'
        legend = True
        miti_txt = True
        
        tars_all, ptws = read_emis()
        plot_emis()
        
        # %%
        path_to_output = Path(meta.path.output, 'output_for_paper', 'updated_ndcs_inclUSA')
        
        folders_reclass = [
         'ndcs_20210428_1211_SSP1_typeReclass_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1304_SSP2_typeReclass_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1356_SSP3_typeReclass_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1423_SSP4_typeReclass_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1538_SSP5_typeReclass_inclUSA_SMD20201231_PMH21']
        folders_reclass100 = [
         'ndcs_20210428_1225_SSP1_typeReclass_pccov100_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1318_SSP2_typeReclass_pccov100_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1409_SSP3_typeReclass_pccov100_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1436_SSP4_typeReclass_pccov100_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1550_SSP5_typeReclass_pccov100_inclUSA_SMD20201231_PMH21']
        
        folders_main = [
         'ndcs_20210428_1142_SSP1_typeMain_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1238_SSP2_typeMain_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1331_SSP3_typeMain_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1449_SSP4_typeMain_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1514_SSP5_typeMain_inclUSA_SMD20201231_PMH21']
        folders_main100 = [
         'ndcs_20210428_1155_SSP1_typeMain_pccov100_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1251_SSP2_typeMain_pccov100_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1344_SSP3_typeMain_pccov100_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1502_SSP4_typeMain_pccov100_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1527_SSP5_typeMain_pccov100_inclUSA_SMD20201231_PMH21']
        
        folders_reclass_constant_path = [
         'ndcs_20210428_1221_SSP1_typeReclass_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1314_SSP2_typeReclass_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1406_SSP3_typeReclass_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1432_SSP4_typeReclass_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1547_SSP5_typeReclass_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21']
        folders_reclass100_constant_path = [
         'ndcs_20210428_1234_SSP1_typeReclass_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1327_SSP2_typeReclass_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1419_SSP3_typeReclass_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1446_SSP4_typeReclass_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1559_SSP5_typeReclass_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21']
        
        folders_main_constant_path = [
         'ndcs_20210428_1152_SSP1_typeMain_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1247_SSP2_typeMain_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1340_SSP3_typeMain_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1458_SSP4_typeMain_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1523_SSP5_typeMain_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21']
        folders_main100_constant_path = [
         'ndcs_20210428_1206_SSP1_typeMain_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1300_SSP2_typeMain_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1352_SSP3_typeMain_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1510_SSP4_typeMain_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1535_SSP5_typeMain_pccov100_constEmiAfterLastTar_inclUSA_SMD20201231_PMH21']
        
        folders_reclass_baselineUncondi = [
         'ndcs_20210428_1217_SSP1_typeReclass_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1310_SSP2_typeReclass_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1401_SSP3_typeReclass_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1428_SSP4_typeReclass_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1543_SSP5_typeReclass_BLForUCAboveBL_inclUSA_SMD20201231_PMH21']
        folders_reclass100_baselineUncondi = [
         'ndcs_20210428_1231_SSP1_typeReclass_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1323_SSP2_typeReclass_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1415_SSP3_typeReclass_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1442_SSP4_typeReclass_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1555_SSP5_typeReclass_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21']
        
        folders_main_baselineUncondi = [
         'ndcs_20210428_1148_SSP1_typeMain_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1243_SSP2_typeMain_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1336_SSP3_typeMain_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1454_SSP4_typeMain_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1519_SSP5_typeMain_BLForUCAboveBL_inclUSA_SMD20201231_PMH21']
        folders_main100_baselineUncondi = [
         'ndcs_20210428_1202_SSP1_typeMain_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1256_SSP2_typeMain_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1349_SSP3_typeMain_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1507_SSP4_typeMain_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1532_SSP5_typeMain_pccov100_BLForUCAboveBL_inclUSA_SMD20201231_PMH21']
        
        folders_reclass_fao = [
         'ndcs_20210428_1211_SSP1_typeReclass_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1304_SSP2_typeReclass_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1356_SSP3_typeReclass_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1423_SSP4_typeReclass_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1538_SSP5_typeReclass_inclUSA_FAO_SMD20201231_PMH21']
        folders_reclass100_fao = [
         'ndcs_20210428_1225_SSP1_typeReclass_pccov100_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1318_SSP2_typeReclass_pccov100_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1409_SSP3_typeReclass_pccov100_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1436_SSP4_typeReclass_pccov100_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1550_SSP5_typeReclass_pccov100_inclUSA_FAO_SMD20201231_PMH21']
        
        folders_main_fao = [
         'ndcs_20210428_1142_SSP1_typeMain_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1238_SSP2_typeMain_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1331_SSP3_typeMain_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1449_SSP4_typeMain_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1514_SSP5_typeMain_inclUSA_FAO_SMD20201231_PMH21']
        folders_main100_fao = [
         'ndcs_20210428_1155_SSP1_typeMain_pccov100_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1251_SSP2_typeMain_pccov100_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1344_SSP3_typeMain_pccov100_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1502_SSP4_typeMain_pccov100_inclUSA_FAO_SMD20201231_PMH21',
         'ndcs_20210428_1527_SSP5_typeMain_pccov100_inclUSA_FAO_SMD20201231_PMH21']
        
        folders_reclass_const_diff = [
         'ndcs_20210428_1223_SSP1_typeReclass_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1316_SSP2_typeReclass_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1407_SSP3_typeReclass_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1434_SSP4_typeReclass_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1548_SSP5_typeReclass_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21']
        folders_reclass100_const_diff = [
         'ndcs_20210428_1236_SSP1_typeReclass_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1329_SSP2_typeReclass_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1421_SSP3_typeReclass_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1447_SSP4_typeReclass_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1601_SSP5_typeReclass_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21']
        
        folders_main_const_diff = [
         'ndcs_20210428_1153_SSP1_typeMain_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1249_SSP2_typeMain_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1342_SSP3_typeMain_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1500_SSP4_typeMain_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1525_SSP5_typeMain_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21']
        folders_main100_const_diff = [
         'ndcs_20210428_1208_SSP1_typeMain_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1302_SSP2_typeMain_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1354_SSP3_typeMain_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1512_SSP4_typeMain_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1537_SSP5_typeMain_pccov100_constDiffAfterLastTar_inclUSA_SMD20201231_PMH21']
        
        folders_reclass_bl_tar = [
         'ndcs_20210428_1901_SSP1_typeReclass_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1908_SSP2_typeReclass_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1915_SSP3_typeReclass_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1919_SSP4_typeReclass_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1930_SSP5_typeReclass_BLForTarAboveBL_inclUSA_SMD20201231_PMH21']
        folders_reclass100_bl_tar = [
         'ndcs_20210428_1902_SSP1_typeReclass_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1910_SSP2_typeReclass_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1917_SSP3_typeReclass_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1921_SSP4_typeReclass_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1932_SSP5_typeReclass_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21']
        
        folders_main_bl_tar = [
         'ndcs_20210428_1857_SSP1_typeMain_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1904_SSP2_typeMain_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1912_SSP3_typeMain_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1923_SSP4_typeMain_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1927_SSP5_typeMain_BLForTarAboveBL_inclUSA_SMD20201231_PMH21']
        folders_main100_bl_tar = [
         'ndcs_20210428_1859_SSP1_typeMain_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1906_SSP2_typeMain_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1914_SSP3_typeMain_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1925_SSP4_typeMain_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21',
         'ndcs_20210428_1928_SSP5_typeMain_pccov100_BLForTarAboveBL_inclUSA_SMD20201231_PMH21']
        
        folders_reclass_cat = [
         'ndcs_20210429_0211_SSP1_typeReclass_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0220_SSP2_typeReclass_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0228_SSP3_typeReclass_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0232_SSP4_typeReclass_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0243_SSP5_typeReclass_CAT_inclUSA_SMD20201231_PMH21']
        folders_reclass100_cat = [
         'ndcs_20210429_0213_SSP1_typeReclass_pccov100_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0222_SSP2_typeReclass_pccov100_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0230_SSP3_typeReclass_pccov100_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0234_SSP4_typeReclass_pccov100_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0245_SSP5_typeReclass_pccov100_CAT_inclUSA_SMD20201231_PMH21']
        
        folders_main_cat = [
         'ndcs_20210429_0207_SSP1_typeMain_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0216_SSP2_typeMain_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0224_SSP3_typeMain_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0236_SSP4_typeMain_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0240_SSP5_typeMain_CAT_inclUSA_SMD20201231_PMH21']
        folders_main100_cat = [
         'ndcs_20210429_0209_SSP1_typeMain_pccov100_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0218_SSP2_typeMain_pccov100_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0226_SSP3_typeMain_pccov100_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0238_SSP4_typeMain_pccov100_CAT_inclUSA_SMD20201231_PMH21',
         'ndcs_20210429_0241_SSP5_typeMain_pccov100_CAT_inclUSA_SMD20201231_PMH21']
        
        ax_emi = fig.add_subplot(2, 2, 2)
        ax_emi.set_xlim(XL_emi)
        title = '(b) Baseline emissions'
        explanation = 'upper lines: prio NDCs (31/12/2020, for type_reclass)\nlower lines: prio SSPs (for type_main)'
        legend = False
        miti_txt = False
        
        tars_all, ptws = read_emis()
        plot_emis()
        
        # %%
        # POP & GDP
        
        linestyle = {'SSP1BLIMAGE': '--', 'SSP2BLMESGB': '-', 'SSP3BLAIMCGE': '--', 'SSP4BLGCAM4': ':', 'SSP5BLREMMP': ':'}
        
        ax_pop = fig.add_subplot(2, 2, 3)
        ax_gdp = fig.add_subplot(2, 2, 4)
        years = range(1990, tar_yri+1)
        
        ssps = meta.ssps.scens.long
        colours_ssps = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
            'colours', 'colours_ssps.csv'), index_col=0)
        
        ax_p = ax_pop
        ax_g = ax_gdp
        XL = XL_emi
        #YL_p = [6.8e9, 8.75e9]
        #YL_g = [80e12, 220e12]
        YL_p = [6.8, 8.75]
        YL_g = [80, 220]
        
        if tar_yri == 2050:
            
            YL_p = [6.8, 10.1]
            YL_g = [80, 480]
        
        for ssp, count, add_x in zip(ssps + [ssps[1]], range(len(ssps + [ssps[1]])), [-.2, -.1, 0, .1, .2]):
            
            colour_act = colours_ssps.loc[ssp, :].to_list()
            
            ax_p.plot(1e-9 * pop_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
                color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp], label=(f"dm{ssp}" if count != 5 else '__nolegend__'))
            
            ax_g.plot(1e-12 * gdp_filled[ssp].data.loc[:, years].reindex(index=meta.isos.EARTH).sum(),
                color=colour_act, linewidth=linewdth, linestyle=linestyle[ssp], label=(f"dm{ssp}" if count != 5 else '__nolegend__'))
        
        if ax_p == ax_pop:
            
            ax_p.set_xlabel('year', fontweight='bold')
            ax_g.set_xlabel('year', fontweight='bold')
            # ax_p.set_ylabel('population / Pers', fontweight='bold')
            # ax_g.set_ylabel('GDP (PPP) / 2011 GK$', fontweight='bold')
            ax_p.set_ylabel('population / Billion Pers (1e9)', fontweight='bold')
            ax_g.set_ylabel('GDP (PPP) / Trillion 2011 GK$ (1e12)', fontweight='bold')
                        
            for axa, txt, YL in zip([ax_p, ax_g], ['(c) Population', '(d) GDP (PPP)'], [YL_p, YL_g]):
                
                axa.xaxis.set_ticks(range(2010, tar_yri+1, 5))
                axa.yaxis.set_ticks_position('both')
                axa.text(XL[0] + .05*np.diff(XL), YL[1] - .05*np.diff(YL), txt, fontweight='bold', ha='left', va='top')
                axa.set_xlim(XL)
                axa.set_ylim(YL)
        
        hpf.set_ticks_scientific_notation(ax_p, 'y')
        hpf.set_ticks_scientific_notation(ax_g, 'y')
        
        ax_p.set_xlim(XL)
        ax_g.set_xlim(XL)
        
        # %%
        #fig.subplots_adjust(left=.1, right=.9)
        plt.savefig(str(path_to_plot).replace('.png', '.png'), dpi=300)
        path_to_pdf = str(path_to_plot).replace('.png', '.pdf')
        plt.savefig(path_to_pdf, dpi=300)
        hpf.crop_pdf(path_to_pdf)
        plt.clf()
        plt.close(fig)

# %%
