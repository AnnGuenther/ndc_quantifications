# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from setup_metadata import setup_metadata
import helpers_functions as hpf

# %%
meta = setup_metadata()
iso3 = 'IND'

# %%
"""
Latex table with information regarding India's target with pc_cov != 100% and pc_cov == 100%.'
"""
path_to_folder_100pc_calc = 'ndcs_20200628_2122_SSP2_typeCalc_pccov100'
path_to_folder_calc = 'ndcs_20200628_2120_SSP2_typeCalc'

tars_100 = pd.read_csv(Path(meta.path.output, 
    path_to_folder_100pc_calc, 'ndc_targets.csv'))
tars_not100 = pd.read_csv(Path(meta.path.output, 
    path_to_folder_calc, 'ndc_targets.csv'))

print("Based on quantifications under SSP2 and an assumed 100\% coverage, India's emissions target ranges between " +
      f"{int(float(tars_100.loc[(tars_100.iso3 == iso3) & (tars_100.rge == 'best'), 'tar_emi_exclLU'].values[0]))} Mt~CO$_2$~eq " +
      f"and {int(float(tars_100.loc[(tars_100.iso3 == iso3) & (tars_100.rge == 'worst'), 'tar_emi_exclLU'].values[0]))} Mt~CO$_2$~eq " +
      "for emissions excluding LULUCF, and between " +
      f"{int(float(tars_100.loc[(tars_100.iso3 == iso3) & (tars_100.rge == 'best'), 'tar_emi_inclLU'].values[0]))} Mt~CO$_2$~eq " +
      f"and {int(float(tars_100.loc[(tars_100.iso3 == iso3) & (tars_100.rge == 'worst'), 'tar_emi_inclLU'].values[0]))} Mt~CO$_2$~eq " +
      "for emissions including LULUCF.")
print("With the estimated coverage following information in Section~\\ref{sec:coveredEmissions}, the emissions target ranges between " +
      f"{int(float(tars_not100.loc[(tars_not100.iso3 == iso3) & (tars_not100.rge == 'best'), 'tar_emi_exclLU'].values[0]))} Mt~CO$_2$~eq " +
      f"and {int(float(tars_not100.loc[(tars_not100.iso3 == iso3) & (tars_not100.rge == 'worst'), 'tar_emi_exclLU'].values[0]))} Mt~CO$_2$~eq " +
      "for emissions excluding LULUCF, and between " +
      f"{int(float(tars_not100.loc[(tars_not100.iso3 == iso3) & (tars_not100.rge == 'best'), 'tar_emi_inclLU'].values[0]))} Mt~CO$_2$~eq " +
      f"and {int(float(tars_not100.loc[(tars_not100.iso3 == iso3) & (tars_not100.rge == 'worst'), 'tar_emi_inclLU'].values[0]))} Mt~CO$_2$~eq " +
      "for emissions including LULUCF.")

 #%%
cols = ['tar_emi_exclLU', 'tar_emi_inclLU', 
        'emi_bl_exclLU_refyr', 'emi_bl_exclLU_taryr',
        'emi_bl_LU_refyr', 'emi_bl_LU_taryr', 
        'pc_cov_exclLU_refyr', 'pc_cov_exclLU_taryr',
        'gdp_refyr', 'gdp_taryr']
tars_100 = tars_100.loc[(tars_100.iso3 == iso3) & (tars_100.rge == 'best'), cols].astype(float)
tars_not100 = tars_not100.loc[(tars_not100.iso3 == iso3) & (tars_not100.rge == 'best'), cols].astype(float)

# %%
# Use the 35% reduction.

txt = "& 2005 & 2030 & Target with 'real' coverage & Target with 100\% coverage \\tabularnewline \\hline"

txt += f"\nEmissions (excl. LULUCF) in MtCO$_2$eq AR4 & {tars_100['emi_bl_exclLU_refyr'].values[0] :.1f} & "
txt += f"{tars_100['emi_bl_exclLU_taryr'].values[0] :.1f} & "
txt += f"{tars_not100['tar_emi_exclLU'].values[0] :.1f} & "
txt += f"{tars_100['tar_emi_exclLU'].values[0] :.1f} \\tabularnewline"

