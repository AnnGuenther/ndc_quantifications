# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.pd
Last updated in 03/2020.
"""

# %%
import pandas as pd
from pathlib import Path
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from setup_metadata import setup_metadata
import helpers_functions as hpf

# %%
def get_table(path_to_file):
    
    gwp = 'AR4'
    unit = 'MtCO2eq'
    
    # Get table and convert the units.
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        path_to_file)
    
    table.ent = (table.ent if hasattr(table, 'ent') else table.entity.replace('AR4', ''))
    table.cat = (table.cat if hasattr(table, 'cat') else table.category)
    table.__convert_unit__(unit, entity=table.ent, gwp=gwp)
    
    return table

# %%
meta = setup_metadata()

infos_from_ndcs = hpf.get_infos_from_ndcs(meta)

year = 2017

kyotoghg_ipcm0el = get_table(Path(meta.path.matlab, 'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_' + 
    meta.primap.current_version['emi'] + '.csv')).__reindex__(years=year)
global_share_2017 = 100. * kyotoghg_ipcm0el.__global_share__(years=year)

# %%
"""
Countries with ABS and AEI targets (type_calc): which part of emissions are not covered?
"""

emi_notcov = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.pc_cov, 'KYOTOGHG_IPCM0EL_NOTCOV_EMI_SSP2BLMESGBFILLED_CORR.csv')).data
emi_tot = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_SSP2BLMESGBFILLED_PMSSPBIE.csv')).data
ndcs_info = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0)
ndcs_info.loc['USA', :] = np.nan

isos_ABS_AEI = [xx for xx in ndcs_info.index if ndcs_info.loc[xx, 'TYPE_CALC'] in ['ABS', 'AEI']]

for yr in [2017, 2030]:
    print(f"% {yr}: the not-covered part of emissions for countries with ABS or AEI targets (type_calc; compared to global SSP2 emissions) is " +
          f"{100.*emi_notcov.loc[isos_ABS_AEI, yr].sum()/emi_tot.loc[:, yr].sum() :.1f}%. " +
          f"They represent {100.*emi_tot.loc[isos_ABS_AEI, yr].sum()/emi_tot.loc[:, yr].sum() :.1f}% of the global emissions.")

# %%
# Which countries have different TYPE_CALC than TYPE_ORIG?
countries_with_different_type_calc_type_orig = pd.DataFrame([[xx, infos_from_ndcs.loc[xx, 'TYPE_CALC'], infos_from_ndcs.loc[xx, 'TYPE_ORIG']]
    for xx in infos_from_ndcs.index if (infos_from_ndcs.loc[xx, 'TYPE_CALC'] != infos_from_ndcs.loc[xx, 'TYPE_ORIG'] 
    and type(infos_from_ndcs.loc[xx, 'TYPE_CALC']) == str)], columns=['iso3', 'TYPE_CALC', 'TYPE_ORIG'])
print(f'\nHow many countries have different TYPE_CALC than TYPE_ORIG: {len(countries_with_different_type_calc_type_orig):.1f}')
print(f'They represented {global_share_2017.loc[countries_with_different_type_calc_type_orig.iso3].sum().values[0]:.1f}% of global emissions in 2017.')

# %%
# EARTH 2017 values for IPCM0EL.
print(f'\nKYOTOGHG_IPCM0EL EARTH 2017 {kyotoghg_ipcm0el.data.sum().values[0]:.1f}',
    f'{kyotoghg_ipcm0el.unit} {kyotoghg_ipcm0el.gwp}') # 47649.817667 Mt CO2eq AR4.

# %%
"""
How many (I)NDCs were assessed to have the coverage 'YES' in which gas / sector.
Original and 'used' / adapted.
"""
cov_orig = pd.read_csv(Path(meta.path.preprocess, 'coverage_orig_per_gas_and_per_sector_and_combi.csv'), index_col='ISO3')
cov_used = pd.read_csv(Path(meta.path.preprocess, 'coverage_used_per_gas_and_per_sector_and_combi.csv'), index_col='ISO3')
cov_orig.loc['USA', :] = 'NO'
cov_used.loc['USA', :] = 'NO'

table_orig = pd.DataFrame(columns=['Per sector'] + meta.gases.kyotoghg, index=['Per gas'] + meta.categories.main.exclLU)
table_used = pd.DataFrame(columns=['Per sector'] + meta.gases.kyotoghg, index=['Per gas'] + meta.categories.main.exclLU)
shares_used = pd.DataFrame(columns=['Per sector'] + meta.gases.kyotoghg, index=['Per gas'] + meta.categories.main.exclLU)

for gas in meta.gases.kyotoghg:
    table_orig.loc['Per gas', gas] = len(cov_orig.index[cov_orig.loc[:, gas] == 'YES'])
    table_used.loc['Per gas', gas] = len(cov_used.index[cov_used.loc[:, gas] == 'YES'])
    
    table_gas = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.pc_cov, gas + '_IPCM0EL_COV_EMI_HISTORY_PRIMAPHIST21.csv')). \
        __reindex__(years=[2017], isos=meta.isos.EARTH).data
    table_gas.loc['USA', :] = 0.
    table_gas = table_gas.sum()
    table_ref = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', gas + '_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
        __reindex__(years=[2017], isos=meta.isos.EARTH).data.sum()
    shares_used.loc['Per gas', gas] = '('+'{:.0f}'.format(100. * table_gas.div(table_ref).values[0])+')'
    
    for cat in meta.categories.main.exclLU:
        table_orig.loc[cat, 'Per sector'] = len(cov_orig.index[cov_orig.loc[:, cat] == 'YES'])
        table_used.loc[cat, 'Per sector'] = len(cov_used.index[cov_used.loc[:, cat] == 'YES'])
        
        table_cat = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.pc_cov, 'KYOTOGHG_' + cat + '_COV_EMI_HISTORY_PRIMAPHIST21.csv')). \
            __reindex__(years=[2017], isos=meta.isos.EARTH).data
        table_cat.loc['USA', :] = 0.
        table_cat = table_cat.sum()
        table_ref = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', 'KYOTOGHG_' + cat + '_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
            __reindex__(years=[2017], isos=meta.isos.EARTH).data.sum()
        shares_used.loc[cat, 'Per sector'] =  '('+'{:.0f}'.format(100. * table_cat.div(table_ref).values[0])+')'
        
        gas_cat = gas + '_' + cat
        if gas_cat in cov_used.columns:
            table_used.loc[cat, gas] = len(cov_used.index[cov_used.loc[:, gas_cat] == 'YES'])
    
            table_gas_cat = hpf.import_table_to_class_metadata_country_year_matrix(
                Path(meta.path.pc_cov, gas + '_' + cat + '_COV_EMI_HISTORY_PRIMAPHIST21.csv')). \
                __reindex__(years=[2017], isos=meta.isos.EARTH).data
            table_gas_cat.loc['USA', :] = 0.
            table_gas_cat = table_gas_cat.sum()
            table_ref = hpf.import_table_to_class_metadata_country_year_matrix(
                Path(meta.path.preprocess, 'tables', gas + '_' + cat + '_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
                __reindex__(years=[2017], isos=meta.isos.EARTH).data.sum()
            shares_used.loc[cat, gas] = '('+'{:.0f}'.format(100. * table_gas_cat.div(table_ref).values[0])+')'

table_gas_cat = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.pc_cov, 'KYOTOGHG_IPCM0EL_COV_EMI_HISTORY_PRIMAPHIST21.csv')). \
    __reindex__(years=[2017], isos=meta.isos.EARTH).data
table_gas_cat.loc['USA', :] = 0.
table_gas_cat = table_gas_cat.sum()
table_ref = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    __reindex__(years=[2017], isos=meta.isos.EARTH).data.sum()
shares_used.loc['Per gas', 'Per sector'] = '('+'{:.0f}'.format(100. * table_gas_cat.div(table_ref).values[0])+')'

# Make a 'latex' table out of it.
txt = "(I)NDC | 'Adapted' & {\\bfseries " + \
    "} & {\\bfseries ".join([meta.gases.gas_to_label[xx] 
        if xx in meta.gases.gas_to_label.keys() else xx for xx in table_used.columns]) + \
        "} \\tabularnewline \hline \hline \n"
for cat in table_used.index:
    if cat != 'Per gas':
        txt += meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[cat]] + " & " + \
            str(table_orig.loc[cat, 'Per sector']) + " | " + str(table_used.loc[cat, 'Per sector']) + " & " + \
            " & ".join([str(table_used.loc[cat, xx]) for xx in table_used.columns[1:]]) + " \\tabularnewline \n"
    else:
        txt += cat + " & " + \
            str(table_orig.loc[cat, 'Per sector']) + " | " + str(table_used.loc[cat, 'Per sector']) + " & " + \
            " & ".join([str(table_orig.loc[cat, xx]) + " | " + str(table_used.loc[cat, xx]) for xx in table_used.columns[1:]]) + \
            " \\tabularnewline \hline \n"

txt = txt[:-len("\\tabularnewline \n")]
txt = txt.replace('nan', '--')

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'coverage_table_latex.csv'))

# Make a 'latex' table out of it. Including pc_cov.
txt = "\\textit{NDCs} | 'Adapted' (share) & {\\bfseries " + \
    "} & {\\bfseries ".join([meta.gases.gas_to_label[xx] 
    if xx in meta.gases.gas_to_label.keys() else xx for xx in table_used.columns]) + \
    "} \\tabularnewline \hline \hline \n"
for cat in table_used.index:
    
    if cat != 'Per gas':
        txt += meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[cat]] + \
            " & \\textit{" + ('~~~~' if cat == 'IPC5' else '') + \
            str(table_orig.loc[cat, 'Per sector']) + "} | " + str(table_used.loc[cat, 'Per sector']) + \
            " " + str(shares_used.loc[cat, 'Per sector']).replace(')', '\%)') + \
            " & " + \
            " & ".join([str(table_used.loc[cat, xx]) + " " + str(shares_used.loc[cat, xx]).replace(')', '\%)')
            for xx in table_used.columns[1:]]) + " \\tabularnewline \n"
    else:
        txt += cat + " & \\bfseries Total " + \
            " & " + \
            " & ".join(['\\textit{' + str(table_orig.loc[cat, xx]) + "} | " + str(table_used.loc[cat, xx]) 
            for xx in table_used.columns[1:]]) + " " + \
            " \\tabularnewline \n"
        txt += " & " + str(shares_used.loc[cat, 'Per sector']).replace(')', '\%)') + \
            " & " + \
            " & ".join([str(shares_used.loc[cat, xx]).replace(')', '\%)') 
            for xx in table_used.columns[1:]]) + \
            " \\tabularnewline \hline \n"

txt = txt[:-len("\\tabularnewline \n")]
txt = txt.replace('nan nan', '--')

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'coverage_table_latex2.csv'))

# %%
"""
What do the differences between cov_orig and cov_used result from?
How many countries have (I)NDC but do not mention the gas-coverage?
How many countries have economy-wide coverage?
For how many countries with economy-wide target are the originally covered sectors 
(excl. LULUCF and Other) not the same as the covered sectors used for the quantifications?
Which countries cover an F-gas but not the IPPU sector?
How many countries say that they cover everything (sectors (incl/exclLU/onlyLU, exclOther) / gases (incl/exclNF3))?
How many countries say that they cover CO2 + CH4 + N2O?
"""

# For cov_orig:
gases_nothing_on_coverage_isos = []
economy_wide_isos = []
economy_wide_but_differ_isos = []
cats_check = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4']
fgases_ippu_isos = []
all_sectors_covered_inclLU = []
all_sectors_covered_exclLU = []
LU_covered = []
all_gases_covered = []
all_non_fgases_covered = []
all_gases_covered_exclNF3 = []

gases_cats = meta.gases.kyotoghg + meta.categories.main.inclLU
txt = ''

for iso3 in cov_orig.index:
    
    cov_orig_iso3 = cov_orig.loc[iso3, gases_cats]
    cov_used_iso3 = cov_used.loc[iso3, gases_cats]
    
    if all([True if cov_orig_iso3[xx].upper() == 'YES' else False for xx in ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPCMLULUCF']]):
        all_sectors_covered_inclLU += [iso3]
    
    if all([True if cov_orig_iso3[xx].upper() == 'YES' else False for xx in ['IPC1', 'IPC2', 'IPCMAG', 'IPC4']]):
        all_sectors_covered_exclLU += [iso3]
    
    if cov_orig_iso3['IPCMLULUCF'].upper() == 'YES':
        LU_covered += [iso3]
    
    if all([True if cov_orig_iso3[xx].upper() == 'YES' else False for xx in meta.gases.kyotoghg]):
        all_gases_covered += [iso3]
    
    if all([True if cov_orig_iso3[xx].upper() == 'YES' else False for xx in ['CO2', 'CH4', 'N2O']]):
        all_non_fgases_covered += [iso3]
    
    if all([True if cov_orig_iso3[xx].upper() == 'YES' else False for xx in ['CO2', 'CH4', 'N2O', 'HFCS', 'PFCS', 'SF6']]):
        all_gases_covered_exclNF3 += [iso3]
    
    if (type(infos_from_ndcs.loc[iso3, 'ECONOMY_WIDE']) == str and infos_from_ndcs.loc[iso3, 'ECONOMY_WIDE'].upper() == 'YES'):
        economy_wide_isos += [iso3]
        economy_wide_true = True
        
        if cov_orig_iso3[cats_check].to_list() != cov_used_iso3[cats_check].to_list():
            economy_wide_but_differ_isos += [iso3]
        
    else:
        economy_wide_true = False
    
    if all([True if cov_orig_iso3[xx].upper() == 'NAN' else False for xx in meta.gases.kyotoghg]):
        if( type(infos_from_ndcs.loc[iso3, 'NDC_INDC']) == str and infos_from_ndcs.loc[iso3, 'NDC_INDC'] in ['NDC', 'INDC']):
            txt += f'\n{iso3}: all gases are NaN.'
            gases_nothing_on_coverage_isos += [iso3]
    for gas_cat in gases_cats:
        if (cov_used_iso3[gas_cat] == 'YES' and cov_orig_iso3[gas_cat] != 'YES' and gas_cat != 'IPC5'):
            txt += f'\n{iso3}: {gas_cat}: orig {cov_orig_iso3[gas_cat]}, used {cov_used_iso3[gas_cat]}. '
            if (gas_cat in meta.categories.main.inclLU and economy_wide_true):
                txt += 'The country has economy-wide coverage.'
    
    if (any([True if cov_orig_iso3[xx] == 'YES' else False for xx in meta.gases.fgases])
        and cov_orig_iso3['IPC2'] != 'YES'):
        fgases_ippu_isos += [iso3]

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'why_cov_used_differs_from_cov_orig.txt'))

print(f"\n% {len(gases_nothing_on_coverage_isos)} countries have an (I)NDC, but we assessed there to be no information on covered gases.")
print(f"% These are {', '.join(gases_nothing_on_coverage_isos)}.")
print(f"% They represented {global_share_2017.loc[gases_nothing_on_coverage_isos].sum().values[0] :.1f}% of global KYOTOGHGAR4_IPCM0EL emissions in 2017.")
gases_nothing_on_coverage_highest_share = global_share_2017.loc[gases_nothing_on_coverage_isos].sort_values(by=2017, ascending=False)
print(f"% {gases_nothing_on_coverage_highest_share.index[0]} had the highest share of these countries " +
      f"({gases_nothing_on_coverage_highest_share.loc[gases_nothing_on_coverage_highest_share.index[0]].values[0] :.1f}%).")

print(f"\n% {len(economy_wide_isos)} countries have an economy-wide (I)NDC.")
print(f"% These are {', '.join(economy_wide_isos)}.")
print(f"% They represented {global_share_2017.loc[economy_wide_isos].sum().values[0] :.1f}% of global KYOTOGHGAR4_IPCM0EL emissions in 2017.")

print(f"\n% {len(economy_wide_but_differ_isos)} countries have economy-wide targets but the values for " +
      f"{', '.join(cats_check)} differ between 'cov_orig' and 'cov_used'.")
print(f"% These are {', '.join(economy_wide_but_differ_isos)}.")
print(f"% They represented {global_share_2017.loc[economy_wide_but_differ_isos].sum().values[0] :.1f}% of global KYOTOGHGAR4_IPCM0EL emissions in 2017.")

print(f"\n% {len(fgases_ippu_isos)} countries cover one out of {', '.join(meta.gases.fgases)} " +
      "but do not cover IPPU (based on cov_orig).")
print(f"% These are {', '.join(fgases_ippu_isos)}.")
print(f"% They represented {global_share_2017.loc[fgases_ippu_isos].sum().values[0] :.1f}% of global KYOTOGHGAR4_IPCM0EL emissions in 2017.")

for what, isos in \
    ['all sectors (excl Other, inclLU) are covered', all_sectors_covered_inclLU], \
    ['all sectors (excl Other, exclLU) are covered', all_sectors_covered_exclLU], \
    ['LU is covered', LU_covered], \
    ['all gases are covered', all_gases_covered], \
    ['all gases (excl NF3) are covered', all_gases_covered_exclNF3], \
    ['all non-F-gases are covered', all_non_fgases_covered]:
    print(f"\n% {len(isos)} countries have {what} (based on cov_orig).")
    #print(f"% These are {', '.join(isos)}.")
    print(f"% They represented {global_share_2017.loc[isos].sum().values[0] :.1f}% of global KYOTOGHGAR4_IPCM0EL emissions in 2017.")

# %%
# 10 biggest emitters in 2017.
share_sorted = global_share_2017.sort_values(by=2017, ascending=False)
biggest_10 = share_sorted.index[:10].to_list()
print(f'\n% 10 biggest emitters in 2017 (share of KYOTOGHGAR4_IPCM0EL emissions; ordered): {", ".join(biggest_10)}')
print(f'% Global share: {share_sorted.loc[biggest_10].sum().values[0] :.1f}%')

# Counting EU28 as one.
share_sorted_EU28 = deepcopy(share_sorted)
share_sorted_EU28.loc['EU28', 2017] = share_sorted_EU28.loc[meta.isos.EU28, 2017].sum()
share_sorted_EU28.drop(index=meta.isos.EU28, inplace=True)
share_sorted_EU28 = share_sorted_EU28.sort_values(by=2017, ascending=False)
biggest_10_EU28 = share_sorted_EU28.index[:10].to_list()
print(f'% Counting EU28 as one: 10 biggest emitters in 2017 (share of KYOTOGHGAR4_IPCM0EL emissions; ordered): {", ".join(biggest_10_EU28)}')
print(f'% Global share: {share_sorted_EU28.loc[biggest_10_EU28].sum().values[0] :.1f}%')

# %%
# Estimate the impact of different GWPs.
# Globally:
kyotoghg_ipcm0el_AR2 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.matlab, 'KYOTOGHGAR2_IPCM0EL_TOTAL_NET_HISTCR_' + 
    meta.primap.current_version['emi'] + '.csv')).__reindex__(years=year).__reindex__(isos=meta.isos.EARTH)
earth_ar2 = kyotoghg_ipcm0el_AR2.data.sum().values[0]
print(f'\nEARTH 2017 KYOTOGHGAR2_IPCM0EL {earth_ar2 :.1f}',
    f'{kyotoghg_ipcm0el_AR2.unit} {kyotoghg_ipcm0el_AR2.gwp}')
earth_ar4 = kyotoghg_ipcm0el.data.reindex(index=meta.isos.EARTH).sum().values[0]
print(f'EARTH 2017 KYOTOGHGAR4_IPCM0EL {earth_ar4 :.1f}',
    f'{kyotoghg_ipcm0el.unit} {kyotoghg_ipcm0el.gwp}')
print(f'Percentage difference regarding AR2: {100*(earth_ar4-earth_ar2)/earth_ar2 :.1f}%')

# Per country:
pc_diff_per_country = 100*kyotoghg_ipcm0el.data.reindex(index=meta.isos.EARTH).add(-kyotoghg_ipcm0el_AR2.data).div(
    kyotoghg_ipcm0el_AR2.data)
pc_diff_per_country.drop(index=pc_diff_per_country.index[pc_diff_per_country.loc[:, 2017].isnull()], inplace=True)
pc_diff_sorted = pc_diff_per_country.sort_values(by=2017)
print(f'Maximal percentage difference (per-country): {pc_diff_sorted.loc[pc_diff_sorted.index[-1]].values[0] :.1f}%',
    f'({pc_diff_sorted.index[-1]})')
print(f'Minimal percentage difference (per-country): {pc_diff_sorted.loc[pc_diff_sorted.index[0]].values[0] :.1f}%',
    f'({pc_diff_sorted.index[0]})')

# Per country - only biggest 10:
pc_diff_per_country = 100*kyotoghg_ipcm0el.data.reindex(index=biggest_10).add(
    -kyotoghg_ipcm0el_AR2.data.loc[biggest_10, :]).div(
    kyotoghg_ipcm0el_AR2.data.loc[biggest_10, :])
pc_diff_per_country.drop(index=pc_diff_per_country.index[pc_diff_per_country.loc[:, 2017].isnull()], inplace=True)
pc_diff_sorted = pc_diff_per_country.sort_values(by=2017)
print('For biggest 10 emitting countries (EU28 as single countries), 2017:')
print(f'Maximal percentage difference (per-country): {pc_diff_sorted.loc[pc_diff_sorted.index[-1]].values[0] :.1f}%',
    f'({pc_diff_sorted.index[-1]})')
print(f'Minimal percentage difference (per-country): {pc_diff_sorted.loc[pc_diff_sorted.index[0]].values[0] :.1f}%',
    f'({pc_diff_sorted.index[0]})')

# %%
print("\nSSPs: missing data.")
# For which countries are no SSP data available, and which share of 2017 emissions / population / gdp do they stand for.
# For how many countries SSP data are available for some SSPs, and not for others?
emi_primap = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
    'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')).__reindex__(isos=meta.isos.EARTH)
pop_primap = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
    'POP_DEMOGR_TOTAL_NET_HISTORY_PMHSOCIOECO21.csv')).__reindex__(isos=meta.isos.EARTH)
gdp_primap = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
    'GDPPPP_ECO_TOTAL_NET_HISTORY_PMHSOCIOECO21.csv')).__reindex__(isos=meta.isos.EARTH)
emi_global_share_2017 = 100. * emi_primap.__global_share__(years=year)
pop_global_share_2017 = 100. * pop_primap.__global_share__(years=year)
gdp_global_share_2017 = 100. * gdp_primap.__global_share__(years=year)
# Maximal share:
max_emi = 0
max_pop = 0
max_gdp = 0
# No data available:
keep_countries_emi = {}
keep_countries_pop = {}
keep_countries_gdp = {}

for ssp in meta.ssps.scens.long:
    emi_ssp = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
        'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_' + ssp + '_PMSSPBIE.csv')).__reindex__(isos=meta.isos.EARTH)
    pop_ssp = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
        'POP_DEMOGR_TOTAL_NET_' + ssp + '_PMSSPBIEMISC.csv')).__reindex__(isos=meta.isos.EARTH)
    gdp_ssp = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
        'GDPPPP_ECO_TOTAL_NET_' + ssp + '_PMSSPBIEMISC.csv')).__reindex__(isos=meta.isos.EARTH)
    # Which countries have no future data?
    emi_ssp_no_data = emi_ssp.data.index[emi_ssp.data.loc[:, range(2020, 2051)].isnull().all(axis=1)].to_list()
    pop_ssp_no_data = pop_ssp.data.index[pop_ssp.data.loc[:, range(2020, 2051)].isnull().all(axis=1)].to_list()
    gdp_ssp_no_data = gdp_ssp.data.index[gdp_ssp.data.loc[:, range(2020, 2051)].isnull().all(axis=1)].to_list()
    # Keep the countries.
    keep_countries_emi[ssp] = emi_ssp_no_data
    keep_countries_pop[ssp] = pop_ssp_no_data
    keep_countries_gdp[ssp] = gdp_ssp_no_data
    # Which global share do they have - in 2017?
    emi_share = emi_global_share_2017.loc[emi_ssp_no_data].sum().values[0]
    pop_share = pop_global_share_2017.loc[pop_ssp_no_data].sum().values[0]
    gdp_share = gdp_global_share_2017.loc[gdp_ssp_no_data].sum().values[0]
    # Maximal shares.
    max_emi = max([max_emi, emi_share])
    max_pop = max([max_pop, pop_share])
    max_gdp = max([max_gdp, gdp_share])
    
    print('%', ssp, 'sum over global shares of countries without data (share for 2017)')
    print(f"% emi: {emi_share :.1f}% ({len(emi_ssp_no_data)} counties, {', '.join(emi_ssp_no_data)})")
    print(f"% pop: {pop_share :.1f}% ({len(pop_ssp_no_data)} counties, {', '.join(pop_ssp_no_data)})")
    print(f"% gdp: {gdp_share :.1f}% ({len(gdp_ssp_no_data)} counties, {', '.join(gdp_ssp_no_data)})\n")

print(f"% Maximal total shares (sum over all countries with missing data): emi {max_emi :.1f}%, pop {max_pop :.1f}%, gdp {max_gdp :.1f}%")

# Which countries are not in all keep_countries_emi[ssp]?
def print_isos_with_data_in_some_ssps(keep_countries):
    isos = []
    for iso3 in meta.isos.EARTH:
        available = []
        for ssp in keep_countries.keys():
            if iso3 in keep_countries[ssp]:
                available.append(ssp)
        
        if (len(available) > 0 and len(available) < len(keep_countries.keys())):
            isos.append(iso3)
    
    return isos

ctrs_emi = print_isos_with_data_in_some_ssps(keep_countries_emi)
ctrs_pop = print_isos_with_data_in_some_ssps(keep_countries_pop)
ctrs_gdp = print_isos_with_data_in_some_ssps(keep_countries_gdp)
print(f"% {len(ctrs_emi)} countries with data in some SSPs, but not in all (emi): {', '.join(ctrs_emi)} " +
      f"with total global share of {emi_global_share_2017.loc[ctrs_emi].sum().values[0] :.2f}%.")
print(f"% {len(ctrs_pop)} countries with data in some SSPs, but not in all (pop): {', '.join(ctrs_pop)} " +
      f"with total global share of {pop_global_share_2017.loc[ctrs_pop].sum().values[0] :.2f}%.")
print(f"% {len(ctrs_gdp)} countries with data in some SSPs, but not in all (gdp): {', '.join(ctrs_gdp)} " +
      f"with total global share of {gdp_global_share_2017.loc[ctrs_gdp].sum().values[0] :.2f}%.")

# %%
"""
What are the differences between the original SSP EARTH values and the 'filled' ones.
"""
print("\nDifferences between SSP EARTH and filled data.")

ssps = meta.ssps.scens.long

for what in ['emissions', 'population', 'GDP (PPP)']:
    
    print(f'EARTH {what} from filled time series are xx higher than from the originals:')
    
    for ssp in ssps:
        
        if what == 'emissions':
            table_f = f'KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp}FILLED_PMSSPBIE.csv'
            table_o = f'KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp}_PMSSPBIE.csv'
        
        elif what == 'population':
            table_f = f'POP_DEMOGR_TOTAL_NET_{ssp}FILLED_PMSSPBIEMISC.csv'
            table_o = f'POP_DEMOGR_TOTAL_NET_{ssp}_PMSSPBIEMISC.csv'
        
        elif what == 'GDP (PPP)':
            table_f = f'GDPPPP_ECO_TOTAL_NET_{ssp}FILLED_PMSSPBIEMISC.csv'
            table_o = f'GDPPPP_ECO_TOTAL_NET_{ssp}_PMSSPBIEMISC.csv'
        
        filled = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', table_f))
        filled = filled.data.loc[:, 2030].reindex(index=meta.isos.EARTH).sum()
        orig = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', table_o))
        orig = orig.data.loc[:, 2030].reindex(index=meta.isos.EARTH).sum()
        
        print(f'    {ssp}: {100. * filled/orig - 100. :.1f}%')

# %%
# Contribution of FGASES to KYOTOGHG in 2017, and %share of HFCs, PFCs, SF6 and NF3.
# Globally and per country.
fgases = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
    'FGASESAR4_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
    __reindex__(years=[year], isos=meta.isos.EARTH)
for gas in ['FGASES', 'HFCS', 'PFCS', 'SF6', 'NF3']:
    gas_act = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
        gas + 'AR4_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
        __reindex__(years=[year], isos=meta.isos.EARTH)
    if gas == 'FGASES':
        share_act = 100 * gas_act.data.div(kyotoghg_ipcm0el.__reindex__(isos=meta.isos.EARTH).data)
        share_act.sort_values(by=2017, ascending=False, inplace=True)
        print(f"% The maximum share of {gas} in 2017 is {share_act.loc[share_act.index[0]].values[0] :.1f}% of national KYOTOGHGAR4_IPCM0EL for {share_act.index[0]}.")
        print(f"%     The global share of {gas} in 2017 is {(100. * gas_act.data.sum()/kyotoghg_ipcm0el.data.sum().values[0]).values[0] :.1f}% of total KYOTOGHGAR4_IPCM0EL.")
    else:
        share_act = 100 * gas_act.data.div(fgases.__reindex__(isos=meta.isos.EARTH).data)
        share_act.sort_values(by=2017, ascending=False, inplace=True)
        print(f"% The maximum share of {gas} in 2017 is {share_act.loc[share_act.index[0]].values[0] :.1f}% of national FGASESAR4_IPCM0EL for {share_act.index[0]}.")
        print(f"%     The global share of {gas} in 2017 is {(100. * gas_act.data.sum()/fgases.data.sum().values[0]).values[0] :.1f}% of total FGASESAR4_IPCM0EL.")
    
# %%
# Covered part of emissions: globally.
# Pay attention to the countries that do not have (I)NDCs.
ndcs = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0).reindex(index=meta.isos.EARTH)
countries_without_indc = [xx for xx in meta.isos.EARTH if (type(ndcs.loc[xx, 'NDC_INDC']) != str or ndcs.loc[xx, 'NDC_INDC'] not in ['NDC', 'INDC'])]
countries_with_indc = [xx for xx in meta.isos.EARTH if (type(ndcs.loc[xx, 'NDC_INDC']) == str and ndcs.loc[xx, 'NDC_INDC'] in ['NDC', 'INDC'])]

years_cov = [1990, 2000, 2010, 2017, 2020, 2030]

emi_cov = 1e-3 * hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.pc_cov,
    'KYOTOGHG_IPCM0EL_COV_EMI_SSP2BLMESGBFILLED_CORR.csv')).__reindex__(isos=meta.isos.EARTH, years=years_cov). \
    data.loc[countries_with_indc, :].sum()
emi_tot = kyotoghg_ipcm0el = 1e-3 * get_table(Path(meta.path.preprocess, 'tables', 
    'KYOTOGHG_IPCM0EL_TOTAL_NET_SSP2BLMESGB_PMSSPBIE.csv')).__reindex__(isos=meta.isos.EARTH, years=years_cov). \
    data.sum()
pc_cov = 100. * emi_cov.div(emi_tot)

# Create latex table with emi_tot, emi_cov and pc_cov.
txt = 'Year & ' + ' & '.join([str(xx) for xx in years_cov]) + " \\\\ \n" + \
    'Total emissions (Gg CO$_2$eq AR4) & ' + ' & '.join(['{:.1f}'.format(xx) for xx in emi_tot]) + " \\\\ \n" + \
    'Covered emissions (Gg CO$_2$eq AR4) & ' + ' & '.join(['{:.1f}'.format(xx) for xx in emi_cov]) + " \\\\ \n" + \
    'Share of covered emissions (\%) & ' + ' & '.join(['{:.1f}'.format(xx) for xx in pc_cov])

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'covered_emissions_table_latex.csv'))

# %%
"""
For how many countries are CO2_IPC1 emissions the major share of national emissions?
And how much is the total share of these countries on global KYOTOGHG_IPCM0EL emissions?
Which are the second and third most important ent_cat combis?
"""
print("\nCO2_IPC1")
nat_share = pd.read_csv(Path(meta.path.main, 'data', 'other', 'national_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)
nat_share.drop(columns=[xx for xx in nat_share.columns if ('KYOTOGHG' in xx or 'IPCM0EL' in xx)], inplace=True)
nat_share = nat_share.loc[meta.isos.EARTH, :]
co2_ipc1 = [xx for xx in nat_share.index if nat_share.loc[xx, 'CO2_IPC1'] == nat_share.loc[xx, :].max()]
max_combis = pd.Series([nat_share.loc[xx, :].sort_values(ascending=False).index[0] for xx in nat_share.index], index=nat_share.index)

share_per_gas_per_sec = pd.read_csv(Path(meta.path.main, 'data', 'other', 'share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)

shares = pd.DataFrame(index=max_combis.unique(), columns=['countries', 'share'])
for ind in shares.index:
    shares.loc[ind, 'countries'] = len(max_combis[max_combis == ind])
    shares.loc[ind, 'share'] = share_per_gas_per_sec.loc[[xx for xx in max_combis.index if max_combis[xx] == ind], ind].sum()

shares.sort_values(by=['countries'], ascending=False, inplace=True)
for ind in shares.index[:4]:
    print(f"In 2017, {shares.loc[ind, 'countries']} countries had their highest share of " + \
          f"national KYOTOGHG_IPCM0EL emissions from {ind}, representing {shares.loc[ind, 'share'] :.2f}% " + \
              "of global KYOTOGHG_IPCM0EL emissions.")

# %%
"""
LULUCF data source: how many countries per source.
"""
print("\nLULUCF data sources.")
lulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv'))
lulucf_source = lulucf.note
data_tot = lulucf.data.reindex(index=meta.isos.EARTH).loc[:, 2017].sum()
lulucf_split = lulucf_source.split('. ')[-1].split('; ')

overview = {}
for txt in lulucf_split:
    srce, isos = txt.split(': ')[0], txt.split(': ')[-1].split(', ')
    data_sum = lulucf.data.loc[isos, 2017].sum()
    txt_act = f"% {srce}: {len(isos)} countries" + \
        f"\n% {srce}: {data_sum :.0f} Mt CO2eq AR4 in 2017 ({100.*data_sum/data_tot :.0f}%)." + \
        f"\n% {srce}: {', '.join(isos)}"
    print(txt_act)
    overview[srce] = f'{len(isos)} countries ({data_sum :.1f}~Mt~CO$_2$eq)'

# %%
"""
Share of PFCS + SF6 + NF3 in VCT national emissions.
"""

nat_share = pd.read_csv(
    Path(meta.path.main, 'data', 'other', 'national_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0). \
    loc['VCT', :]

print("\nShare of PFCS + SF6 + NF3 in VCT.", nat_share[['PFCS_IPCM0EL', 'SF6_IPCM0EL', 'NF3_IPCM0EL']])

# %%
"""
Plot the baseline emissions and the mitigated pathways (EARTH) for type_calc and type_orig, and for 100% coverage and real coverage.
Per SSP.
"""

folders_calc = [
    'ndc_quantifications_20200628_2218_SSP1_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2120_SSP2_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2229_SSP3_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2243_SSP4_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2258_SSP5_typeCalcForAllCountries']
folders_calc100 = [
    'ndc_quantifications_20200628_2221_SSP1pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2122_SSP2pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2234_SSP3pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2248_SSP4pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2301_SSP5pccov100ForAllCountries_typeCalcForAllCountries']

folders_orig = [
    'ndc_quantifications_20200702_0834_SSP1_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0829_SSP2_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0839_SSP3_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0844_SSP4_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0848_SSP5_typeOrigForAllCountries']
folders_orig100 = [
    'ndc_quantifications_20200702_0836_SSP1_pccov100ForAllCountries_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0830_SSP2_pccov100ForAllCountries_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0840_SSP3_pccov100ForAllCountries_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0845_SSP4_pccov100ForAllCountries_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0849_SSP5_pccov100ForAllCountries_typeOrigForAllCountries']

years_int = list(range(1990, 2030))
years_str = [str(xx) for xx in years_int]

fig = plt.figure(figsize=(10, 10))

for ssp, count in zip(meta.ssps.scens.short, range(len(folders_calc))):
    
    ax_calc = fig.add_subplot(2, 2, 1)
    ax_orig = fig.add_subplot(2, 2, 2)
    ax_calc_100 = fig.add_subplot(2, 2, 3)
    ax_orig_100 = fig.add_subplot(2, 2, 4)
    
    for folder, axa, title in [folders_calc, ax_calc, 'calc'], [folders_orig, ax_orig, 'orig'], \
        [folders_calc100, ax_calc_100, 'calc 100%'], [folders_orig100, ax_orig_100, 'orig 100%']:
        
        data = pd.read_csv(
            Path(meta.path.output, folder[count], 'ndc_targets_pathways_per_group.csv'))
        data = data.loc[(data.group == 'EARTH') & (data.condi.isin(['emi_bau', 'unconditional', 'conditional']))]
        for ind in data.index:
            axa.plot(years_int, data.loc[ind, years_str].values, label=f"{data.condi[ind]}_{data.rge[ind]}")
        
        axa.set_title(title, fontweight='bold')
        axa.legend(loc='upper left')
        
    fig.savefig(Path(meta.path.main, 'plots', 'test', f"{ssp}.png"), dpi=300)
    plt.clf()

plt.close(fig)

"""
How many countries have uncondi_worst above baseline, and for which targets?
"""

for ssp, count in zip(meta.ssps.scens.short, range(len(folders_calc))):
    
    for folder, title in [folders_calc, 'calc'], [folders_orig, 'orig'], \
        [folders_calc100, 'calc 100%'], [folders_orig100, 'orig 100%']:
            
        tars_above_bl = []
        
        data = pd.read_csv(
            Path(meta.path.output, folder[count], 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
        
        for iso3 in sorted(data.iso3.unique()):
            
            data_iso3= data.loc[(data.iso3 == iso3) & (data.condi.isin(['emi_bau', 'unconditional']))]
            
            if data_iso3.loc[(data_iso3.condi == 'unconditional') & (data_iso3.rge == 'worst'), '2030'].values[0] \
                > data_iso3.loc[(data_iso3.condi == 'emi_bau'), '2030'].values[0]:
                tars_above_bl += [[xx for xx in data_iso3.tar_type_used.unique() if type(xx) == str][0]]
        
        print("%", ssp, title, len(tars_above_bl), ', '.join(sorted(tars_above_bl)))

# %%
"""
Countries for which the second attempt for tar_exclLU from tar_inclLU was needed.
And countries for which ABU_exclLU lead to negative tar_exclLU.
What were their contributions to 2017 emissions.
For input_SSP2_pccov100ForAllCountries_typeCalcForAllCountries.
"""

iso3_2ndTry = ['BDI', 'ISL', 'KNA', 'NAM', 'PRK', 'PRY', 'SLB']
iso3_ABU = ['URY', 'TON']
emi = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv'))
emitot = emi.data.reindex(index=meta.isos.EARTH).loc[:, 2017].sum()
print(f"tar_exclLU from tar_inclLU second try: {emi.data.loc[iso3_2ndTry, 2017].sum()/emitot*100 :.1f}% of global 2017 emissions (ipcm0el).")
print(f"tar_exclLU negative from ABU_exclLU: {emi.data.loc[iso3_ABU, 2017].sum()/emitot*100 :.1f}% of global 2017 emissions (ipcm0el).")

# URY: type_calc and type_orig are not ABU.
print(f"tar_exclLU negative from ABU_exclLU: {emi.data.loc['TON', 2017]/emitot*100 :.3f}% of global 2017 emissions (ipcm0el).")

# %%
"""
How many countries for which 100% coverage targets are worse than estimated coverage targets?
SSP2 type_calc and type_orig.
"""
print("Countries with higher condi_best 2030 values for 100% coverage than for estimated coverage.")

folders_calc = [
    'ndc_quantifications_20200628_2218_SSP1_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2120_SSP2_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2229_SSP3_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2243_SSP4_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2258_SSP5_typeCalcForAllCountries']
folders_calc100 = [
    'ndc_quantifications_20200628_2221_SSP1pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2122_SSP2pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2234_SSP3pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2248_SSP4pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200628_2301_SSP5pccov100ForAllCountries_typeCalcForAllCountries']

folders_orig = [
    'ndc_quantifications_20200702_0834_SSP1_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0829_SSP2_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0839_SSP3_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0844_SSP4_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0848_SSP5_typeOrigForAllCountries']
folders_orig100 = [
    'ndc_quantifications_20200702_0836_SSP1_pccov100ForAllCountries_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0830_SSP2_pccov100ForAllCountries_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0840_SSP3_pccov100ForAllCountries_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0845_SSP4_pccov100ForAllCountries_typeOrigForAllCountries',
    'ndc_quantifications_20200702_0849_SSP5_pccov100ForAllCountries_typeOrigForAllCountries']

for condi, rge in ['unconditional', 'worst'], ['conditional', 'best']:
    
    print(f"\n{condi}, {rge}")
    
    for ssp, count in zip(meta.ssps.scens.short, range(len(folders_calc))):
        print(f"\n{ssp}")
        for folder, folder100, what in \
            [folders_calc[count], folders_calc100[count], 'type_calc'], \
            [folders_orig[count], folders_orig100[count], 'type_orig']:
            print(f"\n{what}")
            data = pd.read_csv(
                Path(meta.path.output, folder, 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
            data100 = pd.read_csv(
                Path(meta.path.output, folder100, 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
            isos = ""
            for iso3 in data.iso3.unique():
                if data100.loc[(data100.iso3 == iso3) & (data100.condi == condi) & (data100.rge == rge), '2030'].values[0] \
                    > data.loc[(data.iso3 == iso3) & (data.condi == condi) & (data.rge == rge), '2030'].values[0]:
                    isos += f", {iso3}"
            print(isos)

# %%
"""
EARTH 2017 values for LULUCF (sum, all negatives, all positives).
And with FAO prioritisation.
"""

year_lu = 2017
print(f"Global Kyoto GHG LULUCF, {year_lu}")

# Latex table.
txt = f"Prioritised data sources & Total & Net sources & Net sinks  & {year_lu :.0f} \\\\ \\hline \n"

for fao in ['', 'UNFCCC', 'FAO']:
    
    print(f"\nVARIOUS{fao}")
    
    lulucf = get_table(Path(meta.path.preprocess, 'tables', f'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS{fao}.csv')). \
        __reindex__(isos=meta.isos.EARTH).__reindex__(years=year_lu)
    
    print(f'all together: {1/1000*lulucf.data.sum().values[0]:.1f} GgCO2eq AR4')
    print(f'all positive: {1/1000*lulucf.data[lulucf.data > 0.].sum().values[0]:.1f} GgCO2eq AR4')
    print(f'all negative: {1/1000*lulucf.data[lulucf.data < 0.].sum().values[0]:.1f} GgCO2eq AR4')
    
    if fao == '':
        txt += "CRF, BUR, UNFCCC, FAO"
    elif fao == 'FAO':
        txt += "FAO, CRF, BUR, UNFCCC"
    elif fao == 'UNFCCC':
        txt += "UNFCCC, CRF, BUR, FAO"
    
    txt += f" & {1/1000*lulucf.data.sum().values[0]:.1f}"
    txt += f" & {1/1000*lulucf.data[lulucf.data > 0.].sum().values[0]:.1f}"
    txt += f" & {1/1000*lulucf.data[lulucf.data < 0.].sum().values[0]:.1f}"
    txt += " & Gg~CO$_2$eq (AR4) \\\\ \n"

kyotoghg_ipcm0el_act = get_table(Path(meta.path.matlab, 'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_' + 
    meta.primap.current_version['emi'] + '.csv')).__reindex__(years=year_lu)
print(f'\nGlobal Kyoto GHG IPCM0EL {1/1000*kyotoghg_ipcm0el_act.data.sum().values[0]:.1f} GgCO2eq AR4')

hpf.write_text_to_file(txt[:-2], Path(meta.path.main, 'data', 'other', 'lulucf_comparison_of_prio_EARTH_AR4_GgCO2eq_latex.txt'))

# %%