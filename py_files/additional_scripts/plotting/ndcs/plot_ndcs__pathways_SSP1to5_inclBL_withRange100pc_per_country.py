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

colour_100pc = (0, .7, .5)
colour_estpc = (.3, .3, .3)
colour_prioNDCs = (.5, .7, 0)
colour_prioSSPs = (.7, .7, .7)

# %%
fig = plt.figure(figsize=(12, 4))

for iso3 in ['AFG']: #meta.isos.EARTH[:10]:
    
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
            yr_plt = 2017 - .05
                       
            for opt, data_opt in \
                ['default', tpe_data100], \
                ['bl uncondi', tpe_blUncondi100], \
                ['const. emi', tpe_const100], \
                ['LU FAO', tpe_fao100], \
                ['default (*)', tpe_data], \
                ['bl uncondi (*)', tpe_blUncondi], \
                ['const. emi (*)', tpe_const], \
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
                    [data_lower2030, data_upper2030], 
                    color=colour_act, linewidth=linewdth_all)
                
#                yr_plt += yr_add
                
                data_act = data_opt[ssp]
                data_act = 1e-3 * data_act.loc[
                    (data_act.iso3 == iso3) & 
                    (data_act.condi.isin(['unconditional', 'conditional'])) &
                    (data_act.category == cat), '2030']
                
                axa.scatter([yr_plt + add_xx]*4, data_act.values, 1.7, marker='s', color=colour_act)
                
                yr_plt += yr_add
                
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
            handles[ssp], = ax_emi.plot(years_int, data, color=colour_act, 
                linewidth=(linewdth if 'main' in tpe else .5*linewdth), linestyle=linestyle[ssp])
    
    tpe_act = 'main'
    tar_type_main = ptws[tpe_act]['SSP1'].loc[ptws[tpe_act]['SSP1'].iso3 == iso3, 'tar_type_used'].unique()
    tar_type_main = [xx for xx in tar_type_main if type(xx) == str][0]
    tpe_act = 'reclass'
    tar_type_reclass = ptws[tpe_act]['SSP1'].loc[ptws[tpe_act]['SSP1'].iso3 == iso3, 'tar_type_used'].unique()
    tar_type_reclass = [xx for xx in tar_type_reclass if type(xx) == str][0]
    
    YL_emi = [min([ax_emi.get_ylim()[0], ax_tars.get_ylim()[0]]),
              max([ax_emi.get_ylim()[1], ax_tars.get_ylim()[1]])*1.05]
    for axa, txt, XL in \
        [ax_emi, '(a) Baseline emissions', XL_emi], \
        [ax_tars, '(b) NDC pathway for 2030', XL_tars]:
        axa.set_ylim(YL_emi)
        axa.text(XL[0], YL_emi[1] + .2*np.diff(YL_emi), 
            txt, fontweight='bold', ha='left', va='bottom')
        if axa == ax_emi:
            txt1 = f'\nthinner lines per dmSSP: prio NDC (type_reclass = {tar_type_reclass})'
            txt2 = f'thicker lines per dmSSP: prio SSPs (type_main = {tar_type_main})'
            txt3 = 'shaded area for conditionality range (default; prio NDC vs. SSPs)'
        else:
            txt1 = '\n'
            txt2 = '\n'
            txt3 = '\n'
        axa.text(XL[0], YL_emi[1] + .14*np.diff(YL_emi), 
                 txt1, ha='left', va='bottom')
        axa.text(XL[0], YL_emi[1] + .08*np.diff(YL_emi), 
                 txt2, ha='left', va='bottom')
        axa.text(XL[0], YL_emi[1] + .02*np.diff(YL_emi), 
                 txt3, ha='left', va='bottom')
        
        if axa == ax_tars:
            yval = 2*[YL_emi[1] - .02*np.diff(YL_emi)]
            # prio NDCs, type_reclass
            for xx in np.arange(2016.85, 2035, 4):
                axa.plot([xx, xx + 1.8], yval, color=colour_prioNDCs, linewidth=3)
            # prio SSPs, type_main
            for xx in np.arange(2018.85, 2035, 4):
                axa.plot([xx, xx + 1.8], yval, color=colour_prioSSPs, linewidth=3)
            yval = 2*[YL_emi[1] - .04*np.diff(YL_emi)]
            # 100% cov
            for xx in np.arange(2016.85, 2036, 2):
                axa.plot([xx, xx + .8], yval, color=colour_100pc, linewidth=3)
            # estimated cov
            for xx in np.arange(2017.85, 2036, 2):
                axa.plot([xx, xx + .8], yval, color=colour_estpc, linewidth=3)
            # text
            axa.text(XL[0] + .0*np.diff(XL), YL_emi[1] + .14*np.diff(YL_emi), 
                     'prio NDC', color=colour_prioNDCs, ha='left', va='bottom')
            axa.text(XL[0] + .15*np.diff(XL), YL_emi[1] + .14*np.diff(YL_emi), 
                     'vs.', color='k', ha='left', va='bottom')
            axa.text(XL[0] + .2*np.diff(XL), YL_emi[1] + .14*np.diff(YL_emi), 
                     'prio SSPs', color=colour_prioSSPs, ha='left', va='bottom')
            axa.text(XL[0] + .0*np.diff(XL), YL_emi[1] + .08*np.diff(YL_emi), 
                     '100% coverage', color=colour_100pc, ha='left', va='bottom')
            axa.text(XL[0] + .26*np.diff(XL), YL_emi[1] + .08*np.diff(YL_emi), 
                     'vs.', color='k', ha='left', va='bottom')
            axa.text(XL[0] + .31*np.diff(XL), YL_emi[1] + .08*np.diff(YL_emi), 
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
    ax_tars.text(XL[0], YL_emi[1] + .02*np.diff(YL_emi), 
        f'Quadruples: options "{txt_options[0]}", "{txt_options[1]}", "{txt_options[2]}", "{txt_options[3]}"',
        ha='left', va='bottom')
    
    ax_emi.xaxis.set_ticks(range(2010, 2032, 5))
        
    fig.subplots_adjust(left=.1, right=.99, top=.8)
    path_to_plot = Path(meta.path.main, 'latex_files', #iso3, 
        f'ndc_tars_{cat}_{iso3}.png')
    plt.savefig(path_to_plot, dpi=300)
    plt.clf()

plt.close(fig)

# %%
