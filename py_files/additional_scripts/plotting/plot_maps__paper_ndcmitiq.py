# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
from pathlib import Path
import pandas as pd
import numpy as np
from setup_metadata import setup_metadata
import helpers_functions as hpf

meta = setup_metadata()

# %%
infos = pd.read_csv(Path(meta.path.preprocess, 'pc_cov_20210428_0834_SMD20200417_PMH21', 'infos_from_ndcs_SMD20200417.csv'), index_col=0)

colours_ndc_types = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
    'colours', 'colours_ndc_types.csv'), index_col=0)
colour_dict_ndc_types = {}
for ndc_type in ['ABS', 'RBY', 'RBU', 'ABU', 'REI_RBY', 'REI_RBU', 'AEI', 'NGT', 'NAN']:
    colour_dict_ndc_types[ndc_type] = colours_ndc_types.loc[ndc_type, :].to_list()

path_to_folder = Path(meta.path.main, 'paper_accepted_202107', 'figures_tables', 'better_figures')

yrs = list(range(2010, meta.primap.last_year+1))

ndcs_info = infos
isos_without_indc = [xx for xx in ndcs_info.index if (type(ndcs_info.loc[xx, 'NDC_INDC']) != str
                     or ndcs_info.loc[xx, 'NDC_INDC'] not in ['NDC', 'INDC'])]

# %%
# Plot the NDC types on a worldmap.

pd_series = hpf.get_isos_per_target_type(infos.loc[:, 'TYPE_MAIN'], infos.loc[:, 'BASEYEAR'],
    split_REI=True, dtype='series')
path_to_file = Path(path_to_folder, 'fig02_1.svg')
#annotation = 'NDC types (type_main)'

hpf.plot_maps(pd_series, colour_dict_ndc_types, path_to_file, #annotation=annotation, 
    nr_instances=True, plot_pdf=True)

# Plot the NDC types on a worldmap.
pd_series = hpf.get_isos_per_target_type(infos.loc[:, 'TYPE_RECLASS'], infos.loc[:, 'BASEYEAR'],
    split_REI=True, dtype='series')
path_to_file = Path(path_to_folder, 'fig02_2.svg')
#annotation = 'NDC types (type_reclass)'

hpf.plot_maps(pd_series, colour_dict_ndc_types, path_to_file, #annotation=annotation, 
    nr_instances=True, plot_pdf=True)

# %%
# Plot the share of KYOTOGHG_IPCM0EL emissions covered by the NDCs (for 2017).
pc_cov = 100. * hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'pc_cov_20210428_0834_SMD20200417_PMH21',
         f"KYOTOGHGAR4_IPCM0EL_COV_PC_HISTORY_PMH21.csv")).data
pd_series = pc_cov.loc[:, 2017]

colours = pd.read_csv(Path(setup_metadata().path.py_files, 'additional_scripts', 
    'plotting', 'colours', 'colourmap_plasma.csv'))
colours = colours.loc[np.arange(colours.index[-1], -1, -1), :]
colours.index = range(0, len(colours.index))

path_to_file = Path(path_to_folder, 'fig06_1.svg')

pd_series = pd_series.reindex(index=meta.isos.EARTH)
pd_series[isos_without_indc] = np.nan

hpf.plot_maps_bins(pd_series, path_to_file, colours=colours, 
    bounds=[20, 40, 60, 70, 80, 90, 95, 99], nr_instances=True, plot_pdf=False)

pd_series_pc_cov = pd_series

# %%
# Plot the slope of the regression line for pc_cov for 2010 to 2017.
pd_series = pd.Series(index=pc_cov.index, dtype='float64')

for iso3 in pd_series.index:
    x, y, linreg = hpf.linear_regression(yrs, pc_cov.loc[iso3, yrs])
    # Calculate the percentage in/decrease from 2010 to 2017, but then break it down to annual in/decrease.
    increase = [linreg.slope*xx + linreg.intercept for xx in [x[0], x[-1]]]
    increase = (increase[1] - increase[0]) / increase[0] * 100 # percentage increase from 2010 to 2017.
    pd_series[iso3] = increase / (x[-1] - x[0]) # annual percentage increase.