txt += f"\nEmissions (LULUCF) in MtCO$_2$eq AR4 & {tars_100['emi_bl_LU_refyr'].values[0] :.1f} & "
txt += f"{tars_100['emi_bl_LU_taryr'].values[0] :.1f} & "
txt += f"{tars_not100['tar_emi_inclLU'].values[0] - tars_not100['tar_emi_exclLU'].values[0] :.1f} & "
txt += f"{tars_100['tar_emi_inclLU'].values[0] - tars_100['tar_emi_exclLU'].values[0] :.1f} \\tabularnewline"

txt += f"\npc\_cov (excl. LULUCF) in \% & {100. * tars_not100['pc_cov_exclLU_refyr'].values[0] :.1f} & "
txt += f"{100. * tars_not100['pc_cov_exclLU_taryr'].values[0] :.1f} & & \\tabularnewline"

txt += f"\nGDP (PPP) in 2011 US\$ & {tars_100['gdp_refyr'].values[0] :.1e} & "
txt += f"{tars_100['gdp_taryr'].values[0] :.1e} & &"

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', f"{iso3}_target_real_coverage_vs_100pc_latex_table.csv"))

# %%
"""
Plot IND data. Emissions with targets (SSP1 to SSP5).
SSP2: 100% coverage vs. 'real' coverage.
GDP for SSP1 to SSP5.
"""
# ndc_targets_pathways_per_country.csv
ptws_100_ssp2 = pd.read_csv(Path(meta.path.output, 
    path_to_folder_100pc_calc, 'ndc_targets_pathways_per_country.csv'))
ptws_100_ssp2 = ptws_100_ssp2.loc[ptws_100_ssp2.iso3 == iso3, :]
# ndc_targets.csv
tars_100_ssp2 = pd.read_csv(Path(meta.path.output, 
    path_to_folder_100pc_calc, 'ndc_targets.csv'))
tars_100_ssp2 = tars_100_ssp2.loc[tars_100_ssp2.iso3 == iso3, :]

ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_NDCSSP2BLMESGB_NDCPMSSPBIE.csv'))

ptws_not100 = {}
tars_not100 = {}
for ssp, file in \
    ['ssp1', 'ndcs_20200628_2218_SSP1_typeCalc'], \
    ['ssp2', path_to_folder_calc], \
    ['ssp3', 'ndcs_20200628_2229_SSP3_typeCalc'], \
    ['ssp4', 'ndcs_20200628_2243_SSP4_typeCalc'], \
    ['ssp5', 'ndcs_20200628_2258_SSP5_typeCalc']:
    data = pd.read_csv(Path(meta.path.output, 
        file, 'ndc_targets_pathways_per_country.csv'))
    ptws_not100[ssp] = data.loc[data.iso3 == iso3, :]
    data = pd.read_csv(Path(meta.path.output, 
        file, 'ndc_targets.csv'))
    tars_not100[ssp] = data.loc[data.iso3 == iso3, :]

colours_ssps = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
    'colours', 'colours_ssps.csv'), index_col=0)
colour_ssp2 = colours_ssps.loc[meta.ssps.scens.short_to_long['SSP2'], :].to_list()

fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

years_int = range(1990, 2031)
years_str = [str(xx) for xx in years_int]

linewdth_ssp2 = 2
linewdth_notssp2 = 1.5

condi = 'unconditional'
for rge in ['best', 'worst']:
    
    # ptws
    data = ptws_100_ssp2
    ax1.plot(years_int, data.loc[(data.tar_type_used == 'REI') & (data.condi == condi) & 
        (data.rge == rge) & (data.category == 'IPCM0EL'), years_str].values[0], ':', color=[.5*xx for xx in colour_ssp2],
        linewidth=linewdth_notssp2, label='__nolegend__')
    data = ptws_not100['ssp2']
    ax1.plot(years_int, data.loc[(data.tar_type_used == 'REI') & (data.condi == condi) & 
        (data.rge == rge) & (data.category == 'IPCM0EL'), years_str].values[0], ':', color=colour_ssp2,
        linewidth=linewdth_notssp2, label='__nolegend__')

