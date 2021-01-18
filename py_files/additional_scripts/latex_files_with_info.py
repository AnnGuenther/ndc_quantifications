# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 11/2020.
"""

# %%
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
# Get general information.

meta = setup_metadata()

path_out = Path(meta.path.main, 'latex_files')
Path(path_out).mkdir(parents=True, exist_ok=True)

units = meta.units.default

infos_from_ndcs = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0)

tar_to_long = {
    'ABS': "absolute emissions target",
    'RBY': "relative reduction against base year emissions",
    'RBU': "relative reduction compared to Business-As-Usual",
    'ABU': "absolute reduction compared to Business-As-Usual",
    'REI': "relative emissions intensity reduction",
    'AEI': "absolute emissions intensity target",
    'NGT': "non-GHG target"}

tars_nonABS = set(set(tar_to_long.keys()) - set(['ABS']))

gwps = hpf.get_gwps_for_gases('all', meta.gwps.default)
hfcs = hpf.get_members_of_basket('HFCS')
pfcs = hpf.get_members_of_basket('PFCS')

colours = {}
path_to_colours = Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours')
colours['ssps'] = pd.read_csv(Path(path_to_colours, 'colours_ssps.csv'), index_col=0)
colours['cats'] = pd.read_csv(Path(path_to_colours, 'colours_categories_ipc.csv'), index_col=0)
colours['gases'] = pd.read_csv(Path(path_to_colours, 'colours_gases.csv'), index_col=0)
# LULUCF
cmp = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colourmap_viridis.csv'))
lulucf_prios = meta.lulucf.source_prioritisation
colours['lulucf'] = cmp.loc[list(range(0, cmp.index[-1], int(np.ceil(cmp.index[-1]/(len(meta.lulucf.source_prioritisation)-1))))) + [cmp.index[-1]]]
colours['lulucf'].index = meta.lulucf.source_prioritisation
colours['lulucf'].loc['CHOSEN', :] = (1, 0, 1)
                
colour_100pc = (0, .7, .5)
colour_estpc = (.3, .3, .3)
colour_prioNDCs = (.5, .7, 0)
colour_prioSSPs = (.7, .7, .7)

ssps_linestyle = {'SSP1': '--', 'SSP2': '-', 'SSP3': '--', 'SSP4': ':', 'SSP5': ':'}    

links = pd.read_csv(Path(meta.path.main, 'infos', 'links_to_interesting_country_info.csv'))

info_lulucf_chosen = pd.read_csv(
    Path(meta.path.preprocess, 'info_per_country.csv'), index_col=0). \
    loc[:, 'lulucf_source']

isos_annexi = hpf.get_isos_for_groups('ANNEXI', 'ISO3')
isos_nonannexi = set(set(meta.isos.EARTH) - set(isos_annexi))

# %%
# Covered sectors and gases.

cov_ndcs = pd.read_csv(Path(meta.path.preprocess, 'coverage_orig_per_gas_and_per_sector_and_combi.csv'), index_col=[0]).astype(str)
cov_used = pd.read_csv(Path(meta.path.preprocess, 'coverage_used_per_gas_and_per_sector_and_combi.csv'), index_col=[0]).astype(str)

dct = {'ndcs': cov_ndcs, 'used': cov_used}

for attr in dct.keys():
    
    # Replace yes by +, no by - and nan by /.
    act = dct[attr]
    act[act.isin(['YES', 'yes', 'Yes'])] = '+'
    act[act.isin(['NO', 'no', 'No'])] = '--'
    act[act.isin(['NAN', 'nan', 'NaN'])] = '/'

secs_check = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4']
gases_check = meta.gases.kyotoghg

# %%
# Get SSP data (historical years == PRIMAP data).

tables = hpf.create_class(name='tables')

# Emissions, GDP and POP.
# SSP for overview: SSP2.
ssp2_short = 'SSP2'
ssp2_long = [xx for xx in meta.ssps.scens.long if 'SSP2' in xx][0]

for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
    
    tables_to_add = {
        f"{ssp_short}_emi": f'KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp_long}FILLED_PMSSPBIE',
        f"{ssp_short}_gdp": f'GDPPPP_ECO_TOTAL_NET_{ssp_long}FILLED_PMSSPBIEMISC',
        f"{ssp_short}_pop": f'POP_DEMOGR_TOTAL_NET_{ssp_long}FILLED_PMSSPBIEMISC'}
    
    for tpe in tables_to_add.keys():
        table = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', tables_to_add[tpe] + '.csv')). \
                    __convert_to_baseunit__().__reindex__(index=meta.isos.EARTH)
        if tpe == f'{ssp_short}_emi':
            setattr(tables, tpe, table.__change_gwp__(meta.gwps.default))
        else:
            setattr(tables, tpe, table)
    
    # emi/GDP, emi/capita.
    setattr(tables, f"{ssp_short}_emi_gdp", hpf.combine_tables('divide', 
        [getattr(tables, f"{ssp_short}_emi"), getattr(tables, f"{ssp_short}_gdp")]))
    setattr(tables, f"{ssp_short}_emi_pop", hpf.combine_tables('divide', 
        [getattr(tables, f"{ssp_short}_emi"), getattr(tables, f"{ssp_short}_pop")]))

# Global share.
for case in ['SSP2_emi', 'SSP2_gdp', 'SSP2_pop', 'SSP2_emi_gdp', 'SSP2_emi_pop']:
    share = hpf.copy_table(getattr(tables, case))
    share.data = share.data.div(share.data.reindex(index=meta.isos.EARTH).sum(axis=0))
    share.unit = share.unit + ' / ' + share.unit
    setattr(tables, case + '_share', share)

# Get data per gas and category.

for gas in ['KYOTOGHG'] + meta.gases.kyotoghg:
    
    setattr(tables, f"{gas}_IPCM0EL", hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
        gas + '_IPCM0EL_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))
    
    if gas in meta.gases.fgases:
        table_code = gas + '_IPCM0EL_TOTAL_NET_' + meta.ssps.scens.long[1] + 'FILLED_SSPSPLIT.csv'
    else:
        table_code = gas + '_IPCM0EL_TOTAL_NET_' + meta.ssps.scens.long[1] + 'FILLED_' + meta.ssps.emi['srce'] + '.csv'
    
    setattr(tables, f"SSP2_{gas}", hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', table_code)). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

for cat in ['IPCM0EL'] + meta.categories.main.inclLU:
    setattr(tables, f"KYOTOGHG_{cat}", hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
        'KYOTOGHG_' + cat + '_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

for cat in ['IPC1A', 'IPC1B', 'IPCMAGELV', 'IPC3A']:
    table = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.matlab, 
        f'KYOTOGHGAR4_{cat}_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv'))
    table.__attrs_primap_to_ndcs__()
    setattr(tables, f"KYOTOGHG_{cat}", table. \
        __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))    

for ssp in meta.ssps.scens.long:
    setattr(tables, f"{ssp[:4]}_emi", hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
        'KYOTOGHG_IPCM0EL_TOTAL_NET_' + ssp + 'FILLED_PMSSPBIE.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# TODO: calculate rvalues for the combinations, which entity+category does have most influence on the trend in the total emissions?

combis_KYOTOGHG = [f'KYOTOGHG_{xx}' for xx in ['IPCM0EL'] + meta.categories.main.exclLU]
for combi in combis_KYOTOGHG:
    setattr(tables, combi, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', combi + '_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
            __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

combis_IPCM0EL = [f'{xx}_IPCM0EL' for xx in ['KYOTOGHG'] + meta.gases.kyotoghg]
for combi in combis_IPCM0EL:
    setattr(tables, combi, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', combi + '_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
            __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

combis_ent_cat = [
    'CO2_IPC1', 'CO2_IPC2', 'CO2_IPCMAG', 'CO2_IPC4', 'CO2_IPC5',
    'CH4_IPC1', 'CH4_IPC2', 'CH4_IPCMAG', 'CH4_IPC4', 'CH4_IPC5',
    'N2O_IPC1', 'N2O_IPC2', 'N2O_IPCMAG', 'N2O_IPC4', 'N2O_IPC5',
    'FGASES_IPC2']
for combi in combis_ent_cat:
    setattr(tables, combi, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', combi + '_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
            __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# PRIMAP-hist 1850 to 2017.
setattr(tables, 'emi_his_all', hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
    'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '__allYears.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# LULUCF emissions.
for srce in meta.lulucf.source_prioritisation:
    if 'FAO' not in srce:
        setattr(tables, f"LULUCF_{srce}", hpf.import_table_to_class_metadata_country_year_matrix(
                Path(meta.path.preprocess, 'tables', f'KYOTOGHG_IPCMLULUCF_TOTAL_NET_HISTORY_{srce}.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# FAO (had to be summed over CO2 + CH4 + N2O).
setattr(tables, f"LULUCF_FAO2019BI", hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_FAO2019BI.csv')). \
        __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# Chosen source.
setattr(tables, f"LULUCF_CHOSEN", hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv')). \
        __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# Energy CO2 per GDP or per capita (only available for historical values).
setattr(tables, "CO2_IPC1_emi_gdp", hpf.combine_tables('divide', 
        [getattr(tables, "CO2_IPC1"), getattr(tables, f"SSP2_gdp")]))
setattr(tables, "CO2_IPC1_emi_pop", hpf.combine_tables('divide', 
        [getattr(tables, "CO2_IPC1"), getattr(tables, f"SSP2_pop")]))

# Covered emissions.
for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
    
    table_act = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.pc_cov, f"KYOTOGHG_IPCM0EL_COV_EMI_{ssp_long}FILLED_CORR.csv"))
    setattr(table_act, 'family', 'emi') # TODO: somehow there is no family info in here. Check that in preprocessing.
    table_act = table_act.__convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH)
    setattr(tables, f"{ssp_short}_emi_cov", table_act)
    
    setattr(tables, f"{ssp_short}_pc_cov", hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.pc_cov, f"KYOTOGHG_IPCM0EL_COV_PC_{ssp_long}FILLED_CORR.csv")). \
        __reindex__(index=meta.isos.EARTH)) # TODO: somehow there is no family info in here. Check that in preprocessing.

# Emissions from NDCs.
for what in ['exclLU', 'inclLU', 'onlyLU']:
    table = hpf.create_table(
        tablename=f"emi_ndcs_{what}", tpe="emi", family="emi", unit="MtCO2eq", gwp="AR4")
    data = pd.read_csv(
        Path(meta.path.preprocess, f'infos_from_ndcs_emi_{what}.csv'), index_col=0)
    data.columns = [int(xx) for xx in data.columns]
    table.data = data
    setattr(tables, f"emi_ndcs_{what}", table)

# %%
# Cumulative historical emissions.
yr_his = 2017
yr_sum_start1850 = 1850
yr_sum_start1990 = 1990
sum_start1850 = hpf.copy_table(getattr(tables, 'emi_his_all')).data.reindex(columns=range(yr_sum_start1850, yr_his+1)).sum(axis=1)
sum_start1990 = hpf.copy_table(getattr(tables, 'emi_his_all')).data.reindex(columns=range(yr_sum_start1990, yr_his+1)).sum(axis=1)

# %%
# NDC quantifications (exclUSA).

ndc_quantis_exclUSA = {
    'prio_SSPs': {
        'cov100': {
            'folders': {
                'SSP1': 'ndcs_20201122_1029_SSP1_typeMain_pccov100',
                'SSP2': 'ndcs_20201122_1103_SSP2_typeMain_pccov100',
                'SSP3': 'ndcs_20201122_1141_SSP3_typeMain_pccov100',
                'SSP4': 'ndcs_20201122_1245_SSP4_typeMain_pccov100',
                'SSP5': 'ndcs_20201122_1303_SSP5_typeMain_pccov100'}},
        'cov100_lulucf_unfccc': {
            'folders': {
                'SSP1': 'ndcs_20201122_1029_SSP1_typeMain_pccov100_UNFCCC',
                'SSP2': 'ndcs_20201122_1103_SSP2_typeMain_pccov100_UNFCCC',
                'SSP3': 'ndcs_20201122_1141_SSP3_typeMain_pccov100_UNFCCC',
                'SSP4': 'ndcs_20201122_1245_SSP4_typeMain_pccov100_UNFCCC',
                'SSP5': 'ndcs_20201122_1303_SSP5_typeMain_pccov100_UNFCCC'}},
        'cov100_lulucf_fao': {
            'folders': {
                'SSP1': 'ndcs_20201122_1029_SSP1_typeMain_pccov100_FAO',
                'SSP2': 'ndcs_20201122_1103_SSP2_typeMain_pccov100_FAO',
                'SSP3': 'ndcs_20201122_1141_SSP3_typeMain_pccov100_FAO',
                'SSP4': 'ndcs_20201122_1245_SSP4_typeMain_pccov100_FAO',
                'SSP5': 'ndcs_20201122_1303_SSP5_typeMain_pccov100_FAO'}},
        'cov100_bl_uncondi': {
            'folders': {
                'SSP1': 'ndcs_20201122_1033_SSP1_typeMain_pccov100_BLForUCAboveBL',
                'SSP2': 'ndcs_20201122_1110_SSP2_typeMain_pccov100_BLForUCAboveBL',
                'SSP3': 'ndcs_20201122_1148_SSP3_typeMain_pccov100_BLForUCAboveBL',
                'SSP4': 'ndcs_20201122_1251_SSP4_typeMain_pccov100_BLForUCAboveBL',
                'SSP5': 'ndcs_20201122_1308_SSP5_typeMain_pccov100_BLForUCAboveBL'}},
        'cov100_const_emi': {
            'folders': {
                'SSP1': 'ndcs_20201122_1035_SSP1_typeMain_pccov100_constEmiAfterLastTar',
                'SSP2': 'ndcs_20201122_1112_SSP2_typeMain_pccov100_constEmiAfterLastTar',
                'SSP3': 'ndcs_20201122_1151_SSP3_typeMain_pccov100_constEmiAfterLastTar',
                'SSP4': 'ndcs_20201122_1252_SSP4_typeMain_pccov100_constEmiAfterLastTar',
                'SSP5': 'ndcs_20201122_1310_SSP5_typeMain_pccov100_constEmiAfterLastTar'}},
        'covest': {
            'folders': {
                'SSP1': 'ndcs_20201122_1013_SSP1_typeMain',
                'SSP2': 'ndcs_20201122_1054_SSP2_typeMain',
                'SSP3': 'ndcs_20201122_1131_SSP3_typeMain',
                'SSP4': 'ndcs_20201122_1237_SSP4_typeMain',
                'SSP5': 'ndcs_20201122_1254_SSP5_typeMain'}},
        'covest_lulucf_unfccc': {
            'folders': {
                'SSP1': 'ndcs_20201122_1013_SSP1_typeMain_UNFCCC',
                'SSP2': 'ndcs_20201122_1054_SSP2_typeMain_UNFCCC',
                'SSP3': 'ndcs_20201122_1131_SSP3_typeMain_UNFCCC',
                'SSP4': 'ndcs_20201122_1237_SSP4_typeMain_UNFCCC',
                'SSP5': 'ndcs_20201122_1254_SSP5_typeMain_UNFCCC'}},
        'covest_lulucf_fao': {
            'folders': {
                'SSP1': 'ndcs_20201122_1013_SSP1_typeMain_FAO',
                'SSP2': 'ndcs_20201122_1054_SSP2_typeMain_FAO',
                'SSP3': 'ndcs_20201122_1131_SSP3_typeMain_FAO',
                'SSP4': 'ndcs_20201122_1237_SSP4_typeMain_FAO',
                'SSP5': 'ndcs_20201122_1254_SSP5_typeMain_FAO'}},
        'covest_bl_uncondi': {
            'folders': {
                'SSP1': 'ndcs_20201122_1026_SSP1_typeMain_BLForUCAboveBL',
                'SSP2': 'ndcs_20201122_1100_SSP2_typeMain_BLForUCAboveBL',
                'SSP3': 'ndcs_20201122_1137_SSP3_typeMain_BLForUCAboveBL',
                'SSP4': 'ndcs_20201122_1242_SSP4_typeMain_BLForUCAboveBL',
                'SSP5': 'ndcs_20201122_1259_SSP5_typeMain_BLForUCAboveBL'}},
        'covest_const_emi': {
            'folders': {
                'SSP1': 'ndcs_20201122_1028_SSP1_typeMain_constEmiAfterLastTar',
                'SSP2': 'ndcs_20201122_1102_SSP2_typeMain_constEmiAfterLastTar',
                'SSP3': 'ndcs_20201122_1139_SSP3_typeMain_constEmiAfterLastTar',
                'SSP4': 'ndcs_20201122_1244_SSP4_typeMain_constEmiAfterLastTar',
                'SSP5': 'ndcs_20201122_1301_SSP5_typeMain_constEmiAfterLastTar'}}},
    'prio_NDCs': {
        'cov100': {
            'folders': {
                'SSP1': 'ndcs_20201122_1044_SSP1_typeReclass_pccov100',
                'SSP2': 'ndcs_20201122_1122_SSP2_typeReclass_pccov100',
                'SSP3': 'ndcs_20201122_1208_SSP3_typeReclass_pccov100',
                'SSP4': 'ndcs_20201122_1230_SSP4_typeReclass_pccov100',
                'SSP5': 'ndcs_20201122_1322_SSP5_typeReclass_pccov100'}},
        'cov100_lulucf_unfccc': {
            'folders': {
                'SSP1': 'ndcs_20201122_1044_SSP1_typeReclass_pccov100_UNFCCC',
                'SSP2': 'ndcs_20201122_1122_SSP2_typeReclass_pccov100_UNFCCC',
                'SSP3': 'ndcs_20201122_1208_SSP3_typeReclass_pccov100_UNFCCC',
                'SSP4': 'ndcs_20201122_1230_SSP4_typeReclass_pccov100_UNFCCC',
                'SSP5': 'ndcs_20201122_1322_SSP5_typeReclass_pccov100_UNFCCC'}},
        'cov100_lulucf_fao': {
            'folders': {
                'SSP1': 'ndcs_20201122_1044_SSP1_typeReclass_pccov100_FAO',
                'SSP2': 'ndcs_20201122_1122_SSP2_typeReclass_pccov100_FAO',
                'SSP3': 'ndcs_20201122_1208_SSP3_typeReclass_pccov100_FAO',
                'SSP4': 'ndcs_20201122_1230_SSP4_typeReclass_pccov100_FAO',
                'SSP5': 'ndcs_20201122_1322_SSP5_typeReclass_pccov100_FAO'}},
        'cov100_bl_uncondi': {
            'folders': {
                'SSP1': 'ndcs_20201122_1050_SSP1_typeReclass_pccov100_BLForUCAboveBL',
                'SSP2': 'ndcs_20201122_1128_SSP2_typeReclass_pccov100_BLForUCAboveBL',
                'SSP3': 'ndcs_20201122_1217_SSP3_typeReclass_pccov100_BLForUCAboveBL',
                'SSP4': 'ndcs_20201122_1234_SSP4_typeReclass_pccov100_BLForUCAboveBL',
                'SSP5': 'ndcs_20201122_1329_SSP5_typeReclass_pccov100_BLForUCAboveBL'}},
        'cov100_const_emi': {
            'folders': {
                'SSP1': 'ndcs_20201122_1052_SSP1_typeReclass_pccov100_constEmiAfterLastTar',
                'SSP2': 'ndcs_20201122_1130_SSP2_typeReclass_pccov100_constEmiAfterLastTar',
                'SSP3': 'ndcs_20201122_1220_SSP3_typeReclass_pccov100_constEmiAfterLastTar',
                'SSP4': 'ndcs_20201122_1236_SSP4_typeReclass_pccov100_constEmiAfterLastTar',
                'SSP5': 'ndcs_20201122_1331_SSP5_typeReclass_pccov100_constEmiAfterLastTar'}},
        'covest': {
            'folders': {
                'SSP1': 'ndcs_20201122_1037_SSP1_typeReclass',
                'SSP2': 'ndcs_20201122_1114_SSP2_typeReclass',
                'SSP3': 'ndcs_20201122_1154_SSP3_typeReclass',
                'SSP4': 'ndcs_20201122_1221_SSP4_typeReclass',
                'SSP5': 'ndcs_20201122_1312_SSP5_typeReclass'}},
        'covest_lulucf_unfccc': {
            'folders': {
                'SSP1': 'ndcs_20201122_1037_SSP1_typeReclass_UNFCCC',
                'SSP2': 'ndcs_20201122_1114_SSP2_typeReclass_UNFCCC',
                'SSP3': 'ndcs_20201122_1154_SSP3_typeReclass_UNFCCC',
                'SSP4': 'ndcs_20201122_1221_SSP4_typeReclass_UNFCCC',
                'SSP5': 'ndcs_20201122_1312_SSP5_typeReclass_UNFCCC'}},
        'covest_lulucf_fao': {
            'folders': {
                'SSP1': 'ndcs_20201122_1037_SSP1_typeReclass_FAO',
                'SSP2': 'ndcs_20201122_1114_SSP2_typeReclass_FAO',
                'SSP3': 'ndcs_20201122_1154_SSP3_typeReclass_FAO',
                'SSP4': 'ndcs_20201122_1221_SSP4_typeReclass_FAO',
                'SSP5': 'ndcs_20201122_1312_SSP5_typeReclass_FAO'}},
        'covest_bl_uncondi': {
            'folders': {
                'SSP1': 'ndcs_20201122_1041_SSP1_typeReclass_BLForUCAboveBL',
                'SSP2': 'ndcs_20201122_1119_SSP2_typeReclass_BLForUCAboveBL',
                'SSP3': 'ndcs_20201122_1203_SSP3_typeReclass_BLForUCAboveBL',
                'SSP4': 'ndcs_20201122_1227_SSP4_typeReclass_BLForUCAboveBL',
                'SSP5': 'ndcs_20201122_1318_SSP5_typeReclass_BLForUCAboveBL'}},
        'covest_const_emi': {
            'folders': {
                'SSP1': 'ndcs_20201122_1043_SSP1_typeReclass_constEmiAfterLastTar',
                'SSP2': 'ndcs_20201122_1120_SSP2_typeReclass_constEmiAfterLastTar',
                'SSP3': 'ndcs_20201122_1206_SSP3_typeReclass_constEmiAfterLastTar',
                'SSP4': 'ndcs_20201122_1228_SSP4_typeReclass_constEmiAfterLastTar',
                'SSP5': 'ndcs_20201122_1320_SSP5_typeReclass_constEmiAfterLastTar'}}}}

# %%
# NDC quantifications (inclUSA).

ndc_quantis_inclUSA = {
    'prio_SSPs': {
        'cov100': {
            'folders': {
                'SSP1': 'ndcs_20201220_2222_SSP1_typeMain_pccov100_inclUSA',
                'SSP2': 'ndcs_20201220_2303_SSP2_typeMain_pccov100_inclUSA',
                'SSP3': 'ndcs_20201220_2346_SSP3_typeMain_pccov100_inclUSA',
                'SSP4': 'ndcs_20201221_0038_SSP4_typeMain_pccov100_inclUSA',
                'SSP5': 'ndcs_20201221_0051_SSP5_typeMain_pccov100_inclUSA'}},
        'cov100_lulucf_unfccc': {
            'folders': {
                'SSP1': 'ndcs_20201220_2222_SSP1_typeMain_pccov100_inclUSA_UNFCCC',
                'SSP2': 'ndcs_20201220_2303_SSP2_typeMain_pccov100_inclUSA_UNFCCC',
                'SSP3': 'ndcs_20201220_2346_SSP3_typeMain_pccov100_inclUSA_UNFCCC',
                'SSP4': 'ndcs_20201221_0038_SSP4_typeMain_pccov100_inclUSA_UNFCCC',
                'SSP5': 'ndcs_20201221_0051_SSP5_typeMain_pccov100_inclUSA_UNFCCC'}},
        'cov100_lulucf_fao': {
            'folders': {
                'SSP1': 'ndcs_20201220_2222_SSP1_typeMain_pccov100_inclUSA_FAO',
                'SSP2': 'ndcs_20201220_2303_SSP2_typeMain_pccov100_inclUSA_FAO',
                'SSP3': 'ndcs_20201220_2346_SSP3_typeMain_pccov100_inclUSA_FAO',
                'SSP4': 'ndcs_20201221_0038_SSP4_typeMain_pccov100_inclUSA_FAO',
                'SSP5': 'ndcs_20201221_0051_SSP5_typeMain_pccov100_inclUSA_FAO'}},
        'cov100_bl_uncondi': {
            'folders': {
                'SSP1': 'ndcs_20201220_2227_SSP1_typeMain_pccov100_BLForUCAboveBL_inclUSA',
                'SSP2': 'ndcs_20201220_2310_SSP2_typeMain_pccov100_BLForUCAboveBL_inclUSA',
                'SSP3': 'ndcs_20201220_2352_SSP3_typeMain_pccov100_BLForUCAboveBL_inclUSA',
                'SSP4': 'ndcs_20201221_0042_SSP4_typeMain_pccov100_BLForUCAboveBL_inclUSA',
                'SSP5': 'ndcs_20201221_0055_SSP5_typeMain_pccov100_BLForUCAboveBL_inclUSA'}},
        'cov100_const_emi': {
            'folders': {
                'SSP1': 'ndcs_20201220_2229_SSP1_typeMain_pccov100_constEmiAfterLastTar_inclUSA',
                'SSP2': 'ndcs_20201220_2313_SSP2_typeMain_pccov100_constEmiAfterLastTar_inclUSA',
                'SSP3': 'ndcs_20201220_2354_SSP3_typeMain_pccov100_constEmiAfterLastTar_inclUSA',
                'SSP4': 'ndcs_20201221_0043_SSP4_typeMain_pccov100_constEmiAfterLastTar_inclUSA',
                'SSP5': 'ndcs_20201221_0057_SSP5_typeMain_pccov100_constEmiAfterLastTar_inclUSA'}},
       'covest': {
            'folders': {
                'SSP1': 'ndcs_20201220_2213_SSP1_typeMain_inclUSA',
                'SSP2': 'ndcs_20201220_2252_SSP2_typeMain_inclUSA',
                'SSP3': 'ndcs_20201220_2338_SSP3_typeMain_inclUSA',
                'SSP4': 'ndcs_20201221_0032_SSP4_typeMain_inclUSA',
                'SSP5': 'ndcs_20201221_0045_SSP5_typeMain_inclUSA'}},
        'covest_lulucf_unfccc': {
            'folders': {
                'SSP1': 'ndcs_20201220_2213_SSP1_typeMain_inclUSA_UNFCCC',
                'SSP2': 'ndcs_20201221_0751_SSP2_typeMain_inclUSA_UNFCCC',
                'SSP3': 'ndcs_20201220_2338_SSP3_typeMain_inclUSA_UNFCCC',
                'SSP4': 'ndcs_20201221_0032_SSP4_typeMain_inclUSA_UNFCCC',
                'SSP5': 'ndcs_20201221_0045_SSP5_typeMain_inclUSA_UNFCCC'}},
        'covest_lulucf_fao': {
            'folders': {
                'SSP1': 'ndcs_20201220_2213_SSP1_typeMain_inclUSA_FAO',
                'SSP2': 'ndcs_20201220_2252_SSP2_typeMain_inclUSA_FAO',
                'SSP3': 'ndcs_20201220_2338_SSP3_typeMain_inclUSA_FAO',
                'SSP4': 'ndcs_20201221_0032_SSP4_typeMain_inclUSA_FAO',
                'SSP5': 'ndcs_20201221_0045_SSP5_typeMain_inclUSA_FAO'}},
        'covest_bl_uncondi': {
            'folders': {
                'SSP1': 'ndcs_20201220_2218_SSP1_typeMain_BLForUCAboveBL_inclUSA',
                'SSP2': 'ndcs_20201220_2258_SSP2_typeMain_BLForUCAboveBL_inclUSA',
                'SSP3': 'ndcs_20201220_2342_SSP3_typeMain_BLForUCAboveBL_inclUSA',
                'SSP4': 'ndcs_20201221_0036_SSP4_typeMain_BLForUCAboveBL_inclUSA',
                'SSP5': 'ndcs_20201221_0049_SSP5_typeMain_BLForUCAboveBL_inclUSA'}},
        'covest_const_emi': {
            'folders': {
                'SSP1': 'ndcs_20201220_2220_SSP1_typeMain_constEmiAfterLastTar_inclUSA',
                'SSP2': 'ndcs_20201220_2301_SSP2_typeMain_constEmiAfterLastTar_inclUSA',
                'SSP3': 'ndcs_20201220_2344_SSP3_typeMain_constEmiAfterLastTar_inclUSA',
                'SSP4': 'ndcs_20201221_0037_SSP4_typeMain_constEmiAfterLastTar_inclUSA',
                'SSP5': 'ndcs_20201221_0050_SSP5_typeMain_constEmiAfterLastTar_inclUSA'}}},
    'prio_NDCs': {
        'cov100': {
            'folders': {
                'SSP1': 'ndcs_20201220_2241_SSP1_typeReclass_pccov100_inclUSA',
                'SSP2': 'ndcs_20201220_2330_SSP2_typeReclass_pccov100_inclUSA',
                'SSP3': 'ndcs_20201221_0007_SSP3_typeReclass_pccov100_inclUSA',
                'SSP4': 'ndcs_20201221_0025_SSP4_typeReclass_pccov100_inclUSA',
                'SSP5': 'ndcs_20201221_0105_SSP5_typeReclass_pccov100_inclUSA'}},
        'cov100_lulucf_unfccc': {
            'folders': {
                'SSP1': 'ndcs_20201220_2241_SSP1_typeReclass_pccov100_inclUSA_UNFCCC',
                'SSP2': 'ndcs_20201220_2330_SSP2_typeReclass_pccov100_inclUSA_UNFCCC',
                'SSP3': 'ndcs_20201221_0007_SSP3_typeReclass_pccov100_inclUSA_UNFCCC',
                'SSP4': 'ndcs_20201221_0025_SSP4_typeReclass_pccov100_inclUSA_UNFCCC',
                'SSP5': 'ndcs_20201221_0105_SSP5_typeReclass_pccov100_inclUSA_UNFCCC'}},
        'cov100_lulucf_fao': {
            'folders': {
                'SSP1': 'ndcs_20201220_2241_SSP1_typeReclass_pccov100_inclUSA_FAO',
                'SSP2': 'ndcs_20201220_2330_SSP2_typeReclass_pccov100_inclUSA_FAO',
                'SSP3': 'ndcs_20201221_0007_SSP3_typeReclass_pccov100_inclUSA_FAO',
                'SSP4': 'ndcs_20201221_0025_SSP4_typeReclass_pccov100_inclUSA_FAO',
                'SSP5': 'ndcs_20201221_0105_SSP5_typeReclass_pccov100_inclUSA_FAO'}},
        'cov100_bl_uncondi': {
            'folders': {
                'SSP1': 'ndcs_20201220_2247_SSP1_typeReclass_pccov100_BLForUCAboveBL_inclUSA',
                'SSP2': 'ndcs_20201220_2335_SSP2_typeReclass_pccov100_BLForUCAboveBL_inclUSA',
                'SSP3': 'ndcs_20201221_0013_SSP3_typeReclass_pccov100_BLForUCAboveBL_inclUSA',
                'SSP4': 'ndcs_20201221_0029_SSP4_typeReclass_pccov100_BLForUCAboveBL_inclUSA',
                'SSP5': 'ndcs_20201221_0108_SSP5_typeReclass_pccov100_BLForUCAboveBL_inclUSA'}},
        'cov100_const_emi': {
            'folders': {
                'SSP1': 'ndcs_20201220_2249_SSP1_typeReclass_pccov100_constEmiAfterLastTar_inclUSA',
                'SSP2': 'ndcs_20201220_2337_SSP2_typeReclass_pccov100_constEmiAfterLastTar_inclUSA',
                'SSP3': 'ndcs_20201221_0016_SSP3_typeReclass_pccov100_constEmiAfterLastTar_inclUSA',
                'SSP4': 'ndcs_20201221_0030_SSP4_typeReclass_pccov100_constEmiAfterLastTar_inclUSA',
                'SSP5': 'ndcs_20201221_0110_SSP5_typeReclass_pccov100_constEmiAfterLastTar_inclUSA'}},
        'covest': {
            'folders': {
                'SSP1': 'ndcs_20201220_2232_SSP1_typeReclass_inclUSA',
                'SSP2': 'ndcs_20201220_2316_SSP2_typeReclass_inclUSA',
                'SSP3': 'ndcs_20201220_2356_SSP3_typeReclass_inclUSA',
                'SSP4': 'ndcs_20201221_0018_SSP4_typeReclass_inclUSA',
                'SSP5': 'ndcs_20201221_0058_SSP5_typeReclass_inclUSA'}},
        'covest_lulucf_unfccc': {
            'folders': {
                'SSP1': 'ndcs_20201220_2232_SSP1_typeReclass_inclUSA_UNFCCC',
                'SSP2': 'ndcs_20201220_2316_SSP2_typeReclass_inclUSA_UNFCCC',
                'SSP3': 'ndcs_20201220_2356_SSP3_typeReclass_inclUSA_UNFCCC',
                'SSP4': 'ndcs_20201221_0018_SSP4_typeReclass_inclUSA_UNFCCC',
                'SSP5': 'ndcs_20201221_0058_SSP5_typeReclass_inclUSA_UNFCCC'}},
        'covest_lulucf_fao': {
            'folders': {
                'SSP1': 'ndcs_20201220_2232_SSP1_typeReclass_inclUSA_FAO',
                'SSP2': 'ndcs_20201220_2316_SSP2_typeReclass_inclUSA_FAO',
                'SSP3': 'ndcs_20201220_2356_SSP3_typeReclass_inclUSA_FAO',
                'SSP4': 'ndcs_20201221_0018_SSP4_typeReclass_inclUSA_FAO',
                'SSP5': 'ndcs_20201221_0058_SSP5_typeReclass_inclUSA_FAO'}},
        'covest_bl_uncondi': {
            'folders': {
                'SSP1': 'ndcs_20201220_2237_SSP1_typeReclass_BLForUCAboveBL_inclUSA',
                'SSP2': 'ndcs_20201220_2324_SSP2_typeReclass_BLForUCAboveBL_inclUSA',
                'SSP3': 'ndcs_20201221_0003_SSP3_typeReclass_BLForUCAboveBL_inclUSA',
                'SSP4': 'ndcs_20201221_0022_SSP4_typeReclass_BLForUCAboveBL_inclUSA',
                'SSP5': 'ndcs_20201221_0102_SSP5_typeReclass_BLForUCAboveBL_inclUSA'}},
        'covest_const_emi': {
            'folders': {
                'SSP1': 'ndcs_20201220_2239_SSP1_typeReclass_constEmiAfterLastTar_inclUSA',
                'SSP2': 'ndcs_20201220_2327_SSP2_typeReclass_constEmiAfterLastTar_inclUSA',
                'SSP3': 'ndcs_20201221_0005_SSP3_typeReclass_constEmiAfterLastTar_inclUSA',
                'SSP4': 'ndcs_20201221_0024_SSP4_typeReclass_constEmiAfterLastTar_inclUSA',
                'SSP5': 'ndcs_20201221_0103_SSP5_typeReclass_constEmiAfterLastTar_inclUSA'}}}}

# %%
def get_quantis(ndc_quantis, path_to_quantis):
    
    ndc_quantis_tars = {}
    ndc_quantis_ptws = {}
    ndc_quantis_ptws_earth = {}
    
    for prio in ndc_quantis.keys():
        
        ndc_quantis_tars[prio] = {}
        ndc_quantis_ptws[prio] = {}
        ndc_quantis_ptws_earth[prio] = {}
        
        for what in ndc_quantis[prio].keys():
            
            ndc_quantis_tars[prio][what] = {}
            ndc_quantis_ptws[prio][what] = {}
            ndc_quantis_ptws_earth[prio][what] = {}
            
            for ssp in ndc_quantis[prio][what]['folders'].keys():
                
                ndc_quantis_tars[prio][what][ssp] = pd.read_csv(Path(path_to_quantis, 
                    ndc_quantis[prio][what]['folders'][ssp], 
                    "ndc_targets.csv"))
                ndc_quantis_ptws[prio][what][ssp] = pd.read_csv(Path(path_to_quantis, 
                    ndc_quantis[prio][what]['folders'][ssp],
                    "ndc_targets_pathways_per_country_used_for_group_pathways.csv"))
                ndc_quantis_ptws_earth[prio][what][ssp] = pd.read_csv(Path(path_to_quantis, 
                    ndc_quantis[prio][what]['folders'][ssp],
                    "ndc_targets_pathways_per_group.csv"))
    
    return ndc_quantis_tars, ndc_quantis_ptws, ndc_quantis_ptws_earth

ndc_quantis_tars_exclUSA, ndc_quantis_ptws_exclUSA, ndc_quantis_ptws_earth_exclUSA = \
    get_quantis(ndc_quantis_exclUSA, Path(meta.path.main, 'data', 'output', 'output_for_paper'))
ndc_quantis_tars_inclUSA, ndc_quantis_ptws_inclUSA, ndc_quantis_ptws_earth_inclUSA = \
    get_quantis(ndc_quantis_inclUSA, Path(meta.path.main, 'data', 'output'))

# %%
def include_graphics(path_to_figure, caption, label, width):
    
    path_to_figure = str(path_to_figure).replace("\\", "/")
    
    figure = \
        "\n\n \\begin{figure}[H]" + \
        "\n \\centering" + \
        f"\n \\includegraphics[width={width}]" + \
        "{" f"{path_to_figure}" "}" + \
        "\n \\caption{" f"{caption}" "}" + \
        "\n \\label{" f"{label}" "}" + \
        "\n \\end{figure}"
    
    return figure

# %%
def include_graphics2(path_to_figure1, path_to_figure2, caption, label, width1, width2):
    
    path_to_figure1 = str(path_to_figure1).replace("\\", "/")
    path_to_figure2 = str(path_to_figure2).replace("\\", "/")
    
    figure = \
        "\n\n \\begin{figure}[H]" + \
        "\n \\centering" + \
        f"\n \\includegraphics[width={width1}]" + \
        "{" f"{path_to_figure1}" "}" + \
        f"\n \\includegraphics[width={width2}]" + \
        "{" f"{path_to_figure2}" "}" + \
        "\n \\caption{" f"{caption}" "}" + \
        "\n \\label{" f"{label}" "}" + \
        "\n \\end{figure}"
    
    return figure

# %%
def plot_map():
    # Plot the global share in 10 equally sized bins.
    share = pd.read_csv(Path(meta.path.main, 'data', 'other',
        'global_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)
    ent_cat = 'KYOTOGHGAR4_IPCM0EL'
    share = share.loc[:, ent_cat]
    path_to_png = Path(path_to_tex_files, f'emi_share_map_2017.png')
    hpf.plot_maps_bins(share, path_to_png, bounds=[.05, .1, .2, .4, .6, .8, 1, 1.5, 2.5, 10], 
        flipud=True, nr_instances=True, plot_pdf=False)
    
    # In/decrease in share between 2017 and 2030 (dmSSP2)
    emi_2030_ssp2 = tables.SSP2_KYOTOGHG.data.loc[:, 2030].reindex(index=meta.isos.EARTH)
    share_2030_ssp2 = 100*emi_2030_ssp2.div(emi_2030_ssp2.sum())
    share_diff = share_2030_ssp2.add(-share)
    path_to_png = Path(path_to_tex_files, f'emi_share_map_diff_2030_dmssp2_minus_2017.png')
    bounds = [-1.8, -.4, -.1, 0, .1, .4, 1.4, 2.4]
    bounds = [-1.8, -.4, -.05, 0, .05, .4, 1.4, 2.4]
    colours_diff = hpf.create_colormap(
        pd.DataFrame([[.2, .8, .2], [.2, .2, .8], [.8, .2, .2]], index=[-2.4, 0, 2.4]))
    colours_diff = colours_diff.loc[[xx for xx in colours_diff.index if (xx >= bounds[0] and xx <= bounds[-1])], :]
    hpf.plot_maps_bins(share_diff, path_to_png, bounds=bounds, 
        colours=colours_diff, flipud=False, nr_instances=True, plot_pdf=False)

# %%
def plot_ts_nonLULUCF():
    
    fig = plt.figure(figsize=(12, 6))
    
    ax_sec = fig.add_subplot(1, 2, 1)
    ax_gas = fig.add_subplot(1, 2, 2)
    
    yrs_to_plot = range(1990, 2051)
    
    yrs_to_plot_cats = range(1990, 2018)
    cats_to_plot = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5']
    data_cats = pd.DataFrame(index=cats_to_plot, columns=yrs_to_plot_cats)
    
    for cat in cats_to_plot:
        data_cats.loc[cat, :] = getattr(tables_iso, f"KYOTOGHG_{cat}").data.reindex(index=[iso3]).reindex(columns=yrs_to_plot_cats).values[0]
    
    lower_lim = [0] * len(yrs_to_plot_cats)
    for cat in cats_to_plot:
        upper_lim = list(lower_lim + data_cats.loc[cat, :].values)
        ax_sec.fill_between(yrs_to_plot_cats, lower_lim, upper_lim, color=colours['cats'].loc[cat, :].values,
                            label=meta.categories.main.cat_to_sec[cat])
        lower_lim = upper_lim
            
    for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
        data_ssp = getattr(tables_iso, f"{ssp_short}_emi")
        ax_sec.plot(yrs_to_plot, data_ssp.data.loc[iso3, yrs_to_plot], ssps_linestyle[ssp_short],
                    color=colours['ssps'].loc[ssp_long, :].to_list(), label=f"dm{ssp_short}",
                    linewidth=linewdth)
    
    gases_to_plot = meta.gases.kyotoghg
    data_gases = pd.DataFrame(index=gases_to_plot, columns=yrs_to_plot)
    
    for gas in gases_to_plot:
        data_gases.loc[gas, :] = getattr(tables_iso, f"SSP2_{gas}").data.reindex(index=[iso3]).reindex(columns=yrs_to_plot).values[0]
    
    lower_lim = [0] * len(yrs_to_plot)
    for gas in gases_to_plot:
        upper_lim = list(lower_lim + data_gases.loc[gas, :].values)
        ax_gas.fill_between(yrs_to_plot, lower_lim, upper_lim, color=colours['gases'].loc[gas, :].values,
                            label=meta.gases.gas_to_label[gas])
        lower_lim = upper_lim
    
    # SSP2
    data_ssp = getattr(tables_iso, "SSP2_emi")
    ax_gas.plot(yrs_to_plot, data_ssp.data.loc[iso3, yrs_to_plot], ssps_linestyle['SSP2'],
                color=colours['ssps'].loc[meta.ssps.scens.long[1], :].to_list(), label='dmSSP2',
                linewidth=linewdth)
    
    YL = [0, ax_sec.get_ylim()[1]]
    XL = [yrs_to_plot[0], yrs_to_plot[-1]]
    
    for axa, label in zip([ax_sec, ax_gas], ['(a) Per main sector', '(b) Per Kyoto GHG']):
        axa.set_xlim(XL)
        axa.set_ylim(YL)
        axa.text(XL[0] + .03*np.diff(XL), YL[1] - .05*np.diff(YL), label,
            fontweight='bold', ha='left', va='top')
        axa.set_xlabel('year', fontweight='bold')
    
    for axa in [ax_sec, ax_gas]:
        XL = axa.get_xlim()
        YL = axa.get_ylim()
        yloc = YL[1] + .01*np.diff(YL)
        axa.text(2016, yloc, 'PRIMAP-hist', va='bottom', ha='right')
        axa.text(2017, yloc, '|', va='bottom', ha='center')
        axa.text(2018, yloc, 'dmSSPs', va='bottom', ha='left')
        for yr in [2017, 2030]:
            axa.plot([yr, yr], YL, 'k:', linewidth=.3)
    
    ax_sec.set_ylabel("national emissions (exclLU)" f"\n{units_iso['emi']['label']}",
        fontweight='bold')
    
    ax_sec.legend(loc='center', bbox_to_anchor=(.5, -.25), ncol=4)
    ax_gas.legend(loc='center', bbox_to_anchor=(.5, -.25), ncol=4)
    
    fig.subplots_adjust(left=.1, bottom=.25, right=.95, top=.95)
    path_to_png = Path(path_to_tex_files, f'ts_emi_exclLU_{iso3}.png')
    plt.savefig(path_to_png, dpi=300)
    plt.clf()
    plt.close(fig)

# %%
def plot_ts_normalised_nonLULUCF():
    """
    Plot stacked time series of PRIMAP-hist data per main + subsector, and per gas, normalised to 100%.
    """
    
    ipcm0el = [f'IPC{xx}' for xx in ['1', '2', 'MAG', '4', '5']]
    ipc1 = ['IPC1A', 'IPC1B']
    ipcmag = ['IPCMAGELV', 'IPC3A']
    cats_all = ipc1 + ['IPC2'] + ipcmag + ['IPC4', 'IPC5']
    cats_labels = {
        'IPC1': 'Energy', 'IPC2': 'IPPU', 'IPCMAG': 'Agri', 'IPC4': 'Waste', 'IPC5': 'Other',
        'IPC1A': 'FuelComb', 'IPC1B': 'FugEmiFromFuels',
        'IPCMAGELV': 'AgriExclLivestock', 'IPC3A': 'Livestock'}
    
    yrs = range(1990, 2018)
    
    fig = plt.figure(figsize=(12, 5))
    
    ax_cat = fig.add_subplot(1, 2, 1)
    ax_gas = fig.add_subplot(1, 2, 2)
    
    data_earth = tables_iso.KYOTOGHG_IPCM0EL.data.loc[iso3, yrs]
    
    # Outer bars (main sectors).
    bottom = [0]*len(yrs)
    for cat in ipcm0el:
        try:
            data_plot = getattr(tables_iso, f"KYOTOGHG_{cat}").data.loc[iso3, yrs]/data_earth*100
            if data_plot.isnull().all():
                data_plot = pd.Series(0, index=yrs)
        except:
            data_plot = pd.Series(0, index=yrs)
        # ax_cat.bar(yrs, data_plot, bottom=bottom, width=.9, color=colours['cats'].loc[cat, :], 
        #     label=cats_labels[cat])
        ax_cat.bar([xx-.2 for xx in yrs], data_plot, bottom=bottom, width=.4, color=colours['cats'].loc[cat, :], 
            label=cats_labels[cat], edgecolor='k', linewidth=.3)
        bottom = data_plot.add(bottom)
    
    # Inner bars.
    bottom = [0]*len(yrs)
    for cat in cats_all:
        try:
            data_plot = getattr(tables_iso, f"KYOTOGHG_{cat}").data.loc[iso3, yrs]/data_earth*100
            if data_plot.isnull().all():
                data_plot = pd.Series(0, index=yrs)
        except:
            data_plot = pd.Series(0, index=yrs)
        # ax_cat.bar(yrs, data_plot, bottom=bottom, width=.3, color=colours['cats'].loc[cat, :], 
        #     label=(cats_labels[cat] if cat in ipc1 + ipcmag else '__nolegend__'))
        ax_cat.bar([xx+.2 for xx in yrs], data_plot, bottom=bottom, width=.4, color=colours['cats'].loc[cat, :], 
            label=(cats_labels[cat] if cat in ipc1 + ipcmag else '__nolegend__'), edgecolor='k', linewidth=.3)
        bottom = data_plot.add(bottom)
    
    # Gases.
    bottom = [0]*len(yrs)
    for gas in meta.gases.kyotoghg:
        try:
            data_plot = getattr(tables_iso, f"{gas}_IPCM0EL").data.loc[iso3, yrs]/data_earth*100
            if data_plot.isnull().all():
                data_plot = pd.Series(0, index=yrs)
        except:
            data_plot = pd.Series(0, index=yrs)
        ax_gas.bar(yrs, data_plot, bottom=bottom, width=.8, color=colours['gases'].loc[gas, :], 
            label=meta.gases.gas_to_label[gas], edgecolor='k', linewidth=.3)
        bottom = data_plot.add(bottom)
    
    ax_cat.set_ylim([0, 100])
    ax_cat.set_ylabel('national emissions share per sector / %', fontweight='bold')
    ax_cat.set_xlabel('year', fontweight='bold')
    ax_cat.legend(ncol=4, loc='center', bbox_to_anchor=(.5, -.25))
    
    ax_gas.set_ylim([0, 100])
    ax_gas.set_ylabel('national emissions share per Kyoto GHG / %', fontweight='bold')
    ax_gas.set_xlabel('year', fontweight='bold')
    ax_gas.legend(ncol=4, loc='center', bbox_to_anchor=(.5, -.25))
    
    hpf.put_labels_to_subplots(ax_cat, ax_gas)
    fig.subplots_adjust(left=.1, bottom=.25, right=.95, top=.95)
    path_to_plot = Path(path_to_tex_files, 
        f'emi_ts_normalised_per_sec_and_subsec_and_per_gas_{iso3}.png')
    plt.savefig(path_to_plot, dpi=300)
    
    fig.clf()
    plt.close(fig)

# %%
def plot_ts_LULUCF():
    
    fig = plt.figure(figsize=(12, 5))
    ax_lu = fig.add_subplot(1, 1, 1)
    
    yrs_to_plot_his = range(1990, 2018)
    yrs_to_plot = range(1990, 2021)
    
    for srce in meta.lulucf.source_prioritisation:
        
        mark = '<'
        if 'CRF' in srce:
            mark = '*'
        elif 'FAO' in srce:
            mark = 's'
        elif 'EDGAR' in srce:
            mark = 'v'
        elif 'BUR' in srce:
            mark = 'p'
        
        plt_data = getattr(tables_iso, f'LULUCF_{srce}').data.reindex(index=[iso3], columns=yrs_to_plot_his).values[0]
        nr_vals = sum([1 if not np.isnan(xx) else 0 for xx in plt_data])
        ax_lu.plot(yrs_to_plot_his, plt_data,
                   marker=mark, markersize=markersze, linestyle=':', color=colours['lulucf'].loc[srce, :],
                   label=f"{meta.sources.srce_to_label[srce]}, {nr_vals}", linewidth=linewdth)
    
    ax_lu.plot(yrs_to_plot, getattr(tables_iso, 'LULUCF_CHOSEN').data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
               marker='o', markersize=.5*markersze, linestyle='', color=colours['lulucf'].loc['CHOSEN', :],
               label='Prioritised data', linewidth=linewdth)
    
    XL = [yrs_to_plot[0]-1, yrs_to_plot[-1]+1]
    YL = ax_lu.get_ylim()
    ax_lu.plot([2017, 2017], YL, 'k:', linewidth=.3)            
    ax_lu.plot(XL, [0, 0], 'k:', linewidth=.3)
    yloc = YL[1] + .01*np.diff(YL)
    ax_lu.text(2016.5, yloc, 'historical values', ha='right')
    ax_lu.text(2017, yloc, '|', ha='center')
    ax_lu.text(2017.5, yloc, 'extrapolation', ha='left')
    ax_lu.set_xlim(XL)
    ax_lu.set_ylim(YL)
    ax_lu.set_ylabel("emissions (onylLU)" f"\n{units_iso['emi']['label']}", fontweight='bold')
    ax_lu.set_xlabel('year', fontweight='bold')
    ax_lu.legend(loc='center', bbox_to_anchor=(1.13, .5))
    
    fig.subplots_adjust(left=.1, bottom=.1, right=.8, top=.95)
    path_to_png = Path(path_to_tex_files, f'ts_emi_onlyLU_{iso3}.png')
    plt.savefig(path_to_png, dpi=300)
    plt.clf()
    plt.close(fig)

# %%
def plot_ts_gdp_pop():
    
    fig = plt.figure(figsize=(12, 9))
    
    ax_gdp = fig.add_subplot(2, 2, 1)
    ax_emi_gdp = fig.add_subplot(2, 2, 2)
    ax_pop = fig.add_subplot(2, 2, 3)
    ax_emi_pop = fig.add_subplot(2, 2, 4)
    
    yrs_to_plot = range(1990, 2051)
    
    for axa in [ax_gdp, ax_emi_gdp, ax_pop, ax_emi_pop]:
        axa.plot(yrs_to_plot, [0]*len(yrs_to_plot), 'k:', linewidth=.5)
    
    for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
        
        for axa, what in zip([ax_gdp, ax_emi_gdp, ax_pop, ax_emi_pop], ['gdp', 'emi_gdp', 'pop', 'emi_pop']):
            axa.plot(yrs_to_plot, getattr(tables_iso, f"{ssp_short}_{what}").data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
                        linestyle=ssps_linestyle[ssp_short], color=colours['ssps'].loc[ssp_long, :].to_list(),
                        label=f"dm{ssp_short}", linewidth=linewdth)
    
    # TODO ! put in the highest three contributors instead of Energy CO2.
    # Get the highest three contributors per sector + gas combi (for 2017).
    # yrs_his = range(1990, meta.primap.last_year + 1)
    # vals_combi_gdp = pd.DataFrame(columns=yrs_his)
    # vals_combi_pop = pd.DataFrame(columns=yrs_his)
    # ssp2_gdp = getattr(tables_iso, "SSP2_gdp").data.loc[:, yrs_his]
    # ssp2_pop = getattr(tables_iso, "SSP2_pop").data.loc[:, yrs_his]
    # for combi in combis_ent_cat:
    #     try:
    #         data_act = 1/units_iso['emi']['multiplier'] * \
    #             getattr(tables_iso, combi).data.reindex(index=[iso3], columns=yrs_his).values[0]
    #         vals_combi_gdp.loc[combi, yrs_his] = data_act.div(ssp2_gdp)
    #         vals_combi_pop.loc[combi, yrs_his] = data_act.div(ssp2_pop)
    #     except:
    #         vals_combi_gdp.loc[combi, yrs_his] = [np.nan]*len(yrs_to_plot)
    #         vals_combi_pop.loc[combi, yrs_his] = [np.nan]*len(yrs_to_plot)
    
    # vals_combi = vals_combi_gdp.sort_values(2017, ascending=False)
    # bottom_emi_gdp = [0] * len(yrs_his)
    # bottom_emi_pop = [0] * len(yrs_his)
    # for combi in vals_combi_gdp.index[:3]:
    #     ax_emi_gdp.fill_between(yrs_his, bottom_emi_gdp, vals_combi_gdp.loc[combi, :].add(bottom_emi_gdp).values[0], label=combi)
    #     bottom_emi_gdp = vals_combi_gdp.loc[combi, :].add(bottom_emi_gdp).values[0]
    #     ax_emi_pop.fill_between(yrs_his, bottom_emi_pop, vals_combi_pop.loc[combi, :].add(bottom_emi_gdp).values[0], label=combi)
    #     bottom_emi_pop = vals_combi_pop.loc[combi, :].add(bottom_emi_pop).values[0]
    ax_emi_gdp.plot(yrs_to_plot, getattr(tables_iso, f"CO2_IPC1_emi_gdp").data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
            'k-.', label=f"Energy CO$_2$", linewidth=linewdth)
    ax_emi_pop.plot(yrs_to_plot, getattr(tables_iso, f"CO2_IPC1_emi_pop").data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
            'k-.', label=f"Energy CO$_2$", linewidth=linewdth)
    
    XL = [yrs_to_plot[0], yrs_to_plot[-1]]
    for axa, what, label in \
        zip([ax_gdp, ax_emi_gdp, ax_pop, ax_emi_pop], 
            ['gdp', 'emi_gdp', 'pop', 'emi_pop'],
            ['GDP', 'Emissions per GDP', 'Population', 'Emissions per capita']):
        axa.set_xlim(XL)
        ylabel = units_iso[what]['label']
        axa.set_ylabel(f"{label}" f"\n{ylabel}", fontweight='bold')
        axa.set_xlabel("year", fontweight='bold')
    
    for axa, lbl in [ax_gdp, '(a) GDP'], [ax_emi_gdp, '(b) Emissions per unit of GDP'], \
        [ax_pop, '(c) Population'], [ax_emi_pop, '(d) Per capita emissions']:
        XL = axa.get_xlim()
        YL = axa.get_ylim()
        YL = [YL[0], 1.05*YL[1]]
        #if axa in [ax_gdp, ax_emi_gdp]:
        yloc = YL[1] + .01*np.diff(YL)
        axa.text(2016, yloc, 'PRIMAP-hist', va='bottom', ha='right')
        axa.text(2017, yloc, '|', va='bottom', ha='center')
        axa.text(2018, yloc, 'dmSSPs', va='bottom', ha='left')
        axa.text(XL[0] + .03*np.diff(XL), YL[1] - .05*np.diff(YL), lbl, fontweight='bold')
        for yr in [2017, 2030]:
            axa.plot([yr, yr], YL, 'k:', linewidth=.3)
        axa.set_xlim(XL)
        axa.set_ylim(YL)
    
    ax_emi_pop.legend(loc='center', bbox_to_anchor=(-.11, -.28), ncol=6)
    
    fig.subplots_adjust(left=.1, bottom=.14, right=.95, top=.95, hspace=.2, wspace=.3)
    path_to_png = Path(path_to_tex_files, f'ts_gdp_pop_{iso3}.png')
    plt.savefig(path_to_png, dpi=300)
    plt.clf()
    plt.close(fig)

# %%
def df_to_table(table_body, caption, label, columns, hlines, **kwargs):
    
    table = \
        "\n\n \\begin{table}[H]" + \
        (kwargs['fontsize'] if 'fontsize' in kwargs.keys() else '') + \
        "\n \\centering" + \
        "\n \\caption{" f"{caption}" "}" + \
        "\n \\label{" f"{label}" "}" + \
        "\n \\begin{tabular}{" f"{columns}" "}"
    
    for row in range(len(hlines)):
        table += \
            "\n " + \
            " & ".join(table_body.loc[row, :].to_list()) + " \\tabularnewline " + \
            " ".join(['\\hline'] * hlines[row])
    
    table += \
        "\n \\end{tabular}" + \
        "\n \\end{table}"
    
    return table

# %%
def plot_ts_pc_cov():
    
    fig = plt.figure(figsize=(12, 4))
    
    ax_ts = fig.add_subplot(1, 2, 1)
    ax_corr = fig.add_subplot(1, 2, 2)
    
    yrs_to_plot = range(1990, 2031)
    yrs_corr = range(2010, 2018)
    
    ax_ts.set_xlim([yrs_to_plot[0], yrs_to_plot[-1]])
    ax_ts.set_ylim([-1, 101])
    
    for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
        
        ax_ts.plot(yrs_to_plot, 100. * getattr(tables_iso, f"{ssp_short}_pc_cov").data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
            linestyle=ssps_linestyle[ssp_short], color=colours['ssps'].loc[ssp_long, :].to_list(),
            label=f"dm{ssp_short}", linewidth=linewdth)
        
        for markersize, marker, yrs in zip([.5*markersze, markersze], ['o', 's'], [yrs_to_plot, yrs_corr]):
            ax_corr.scatter(
                getattr(tables_iso, f"{ssp_short}_emi").data.reindex(index=[iso3], columns=yrs).values[0],
                getattr(tables_iso, f"{ssp_short}_emi_cov").data.reindex(index=[iso3], columns=yrs).values[0],
                markersize, marker=marker, facecolor=colours['ssps'].loc[ssp_long, :].to_list())
    
    YL = [0, ax_corr.get_xlim()[-1]]
    ax_corr.set_xlim(YL)
    ax_corr.set_ylim(YL)
    
    ax_ts.set_xlabel("year", fontweight='bold')
    ax_ts.set_ylabel("%cov" "\n%", fontweight='bold')
    ax_corr.set_xlabel("national emissions" f"\n{units_iso['emi']['label']}", fontweight='bold')
    ax_corr.set_ylabel("covered emissions" f"\n{units_iso['emi']['label']}", fontweight='bold')
    
    ax_ts.legend(loc='center', bbox_to_anchor=(2.5, .5))
    hpf.put_labels_to_subplots(ax_ts, ax_corr)
    
    fig.subplots_adjust(left=.1, bottom=.15, right=.85, top=.95, wspace=.25)
    path_to_png = Path(path_to_tex_files, f'ts_pc_cov_{iso3}.png')
    plt.savefig(path_to_png, dpi=300)
    plt.clf()
    plt.close(fig)

# %%
def plot_ndcs():
    
    uni_mult_Mt_t = hpf.get_conversion_unit('Mt', 't')
    uni_mult = uni_mult_Mt_t * units_iso['emi']['multiplier']
    
    yrs_to_plot = range(1990, 2031)
    yrs_to_plot_str = [str(xx) for xx in yrs_to_plot]
    
    fig = plt.figure(figsize=(12, 4))
    
    ax_ts = fig.add_subplot(1, 2, 1)
    ax_vert = fig.add_subplot(1, 2, 2)
    
    # ax_ts
    
    for prio, line, colour_shade in \
        ['prio_NDCs', .5*linewdth, .5], \
        ['prio_SSPs', linewdth, 1]:
        
        for what in ['cov100', 'covest']:
            
            for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
                
                color_ssp = colours['ssps'].loc[ssp_long, :]
                data_act = ndc_quantis_ptws[prio][what][ssp_short]
                data_act = data_act.loc[data_act.iso3 == iso3, :]
                data_bau = data_act.loc[data_act.rge == 'emi_bau', yrs_to_plot_str]*uni_mult
                ax_ts.plot(
                    yrs_to_plot, data_bau.values[0], linestyle=ssps_linestyle[ssp_short],
                    linewidth=line, color=color_ssp,
                    label=(f"dm{ssp_short}" if (prio == 'prio_NDCs' and what == 'cov100') else '__nolegend__'))
                
                # Plot target range for SSP2
                if ssp_short == 'SSP2':
                    data_rge = data_act.loc[data_act.rge.isin(['best', 'worst']), yrs_to_plot_str]*uni_mult
                    if len(data_rge.index) != 4:
                        print(f"Warning for {iso3}: the length of data_act in plot_ndcs() is "
                              f"{len(data_act.index)} instead of 4!")
                    ax_ts.fill_between(
                        yrs_to_plot, data_rge.min(), data_rge.max(),
                        color=[xx*colour_shade for xx in color_ssp], alpha=.2)
    
    # ax_vert
    
    count = 0
    vertlines = []
    tars_ssp1_to_4 = []
    tars_ssp1_to_5 = []
    
    for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
        
        for prio in ['prio_NDCs', 'prio_SSPs']:
            
            for what in ['cov100', 'cov100_const_emi', 'cov100_bl_uncondi', 'cov100_lulucf_fao',
                         'covest', 'covest_const_emi', 'covest_bl_uncondi', 'covest_lulucf_fao']:
                
                color_ssp = colours['ssps'].loc[ssp_long, :]
                data_act = ndc_quantis_ptws[prio][what][ssp_short]
                data_act = data_act.loc[data_act.iso3 == iso3, :]
                data_rge = data_act.loc[data_act.rge.isin(['best', 'worst']), '2030']*uni_mult
                if len(data_rge.index) != 4:
                    print(f"Warning for {iso3}: the length of data_act in plot_ndcs() is "
                          f"{len(data_act.index)} instead of 4!")
                ax_vert.plot([count] * 4, data_rge.values, marker='.', markersize=3, color=color_ssp)
                
                if ssp_short != 'SSP5':
                    tars_ssp1_to_4 += data_rge.to_list()
                tars_ssp1_to_5 += data_rge.to_list()
                
                count += 1
                
                if 'fao' in what:
                    count += 1
                    vertlines += [count]
    
    YL = [min(ax_ts.get_ylim()[0], ax_vert.get_ylim()[0]),
          max(ax_ts.get_ylim()[1], ax_vert.get_ylim()[1])]
    YL = [YL[0], YL[1]*1.05]
    ax_ts.set_ylim(YL)
    ax_vert.set_ylim(YL)
    
    ax_ts.set_xlim([2010, 2030.5])
    ax_vert.set_xlim([-1, vertlines[-1]-1])
    
    ax_ts.set_xticks(range(2010, 2031, 5))
    ax_vert.set_xticks(np.arange(9, vertlines[-1], 20))
    ax_vert.set_xticklabels([f"dm{xx}" for xx in meta.ssps.scens.short])
    
    ylocs = [.17, .12, .07, .02]
    XL = ax_ts.get_xlim()
    YL = ax_ts.get_ylim()
    ax_ts.text(XL[0], YL[1] + ylocs[0]*np.diff(YL),
        '(a) Baseline emissions', fontweight='bold', ha='left', va='bottom')
    for yloc, txt in zip(ylocs[1:],
        [f'thinner lines per dmSSP: prio NDC (type_reclass = {type_reclass})',
         f'thicker lines per dmSSP: prio SSPs (type_main = {type_main})',
         'shaded area for conditionality range (default; prio NDC in dark vs. SSPs)']):
        ax_ts.text(XL[0], YL[1] + yloc*np.diff(YL), txt, ha='left', va='bottom', fontsize=8)
    XL = ax_vert.get_xlim()
    YL = ax_vert.get_ylim()
    yloc = YL[1] - .02*np.diff(YL)
    for xx in np.arange(-.5, 100, 20):
        ax_vert.plot([xx, xx + 8.9], [yloc, yloc], color=colour_prioNDCs, linewidth=3)
    for xx in np.arange(9.5, 100, 20):
        ax_vert.plot([xx, xx + 8.9], [yloc, yloc], color=colour_prioSSPs, linewidth=3)
    ax_vert.text(XL[0], YL[1] + ylocs[0]*np.diff(YL),
        '(b) NDC pathway for 2030', fontweight='bold', ha='left', va='bottom')
    ax_vert.text(XL[0], YL[1] + ylocs[1]*np.diff(YL),
        'prio NDC', color=colour_prioNDCs, ha='left', va='bottom', fontsize=8)
    ax_vert.text(XL[0] + .13*np.diff(XL), YL[1] + ylocs[1]*np.diff(YL),
        'vs.', color='k', ha='left', va='bottom', fontsize=8)
    ax_vert.text(XL[0] + .18*np.diff(XL), YL[1] + ylocs[1]*np.diff(YL),
        'prio SSPs', color=colour_prioSSPs, ha='left', va='bottom', fontsize=8)
    yloc = YL[1] - .04*np.diff(YL)
    for xx in np.arange(-.7, 100, 10):
        ax_vert.plot([xx, xx + 4.5], [yloc, yloc], color=colour_100pc, linewidth=2)
    for xx in np.arange(4.3, 100, 10):
        ax_vert.plot([xx, xx + 4.5], [yloc, yloc], color=colour_estpc, linewidth=2)
    ax_vert.text(XL[0], YL[1] + ylocs[2]*np.diff(YL),
        '100% coverage', color=colour_100pc,
        ha='left', va='bottom', fontsize=8)
    ax_vert.text(XL[0] + .21*np.diff(XL), YL[1] + ylocs[2]*np.diff(YL),
        'vs.', color='k',
        ha='left', va='bottom', fontsize=8)
    ax_vert.text(XL[0] + .26*np.diff(XL), YL[1] + ylocs[2]*np.diff(YL),
        'estimated coverage', color=colour_estpc,
        ha='left', va='bottom', fontsize=8)
    ax_vert.text(XL[0], YL[1] + ylocs[3]*np.diff(YL),
        'Quadruples:  options  "default",  "const. emissions",  "bl uncondi.",  "LULUCF FAO"',
        ha='left', va='bottom', fontsize=8)
    
    for vert_line in vertlines[:-1]:
        ax_vert.plot([vert_line-1, vert_line-1], YL, 'k:', linewidth=.5)
    
    ax_ts.legend()
    
    ax_ts.set_xlabel('year', fontweight='bold')
    uni_lbl = f"{units_iso['emi']['label'].replace('~', ' ')} AR4"
    ax_ts.set_ylabel('emissions' f"\n{uni_lbl}", fontweight='bold')
    ax_vert.set_ylabel('emissions' f"\n{uni_lbl}", fontweight='bold')
    
    fig.subplots_adjust(left=.1, bottom=.15, right=.95, top=.8, wspace=.25)
    path_to_png = Path(path_to_tex_files, f'ts_ndcs_quantis_{iso3}.png')
    plt.savefig(path_to_png, dpi=300)
    plt.clf()
    plt.close(fig)
    
    return tars_ssp1_to_4, tars_ssp1_to_5

# %%
def plot_ndcs_earth():
    
    if tars_excl_or_incl_USA == 'exclUSA':
        ndc_quantis_ptws_earth = ndc_quantis_ptws_earth_exclUSA
    if tars_excl_or_incl_USA == 'inclUSA':
        ndc_quantis_ptws_earth = ndc_quantis_ptws_earth_inclUSA
    
    uni_mult = 1e-3 # Mt to Gt
    
    yrs_to_plot = range(1990, 2031)
    yrs_to_plot_str = [str(xx) for xx in yrs_to_plot]
    
    fig = plt.figure(figsize=(12, 4))
    
    ax_ts = fig.add_subplot(1, 2, 1)
    ax_vert = fig.add_subplot(1, 2, 2)
    
    # ax_ts
    
    for prio, line, colour_shade in \
        ['prio_NDCs', .5*linewdth, .5], \
        ['prio_SSPs', linewdth, 1]:
        
        for what in ['cov100', 'covest']:
            
            for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
                
                color_ssp = colours['ssps'].loc[ssp_long, :]
                data_act = ndc_quantis_ptws_earth[prio][what][ssp_short]
                data_act = data_act.loc[data_act.group == 'EARTH', :]
                data_bau = data_act.loc[data_act.rge == 'emi_bau', yrs_to_plot_str]*uni_mult
                ax_ts.plot(
                    yrs_to_plot, data_bau.values[0], linestyle=ssps_linestyle[ssp_short],
                    linewidth=line, color=color_ssp,
                    label=(f"dm{ssp_short}" if (prio == 'prio_NDCs' and what == 'cov100') else '__nolegend__'))
                
                # Plot target range for SSP2
                if ssp_short == 'SSP2':
                    data_rge = data_act.loc[data_act.rge.isin(['best', 'worst']), yrs_to_plot_str]*uni_mult
                    if len(data_rge.index) != 4:
                        print(f"Warning for {iso3}: the length of data_act in plot_ndcs() is "
                              f"{len(data_act.index)} instead of 4!")
                    ax_ts.fill_between(
                        yrs_to_plot, data_rge.min(), data_rge.max(),
                        color=[xx*colour_shade for xx in color_ssp], alpha=.2)
    
    # ax_vert
    
    count = 0
    vertlines = []
    tars_ssp1_to_4 = []
    tars_ssp1_to_5 = []
    
    for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
        
        for prio in ['prio_NDCs', 'prio_SSPs']:
            
            for what in ['cov100', 'cov100_const_emi', 'cov100_bl_uncondi', 'cov100_lulucf_fao',
                         'covest', 'covest_const_emi', 'covest_bl_uncondi', 'covest_lulucf_fao']:
                
                color_ssp = colours['ssps'].loc[ssp_long, :]
                data_act = ndc_quantis_ptws_earth[prio][what][ssp_short]
                data_act = data_act.loc[data_act.group == 'EARTH', :]
                data_rge = data_act.loc[data_act.rge.isin(['best', 'worst']), '2030']*uni_mult
                if len(data_rge.index) != 4:
                    print(f"Warning for {iso3}: the length of data_act in plot_ndcs() is "
                          f"{len(data_act.index)} instead of 4!")
                ax_vert.plot([count] * 4, data_rge.values, marker='.', markersize=3, color=color_ssp)
                
                if ssp_short != 'SSP5':
                    tars_ssp1_to_4 += data_rge.to_list()
                tars_ssp1_to_5 += data_rge.to_list()
                
                count += 1
                
                if 'fao' in what:
                    count += 1
                    vertlines += [count]
    
    YL = [42.5, 67.5]
    ax_ts.set_ylim(YL)
    ax_vert.set_ylim(YL)
    
    ax_ts.set_xlim([2010, 2030.5])
    ax_vert.set_xlim([-1, vertlines[-1]-1])
    
    ax_ts.set_xticks(range(2010, 2031, 5))
    ax_vert.set_xticks(np.arange(9, vertlines[-1], 20))
    ax_vert.set_xticklabels([f"dm{xx}" for xx in meta.ssps.scens.short])
    
#    ylocs = [.17, .12, .07, .02]
#    XL = ax_ts.get_xlim()
#    YL = ax_ts.get_ylim()
#    ax_ts.text(XL[0], YL[1] + ylocs[0]*np.diff(YL),
#        '(a) Baseline emissions', fontweight='bold', ha='left', va='bottom')
#    for yloc, txt in zip(ylocs[1:],
#        [f'thinner lines per dmSSP: prio NDC (type_reclass = {type_reclass})',
#        f'thicker lines per dmSSP: prio SSPs (type_main = {type_main})',
#        'shaded area for conditionality range (default; prio NDC in dark vs. SSPs)']):
#        ax_ts.text(XL[0], YL[1] + yloc*np.diff(YL), txt, ha='left', va='bottom', fontsize=8)
    XL = ax_vert.get_xlim()
    YL = ax_vert.get_ylim()
    yloc = YL[1] - .02*np.diff(YL)
    for xx in np.arange(-.5, 100, 20):
        ax_vert.plot([xx, xx + 8.9], [yloc, yloc], color=colour_prioNDCs, linewidth=3)
    for xx in np.arange(9.5, 100, 20):
        ax_vert.plot([xx, xx + 8.9], [yloc, yloc], color=colour_prioSSPs, linewidth=3)
#    ax_vert.text(XL[0], YL[1] + ylocs[0]*np.diff(YL),
#        '(b) NDC pathway for 2030', fontweight='bold', ha='left', va='bottom')
#    ax_vert.text(XL[0], YL[1] + ylocs[1]*np.diff(YL),
#        'prio NDC', color=colour_prioNDCs, ha='left', va='bottom', fontsize=8)
#    ax_vert.text(XL[0] + .13*np.diff(XL), YL[1] + ylocs[1]*np.diff(YL),
#        'vs.', color='k', ha='left', va='bottom', fontsize=8)
#    ax_vert.text(XL[0] + .18*np.diff(XL), YL[1] + ylocs[1]*np.diff(YL),
#        'prio SSPs', color=colour_prioSSPs, ha='left', va='bottom', fontsize=8)
    yloc = YL[1] - .04*np.diff(YL)
    for xx in np.arange(-.7, 100, 10):
        ax_vert.plot([xx, xx + 4.5], [yloc, yloc], color=colour_100pc, linewidth=2)
    for xx in np.arange(4.3, 100, 10):
        ax_vert.plot([xx, xx + 4.5], [yloc, yloc], color=colour_estpc, linewidth=2)
#    ax_vert.text(XL[0], YL[1] + ylocs[2]*np.diff(YL),
#        '100% coverage', color=colour_100pc,
#        ha='left', va='bottom', fontsize=8)
#    ax_vert.text(XL[0] + .21*np.diff(XL), YL[1] + ylocs[2]*np.diff(YL),
#        'vs.', color='k',
#        ha='left', va='bottom', fontsize=8)
#    ax_vert.text(XL[0] + .26*np.diff(XL), YL[1] + ylocs[2]*np.diff(YL),
#        'estimated coverage', color=colour_estpc,
#        ha='left', va='bottom', fontsize=8)
#    ax_vert.text(XL[0], YL[1] + ylocs[3]*np.diff(YL),
#       'Quadruples:  options  "default",  "const. emissions",  "bl uncondi.",  "LULUCF FAO"',
#        ha='left', va='bottom', fontsize=8)
    
    for hor_line in np.arange(47.5, 67.5, 2.5):
        ax_vert.plot(XL, [hor_line, hor_line], 'k:', linewidth=.5)
    
    for vert_line in vertlines[:-1]:
        ax_vert.plot([vert_line-1, vert_line-1], YL, 'k:', linewidth=.5)
    
    ax_ts.legend()
    
    ax_ts.set_xlabel('year', fontweight='bold')
    uni_lbl = "Gt CO$_2$eq AR4"
    ax_ts.set_ylabel('emissions' f"\n{uni_lbl}", fontweight='bold')
    ax_vert.set_ylabel('emissions' f"\n{uni_lbl}", fontweight='bold')
    
    fig.subplots_adjust(left=.1, bottom=.15, right=.95, top=.8, wspace=.25)
    path_to_png = Path(path_to_tex_files, f'ts_ndcs_quantis_earth_{tars_excl_or_incl_USA}.png')
    plt.savefig(path_to_png, dpi=300)
    plt.clf()
    plt.close(fig)
    
    return tars_ssp1_to_4, tars_ssp1_to_5

# %%
for iso3 in meta.isos.EARTH:
    
    print(iso3)
    
    if iso3 == 'USA':
        ndc_quantis_tars, ndc_quantis_ptws = ndc_quantis_tars_inclUSA, ndc_quantis_ptws_inclUSA
    else:
        ndc_quantis_tars, ndc_quantis_ptws = ndc_quantis_tars_exclUSA, ndc_quantis_ptws_exclUSA
    
    # %%
    ctr = meta.isos.iso3_to_shortname[iso3].replace("&", "\&")
    ctr_the_lc = (f'the {ctr}' if ctr in ['USA'] else ctr)
    ctr_the_uc = (f'The {ctr}' if ctr in ['USA'] else ctr)
    
    path_to_tex_files = Path(path_out, iso3)
    Path(path_to_tex_files).mkdir(parents=True, exist_ok=True)
    
    # %%
    # Get the tables for iso3 and change the units to 'nice looking units'.
    
    # Get highest emissions in SSPs_emi.
    emi_min, emi_max = 0, 0
    for tablename in [f"{xx}_emi" for xx in meta.ssps.scens.short]:
        data = getattr(tables, tablename).__subset__(isos=[iso3]).data
        emi_min = min([emi_min, data.min(axis=1).values[0]])
        emi_max = max([emi_max, data.max(axis=1).values[0]])
    
    units_iso = {}
    units_iso['emi'] = {}
    units_iso['emi']['unit'], units_iso['emi']['multiplier'] = hpf.get_conversion_to_nice_unit([emi_min, emi_max], 
        getattr(tables, 'SSP1_emi').unit) # Have all the same unit.
    
    for tablename in ['SSP2_emi_gdp', 'SSP2_emi_pop', 'SSP2_gdp', 'SSP2_pop']:
        table = getattr(tables, tablename).__subset__(isos=[iso3])
        tpe = tablename.replace('SSP2_', '')
        units_iso[tpe] = {}
        units_iso[tpe]['unit'], units_iso[tpe]['multiplier'] = \
            hpf.get_conversion_to_nice_unit(table.data, table.unit)
    
    # %%
    # Get the table entries for iso3 and convert the units.
    tables_iso = hpf.create_class(name='tables_iso')
    tables_iso_df = pd.DataFrame()
    
    for tablename in hpf.get_all_attributes_of_class(tables):
        
        table = getattr(tables, tablename).__subset__(isos=[iso3])
        
        if ('share' not in tablename) and ('pc_cov' not in tablename):
            
            if table.family == 'emi/gdp':
                unit_act = units_iso['emi_gdp']
            
            elif table.family == 'emi/pop':
                unit_act = units_iso['emi_pop']
            
            else:
                unit_act = units_iso[table.family]
            
            table.data = table.data * unit_act['multiplier']
            table.unit = unit_act['unit']
        
        setattr(tables_iso, tablename, table)
        
        # TODO: not efficient.
        if tablename != 'emi_his_all':
            
            for attr in hpf.get_all_attributes_of_class(table):
                if attr == 'data':
                    for yr in table.data.columns:
                        tables_iso_df.loc[table.tablename, yr] = table.data.loc[iso3, yr]
                else:
                    tables_iso_df.loc[table.tablename, attr] = getattr(table, attr)
    
    # Write data to csv-file.
    tables_iso_df_cols_yrs = [xx for xx in tables_iso_df.columns if type(xx) == int]
    tables_iso_df_cols_attrs = [xx for xx in tables_iso_df.columns if type(xx) == str]
    tables_iso_df.loc[:, tables_iso_df_cols_attrs + tables_iso_df_cols_yrs]. \
        to_csv(Path(path_to_tex_files, f'data_{iso3}.csv'))
    
    if not tables_iso_df.loc['KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21', range(1990, 2018)].isnull().all():
        
        # %%
        sum_start1850_share_iso = 100. * sum_start1850.loc[iso3] / sum_start1850.reindex(index=meta.isos.EARTH).sum()
        sum_start1990_share_iso = 100. * sum_start1990.loc[iso3] / sum_start1990.reindex(index=meta.isos.EARTH).sum()
        #sum_start1850_iso = sum_start1850.loc[iso3] * units_iso['emi']['multiplier']
        #sum_start1990_iso = sum_start1990.loc[iso3] * units_iso['emi']['multiplier']
        
        # %%
        # Which gas / sector was the driver in the recent emissions trend.
        
        # Get the historical entity + sector that has the closest slope to 1 for
        # a linear regression between KYOTOGHG_IPCM0EL and emissions per sector+gas combi.
        combi_slopes = pd.DataFrame(index=combis_ent_cat[1:], columns=['slope', 'rvalue', 'emi_yr_his', 'share_yr_his'])
        yrs_corr = list(range(2010, yr_his+1))
        
        for combi in combis_ent_cat[1:]:
            
            try:
                xx = getattr(tables, 'KYOTOGHG_IPCM0EL').data.loc[iso3, yrs_corr] * units_iso['emi']['multiplier']
                yy = getattr(tables, combi).data.loc[iso3, yrs_corr] * units_iso['emi']['multiplier']
                xx, yy, linreg = hpf.linear_regression(xx, yy)
                combi_slopes.loc[combi, 'rvalue'] = linreg.rvalue
                combi_slopes.loc[combi, 'slope'] = linreg.slope
                combi_slopes.loc[combi, 'emi_yr_his'] = yy[-1]
                combi_slopes.loc[combi, 'share_yr_his'] = 100. * yy[-1] / xx[-1]
            except:
                pass
        
        sec_to_label = meta.sectors.main.sec_to_label
        combi_for_trend = combi_slopes.slope.sort_values(ascending=False)
        lim_slope = .2
        if any(combi_for_trend > lim_slope):
            
            combi_for_trend = combi_for_trend[combi_for_trend > lim_slope]
            trend_gas, trend_sec, trend_gas_txt, trend_sec_txt = [], [], [], []
            for ind in combi_for_trend.index:
                
                gas, cat = ind.split('_')
                trend_gas += [gas]
                trend_sec += [cat]
                
                trend_gas_txt += [meta.gases.gas_to_label[gas]]
                trend_sec_txt += [sec_to_label[meta.categories.main.cat_to_sec[cat]]]
            
            txt_emi_trend = f"\n The trend in total emissions is mostly driven by "
            
            if len(set(trend_gas)) == 1: # 1 gas
                if len(set(trend_sec)) == 1: # 1 sector
                    txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, "
                    nr_trend = 1
                elif len(set(trend_sec)) == 2: # 2 sectors
                    txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} and " + \
                        f"{trend_sec_txt[1]} sectors, "
                    nr_trend = 2
                elif len(set(trend_sec)) > 2: # 3 sectors
                    txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]}, " + \
                        f"{trend_sec_txt[1]}, and {trend_sec_txt[2]} sectors, "
                    nr_trend = 3
            
            elif len(set(trend_gas)) == 2: # 2 gases
                if len(set(trend_sec)) == 1: # 2 gases, 1 sector
                    txt_emi_trend += f"{trend_gas_txt[0]} and {trend_gas_txt[1]} emissions from the {trend_sec_txt[0]} sector, "
                    nr_trend = 2
                elif len(set(trend_sec)) == 2: # 2 gases, 2 sectors
                    txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, " + \
                        f"and {trend_gas_txt[1]} emissions from the {trend_sec_txt[1]} sector, "
                    nr_trend = 2
                elif len(set(trend_sec)) > 2: # 2 gases, 3 sectors.
                    txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, " + \
                        f"{trend_gas_txt[1]} emissions from the {trend_sec_txt[1]} sector, " + \
                        f"and {trend_gas_txt[2]} emissions from the {trend_sec_txt[2]} sector, "
                    nr_trend = 3
            
            elif len(set(trend_gas)) > 2: # 3 gases
                if len(set(trend_sec)) == 1: # 3 gases, 1 sector
                    txt_emi_trend += f"{trend_gas_txt[0]}, {trend_gas_txt[1]} and {trend_gas_txt[2]} " + \
                        f"emissions from the {trend_sec_txt[0]} sector, "
                    nr_trend = 3
                elif len(set(trend_sec)) == 2: # 3 gases, 2 sectors
                    txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, " + \
                        f"{trend_gas_txt[1]} emissions from the {trend_sec_txt[1]} sector, " + \
                        f"and {trend_gas_txt[2]} emissions from the {trend_sec_txt[2]} sector, "
                    nr_trend = 3
                elif len(set(trend_sec)) > 2: # 3 gases, 3 sectors
                    txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, " + \
                        f"{trend_gas_txt[1]} emissions from the {trend_sec_txt[1]} sector, " + \
                        f"and {trend_gas_txt[2]} emissions from the {trend_sec_txt[2]} sector, "
                    nr_trend = 3
            
            if nr_trend == 1:
                number = hpf.num_to_str_one_non_zero_decimal(
                    combi_slopes.loc[trend_gas[0] + '_' + trend_sec[0], 'share_yr_his'].sum())
                txt_emi_trend += f"which contributed {number}\% "
            elif nr_trend == 2:
                number1 = hpf.num_to_str_one_non_zero_decimal(
                    combi_slopes.loc[trend_gas[0] + '_' + trend_sec[0], 'share_yr_his'].sum())
                number2 = hpf.num_to_str_one_non_zero_decimal(
                    combi_slopes.loc[trend_gas[1] + '_' + trend_sec[1], 'share_yr_his'].sum())
                txt_emi_trend += f"which contributed {number1}\% and {number2}\% "
            elif nr_trend == 3:
                number1 = hpf.num_to_str_one_non_zero_decimal(
                    combi_slopes.loc[trend_gas[0] + '_' + trend_sec[0], 'share_yr_his'].sum())
                number2 = hpf.num_to_str_one_non_zero_decimal(
                    combi_slopes.loc[trend_gas[1] + '_' + trend_sec[1], 'share_yr_his'].sum())
                number3 = hpf.num_to_str_one_non_zero_decimal(
                    combi_slopes.loc[trend_gas[2] + '_' + trend_sec[2], 'share_yr_his'].sum())
                txt_emi_trend += f"which contributed {number1}\%, {number2}\%, and {number3}\% "
            
            txt_emi_trend += f"to {ctr_the_lc}'s 2017 emissions."
            txt_emi_trend += \
                "\\footnote{" + \
                "Analysis based on the correlations between total national emissions (exclLU) " + \
                "versus the emissions of the combinations of main-sectors \& the gases " + \
                "CO$_2$, CH$_4$, N$_2$O and F-gases. " + \
                f"\n Only data from {yrs_corr[0]} to {yrs_corr[-1]} are assessed. " + \
                "\n The (up to) three gas \& sector combinations are chosen for which the slope of the " + \
                f"regression line to the correlated values exceeds {lim_slope}." + \
                "}"
        
        else:
            txt_emi_trend = ""
    
        # %%
        # Nicer unit lables.
        units_iso['emi']['label'] = units_iso['emi']['unit'].replace('CO2', 'CO$_2$')
        units_iso['gdp']['label'] = units_iso['gdp']['unit'].replace('2011GKD', ' 2011 GK\$')
        units_iso['emi_gdp']['label'] = units_iso['emi_gdp']['unit'].replace('CO2', 'CO$_2$').replace('2011GKD', ' 2011 GK\$')
        units_iso['pop']['label'] = units_iso['pop']['unit'].replace('Pers', ' Pers')
        units_iso['emi_pop']['label'] = units_iso['emi_pop']['unit'].replace('CO2', 'CO$_2$').replace('Pers', ' Pers')
        for what in ['emi', 'gdp' ,'emi_gdp', 'pop', 'emi_pop']:
            units_iso[what]['label'] = units_iso[what]['label'].replace(' ', '~')
        
        # %% For Overview
        
        # Table with total emissions, share of global emissions and ranking (1990 & 2017 & 2030).
        # Also for GDP, population and emi/GDP, emi/capita.
        # SSP2.
        
        overview_table = pd.DataFrame(
            columns=['unit', 'tot_his', 'share_his', 'rank_his', 'tot_fut', 'share_fut', 'rank_fut'],
            index=['emi', 'gdp', 'emi_gdp', 'pop', 'emi_pop'])
        yr_fut = 2030
        
        for tpe in overview_table.index:
            for when, yr in ['1990', 1990], ['his', yr_his], ['fut', yr_fut]:
                overview_table.loc[tpe, 'tot_' + when] = \
                    getattr(tables_iso, 'SSP2_' + tpe).data.loc[iso3, yr]
                overview_table.loc[tpe, 'share_' + when] = \
                    getattr(tables_iso, 'SSP2_' + tpe + '_share').data.loc[iso3, yr] * 100.
                overview_table.loc[tpe, 'rank_' + when] = \
                    '{:.0f}'.format(getattr(tables, 'SSP2_' + tpe + '_share').data.reindex(index=meta.isos.EARTH).reindex(columns=[yr]). \
                        rank(method='dense', ascending=False).loc[iso3, yr])
            
            # Put in the units.
            unit_act = getattr(tables_iso, 'SSP2_' + tpe).unit
            unit_act = (unit_act.replace('CO2', 'CO$_2$') if 'CO2' in unit_act else unit_act)
            unit_act = (unit_act.replace('2011GKD', ' 2011~GK\$') if '2011GKD' in unit_act else unit_act)
            unit_act = (unit_act.replace('Pers', ' Pers') if 'Pers' in unit_act else unit_act)
            overview_table.loc[tpe, 'unit'] = unit_act
        
        # Table of strings.
        mapping = {'emi': 'Emissions', 'gdp': 'GDP (PPP)', 'emi_gdp': 'Emissions per GDP (PPP)',
                   'pop': 'Population', 'emi_pop': 'Emissions per capita'}
        overview_table_str = pd.DataFrame()
        row = 0
        for tpe in mapping.keys():
            overview_table_str.loc[row, 'Year'] = '1990'
            overview_table_str.loc[row+1, 'Year'] = str(yr_his)
            overview_table_str.loc[row+2, 'Year'] = str(yr_fut)
            overview_table_str.loc[row, 'Total'] = hpf.num_to_str_one_non_zero_decimal(
                overview_table.loc[tpe, 'tot_1990'])
            overview_table_str.loc[row+1, 'Total'] = hpf.num_to_str_one_non_zero_decimal(
                overview_table.loc[tpe, 'tot_his'])
            overview_table_str.loc[row+2, 'Total'] = hpf.num_to_str_one_non_zero_decimal(
                overview_table.loc[tpe, 'tot_fut'])
            overview_table_str.loc[[row, row+1, row+2], 'Unit'] = overview_table.loc[tpe, 'unit']
            overview_table_str.loc[row, 'Glob. share'] = hpf.num_to_str_one_non_zero_decimal(
                overview_table.loc[tpe, 'share_1990']) + "\%"
            overview_table_str.loc[row+1, 'Glob. share'] = hpf.num_to_str_one_non_zero_decimal(
                overview_table.loc[tpe, 'share_his']) + "\%"
            overview_table_str.loc[row+2, 'Glob. share'] = hpf.num_to_str_one_non_zero_decimal(
                overview_table.loc[tpe, 'share_fut']) + "\%"
            overview_table_str.loc[row, 'Rank'] = \
                '{:}'.format(overview_table.loc[tpe, 'rank_1990'])
            overview_table_str.loc[row+1, 'Rank'] = \
                '{:}'.format(overview_table.loc[tpe, 'rank_his'])
            overview_table_str.loc[row+2, 'Rank'] = \
                '{:}'.format(overview_table.loc[tpe, 'rank_fut'])
            row += 3
        
        overview_table_str.insert(0, '', 
            ['Emissions', '', '', 'GDP', '', '', 'Emissions', 'per GDP', '',
             'Population', '', '', 'Emissions', 'per capita', ''])
        
        # %%
        gases_table = pd.DataFrame(index=['KYOTOGHG'] + meta.gases.kyotoghg, columns=['emi', 'share'])
        for gas in gases_table.index:
            gases_table.loc[gas, 'emi'] = getattr(tables_iso, f"{gas}_IPCM0EL").data.loc[iso3, yr_his]
            gases_table.loc[gas, 'share'] = 100. * gases_table.loc[gas, 'emi'] / gases_table.loc['KYOTOGHG', 'emi']
        
        cats_table = pd.DataFrame(index=['IPCM0EL'] + meta.categories.main.exclLU, columns=['emi', 'share'])
        for cat in cats_table.index:
            cats_table.loc[cat, 'emi'] = getattr(tables_iso, f"KYOTOGHG_{cat}").data.loc[iso3, yr_his]
            cats_table.loc[cat, 'share'] = 100. * cats_table.loc[cat, 'emi'] / cats_table.loc['IPCM0EL', 'emi']
        
        ssps_table = pd.DataFrame(index=meta.ssps.scens.short, columns=[2017, 2030, 2050])
        for yr in ssps_table.columns:
            for ssp in ssps_table.index:
                ssps_table.loc[ssp, yr] = getattr(tables_iso, f"{ssp}_emi").data.loc[iso3, yr]
        
        # %%
        tot_emi_his = hpf.num_to_str_one_non_zero_decimal(
            cats_table.loc['IPCM0EL', 'emi'])
        
        highest_sec_his_1st = sec_to_label[meta.categories.main.cat_to_sec[
            cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False).index[0]]]
        highest_sec_his_share_1st = hpf.num_to_str_one_non_zero_decimal(
            cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False)[0])
        highest_sec_his_2nd = sec_to_label[meta.categories.main.cat_to_sec[
            cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False).index[1]]]
        highest_sec_his_share_2nd = hpf.num_to_str_one_non_zero_decimal(
            cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False)[1])
        highest_sec_his_3rd = sec_to_label[meta.categories.main.cat_to_sec[
            cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False).index[2]]]
        highest_sec_his_share_3rd = hpf.num_to_str_one_non_zero_decimal(
            cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False)[2])
        
        highest_gas_his_1st = meta.gases.gas_to_label[gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False).index[0]]
        highest_gas_his_share_1st = hpf.num_to_str_one_non_zero_decimal(
            gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False)[0])
        highest_gas_his_2nd = meta.gases.gas_to_label[gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False).index[1]]
        highest_gas_his_share_2nd = hpf.num_to_str_one_non_zero_decimal(
            gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False)[1])
        highest_gas_his_3rd = meta.gases.gas_to_label[gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False).index[2]]
        highest_gas_his_share_3rd = hpf.num_to_str_one_non_zero_decimal(
            gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False)[2])
        
        share_fgases_his = hpf.num_to_str_one_non_zero_decimal(
            gases_table.loc[meta.gases.fgases, 'share'].sum())
        
        ssp2_2030 = hpf.num_to_str_one_non_zero_decimal(
            ssps_table.loc[ssp2_short, 2030])
        ssp2_2030_pc = hpf.num_to_str_one_non_zero_decimal(
            100. * (ssps_table.loc[ssp2_short, 2030] / ssps_table.loc[ssp2_short, 2017] - 1))
                
        # %%
        # Calculate the linear regressions for gdp, pop and emi/gdp and emi/pop for 2010 to most recent value.
        # SSP2.
        
        yrs_linreg = range(2010, 2018)
        _, _, gdp_linreg = hpf.linear_regression(yrs_linreg, tables_iso.SSP2_gdp.data.loc[iso3, yrs_linreg])
        _, _, emi_gdp_linreg = hpf.linear_regression(yrs_linreg, tables_iso.SSP2_emi_gdp.data.loc[iso3, yrs_linreg])
        _, _, pop_linreg = hpf.linear_regression(yrs_linreg, tables_iso.SSP2_pop.data.loc[iso3, yrs_linreg])
        _, _, emi_pop_linreg = hpf.linear_regression(yrs_linreg, tables_iso.SSP2_emi_pop.data.loc[iso3, yrs_linreg])
        
        # %%
        ndc_iso3 = infos_from_ndcs.loc[iso3, :]
        has_ndc = ndc_iso3['NDC_INDC']
        type_main = ndc_iso3['TYPE_MAIN']
        type_reclass = ndc_iso3['TYPE_RECLASS']
        
        # %%
        linewdth = 2
        markersze = 10
        
        # %%
        plot_map()
        plot_ts_nonLULUCF()
        plot_ts_normalised_nonLULUCF()
        plot_ts_LULUCF()
        plot_ts_gdp_pop()
        
        # %%
        txt = \
            "\\documentclass[12pt]{article}" + \
            "\n\n %%%" + \
            "\n \\usepackage[utf8]{inputenc}" + \
            "\n \\usepackage{graphicx}" + \
            "\n \\usepackage{xcolor}" + \
            "\n \\usepackage{hyperref}" + \
            "\n \\hypersetup{colorlinks, linkcolor = black, citecolor = black, filecolor = black, " + \
            "urlcolor = [RGB]{227, 114, 34}}" + \
            "\n \\usepackage{float}" + \
            "\n \\usepackage{geometry}\geometry{a4paper, total={170mm,257mm}, left=20mm, top=20mm}" + \
            "\n\n \\definecolor{PIKorange}{RGB}{227, 114, 34}" + \
            "\n \\definecolor{PIKgray}{RGB}{142, 144, 143}"
        
        # %%
        txt += \
            "\n\n \\title{" " \\bfseries \\color{PIKorange} " + \
            f"{ctr}: information on national emissions, population and GDP, and mitigation targets" "}"
    
        txt += \
            "\n\n %%%" + \
            "\n\n \\begin{document}"
        
        txt += \
            "\n\n \\maketitle" #+ \
#            "\n\n %%%" + \
#            "\n \\noindent \\textbf{Authors:} \\newline" + \
#            "\n \\indent Annika Guenther$^{1}$ \\newline" + \
#            "\n \\indent Johannes Guetschow$^{1}$ \\newline" + \
#            "\n \\noindent \\textbf{Affiliations:} \\newline" + \
#            "\n \\indent 1. Potsdam Institute for Climate Impact Research, Germany \\newline" + \
#            "\n \\noindent \\textbf{DOI:} [to be added] \\newline"
       
        # %%
        # TODO!
        # txt += \
        #     "\n\n \\textbf{TODO}" + \
        #     "\n \\begin{itemize}" + \
        #     "\n \\item GWP: NDC emissions coverted from AR2 to AR4 by national conversion factor (2010--2017, PRIMAP-hist v2.1)." + \
        #     "\n \\item References!" + \
        #     "\n \\item Only plot the \% cov if it is not above 99 or below 1." + \
        #     "\n \\item Maybe plot world maps? Emissions, population, GDP? And zoom into the country's area?" + \
        #     "\n \\end{itemize}"
        
        # %% Non-LULUCF emissions and socioeconomic data.
        txt += \
            "\n\n \\section{Emissions and socioeconomic data}" + \
            "\n \\label{sec:nonLULUCFSocioEco}"
        
        number1 = hpf.num_to_str_one_non_zero_decimal(
            overview_table.loc['emi', 'share_his'])
        number2 = hpf.num_to_str_one_non_zero_decimal(
            overview_table.loc['emi', 'share_fut'])
        
        if number1 == number2:
            txt_act1, txt_act2 = "and", "stay at a similar level"
        else:
            txt_act1, txt_act2 = "while", \
                ("increase to" if float(number2) > float(number1) else "decrease to") + f" {number2}\%"
        
        txt += \
            f"\n With national emissions of {tot_emi_his}~{units_iso['emi']['label']}, {ctr_the_lc} contributed " + \
            f"{number1}\% to global emissions in {yr_his} " "(Fig.~\\ref{fig:tsEmiMap}), " + \
            f"{txt_act1} in {yr_fut} its share is estimated to {txt_act2} " "(Table~\\ref{tab:overview})." + \
            f"\n The estimate for {yr_fut} is based on the {ssp2_short}" + \
            f" 'Middle of the Road' marker scenario, which has been downscaled to country-level (dm{ssp2_short})." + \
            f"\nIn this scenario, {ctr_the_lc} is estimated to emit " + \
            f"{ssp2_2030}~{units_iso['emi']['label']} in {yr_fut}, "
        if float(ssp2_2030_pc) > 0.:
            txt += ("an increase" if float(ssp2_2030_pc) < 10 else "a substantial increase")
        elif float(ssp2_2030_pc) < 0.:
            txt += ("a decrease" if float(ssp2_2030_pc) > -10 else "a substantial decrease")
        elif float(ssp2_2030_pc) == 0:
            txt += "no real change"
        txt += f" of {ssp2_2030_pc}\% compared to {yr_his}. "
        ##
        number1 = hpf.num_to_str_one_non_zero_decimal(
            ssps_table.loc[:, 2030].min())
        number2 = hpf.num_to_str_one_non_zero_decimal(
            ssps_table.loc[:, 2030].max())
        number3 = hpf.num_to_str_one_non_zero_decimal(
            ssps_table.loc[:, 2050].min())
        number4 = hpf.num_to_str_one_non_zero_decimal(
            ssps_table.loc[:, 2050].max())
        txt += \
            f"\n The pathways dmSSP1--5 show a range of {number1}" + \
            f"--{number2}~{units_iso['emi']['label']} in 2030, and of " + \
            f"{number3}--{number4}~{units_iso['emi']['label']} in 2050 " + \
            "(Fig.~\\ref{fig:tsEmi})." + \
            "\n The different SSP projections are based on five socioeconomic narratives and " + \
            "coherent challenges in terms of mitigation and adaptation."
        ##
        if ((f"{overview_table.loc['emi_gdp', 'rank_his']}" != "nan")
            and (f"{overview_table.loc['emi_pop', 'rank_his']}" != "nan")):
            txt_act = \
                "\n The country's global rank in terms of total emissions per unit of GDP was " + \
                    f"{overview_table.loc['emi_gdp', 'rank_his']} in {yr_his}, " + \
                    ('while it was ' if (abs(int(overview_table.loc['emi_pop', 'rank_his']) - int(overview_table.loc['emi_gdp', 'rank_his'])) > 5)
                     else 'and ') + \
                    f"{overview_table.loc['emi_pop', 'rank_his']} regarding the per-capita emissions"
            txt_act += \
                (f" ({overview_table.loc['emi_gdp', 'rank_fut']} and {overview_table.loc['emi_pop', 'rank_fut']} in {yr_fut}, respectively)."
                 if f"{overview_table.loc['emi_gdp', 'rank_fut']}" != "nan" else ".")
        elif f"{overview_table.loc['emi_gdp', 'rank_his']}" != "nan":
            txt_act = \
                "\n The country's global rank in terms of total emissions per unit of GDP was " + \
                    f"{overview_table.loc['emi_gdp', 'rank_his']} in {yr_his}"
            txt_act += \
                (f" ({overview_table.loc['emi_gdp', 'rank_fut']} in {yr_fut})."
                 if f"{overview_table.loc['emi_gdp', 'rank_fut']}" != "nan" else ".")
        elif f"{overview_table.loc['emi_pop', 'rank_his']}" != "nan":
            txt_act = \
                "\n The country's global rank in terms of total per-capita emissions was " + \
                    f"{overview_table.loc['emi_pop', 'rank_his']} in {yr_his}"
            txt_act += \
                (f" ({overview_table.loc['emi_pop', 'rank_fut']} in {yr_fut})."
                 if f"{overview_table.loc['emi_pop', 'rank_fut']}" != "nan" else ".")
        else:
            txt_act = ""
        
        txt += txt_act
        
        ##
        # Historical share.
        number = hpf.num_to_str_one_non_zero_decimal(sum_start1850_share_iso)
        txt += \
            f"\n As for the accumulated historical emissions, {ctr_the_lc}" + \
            f" contributed to the global {yr_sum_start1850}--{yr_his} emissions by {number}\%. "
        number1 = hpf.num_to_str_one_non_zero_decimal(sum_start1990_share_iso)
        #number2 = hpf.num_to_str_one_non_zero_decimal(sum_start1850_iso)
        #number3 = hpf.num_to_str_one_non_zero_decimal(sum_start1990_iso)
        txt += \
            ("\n However, when " if abs(sum_start1990_share_iso - sum_start1850_share_iso) > 5 else "\n When ") + \
            f"only accounting for the years {yr_sum_start1990}--{yr_his}, with {number1}\% its contribution " + \
            ("stays the same" if number1 == number 
             else (
            ("is higher" if abs(float(number1) - float(number)) < 5 else "is notably higher")
            if float(number1) > float(number) else 
            ("is lower" if abs(float(number1) - float(number)) < 5 else "is notably lower")
            )) + '.'
            # " ({yr_sum_start1850} to {yr_his}: " + \
            # f"{number2}~{units_iso['emi']['label']}, and {yr_sum_start1990} to {yr_his}: " + \
            # f"{number3}~{units_iso['emi']['label']})."
        
        txt += \
            f"\n All of the emissions are presented following GWP~{meta.gwps.default}" + \
            ", and exclude emissions from LULUCF (exclLU)," + \
            " and bunkers fuels emissions (exclBunkers)." + \
            "\nFor further information on, i.a., the data sources and SSPs, please refer to Sect.~\\ref{sec:dataSourcesRefs}."
        ##
        path_to_figure1 = Path(path_to_tex_files, f'emi_share_map_2017.png')
        path_to_figure2 = Path(path_to_tex_files, f'emi_share_map_diff_2030_dmssp2_minus_2017.png')
        caption = \
            "(left panel) national contributions to global 2017' emissions " + \
            "(exclLU and exclBunkers, based on PRIMAP-hist), and " + \
            "(right panel) change in their share in 2030 (dmSSP2)" + \
            "\n The values in brackets indicate the number of countries with a certain share or change in share."
        txt += include_graphics2(path_to_figure1, path_to_figure2, caption, "fig:tsEmiMap", ".49\\textwidth", ".49\\textwidth")
        
        # Table {tab:overview}.
        
        # %%
        
        label = "tab:overview"
        columns = "l || l r l r r"
        hlines = [2, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
        caption = \
            f"National emissions, GDP and population for {ctr_the_lc}, " + \
            "together with the emissions per unit of GDP " + \
            f"and per capita emissions (for 1990, {yr_his} and {yr_fut}). " + \
            "\n Additionally, the global share and its rank are displayed." + \
            f"\n The {yr_fut} estimates are based on dm{ssp2_short}."
        table_body = pd.DataFrame(index=range(len(hlines)), columns=range(6))
        table_body.loc[0, :] = [f"\\bfseries {xx}" for xx in overview_table_str.columns.to_list()]
        table_body.loc[1:, :] = overview_table_str.values
        table_body.loc[1:, 0] = [f"\\bfseries {xx}" for xx in table_body.loc[1:, 0].to_list()]
        table_body[table_body.isin(['nan', 'nan\%'])] = '--'
        txt += df_to_table(table_body, caption, label, columns, hlines)
        ##
        txt += \
            f"\n\n For {ctr_the_lc}, in {yr_his} the main emissions share on sectoral level " + \
            "(Fig.~\\ref{fig:tsEmi}) was emitted in " + \
            f"the {highest_sec_his_1st} sector ({highest_sec_his_share_1st}\%)" + \
            (f", followed by {highest_sec_his_2nd} ({highest_sec_his_share_2nd}\%)"
             if f"{highest_sec_his_share_2nd}" != "nan" else 
             (f", and {highest_sec_his_3rd} ({highest_sec_his_share_3rd}\%)"
              if f"{highest_sec_his_share_3rd}" != "nan" else "")) + "."
            
        ##
        txt += \
            f"\n The Kyoto~GHG" + \
            f" with the highest share in {yr_his} was " + \
            f"{highest_gas_his_1st}, constituting " + \
            ("as much as " if float(highest_gas_his_share_1st) > 70 else " ") + \
            f"{highest_gas_his_share_1st}\% of the national emissions. "
        ##
        if f"{highest_gas_his_share_2nd}" != "nan":
            txt += \
                (f"\n Second largest contributor was {highest_gas_his_2nd} ({highest_gas_his_share_2nd}\%)"
                 if f"{highest_gas_his_share_2nd}" != "nan" else 
                 (f", followed by {highest_gas_his_3rd} ({highest_gas_his_share_3rd}\%)"
                  if f"{highest_gas_his_share_3rd}" != "nan" else "")) + "."
        
        ##
        txt += \
            "\n The total of F-gases " + \
            ("only " if float(share_fgases_his) < 7 else "") + f"represented {share_fgases_his}\%."
        
        # TODO: If CO2 is the highest share, don't repeat the pc share.
        
        # TODO: Something about NDC and target.
        
        txt += txt_emi_trend
        
        # Share of CO2 in 2030 (SSP2).
        try:
            number = hpf.num_to_str_one_non_zero_decimal(
                100. * getattr(tables, 'SSP2_CO2').data.loc[iso3, yr_fut] /
                    getattr(tables, 'SSP2_emi').data.loc[iso3, yr_fut])
            txt += \
                f"\n In {yr_fut} (dmSSP2), CO$_2$ emissions are expected to represent {number}\% " + \
                f"of the national Kyoto~GHG emissions."
        except:
            pass
        
        # Check if the ratios per gas are constant in the future and if they are the same for the different SSPs:
        # They are not constant and are not the same for the SSPs.
        
        # Historical emissions.
        path_to_figure = Path(path_to_tex_files, f'ts_emi_exclLU_{iso3}.png')
        caption = \
            "Timeseries of national emissions per main-sector (a) and Kyoto~GHG (b). " + \
            f"\nBased on PRIMAP-hist and dmSSPs (both exclLU and exclBunkers)." + \
            f"\nFrom the dmSSPs, no information is available on the sectoral contributions after {yr_his}." + \
            "\nIn (a) dmSSP1--5 is included, and in (b) the emissions follow dmSSP2."
        txt += include_graphics(path_to_figure, caption, "fig:tsEmi", "\\textwidth")
        
        # path_to_figure = Path(path_to_tex_files, 
        #     f'emi_ts_normalised_per_sec_and_subsec_and_per_gas_{iso3}.png')
        # caption = \
        #     "'Stacked' timeseries of national emissions (exclLU) per main- and subsector (a) and Kyoto~GHG (b). " +\
        #     "Based on PRIMAP-hist."
        # txt += include_graphics(path_to_figure, caption, "fig:tsEmiNorm", "\\textwidth")
        
        gdp_linreg_nan = np.isnan(gdp_linreg.slope)
        pop_linreg_nan = np.isnan(pop_linreg.slope)
            
        if not (gdp_linreg_nan and pop_linreg_nan):
            path_to_figure = Path(path_to_tex_files, f'ts_gdp_pop_{iso3}.png')
            caption = \
                "Timeseries of national GDP (a) and population (c), " + \
                "and Kyoto~GHG emissions per unit of GDP (b) and per capita (d), with Kyoto~GHG exclLU and exclBunkers." + \
                "\nBlack lines in (b) and (d) indicate the Energy CO$_2$ emissions per unit of GDP or per capita."
            txt += include_graphics(path_to_figure, caption, "fig:tsSocioEco", "\\textwidth")
        
        # Historical data.
        gdp_trend = ('positive' if gdp_linreg.slope > 0. else 'negative')
        emi_gdp_trend = ('positive' if emi_gdp_linreg.slope > 0. else 'negative')
        pop_trend = ('positive' if pop_linreg.slope > 0. else 'negative')
        emi_pop_trend = ('positive' if emi_pop_linreg.slope > 0. else 'negative')
        if not gdp_linreg_nan:
            txt += \
                f"\n\n The national GDP " + \
                ('increased ' if gdp_trend == 'positive' else 'decreased ') + "in recent years, " + \
                ("and the emissions per unit of GDP had a similar trend " if emi_gdp_trend == 'positive' else 
                 "but the emissions per unit of GDP had an opposite trend ") + \
                "(Fig.~\\ref{fig:tsSocioEco})."
        if not pop_linreg_nan:
            txt += \
                "\n The population " + \
                ("increased, " if pop_trend == 'positive' else "decreased, ") + \
                ("and " if (pop_trend == 'positive' and emi_pop_trend == 'positive') else "while ") + \
                "the per capita emissions " + ("were on the rise" if emi_gdp_linreg.slope > 0 else "dropped on average") + "."
        
        # Future data.
        # EMI per GDP: de-coupled?
        yrs_fut = range(2017, 2051)
        yrs_fut_str = [str(xx) for xx in yrs_fut]
        if not tables_iso.SSP2_gdp.data.loc[iso3, yrs_fut].isnull().all():
            yr_of_max = tables_iso.SSP2_gdp.data.loc[iso3, yrs_fut].idxmax()
            txt += f"\nFollowing dm{ssp2_short}, the GDP is projected to "
            txt += \
                (f"increase after {yrs_fut_str[0]} but to drop again before {yrs_fut_str[-1]}" 
                if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
                (f"increase towards {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[-1] else "") + \
                (f"drop" if yr_of_max == yrs_fut[0] else "")
            yr_of_max = tables_iso.SSP2_emi_gdp.data.loc[iso3, yrs_fut].idxmax()
            txt += \
                ", and the emissions per GDP are estimated to " + \
                (f"rise after {yrs_fut_str[0]} but to decrease again before {yrs_fut_str[-1]}" 
                if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
                (f"rise towards {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[-1] else "") + \
                (f"decrease" if yr_of_max == yrs_fut[0] else "") + "."
            
            no_gdp_data = False
        
        else:
            no_gdp_data = True
        
        if not tables_iso.SSP2_pop.data.loc[iso3, yrs_fut].isnull().all():
            yr_of_max = tables_iso.SSP2_pop.data.loc[iso3, yrs_fut].idxmax()
            txt += \
                f"\n{ctr_the_uc}'s population is assumed to " + \
                (f"grow after {yrs_fut_str[0]} but to diminish again before {yrs_fut_str[-1]}" 
                if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
                (f"grow towards {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[-1] else "") + \
                (f"diminish towars {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[0] else "")
            yr_of_max = tables_iso.SSP2_emi_pop.data.loc[iso3, yrs_fut].idxmax()
            txt += \
                ", and the per capita emissions are expected to " + \
                (f"increase after {yrs_fut_str[0]} but to decline again before {yrs_fut_str[-1]}" 
                if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
                (f"increase towards {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[-1] else "") + \
                (f"decline towars {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[0] else "") + "."
            
            no_pop_data = False
        
        else:
            no_pop_data = True
        
        if (no_gdp_data and no_pop_data):
            txt += f"\n For {ctr_the_lc}, no GDP and population data are available from dmSSPs."
        elif no_gdp_data:
            txt += f"\n For {ctr_the_lc}, no GDP data are available from dmSSPs."
        elif no_pop_data:
            txt += f"\n For {ctr_the_lc}, no population data are available from dmSSPs."
        
        # TODO! txt += "\\textbf{\n \\newline Instead of the Energy CO2, include the highest 3 sector plus gas combis and the 'rest' as shaded stacked areas.}"
        # TODO: Maybe include some 'nice' words.
        
        # %% LULUCF emissions
        lu_srces = []
        for lu_srce in meta.lulucf.source_prioritisation:
            lu_data = getattr(tables_iso, f"LULUCF_{lu_srce}").data.loc[iso3, :]. \
                reindex(index=range(1990, yr_his+1))
            lu_srces_data = int(sum([1 for xx in lu_data if not np.isnan(xx)]))
            if lu_srces_data > 0:
                lu_srces += [f"{meta.sources.srce_to_label[lu_srce]}"]
        
        if len(lu_srces) > 0:
            if len(lu_srces) == 1:
                lu_srces = lu_srces[0]
            elif len(lu_srces) == 2:
                lu_srces = f"{lu_srces[0]}, and {lu_srces[1]}"
            else:
                lu_srces = ", ".join(lu_srces[:-1]) + f", and {lu_srces[-1]}"
            
            lu_chosen = tables_iso.LULUCF_CHOSEN.data.loc[iso3, range(1990, yr_his+1)]
            lu_chosen_srce = meta.sources.srce_to_label[info_lulucf_chosen.loc[iso3]]
            emi_onlyLU_yrHis = lu_chosen[yr_his]
            emi_onlyLU_yrHis_str = hpf.num_to_str_one_non_zero_decimal(emi_onlyLU_yrHis)
            emi_exclLU_yrHis = tables_iso.KYOTOGHG_IPCM0EL.data.loc[iso3, yr_his]
            emi_exclLU_yrHis_str = hpf.num_to_str_one_non_zero_decimal(emi_exclLU_yrHis)
            ratio_lu = 100.*emi_onlyLU_yrHis/emi_exclLU_yrHis
            emi_onlyLU_min = lu_chosen.min()
            emi_onlyLU_min_str = hpf.num_to_str_one_non_zero_decimal(emi_onlyLU_min)
            emi_onlyLU_max = lu_chosen.max()
            emi_onlyLU_max_str = hpf.num_to_str_one_non_zero_decimal(emi_onlyLU_max)
            emi_onlyLU_mean = lu_chosen.mean()
            txt += \
                f"\n\n LULUCF emissions data for {ctr_the_lc} are available from the following sources " + \
                "(Fig.~\\ref{fig:tsLULUCF}): " f"{lu_srces}, with the number of available data points in " + \
                f"1990--{yr_his} displayed in the legend." + \
                "\n LULUCF can be a net sink and remove GHGs from the atmosphere, or it is a net source and emits more " + \
                "GHGs than it can remove." + \
                "\n LULUCF emissions can have strong inter-annual fluctuations and uncertainties in emissions estimates are relatively high, " + \
                "which can lead to relatively large differences between data sources for LULUCF emissions." + \
                f"\n The " + ("relatively large "
                 if ((not np.isnan(emi_onlyLU_mean) and emi_onlyLU_mean != 0.) 
                     and (emi_onlyLU_min/emi_onlyLU_mean < .5 or emi_onlyLU_max/emi_onlyLU_mean > 1.5))
                 else "") + f"emissions range for {lu_chosen_srce} data over the period 1990--{yr_his} is " + \
                f"{emi_onlyLU_min_str}--{emi_onlyLU_max_str}~{units_iso['emi']['label']}, and " + \
                f"for the year {yr_his}, LULUCF is estimated to be a net " + \
                ("sink" if emi_onlyLU_yrHis < 0. else "source") + \
                " of \\mbox{" f"{emi_onlyLU_yrHis_str}~{units_iso['emi']['label']}" "}, which in absolute terms is " + \
                ("in the range of" if 90 < ratio_lu < 110 else 
                (("significantly higher than" if ratio_lu > 140 else "higher than")
                if ratio_lu > 110 else 
                ("significantly lower than" if ratio_lu < 60 else "lower than"))) + \
                f" the non-LULUCF emissions of {emi_exclLU_yrHis_str}~{units_iso['emi']['label']}."
                
                # High fluctuations?
                # Difference between sources?
            
            path_to_figure = Path(path_to_tex_files, f'ts_emi_onlyLU_{iso3}.png')
            caption = \
                "Timeseries of emissions from LULUCF (CO$_2$ plus CH$_4$ and N$_2$O) " + \
                "as available from different data-sources. " + \
                "\nThe values in the legend show the number of available data points for 1990--2017." + \
                f"\nIndicated in pink are the prioritised data, as used in our assessment of the country's NDC (if needed). " + \
                "\nThe pink timeseries was inter- and~/ or extrapolated (interpolation: linear, extrapolation: constant)."
            txt += include_graphics(path_to_figure, caption, "fig:tsLULUCF", "\\textwidth")
        
        else:
            lu_srces_all = ", ".join([meta.sources.srce_to_label[xx] for xx in meta.lulucf.source_prioritisation])
            txt += \
                f"\n No LULUCF data are available for {ctr_the_lc} from the following sources: {lu_srces_all}."
        
        # TODO: Only plot it for historical years, as it is kept constant afterwards there is nothing to see.
        # TODO: FAO2019 does not have circles but only a line, as the KYOTOGHG is the sum over CO2, CH4 and N2O ...
        
        # %% Mitigation targets
        txt += \
            "\n\n \\section{Mitigation targets}" + \
            "\n \\label{sec:mitiTars}"
        
        # TODO !:
        #txt += \
        #    "\n\n \\textbf{ " + \
        #    "\n Give the \%cov for the base and target year (and 2017). \\newline" + \
        #    "\n Global share for 2030 for the mitigated pathways and \% reduction relative to 1990 and 2017. \\newline" + \
        #    "\n Table with the 'input' data and the resulting targets (like ndcs\_targets.csv, for SSP2 only?). \\newline" + \
        #    "}"
        
        # %%
        if iso3 == 'USA':
            txt += \
                "Even though the USA has submitted an NDC to the UNFCCC, " + \
                "due to the withdrawal from the Paris Agreement, " + \
                "the USA is no longer considered as country with NDC when aggregating the pathways of mitigated emissions to global level." + \
                "\n In this case, the USA's baseline trajectories are used instead of mitigated pathways." + \
                "\n However, with Joe Biden being the president-elect, chances are high that the USA will rejoin the Paris Agreement." +\
                "\n The information given in the following is based on the USA's former NDC.\n"
        
        if has_ndc not in ['NDC', 'INDC']:
            txt += \
                f"\n {ctr_the_uc} does not have an (I)NDC." + \
                "\n Therefore the assumed 'mitigated' emissions pathways used for global aggregates equal " +\
                "the baseline emissions (dmSSP1--5)."
        
        else:
            
            plot_ts_pc_cov()
            tars_ssp1_to_4, tars_ssp1_to_5 = plot_ndcs()
            tars_excl_or_incl_USA = 'exclUSA'
            tars_ssp1_to_4_earth_exclUSA, tars_ssp1_to_5_earth_exclUSA = plot_ndcs_earth()
            tars_excl_or_incl_USA = 'inclUSA'
            tars_ssp1_to_4_earth_inclUSA, tars_ssp1_to_5_earth_inclUSA = plot_ndcs_earth()
            
            # %%
            txt += \
                f"\n {ctr_the_uc} has an {has_ndc}, with a GHG mitigation target that we classify as " + \
                f"{type_main} ({tar_to_long[type_main]}) as the main target type."
            if type_main != type_reclass:
                txt += \
                    f"\n The reclassified target type is {type_reclass} ({tar_to_long[type_reclass]})." + \
                    f"\n We reclassify a country's target when it has, e.g., an RBY or RBU target ({tar_to_long['RBY']} or {tar_to_long['RBU']}), " + \
                    "and the base year or BAU emissions are provided in its NDC." + \
                    "\n In this case it can be quantified based on the given emissions, and is reclassified from type\_main RBY or RBU to " + \
                    f"type\_reclass~ABS ({tar_to_long['ABS']})." + \
                    f"\n In a similar approach, 'NGT' targets ({tar_to_long['NGT']}) can be reclassified as 'ABU' ({tar_to_long['ABU']}) if the " + \
                    "absolute mitigation effects due to planned policies and measures are provided." + \
                    "\n Our intention is to consider the baseline emissions or target values provided in a country's NDC to quantify its target, if possible. " + \
                    "\n However, in case of missing data, for comparison purposes and to address uncertainties in NDC mitigation targets, " + \
                    "we also quantify the target based on 'external' emissions data (PRIMAP-hist, dmSSPs), when type\_main is not ABS." + \
                    "\n External emissions time series are further used to create trajectories of mitigated emissions, as the data provided in NDCs are generally point values only."
            
            cols = ['type', 'condi', 'rge', 'val', 'refYr', 'tarYr', 'peakYr', 'intRef', 'LU']
            tars_df = pd.DataFrame(columns=cols)
            tars_df.loc[0, :] = ['type',  'condi.', 'range', 'value', 'refYr', 'tarYr', 'peakYr', 'intensRef', 'LU']
            count = 1
            types = ([type_main, type_reclass] if type_main != type_reclass else [type_main])
            types = [xx for xx in types if xx != 'NGT']
            last_tarYr = 0
            condi_of_tars = []
            for tar_tpe in types:
                if tar_tpe in ndc_iso3.index:
                    tars_json = json.loads(ndc_iso3[tar_tpe])
                    for lu in tars_json[tar_tpe].keys():
                        for condi in ['unconditional', 'conditional']:
                            for rge in ['worst', 'best']:
                                try:
                                    for yr in sorted(tars_json[tar_tpe][lu][condi][rge].keys()):
                                        tars_df.loc[count, 'type'] = tar_tpe
                                        condi_of_tars += [condi]
                                        tars_df.loc[count, 'condi'] = condi.replace('tional', '.')
                                        tars_df.loc[count, 'rge'] = rge
                                        tars_df.loc[count, 'tarYr'] = yr
                                        last_tarYr = max([last_tarYr, int(yr)])
                                        tars_df.loc[count, 'LU'] = lu
                                        val = tars_json[tar_tpe][lu][condi][rge][yr]. \
                                            replace('_', ' ').replace('%', '\%'). \
                                            replace('MtCO2', 'Mt~CO$_2$').replace('tCO2', 't~CO$_2$')
                                        # Delete decimals if necessary.
                                        point = [xx for xx in range(len(val)) if val[xx] == '.']
                                        if (len(point) > 0 and '%' not in val):
                                            space = [xx for xx in range(len(val)) if val[xx] == ' ']
                                            if len(space) > 0:
                                                val_nr = val[:space[0]]
                                                unit = val[space[0]:]
                                                val = hpf.num_to_str_one_non_zero_decimal(
                                                    float(val_nr), nr_non_zero=2) + unit
                                        
                                        tars_df.loc[count, 'val'] = val
                                        count += 1
                                except:
                                    pass
            
            if len(tars_df.index) > 1:
                tars_df.loc[1:, 'refYr'] = f"{ndc_iso3['BASEYEAR'] :.0f}"
                tars_df.loc[1:, 'peakYr'] = f"{ndc_iso3['DECLINE_AFTER_YEAR'] :.0f}"
                tars_df.loc[1:, 'intRef'] = ndc_iso3['INTENSITY_PERCAP_GDP']
                tars_df[tars_df == 'nan'] = ''
                tars_df[tars_df.isnull()] = ''
                for col in tars_df.columns:
                    if (tars_df.loc[1:, col] == '').values.all():
                        tars_df.drop(columns=[col], inplace=True)
                
                tars_df.loc[0, :] = [f"\\bfseries {xx}" for xx in tars_df.loc[0, :]]
                
                tars_df.loc[1:, :] = tars_df.loc[1:, :].sort_values(
                    ['type', 'LU', 'tarYr']).values
                
                caption = \
                    f"Information on {ctr_the_lc}'s GHG mitigation target(s)." + \
                    "\n condi.: conditionality (conditional: dependent on, e.g., international finance);" + \
                    "\n range: if a target range is given rather than a fixed value (e.g., unconditional reduction by 26\% (best) to 28\% (worst));" + \
                    "\n value: target value provided within the NDC;" + \
                    "\n refYr: reference year (e.g., for RBY targets this is the base year, for RBU targets it is the target year);" + \
                    "\n tarYr: target year;" +\
                    "\n LU: inclLU if the target includes LULUCF, else exclLU."
                if len(types) == 1:
                    hlines = [2] + [0] * (len(tars_df.index)-1)
                else:
                    hlines = [2] + [0] * (len(tars_df.type[tars_df.type == type_main]) - 1) + [1] + \
                        [0] * (len(tars_df.type[tars_df.type == type_reclass]))
                
                txt += df_to_table(tars_df, caption, "tab:mitiTars", 
                    "".join(["l "] * len(tars_df.columns)), hlines) #, fontsize="\\small"
            
            else:
                txt += \
                    f"\n As the target has been assessed to be NGT, the assumed 'mitigated' " + \
                    "emissions pathways used for global aggregates equal our baseline assumptions (dmSSP1--5)."
            
            # %%
            # TODO
            
            #txt += f"\n\n{ctr_the_uc} has a " + infos_from_ndcs
            #tar_to_long
            
            # %%
            # Covered share of emissions.
            
            # TODO
#            txt += \
#                "\n\n \\textbf{Put in the covered sectors / gases in the text as well! And some information like: " + \
#                "some NDCs only cover parts of the national GHGs and this is taken into account during the quantification. " + \
#                "Also write that the information if LULUCF is included is taken into account.}"
            
            # %%
            # Table with covered sectors and gases.
            
            cats = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5']
            table_combis = pd.DataFrame(index=['NDCs', 'Adap.'] + cats,
                columns=['NDCs', 'Adap.'] + meta.gases.kyotoghg)
            
            for case in [xx for xx in cov_used.columns if '_' in xx]:
                if 'LULUCF' not in case:
                    
                    ent, cat = case.split('_')
                    table_combis.loc[cat, ent] = cov_used.loc[iso3, case]
            
            table_combis.loc[cats, 'NDCs'] = \
                cov_ndcs.loc[iso3, cats].values
            table_combis.loc[cats, 'Adap.'] = \
                cov_used.loc[iso3, cats].values
            table_combis.loc['NDCs', meta.gases.kyotoghg] = \
                cov_ndcs.loc[iso3, :].reindex(index=list(meta.gases.kyotoghg)).values
            table_combis.loc['Adap.', meta.gases.kyotoghg] = \
                cov_used.loc[iso3, :].reindex(index=list(meta.gases.kyotoghg)).values
            
            # Add the information on emissions per sector / gas / combi, and print the covered ones as bold.
            # Print the emissions and the share in national emissions (exclLU).
            
            table_combis_emis = pd.DataFrame(index=cats + ['Total'], columns=meta.gases.kyotoghg + ['Total'])
            table_combis_emis.loc['Total', 'Total'] = getattr(tables_iso, 'KYOTOGHG_IPCM0EL').data.loc[iso3, yr_his]
            
            for cat in cats:
                # Total emissions.
                table_combis_emis.loc[cat, 'Total'] = getattr(tables_iso, f'KYOTOGHG_{cat}').data.loc[iso3, yr_his]
                for gas in meta.gases.main:
                    # Per gas-sector combi.
                    table_combis_emis.loc[cat, gas] = getattr(tables_iso, f'{gas}_{cat}').data.loc[iso3, yr_his]
            
            for gas in meta.gases.fgases:
                table_combis_emis.loc['IPC2', gas] = getattr(tables_iso, f'{gas}_IPCM0EL').data.loc[iso3, yr_his]
            
            for gas in meta.gases.kyotoghg:
                table_combis_emis.loc['Total', gas] = getattr(tables_iso, f'{gas}_IPCM0EL').data.loc[iso3, yr_his]
            
            table_combis_shares = 100. * table_combis_emis / table_combis_emis.loc['Total', 'Total']
            
            # Put data together.
            table_combis_str = table_combis.loc[['NDCs', 'Adap.'], :]
            for row in table_combis_emis.index:
                
                if row != 'Total':
                    table_combis_str.loc[row, 'NDCs'] = table_combis.loc[row, 'NDCs']
                    table_combis_str.loc[row, 'Adap.'] = table_combis.loc[row, 'Adap.']
                
                for col in table_combis_emis.columns:
                    
                    fontweight = ''
                    if (row != 'Total' and col != 'Total'):                
                        if table_combis.loc[row, col] == '+':
                            fontweight = '\\bfseries '
                    
                    share = hpf.num_to_str_one_non_zero_decimal(table_combis_shares.loc[row, col], maximal=2)
                    table_combis_str.loc[row, col] = f"{fontweight}{share}"
            
            table_combis_str[table_combis_str == '\\bfseries nan'] = '\\bfseries /'
            table_combis_str[table_combis_str == 'nan'] = '/'
            
            table_combis_str[table_combis_str == '+'] = '\\bfseries +'
            
            table_combis_str[table_combis_str.isnull()] = ''
            table_combis_str.index = [sec_to_label[meta.categories.main.cat_to_sec[xx]] 
                if xx in meta.categories.main.cat_to_sec.keys() else xx
                for xx in table_combis_str.index]
            table_combis_str.insert(0, '', table_combis_str.index.values)
            table_combis_str.columns = table_combis_str.columns.to_list()[:3] + \
                [meta.gases.gas_to_label[xx] for xx in table_combis_str.columns.to_list()[3:-1]] + ['Total']
            
            # %%
            cov_secs = [meta.categories.main.cat_to_label[xx] for xx in secs_check if table_combis.loc[xx, 'Adap.'] == '+']
            txt += \
                "\n For a better understanding of the part of national emissions targeted by the mitigation pledges, " + \
                "we assessed the covered share of emissions, which is also taken into account during the target quantifications." + \
                "\n The assessment results are shown in Table~\\ref{tab:coveredSectorsGases}." + \
                f"\n Based on the information in the NDC, in the case of {ctr_the_lc}, the main sectors that we assessed to be considered are " + \
                f"{hpf.join_list_but_last_element_different(cov_secs)} (column 'Adap.')."
            if len(cov_secs) == len(secs_check):
                all_secs_cov = True
                txt += \
                    "\n As all main economic sectors are covered, we additionally assume potential emissions in the sector 'Other' to be covered."
            else:
                all_secs_cov = False
            cov_gases = [meta.gases.gas_to_label[xx] for xx in gases_check if table_combis.loc['Adap.', xx] == '+']
            if len(cov_gases) == len(gases_check):
                all_gases_cov = True
                cov_gases = f"all of the gases ({hpf.join_list_but_last_element_different(cov_gases)})"
            else:
                all_gases_cov = False
                cov_gases = hpf.join_list_but_last_element_different(cov_gases)
            txt += \
                f"\n Regarding the Kyoto~GHGs, {cov_gases} are assessed to be covered (row 'Adap.')."
            
            if iso3 in isos_annexi and all_secs_cov and all_gases_cov:
                txt += \
                    "\n This results in a complete coverage of national emissions, " + \
                    "as in line with the request for developed countries to present economy-wide pledges."
            if iso3 in isos_annexi and not (all_secs_cov and all_gases_cov):
                txt += \
                    "\n This results in a less than complete coverage of national emissions, " + \
                    "not in line with the request for developed countries to present economy-wide pledges."
            if iso3 in isos_nonannexi and all_secs_cov and all_gases_cov:
                txt += \
                    "\n This results in a complete coverage of national emissions, " + \
                    "as in line with the PA aim for countries to present economy-wide pledges."
            if iso3 in isos_nonannexi and not (all_secs_cov and all_gases_cov):
                txt += \
                    "\n This results in a less than complete coverage of national emissions, " + \
                    "and in line with the PA aim for countries to present economy-wide pledges, " + \
                    f"eventually {ctr_the_lc} should move towards full coverage."
            
            # Tables with coverage.
            label = "tab:coveredSectorsGases"
            emi_iso3_exclLU = hpf.num_to_str_one_non_zero_decimal(
                table_combis_emis.loc['Total', 'Total'])
            emi_iso3_onlyLU = hpf.num_to_str_one_non_zero_decimal(
                tables_iso.LULUCF_CHOSEN.data.loc[iso3, yr_his])
            caption = \
                f"Information on covered sectors and gases as retrieved from the {has_ndc} and adapted " + \
                f"('Adap.': used to calculate \%cov), and their shares in {ctr_the_lc}'s {yr_his} emissions " + \
                f"(all shares in \% in comparison to total Kyoto~GHG emissions of {emi_iso3_exclLU}~{units_iso['emi']['label']}; exclLU, exclBunkers)." + \
                "\n If either the sector or gas is assessed as 'not-covered', the emissions from this " + \
                "sector-gas combination are counted as not-covered (indicated by '--'). " + \
                "\n Else the emissions are counted as covered ('+'; covered shares given in bold)." + \
                "\n '/' means that no information is available." + \
                "\n The F-gases (HFCs, PFCs, SF$_6$, and NF$_3$ are only relevant in the IPPU sector." + \
                f"\n For LULUCF the coverage is assessed as: {has_ndc} '{cov_ndcs.loc[iso3, 'IPCMLULUCF']}' and " + \
                f"adapted '{cov_used.loc[iso3, 'IPCMLULUCF']}' " + \
                "(based on the prioritised LULUCF data source, see Fig.~\\ref{fig:tsLULUCF}, LULUCF is estimated as a " + \
                ("net sink" if float(emi_iso3_onlyLU) < 0. else "net source") + \
                f" of {emi_iso3_onlyLU}~{units_iso['emi']['label']} in {yr_his})."
            columns = "l || c c || c c c c c c c | c"
            hlines = [2, 0, 2, 0, 0, 0, 0, 1, 0]
            table_body = pd.DataFrame(index=range(len(hlines)), columns=range(11))
            table_body.loc[0, :] = [f"\\bfseries {xx}" for xx in table_combis_str.columns.to_list()]
            table_body.loc[1:, :] = table_combis_str.values
            table_body.loc[1:, 0] = [f"\\bfseries {xx}" for xx in table_body.loc[1:, 0].to_list()]
            table_body.loc[:, 0] = [xx.replace('Agriculture', 'Agri.') if 'Agriculture' in xx else xx
                                     for xx in table_body.loc[:, 0]]
            txt += df_to_table(table_body, caption, label, columns, hlines, fontsize='\\small')
            
            # TODO: Rules for pccov.
            # TODO: Only include the coverage stuff if it has an (I)NDC.
            txt += \
                (f"\n\n As {ctr_the_lc} is part of the NDC by the European Union (27), " + \
                 "the coverage of the EU27 NDC is used." if (iso3 in meta.isos.EU28 and iso3 != 'GBR') else "")
            
#            TODO: only include the figure if it makes sense.
#            path_to_figure = Path(path_to_tex_files, f'ts_pc_cov_{iso3}.png')
#            caption = \
#                f"(a) timeseries of {ctr_the_lc}'s share of national emissions that is assumed to be covered by the NDC (exclLU)." + \
#                "\n (b) correlation between the national and covered part of emissions."
#            txt += include_graphics(path_to_figure, caption, "fig:tsPcCov", "\\textwidth")
            
            # TODO: in brackets include the share of total emissions that combi stands for (2017).
            # TODO: Table with emissions per main-sector and per gas, and per combi?
            
            txt += \
                f"We quantified {ctr_the_lc}'s mitigation targets based on several options " + \
                "as displayed in " "Figure~\\ref{fig:miti}. " + \
                "\n This reflects to some degree the uncertainty range in the target quantifications."
            if min(tars_ssp1_to_5) > 0.1:
                nr_digits = 1
            elif min(tars_ssp1_to_5) > 0.01:
                nr_digits = 2
            else:
                nr_digits = 3
            txt += \
                f"\n The historical baseline data from PRIMAP-hist~v2.1 end with the year {meta.primap.last_year}, " + \
                "while the mitigated pathways are calculated in line with the start of the Paris Agreement period " + \
                "(2021, after the end of the Kyoto Protocol period in 2020), " + \
                "which can be seen in the baseline emissions and mitigated dmSSP2 pathways " + \
                "presented in " "Figure~\\ref{fig:miti}." + \
                f"\n The target was assessed to be {type_main} as main type, "
            if type_main in tars_nonABS and type_reclass == 'ABS':
                print("Check this country for: are the prio NDC and prio SSP values different? With influence of the SSPs?")
                txt += \
                    "however, emissions were provided in the NDC, " + \
                    f"which is why the reclassified target type is {type_reclass}. " + \
                    "\n The quantified targets shown for 'prio NDC' (type\_reclass) " + \
                    f"were quantified based on the emissions provided in {ctr_the_lc}'s NDC, " + \
                    "while for 'prio SSPs' the external data were used (dmSSP baseline emissions). "
            if type_main in tars_nonABS and type_reclass != 'ABS':
                print("Check this country for: are the prio NDC and prio SSP values the same? With influence of SSPs?")
                txt += \
                    "and no sufficient baseline emissions were provided in the NDC to quantify the target, " + \
                    "which is why the reclassified target type is " + \
                    ("also " if type_main == type_reclass else "") + f"{type_reclass}. " + \
                    "\n Therefore, the quantified targets shown for 'prio NDC' (type\_reclass) " + \
                    f"were not quantified based on emissions from {ctr_the_lc}'s NDC, " + \
                    "but as for 'prio SSPs' the external data had to be used (dmSSP baseline emissions). "
            if type_main == 'ABS':
                print("Check this country for: are the prio NDC and prio SSP values the same? And no influence of SSPs?")
                if type_reclass != 'ABS':
                    print("Why is the type_main ABS, but not the type_reclass?!")
                txt += \
                    "which is why the reclassified target type is also ABS. " + \
                    "\n Therefore, the quantified targets shown for 'prio NDC' (type\_reclass) " + \
                    "and 'prio SSPs' (using the external data, dmSSP baseline emissions) are the same."
            
            txt += "\n"
            if last_tarYr < 2030:
                print("Check this country for: last target year < 2030.")
                txt += \
                    f"\n {ctr_the_uc}'s target year is {last_tarYr}, but the mitigated emissions " + \
                    "shown in Figure~\\ref{fig:miti} are presented for 2030 " + \
                    "to ease comparisons with other countries."
                if type_main == 'RBY':
                    txt += \
                        "\n Even though the quantification basis for 'prio NDC' is " + \
                        "the same base year value for all shown results, " + \
                        "values for 2030 differ depending on the reference scenario (dmSSP)."
            txt += \
                "\n In the default setting of our quantifications, the mitigated pathway between the last target year and 2030 " + \
                "is assumed to follow the dmSSP baseline with a constant relative difference after the last target year." + \
                "\n The quantification option 'const. emissions' (second place in quadruples) is based on a different approach, " + \
                "where the emissions after the last target year are kept constant instead of following the baseline trajectory." + \
                "\n This means that after the target year no further mitigation action is assumed, " + \
                "neither do the emissions rebound towards higher levels after the last target year."
            if last_tarYr >= 2030:
                print("Check this country for: last target year >= 2030.")
                f"\n For {ctr_the_lc}, this quantification option shows no effect, as the last target year is not before 2030."
            # The following can be tricky, with the different SSPs.
            txt += '\n'
            if type_main != 'ABS':
                tar_data_check = pd.Series(index=['prio_NDCs', 'prio_SSPs'], dtype='float64')
                for prio in ['prio_NDCs', 'prio_SSPs']:
                    data_act = ndc_quantis_ptws[prio]['cov100']['SSP2']
                    tar_data_check[prio] = \
                        (data_act.loc[(data_act.iso3 == iso3) & (data_act.rge.isin(['best', 'worst'])), '2030']).max()
                txt += \
                    "\n When comparing the mitigation results for 'prio NDC' and 'prio SSPs' (year 2030, dmSSP2, 100\% coverage, default), " + \
                    "the mitigated emissions when prioritising the NDC's emissions "
                if tar_data_check['prio_NDCs'] > tar_data_check['prio_SSPs']:
                    print("Check this country for: prio_NDCs > prio_SSPs.")
                    txt += \
                        "are higher, which means that the provided emissions are higher than the external reference data (PRIMAP-hist, dmSSP2)."
                elif tar_data_check['prio_NDCs'] < tar_data_check['prio_SSPs']:
                    print("Check this country for: prio_NDCs < prio_SSPs.")
                    txt += \
                        "are lower, which means that the provided emissions are lower than the external reference data (PRIMAP-hist, dmSSP2)."
                elif tar_data_check['prio_NDCs'] == tar_data_check['prio_SSPs']:
                    print("Check this country for: prio_NDCs = prio_SSPs.")
                    txt += \
                        "are the same, which means that the data basis is the same as the external reference data (PRIMAP-hist, dmSSP2)."
            if all_secs_cov and all_gases_cov:
                txt += \
                    f"\n As we assessed {ctr_the_lc} to cover all sectors and gases, " + \
                    "the mitigated targets for an assumed coverage of 100\% and for the estimated coverage are equal. "
            else:
                txt += \
                    f"\n As we did not assess {ctr_the_lc} to cover all sectors and gases, " + \
                    "the mitigated targets for an assumed coverage of 100\% and for the estimated coverage can differ. "
            txt += '\n'
            txt += \
                "\n Some countries provided targets that are unconditional, while others connected the " + \
                "implementation of their mitigation targets to a certain conditionality, such as international financial aid." + \
                "\n A third group of Parties chose to submit unconditional and conditional targets to the UNFCCC, " + \
                "in which case a more ambitious target is envisaged under certain conditions." + \
                "\n The default setting in our quantifications regarding the targets' conditionality is:" + \
                "\n (i) if no target is given use the baseline as un-/conditional pathway;" + \
                "\n (ii) if the country only has an unconditional target use it as unconditional and conditional pathway;" + \
                "\n (iii) if the country only has a conditional target use it as conditional pathway, while the baseline is used as unconditional pathway;" + \
                "\n and (iv) if the country has both an unconditional and conditional target, use it as the country's unconditional and conditional pathway, respectively." + \
                "\n The third quantification option we tested (per quadruple) is to use the baseline " + \
                "as unconditional pathway even if its emissions are lower than the conditional pathway."
            if 'unconditional' in condi_of_tars and 'conditional' not in condi_of_tars:
                print("Check this country for: uncondi but not condi.")
                txt += \
                    "\n This option does not have an effect in comparison to the default settings, " + \
                    f"as {ctr_the_lc}'s target is not conditional."
            elif 'unconditional' in condi_of_tars and 'conditional' in condi_of_tars:
                print("Check this country for: uncondi and condi.")
                txt += \
                    "\n This option does not have an effect in comparison to the default settings, " + \
                    f"as {ctr_the_lc}'s has unconditional and conditional targets."
            elif 'unconditional' not in condi_of_tars and 'conditional' in condi_of_tars:
                print("Check this country for: condi but not uncondi.")
                txt += \
                    "\n This option can have an effect in comparison to the default settings, " + \
                    f"as {ctr_the_lc}'s target is conditional."
            txt += '\n'
            # LULUCF: it is possible that the used LULUCF emissions are from the NDC.
            lu_check_NDCs = ndc_quantis_ptws['prio_NDCs']['cov100']['SSP2']
            lu_check_NDCs = lu_check_NDCs.loc[lu_check_NDCs.iso3 == iso3, '2030'].astype('float64')
            lu_check_NDCs_fao = ndc_quantis_ptws['prio_NDCs']['cov100_lulucf_fao']['SSP2']
            lu_check_NDCs_fao = lu_check_NDCs_fao.loc[lu_check_NDCs_fao.iso3 == iso3, '2030'].astype('float64')
            lu_check_NDCs_diff = lu_check_NDCs_fao.add(-lu_check_NDCs)
            lu_check_SSPs = ndc_quantis_ptws['prio_SSPs']['cov100']['SSP2']
            lu_check_SSPs = lu_check_SSPs.loc[lu_check_SSPs.iso3 == iso3, '2030'].astype('float64')
            lu_check_SSPs_fao = ndc_quantis_ptws['prio_SSPs']['cov100_lulucf_fao']['SSP2']
            lu_check_SSPs_fao = lu_check_SSPs_fao.loc[lu_check_SSPs_fao.iso3 == iso3, '2030'].astype('float64')
            lu_check_SSPs_diff = lu_check_SSPs_fao.add(-lu_check_SSPs)
            txt += \
                "\n The last quantification option we tested was a different prioritisation of LULUCF data sources " + \
                "(this does not have an effect if the NDC provided LULUCF emissions; " + \
                "see Fig.~\\ref{fig:tsLULUCF} for LULUCF emissions time series): " + \
                "instead of the default prioritisation (CRF, BUR, UNFCCC, FAO), " + \
                "FAO was prioritised as data source (FAO, CRF, BUR, UNFCCC)"
            if any(lu_check_NDCs_diff != 0) or any(lu_check_SSPs_diff != 0):
                txt += f", which shows an effect for {ctr_the_lc}."
            else:
                txt += "."
            txt += \
                "\n In total, the targets presented in " "Figure~\\ref{fig:miti}" + \
                f"range between {hpf.rnd(min(tars_ssp1_to_5), nr_digits)} and {hpf.rnd(max(tars_ssp1_to_5), nr_digits)}~Mt~CO$_2$eq " + \
                f"({hpf.rnd(min(tars_ssp1_to_4), nr_digits)} and {hpf.rnd(max(tars_ssp1_to_4), nr_digits)}~Mt~CO$_2$eq for dmSSP1--4)." + \
                "\n On global scale (Fig.~\\ref{fig:miti_earth}), the mitigated emissions pathways " + \
                f"range between {hpf.rnd(min(tars_ssp1_to_5_earth_exclUSA), 1)} and {hpf.rnd(max(tars_ssp1_to_5_earth_exclUSA), 1)}~Gt~CO$_2$eq " + \
                f"({hpf.rnd(min(tars_ssp1_to_4_earth_exclUSA), 1)} and {hpf.rnd(max(tars_ssp1_to_4_earth_exclUSA), 1)}~Gt~CO$_2$eq for dmSSP1--4)." + \
                "\n For these global estimates, for the USA, baseline emissions are assumed, as it withdrew from the Paris Agreement." + \
                "\n If including a contribution based on the USA's former NDC, the global aggregates are reduced to " + \
                f"range between {hpf.rnd(min(tars_ssp1_to_5_earth_inclUSA), 1)} and {hpf.rnd(max(tars_ssp1_to_5_earth_inclUSA), 1)}~Gt~CO$_2$eq " + \
                f"({hpf.rnd(min(tars_ssp1_to_4_earth_inclUSA), 1)} and {hpf.rnd(max(tars_ssp1_to_4_earth_inclUSA), 1)}~Gt~CO$_2$eq for dmSSP1--4)."
            txt += \
                "\n\n Bring the targets into global perspective..."
            # TODO: check if I can put something like that in:
            #    "\n For the USA, the largest effect per quadruple is observed when changing ..."
            # TODO: maybe put in a world map with the 2030 emissions, once dmSSP2 baseline, once with the targets (have to chose which ...)
            # TODO: or put in the global emissions plot from paper.
            
            # TODO: Emissions target. Table with assumptions. All target years, etc.
            # TODO: Targets: plots like in UBA.
            path_to_figure = Path(path_to_tex_files, f'ts_ndcs_quantis_{iso3}.png')
            caption = \
                "Quantified mitigation targets (based on different input data and calculation options)." + \
                "\n Vertical lines: conditionality~/ range;" + \
                "\n colour coded: dmSSP1--5;" + \
                "\n first~/ second set of eight: prio NDCs~/ SSPs;" + \
                "\n first~/ second set of four: assumed 100\% coverage vs. estimated coverage (based on sectors and gases assessed as covered); " + \
                "\n quadruples: default; " + \
                "constant emissions after last target year (default: constant relative difference to baseline); " + \
                "baseline emissions as unconditional pathway if the country has no unconditional target, " + \
                "even if the baseline is better than the conditional pathway (default: conditional pathway also used as unconditional pathway in that case); " + \
                "LULUCF prioritisation FAO, CRF, BUR, UNFCCC (default: CRF, BUR, UNFCCC, FAO)."
            txt += include_graphics(path_to_figure, caption, "fig:miti", "\\textwidth")
        
            path_to_figure1 = Path(path_to_tex_files, f'ts_ndcs_quantis_earth_exclUSA.png')
            path_to_figure2 = Path(path_to_tex_files, f'ts_ndcs_quantis_earth_inclUSA.png')
            caption = \
                "As Figure~\\ref{fig:miti}, but for globally aggregated mitigated emissions pathways " + \
                "(upper panel: excluding the former NDC by the USA, as it withdrew from the Paris Agreement; " + \
                "lower panel: including the USA's former NDC."
            txt += include_graphics2(path_to_figure1, path_to_figure2, caption, "fig:miti_earth", "\\textwidth", "\\textwidth")
            
            # TODO: change text if only ABS (e.g. ARG), or if NDC but no tar (e.g., ARE).
            # TODO: check ARM. Check CHN (reg. covered sectors/gases), IND.
        
        # %% Data sources and references
        txt += \
            "\n\n \\section{Data sources, additional information and references}" + \
            "\n \\label{sec:dataSourcesRefs}"
        
        primap_link = "https://dataservices.gfz-potsdam.de/pik/showshort.php?id=escidoc:4736895"
        primap_link_text = f"{meta.sources.srce_to_label[meta.primap.current_version['emi']]}"
        primap_link_paper = "https://essd.copernicus.org/articles/8/571/2016/"
        primap_link_paper_text = "Guetschow et al., 2016"
        txt += \
            "\n\n \\noindent \\textbf{\\href{" f"{primap_link}" "}{" f"{primap_link_text}" "}} " + \
            "(\\href{" f"{primap_link_paper}" "}{" f"{primap_link_paper_text}" "}): " + \
            "\n composite data set of historical emissions with sectoral resolution for the Kyoto~GHG basket as a whole, " + \
            "and for CO$_2$, CH$_4$, N$_2$O, HFCs, PFCs, SF$_6$, and NF$_3$ as single gases~/ gas baskets." + \
            "\n The presented historical emissions are data from the country reported data priority scenario (HISTCR)."
        
        dmSSPs_link = "https://zenodo.org/record/3638137\#.X2syXouxU2w"
        dmSSPs_link_text = "dmSSPs"
        dmSSPs_link_paper = "https://essd.copernicus.org/preprints/essd-2020-101/"
        dmSSPs_link_paper_text = "Guetschow et al. (2020)"
        SSPs_link = "https://www.sciencedirect.com/science/article/pii/S0959378016300681"
        SSPs_link_text = "Riahi et al., 2017"
        txt += \
            "\n\n \\noindent " + \
            "\\textbf{\\href{" f"{dmSSPs_link}" "}{" f"{dmSSPs_link_text}" "}}: " + \
            "\n The dmSSP data are socioeconomic pathways " + \
            "\\href{" f"{SSPs_link}" "}{" f"{SSPs_link_text}" "} " + \
            "that were downscaled to country-level by " + \
            "\\href{" f"{dmSSPs_link_paper}" "}{" f"{dmSSPs_link_paper_text}" "}." + \
            "\n Emissions, population and GDP data presented here are PMSSPBIE data for the five marker scenarios."
        
        primap_crf_data_link = "https://doi.org/10.5281/zenodo.3775575"
        primap_crf_data_text = "Guetschow et al., 2020"
        primap_crf_paper_link = "https://essd.copernicus.org/articles/10/1427/2018/"
        primap_crf_paper_text = "Jeffery et al., 2018"
        crf_link = "https://unfccc.int/process-and-meetings/transparency-and-reporting/reporting-and-review-under-the-convention/greenhouse-gas-inventories-annex-i-parties/national-inventory-submissions-2019"
        crf_link_text = "UNFCCC CRF 2019 submissions"
        txt += \
            "\n\n \\noindent " + \
            "\textbf{PRIMAP-crf}: " + \
            "\n emissions data that was submitted to the UNFCCC by Annex-I countries in the common reporting format (" + \
            "\\href{" f"{crf_link}" "}{" f"{crf_link_text}" "}" ")." + \
            "\n The data was transferred into easily readible format and grouped in IPCC~2006 categories by " + \
            "\\href{" f"{primap_crf_data_link}" "}{" f"{primap_crf_data_text}" "} " + \
            "(paper: \\href{" f"{primap_crf_paper_link}" "}{" f"{primap_crf_paper_text}" "})."
        
        unfccc_bur_link = "https://unfccc.int/BURs"
        unfccc_bur_text = "UNFCCC BUR submissions"
        txt += \
            "\n\n \\noindent " + \
            "\\href{" f"{unfccc_bur_link}" "}{" f"{unfccc_bur_text}" "}:" + \
            "\n emissions data that was submitted to the UNFCCC by non-Annex-I countries in the Biennial Update Reports."
        
        # TODO: UNFCCC and EDGAR.
        # TODO: which data are needed in for the quantification of that country, and are they available.
        
        # %% Footnotes
        tpes_info = ""
        for tpe in tar_to_long.keys():
            tpes_info += " \n \\textit{" f"{tpe}" "}: " f"{tar_to_long[tpe]}; \\newline "
        add_info = {
            "Target types": "All target types considered as type\_main or type\_reclass. \\newline" + tpes_info[:-len('\\newline')],
            "SSPs":
                "Shared Socioeconomic Pathways (" "\\href{" f"{SSPs_link}" "}{" f"{SSPs_link_text}" "} " "). \\newline" +
                "\n Narratives and challenges to mitigation and adaptation in brackets: \\newline" +
                "\n \\textit{SSP1}: Sustainability, Taking the Green Road (low~/ low); \\newline" +
                "\n \\textit{SSP2}: Middle of the Road (medium~/ medium); \\newline" +
                "\n \\textit{SSP3}: Regional Rivalry, A Rocky Road (high~/ high); \\newline"+
                "\n \\textit{SSP4}: Inequality, A Road Divided (low~/ high); and \\newline" +
                "\n \\textit{SSP5}: Fossil-fuelled Development, Taking the Highway (high~/ low).",
            "GDP":
                "Gross Domestic Product. \\newline" +
                "\n Throughout this document the GDP is given as GDP~PPP, with PPP being the Purchasing Power Parity." + \
                "\n It allows for better comparisons between countries and reflects the economic productivity and living standards.",
            "GWP":
                "Global Warming Potential. \\newline" +
                "\n We use GWP values from the IPCC " +
                ("4$^{th}$ Assessment Report (AR4). " if meta.gwps.default == 'AR4' else "") +
                ("2$^{nd}$ Assessment Report (SAR). " if meta.gwps.default in ['SAR', 'AR2'] else "") +
                "\n They reflect the forcing potential of one kilogram of a gas' emissions in comparison " +
                "to one kilogram of CO$_2$ (GWP$_{CO2}$ = 1). " +
                "\n The GWPs correspond to a 100-yr period and are " +
                f"for CH$_4$:~{gwps['CH4'] :.0f}, for N$_2$O:~{gwps['N2O'] :.0f}" +
                f", for SF$_6$:~{gwps['SF6'] :.0f}, and for NF$_3$:~{gwps['NF3'] :.0f}. " +
                f"\n For the basket of HFC-gases the GWPs from AR4 are in the range {gwps[hfcs].min() :.0f}--{gwps[hfcs].max() :.0f}, " +
                f"and for PFCs {gwps.reindex(index=pfcs).min() :.0f}--{gwps.reindex(index=pfcs).max() :.0f}. " +
                "\n To assess emissions of several GHGs, their emissions are weighted by their respective GWPs " +
                "and presented in CO$_2$ equivalents (CO$_2$eq).",
            "LULUCF":
                "Land Use, Land-Use Change and Forestry. \\newline" +
                "\n Emissions from LULUCF are excluded throughout the document, unless stated otherwise.",
            "Bunkers fuels":
                "Emissions from international aviation and shipping.",
            "Kyoto~GHG":
                "Kyoto~GHG (Greenhouse Gas) basket. \\newline" +
                "\n Carbon dioxide (CO$_2$), methane (CH$_4$), nitrous oxide (N$_2$O), " +
                "hydrofluorocarbons (HFCs), perfluorocarbons (PFCs), " +
                "sulfur hexafluoride (SF$_6$), and nitrogen trifluoride (NF$_3$).",
            "F-gases":
                "Fluorinated gases. \\newline" +
                "\n Basket of HFCs, PFCs, and the gases SF$_6$ and NF$_3$. " +
                "\n Some F-gases have very long atmospheric lifetimes and high Global Warming Potentials.",
            "Target reclassification":
                f"When a country has, e.g., an RBU target ({tar_to_long['RBU']}), and the BAU emissions are provided, " +
                "it can be quantified based on the given emissions, and is reclassified from type\_main~RBU to " +
                f"type\_reclass~ABS ({tar_to_long['ABS']})." +
                f"\n Additionally, 'NGT' ({tar_to_long['NGT']}) targets can be reclassified as 'ABU' ({tar_to_long['ABU']}) if " +
                "absolute mitigation effects due to planned policies and measures are provided.",
            "NDC quantification options":
                "Different quantification options were tested. \\newline" +
                "\n \\textit{dmSSP1--5}: down-scaled SSP marker scenarios; \\newline" +
                "\n \\textit{type\_reclass}: external data prioritised (PRIMAP-hist, dmSSPs); \\newline" +
                "\n \\textit{type\_main}: emissions data from within NDCs were prioritised; \\newline" +
                "\n \\textit{100\% coverage \& estimated coverage}: assumed 100\% coverage vs. coverage estimated from information on covered sectors and gases; \\newline" +
                "\n \\textit{constant~emi}: constant emissions after last target year (instead of constant relative difference to baseline); \\newline" +
                "\n \\textit{baseline uncondi}: baseline emissions as uncond. pathways for Parties without uncond. targets, " +
                "even if baseline is better than cond. targets (instead of cond. pathway as uncond. pathways in these cases)."
                }
        
        txt += \
            "\n\n \\begin{description}" + \
            "".join(["\n \\item [" + xx + "] " + add_info[xx] for xx in add_info.keys()]) + \
            "\n \\end{description}"
        
        # %% Links
        isos_links = [iso3, 'EARTH']
        isos_links = (isos_links if iso3 not in meta.isos.EU28 else isos_links + ['EU28'])
        links_iso = links.loc[links.iso3.isin(isos_links), :].sort_values('text')
        txt += \
            "\n\n \\noindent \\textbf{Links to additional information:}" + \
            "\n \\begin{itemize}" + \
            "\n \\item " + \
            "\n \\vspace{-.2cm} \\item ".join([
                "\\href{" +
                f"{links_iso.loc[xx, 'link']}".replace('%', '\%') + "}{" +
                f"{links_iso.loc[xx, 'text']}" "} " +
                (f"({links_iso.loc[xx, 'date']})" if type(links_iso.loc[xx, 'date']) == str else "")
                for xx in links_iso.index]) + \
            "\n \\end{itemize}"
        
        # %%
        txt += \
            "\n\n %%%" + \
            "\n \\end{document}"
        
        # %%
        # Write text to .tex file.
        path_tex_file = Path(path_to_tex_files, f"factsheet_{iso3}.tex")
        tex_file = open(path_tex_file, 'w', encoding='utf8')
        
        print(txt, file=tex_file)
        tex_file.close()
        
        # %%
        # Make a pdf.
        os.chdir(path_to_tex_files)
        os.system("pdflatex " f"{path_tex_file}")
        os.system("pdflatex " f"{path_tex_file}") # Second run as sometimes with one run the labels are wrong...
        os.chdir(meta.path.py_files)
        
        # %%
        # TODO: Include information from info_per_country where needed.
        # TODO: Global page: include the graphics I had done on the data needed.

# %%
# TODO: analysing the targets to find out the text options that need to be implemented.
# - if the baseline emissions are taken from the NDC, they can be the same for all SSPs, and so are the target emissions in that case (for prio NDC, type_reclass)
# - if no baseline emissions are provided in the NDC, the targets for prio NDC and prio SSPs are the same (per SSP), as they are both based on the same non-NDC (SSP) data
# - if the estimated coverage is 100% (in base and target year), the quantifications for estimated and 100% coverage are the same

# BRA

# - why are there no upper and lower lines in the baseline?
#   - it has a base year target, with given ABS
#   - the NDC_SSP and SSP_SSP is the same (as the NDC baseline emissions were only used for future years)
# - why are the targets the same for all SSPs?
#   - base year target
#   - and estimated coverage = 100% in base and target year, else the not-covered part of emissions that is added from the target year might differ for the SSPs
# - why do the quadruples (options 1-4) not really change?
# - **why is the 2025 value different but the 2030 value is not?!**

# ABW: all 2030 baselines the same, and the types are both baseline_emissions

# %%