path_to_file = Path(path_to_folder, 'fig06_2.svg')

pd_series = pd_series.reindex(index=meta.isos.EARTH)
pd_series[isos_without_indc] = np.nan

hpf.plot_maps_bins(pd_series, path_to_file, 
    colours=pd.DataFrame([[.3, 0, 0], [.5, 0, 0], [.7, 0, 0], [0, 0, .7], [0, 0, .5], [0, 0, .3], [0, 0, 0]]), 
    bounds=[-5, -.5, 0, .5, 5, 10], nr_instances=True, plot_pdf=False)

pd_series_linreg_pc_cov = pd_series

# %%
emi_tot = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables_PMH21', f"KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_PMH21.csv")). \
    data.reindex(columns=yrs)

pd_series = pd.Series(index=emi_tot.index, dtype='float64')

for iso3 in pd_series.index:
    x, y, linreg = hpf.linear_regression(yrs, emi_tot.loc[iso3, :])
    # Calculate the percentage in/decrease from 2010 to 2017, but then break it down to annual in/decrease.
    increase = [linreg.slope*xx + linreg.intercept for xx in [x[0], x[-1]]]
    increase = (increase[1] - increase[0]) / increase[0] * 100 # percentage increase from 2010 to 2017.
    pd_series[iso3] = increase / (x[-1] - x[0]) # annual percentage increase.

path_to_file = Path(path_to_folder, 'figA03_4.svg')

hpf.plot_maps_bins(pd_series, path_to_file, 
    colours=pd.DataFrame(np.flipud([[.3, 0, 0], [.5, 0, 0], [.7, 0, 0], [.9, 0, 0], [0, 0, .9], [0, 0, .7]])), 
    bounds=[-2, 0, 2, 5, 10], nr_instances=True, plot_pdf=False)

pd_series_linreg_emi_tot = pd_series

# %%
































# %%
# Plot the global share in 10 equally sized bins.
path_to_folder = Path(meta.path.main, 'paper_accepted_202107', 'figures_tables', 'better_figures')