linewdth_vert = 3

# tars
for ssp, add_x in zip(tars_not100.keys(), [-.2, -.1, 0, .1, .2]):
    
    if ssp == 'ssp2':
        data = tars_100_ssp2
        ax1.plot([2030 + add_x, 2030 + add_x], 
            [float(data.loc[(data.tar_type_used == 'REI') & (data.condi == condi) & 
            (data.rge == xx), 'tar_emi_exclLU']) for xx in ['best', 'worst']], 
            color=[.5*xx for xx in colour_ssp2], label='SSP2 target (excl. LULUCF)\nassumed 100% coverage',
            linewidth=linewdth_vert)

    colour_act = colours_ssps.loc[meta.ssps.scens.short_to_long[ssp.upper()], :].to_list()
    data = tars_not100[ssp]
    ax1.plot([2030 + add_x, 2030 + add_x], 
        [float(data.loc[(data.tar_type_used == 'REI') & (data.condi == condi) & 
        (data.rge == xx), 'tar_emi_exclLU']) for xx in ['best', 'worst']], 
        color=colour_act, 
        label=("SSP2 target (excl. LULUCF)\nestimated coverage" if ssp == 'ssp2' else '__nolegend__'),
        linewidth=linewdth_vert)
    
    data = ptws_not100[ssp]
    ax1.plot(years_int, data.loc[(data.condi == 'emi_bau') & 
        (data.category == 'IPCM0EL'), years_str].values[0], color=colour_act,
        linewidth=(linewdth_ssp2 if ssp == 'ssp2' else linewdth_notssp2), label='__nolegend__')
    
    # GDP
    ax2.plot(years_int, ptws_not100[ssp].loc[(ptws_not100[ssp].condi == 'gdp'), years_str].values[0],
        color=colour_act, label=f'{ssp.upper()}', linewidth=(linewdth_ssp2 if ssp == 'ssp2' else linewdth_notssp2))

ax1.plot(years_int, ptws_100_ssp2.loc[(ptws_100_ssp2.condi == 'emi_bau') & 
    (ptws_100_ssp2.category == 'IPCM0EL'), years_str].values[0], color=colour_ssp2, 
    label='SSP2 national totals (excl. LULUCF)', linewidth=linewdth_ssp2)
ax1.plot(years_int, ptws_not100['ssp2'].loc[(ptws_not100['ssp2'].condi == 'emi_cov') & 
    (ptws_not100['ssp2'].category == 'IPCM0EL'), years_str].values[0], '--', color=colour_ssp2, 
    label='SSP2 covered emissions (excl. LULUCF)', linewidth=linewdth_ssp2)
ax1.plot(years_int, ipcmlulucf.data.loc[iso3, years_int].values, '.', color=[0, .4, 0], 
    label='LULUCF', linewidth=linewdth_ssp2)

ssp = 'ssp2'
ax2.plot(years_int, ptws_not100[ssp].loc[(ptws_not100[ssp].condi == 'gdp'), years_str].values[0],
    color=colour_ssp2, label='__nolegend__', linewidth=linewdth_ssp2)

ax1.legend(loc='upper center', bbox_to_anchor=(.4, 1))
ax2.legend(loc='upper center', bbox_to_anchor=(.2, 1))

XL = [years_int[0] - 2, years_int[-1] + 2]
for axa in [ax1, ax2]:
    axa.plot(XL, [0, 0], 'k--', linewidth=.3)

YL = ax1.get_ylim()
for year in [2005, 2030]:
    ax1.plot([year, year], YL, 'k--', linewidth=.3)
ax1.set_xlim(XL)
ax1.set_ylim(YL)

ax1.text(XL[0], YL[0] - np.diff(YL)*.15,
    'Vertical lines: quantification of mitigation targets (dark blue) based on assumed 100% coverage; ' +
    '(others) based on estimated coverage.')

ax2.set_xlim(XL)
YL = ax2.get_ylim()
for year in [2005, 2030]:
    ax2.plot([year, year], YL, 'k--', linewidth=.3)
ax2.set_ylim(YL)

for axa in [ax1, ax2]:
    axa.set_xlabel('year', fontweight='bold')
    YL = axa.get_ylim()
    ypos = YL[1] + .01*np.diff(YL)
    for year, txt in [2005, 'base year'], [2030, 'target year']:
        axa.text(year, ypos, txt, ha='center', va='bottom', fontweight='bold')

ax1.set_ylabel('emissions / Mt CO$_2$eq AR4', fontweight='bold')
ax2.set_ylabel('GDP (PPP) / 2011 US$', fontweight='bold')

hpf.put_labels_to_subplots(ax1, ax2)

hpf.set_ticks_scientific_notation(ax2, 'y')
fig.subplots_adjust(left=.1, right=.95, bottom=.2)
path_to_png = Path(meta.path.main, 'plots', 'IND', 'IND_pccov_targets_gdp.png')
plt.savefig(path_to_png, dpi=300)
path_to_pdf = str(path_to_png).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
"""
Plot the time series of emissions per sector and gas.
"""

emi_tot_2017 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.matlab, 'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    data.loc['IND', 2017]

# Available UNFCCC2019BI data.
#available_unfccc = pd.read_csv(Path(meta.path.main, 'data', 'other', 'IND_available_data_UNFCCC2019BI_MtCO2eq.csv'), index_col=0)

years_his_int = range(1990, meta.primap.last_year + 1)
years_his_str = [str(xx) for xx in years_his_int]

colours_cats = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting',
    'colours', 'colours_categories_ipc.csv'), index_col=0)
colours_gases = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting',
    'colours', 'colours_gases.csv'), index_col=0)

linewdth = 2.5

fig = plt.figure(figsize=(14, 3.5))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

pc_sec = {}
for cat, axa in ['IPC1', ax1], ['IPC2', ax2], ['IPCMAG', ax3], ['IPC4', ax4], ['IPC5', ax5]:
    
    gases = ['CO2', 'CH4', 'N2O']
    if cat == 'IPC2':
        gases += ['FGASES']
    
    emi_sec = 0
    for gas in gases:
        
        tablename = f'{gas}AR4_{cat}_TOTAL_NET_HISTCR_PRIMAPHIST21'
        table = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.matlab, tablename + '.csv'))
        
        if 'IND' in table.data.index:
            
            colour_act = colours_gases.loc[gas, :].to_list()
            
            table = table.data.loc['IND', years_his_int]
            axa.plot(years_his_int, table, color=colour_act, 
                label=meta.gases.gas_to_label[gas], linewidth=linewdth)
            
            emi_sec += table[2017]
            
            # Available UNFCCC data.
            #ablename = tablename.replace('HISTCR_PRIMAPHIST21', 'HISTORY_UNFCCC2019BI')
            #if 'FGASES' not in gas:
            #    tablename = tablename.replace('AR4', '')
            #
            #if tablename in available_unfccc.index:
            #    unfccc = available_unfccc.loc[tablename, :]
            #    axa.plot([int(xx[1:]) for xx in unfccc.index], unfccc*1e-3, '.', color=colour_act)
    
    sec = meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[cat]]
    axa.set_title(sec, fontweight='bold')
    pc_sec[sec] = f'{emi_sec/emi_tot_2017*100. :.1f}%'

# Set all ylim to the same.
#YL_max = 0
#for axa in [ax1, ax2, ax3, ax4, ax5]:
#    YL_max = max([YL_max, axa.get_ylim()[1]])
#YL = [0, YL_max]
#for axa in [ax1, ax2, ax3, ax4, ax5]:
#    axa.set_ylim(YL)

pc_gas = {}
for gas in meta.gases.kyotoghg:
    tablename = f'{gas}AR4_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21'
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.matlab, tablename + '.csv')).data.loc['IND', 2017]
    pc_gas[gas] = f'{table/emi_tot_2017*100. :.1f}%'