share = pd.read_csv(Path(meta.path.main, 'data', 'other',
    'global_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)
ent_cat = 'KYOTOGHGAR4_IPCM0EL'
pd_series = share.loc[:, ent_cat]
hpf.plot_maps_bins(pd_series, 
    Path(path_to_folder, 'figA03_3.svg'), 
    bounds=[.05, .1, .2, .4, .6, .8, 1, 1.5, 2.5, 10], flipud=True, nr_instances=True, plot_pdf=False)

# %%
# Plot the gas_category combination with the highest share (per country).
share = pd.read_csv(Path(meta.path.main, 'data', 'other',
    'national_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)
share = share.reindex(columns=[xx for xx in share.columns 
    if ('KYOTOGHG' not in xx and 'IPCM0EL' not in xx and 'HFCS' not in xx and 'PFCS' not in xx and 'SF6' not in xx and 'NF3' not in xx)])
pd_series = pd.Series(index=share.index, dtype='object')
for iso3 in share.index:
    pd_series.loc[iso3] = share.loc[iso3, :].sort_values(ascending=False).index[0]

annotation = "PRIMAP-hist v2.1 HISTCR gas+sector combination with highest share compared to KYOTOGHG_IPCM0EL' (AR4) for 2017." + \
    " National totals: excl. LULUCF and bunkers."
title = "Gas plus sector combination with highest national share of emissions" + \
    "\ncompared to national totals of Kyoto GHG emissions"

#colours = pd.read_csv(Path(setup_metadata().path.py_files, 'additional_scripts', 
#    'plotting', 'colours', 'colourmap_plasma.csv'))
#colours = colours.loc[list(range(0, colours.index[-1], int(np.floor(colours.index[-1]/(len(pd_series.unique())-1))))), :]
#colours.index = sorted(pd_series.unique())
#colours_dict = dict(zip(colours.index, np.flipud(colours.values)))

colours_dict = {
    'CO2_IPC1': (.8, 0, .3), 'CH4_IPC1': (.5, 0, 1),
    'CO2_IPC2': (0, .5, 1), 'FGASES_IPC2': (0, .3, .6), 
    'CH4_IPCMAG': (0, .4, 0), 'N2O_IPCMAG': (0, .6, 0),
    'CH4_IPC4': (1, .5, 0)}

for ky in list(colours_dict.keys()):
    if ky not in pd_series.unique():
        del colours_dict[ky]

#hpf.plot_maps(pd_series, colours_dict, Path(meta.path.main, 'plots', 'maps', 'national_share_highest_gas_cat.png'),
#    title=title, annotation=annotation, colour_nan_countries=(.3, .3, .3), nr_instances=True, plot_pdf=True)

# Sector instead of category.
pd_series[:] = [
    meta.gases.gas_to_label[xx.split('_')[0]] + ' ' + 
    meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[xx.split('_')[-1]]]
    for xx in pd_series]
colours_dict_secs = {}
for key in colours_dict.keys():
    colours_dict_secs[
        meta.gases.gas_to_label[key.split('_')[0]]
        + ' ' + 
        meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[key.split('_')[-1]]]
        ] = \
        colours_dict[key]

hpf.plot_maps(pd_series, colours_dict_secs, Path(path_to_folder, 'figA03_1.svg'),
    colour_nan_countries=(.3, .3, .3), nr_instances=True, plot_pdf=False)

# %%
# Plot the gas_category combination with the second highest share (per country).
share = pd.read_csv(Path(meta.path.main, 'data', 'other',
    'national_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)
share = share.reindex(columns=[xx for xx in share.columns 
    if ('KYOTOGHG' not in xx and 'IPCM0EL' not in xx and 'HFCS' not in xx and 'PFCS' not in xx and 'SF6' not in xx and 'NF3' not in xx)])
pd_series = pd.Series(index=share.index, dtype='object')
for iso3 in share.index:
    pd_series.loc[iso3] = share.loc[iso3, :].sort_values(ascending=False).index[1]

annotation = "PRIMAP-hist v2.1 HISTCR gas+sector combination with second highest share compared to KYOTOGHG_IPCM0EL' (AR4) for 2017." + \
    " National totals: excl. LULUCF and bunkers."
title = "Gas plus sector combination with second highest national share of emissions" + \
    "\ncompared to national totals of Kyoto GHG emissions"

#colours = pd.read_csv(Path(setup_metadata().path.py_files, 'additional_scripts', 
#    'plotting', 'colours', 'colourmap_plasma.csv'))
#colours = colours.loc[list(range(0, colours.index[-1], int(np.floor(colours.index[-1]/(len(pd_series.unique())-1))))), :]
#colours.index = sorted(pd_series.unique())
#colours_dict = dict(zip(colours.index, np.flipud(colours.values)))

colours_dict = {
    'CO2_IPC1': (.8, 0, .3), 'CH4_IPC1': (.5, 0, 1),
    'CO2_IPC2': (0, .5, 1), 'FGASES_IPC2': (0, .3, .6), 
    'CH4_IPCMAG': (0, .4, 0), 'N2O_IPCMAG': (0, .6, 0),
    'CH4_IPC4': (1, .5, 0)}

for ky in list(colours_dict.keys()):
    if ky not in pd_series.unique():
        del colours_dict[ky]

#hpf.plot_maps(pd_series, colours_dict, Path(meta.path.main, 'plots', 'maps', 'national_share_second_highest_gas_cat.png'),
#    title=title, annotation=annotation, colour_nan_countries=(.3, .3, .3), nr_instances=True, plot_pdf=True)

# Sector instead of category.
pd_series[:] = [
    meta.gases.gas_to_label[xx.split('_')[0]]
    + ' ' + 
    meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[xx.split('_')[-1]]]
    for xx in pd_series]
colours_dict_secs = {}
for key in colours_dict.keys():
    colours_dict_secs[
        meta.gases.gas_to_label[key.split('_')[0]]
        + ' ' + 
        meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[key.split('_')[-1]]]
        ] = \
        colours_dict[key]

hpf.plot_maps(pd_series, colours_dict_secs, Path(path_to_folder, 'figA03_2.svg'),
    colour_nan_countries=(.3, .3, .3), nr_instances=True, plot_pdf=False)

# %%