XL = ax1.get_xlim()
YL = ax1.get_ylim()
ax1.text(XL[0], YL[0] - .25*np.diff(YL), 
    'In 2017, the share per sector (compared to Kyoto GHG, excl. LULUCF) was: ' +
    ', '.join([f'{xx} {pc_sec[xx]}' for xx in pc_sec.keys()]) + ';\nand per gas: ' +
    ', '.join([f'{meta.gases.gas_to_label[xx]} {pc_gas[xx]}' for xx in pc_gas.keys()]) + 
    '. Data source: PRIMAP-hist v2.1 HISTCR.', va='top', ha='left')

ax2.legend(loc='upper center', bbox_to_anchor=(.35, 1))
ax1.set_ylabel('emissions / Mt CO$_2$eq AR4', fontweight='bold')
for axa in [ax1, ax2, ax3, ax4, ax5]:
    axa.set_xlabel('year', fontweight='bold')

hpf.put_labels_to_subplots(ax1, ax2, ax3, ax4, ax5)

fig.subplots_adjust(left=.05, right=.99, bottom=.25)
path_to_png = Path(meta.path.main, 'plots', 'IND', 'IND_emi_per_gas_and_sector.png')
plt.savefig(path_to_png, dpi=300)
path_to_pdf = str(path_to_png).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
"""
Playing around with pc_cov, based on India's target and values.
Latex table.
"""

data = pd.read_csv(Path(meta.path.output, 
    path_to_folder_calc, 'ndc_targets.csv'))
data = data.loc[(data.iso3 == iso3) & (data.rge == 'best')]

gdp_2005 = float(data['gdp_refyr'])
gdp_2030 = float(data['gdp_taryr'])
emi_2005 = float(data['emi_bl_exclLU_refyr'])
emi_2030 = float(data['emi_bl_exclLU_taryr'])
ndc_level = 1-.35

txt = '\\textbf{REI\_RBY} & \\textbf{refyr: 2005} & \\textbf{taryr: 2030} & '
txt += '\\textbf{A} & \\textbf{+} & \\textbf{B} & \\textbf{-} & \\textbf{C} & \\textbf{=} & \\textbf{D} & '
txt += '\\textbf{E} & \\textbf{F} \\tabularnewline \\hline'

txt += f'\n GDP (PPP) in 2011 US\$ & {gdp_2005 :.1e}* & {gdp_2030 :.1e}* & & & & & & & & & \\tabularnewline'

txt += f'\n Emissions (excl. LULUCF) & {emi_2005 :.0f}* & {emi_2030 :.0f}* & & & & & & & & & \\tabularnewline \\hline'

for pccov_2005, pccov_2030, name, hline in [.66, .81, '\\textbf{pc\_cov (increase)}', False], \
    [.81, .66, 'pc\_cov (decrease)', False], [1, 1, '\\textbf{pc\_cov (100\%)}', False], \
    [.5, .5, 'pc\_cov (50\%)', True], [0, 0, 'pc\_cov (edge case, no mitigation)', False], \
    [0, 1, 'pc\_cov (edge case, unrealistic)', False], [1, 0, 'pc\_cov (edge case, unrealistic)', False]:
    if (pccov_2005 == .66 and pccov_2030 == .81):
        txt += f'\n {name} & {pccov_2005*100 :.0f}\%* & {pccov_2030*100 :.0f}\%* & '
    else:
        txt += f'\n {name} & {pccov_2005*100 :.0f}\% & {pccov_2030*100 :.0f}\% & '
    first = int(gdp_2030/gdp_2005 * ndc_level * pccov_2005 * emi_2005)
    second = emi_2030
    third = int(pccov_2030 * emi_2030)
    last = first + second - third
    pc = (last/emi_2030 - 1) * 100
    pc = (f'+{pc :.0f}\%' if pc > 0 else f'-{pc :.0f}\%')
    pc_refyr = (last/emi_2005 - 1) * 100
    pc_refyr = (f'+{pc_refyr :.0f}\%' if pc_refyr > 0 else f'-{pc_refyr :.0f}\%')
    txt += f'{first :.0f} & + & {second :.0f} & - & {third :.0f} & = & {last :.0f} & {pc_refyr} & {pc} \\tabularnewline '
    if hline:
        txt += '\\hline'

txt = txt[:-len('  \\tabularnewline')]

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'IND_playing_with_pccov_latex_table_REI_RBY.csv'))

txt = '\\textbf{RBY} & \\textbf{refyr: 2005} & \\textbf{taryr: 2030} & '
txt += '\\textbf{A} & \\textbf{+} & \\textbf{B} & \\textbf{-} & \\textbf{C} & \\textbf{=} & \\textbf{D} & '
txt += '\\textbf{E} & \\textbf{F} \\tabularnewline \\hline'

txt += f'\n Emissions (excl. LULUCF) & {emi_2005 :.0f} & {emi_2030 :.0f} & & & & & & & & & \\tabularnewline \\hline'

for pccov_2005, pccov_2030, name, hline in [.66, .81, 'pc\_cov (increase)', False], \
    [.81, .66, 'pc\_cov (decrease)', False], [1, 1, 'pc\_cov (100\%)', False], \
    [.5, .5, 'pc\_cov (50\%)', True], [0, 0, 'pc\_cov (edge case, no mitigation)', False], \
    [0, 1, 'pc\_cov (edge case, unrealistic)', False], [1, 0, 'pc\_cov (edge case, unrealistic)', False]:
    if (pccov_2005 == .66 and pccov_2030 == .81):
        txt += f'\n {name} & {pccov_2005*100 :.0f}\% & {pccov_2030*100 :.0f}\% & '
    else:
        txt += f'\n {name} & {pccov_2005*100 :.0f}\% & {pccov_2030*100 :.0f}\% & '
    first = int(ndc_level * pccov_2005 * emi_2005)
    second = emi_2030
    third = int(pccov_2030 * emi_2030)
    last = first + second - third
    pc = (last/emi_2030 - 1) * 100
    pc = (f'+{pc :.0f}\%' if pc > 0 else f'-{pc :.0f}\%')
    pc_refyr = (last/emi_2005 - 1) * 100
    pc_refyr = (f'+{pc_refyr :.0f}\%' if pc_refyr > 0 else f'-{pc_refyr :.0f}\%')
    txt += f'{first :.0f} & + & {second :.0f} & - & {third :.0f} & = & {last :.0f} & {pc_refyr} & {pc} \\tabularnewline '
    if hline:
        txt += '\\hline'

txt = txt[:-len('  \\tabularnewline')]

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'IND_playing_with_pccov_latex_table_RBY.csv'))

gdp_2005 = gdp_2030
emi_2005 = emi_2030

txt = '\\textbf{RBU} & \\textbf{taryr: 2030} & '
txt += '\\textbf{A} & \\textbf{+} & \\textbf{B} & \\textbf{-} & \\textbf{C} & \\textbf{=} & \\textbf{D} & '
txt += '\\textbf{E} & \\textbf{F} \\tabularnewline \\hline'

txt += f'\n Emissions (excl. LULUCF) & {emi_2030 :.0f} & & & & & & & & \\tabularnewline \\hline'

for pccov_2005, pccov_2030, name, hline in [.5, .5, 'pc\_cov (50\%)', False], \
    [.81, .81, 'pc\_cov (81\%)', False], [1, 1, 'pc\_cov (100\%)', True],  \
    [0, 0, 'pc\_cov (edge case, no mitigation)', False]:
    txt += f'\n {name} & {pccov_2030*100 :.0f}\% & '
    first = int(ndc_level * pccov_2005 * emi_2005)
    second = emi_2030
    third = int(pccov_2030 * emi_2030)
    last = first + second - third
    pc = (last/emi_2030 - 1) * 100
    pc = (f'+{pc :.0f}' if pc > 0 else f'-{pc :.0f}\%')
    txt += f'{first :.0f} & + & {second :.0f} & - & {third :.0f} & = & {last :.0f} & / & {pc} \\tabularnewline '
    if hline:
        txt += '\\hline'

txt = txt[:-len('  \\tabularnewline')]

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'IND_playing_with_pccov_latex_table_RBU.csv'))

# %%