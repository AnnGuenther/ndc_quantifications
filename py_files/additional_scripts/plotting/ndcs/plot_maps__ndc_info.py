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

# %%
meta = setup_metadata()

infos = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0)

colours_ndc_types = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
    'colours', 'colours_ndc_types.csv'), index_col=0)
colour_dict_ndc_types = {}
for ndc_type in ['ABS', 'RBY', 'RBU', 'ABU', 'REI_RBY', 'REI_RBU', 'AEI', 'NGT', 'NAN']:
    colour_dict_ndc_types[ndc_type] = colours_ndc_types.loc[ndc_type, :].to_list()

path_to_folder = Path(meta.path.main, 'plots', 'maps', 'ndcs')

# %%
# Plot the NDC types on a worldmap.

pd_series = hpf.get_isos_per_target_type(infos.loc[:, 'TYPE_ORIG'], infos.loc[:, 'BASEYEAR'],
    split_REI=True, dtype='series')
path_to_file = Path(path_to_folder, 'ndc_types_orig.png')
annotation = 'NDC types (type_main)'

hpf.plot_maps(pd_series, colour_dict_ndc_types, path_to_file, annotation=annotation, 
    nr_instances=True, plot_pdf=True)

# Plot the NDC types on a worldmap.
pd_series = hpf.get_isos_per_target_type(infos.loc[:, 'TYPE_CALC'], infos.loc[:, 'BASEYEAR'],
    split_REI=True, dtype='series')
path_to_file = Path(path_to_folder, 'ndc_types_calc.png')
annotation = 'NDC types (type_reclass)'

hpf.plot_maps(pd_series, colour_dict_ndc_types, path_to_file, annotation=annotation, nr_instances=True, plot_pdf=True)

# %%
# Plot the share of KYOTOGHG_IPCM0EL emissions covered by the NDCs (for 2017).
pc_cov = 100. * hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.pc_cov, f"KYOTOGHG_IPCM0EL_COV_PC_HISTORY_{meta.primap.current_version['emi']}.csv")).data
pd_series = pc_cov.loc[:, 2017]

#annotation = 'Part of national Kyoto GHG emissions (excl. LULUCF and bunkers) covered by an (I)NDC, for 2017.' + \
#    '\nBased on PRIMAP-hist v2.1 HISTCR.'

colours = pd.read_csv(Path(setup_metadata().path.py_files, 'additional_scripts', 
    'plotting', 'colours', 'colourmap_plasma.csv'))
colours = colours.loc[np.arange(colours.index[-1], -1, -1), :]
colours.index = range(0, len(colours.index))

path_to_file = Path(path_to_folder, 'ndc_pc_cov_2017.png')

hpf.plot_maps_bins(pd_series, path_to_file, colours=colours, 
    bounds=[20, 40, 60, 70, 80, 90, 95, 99], nr_instances=True, plot_pdf=True)

pd_series_pc_cov = pd_series

# %%
# Plot the slope of the regression line for pc_cov for 2010 to 2017.
yrs = list(range(2010, meta.primap.last_year+1))
pd_series = pd.Series(index=pc_cov.index, dtype='float64')

for iso3 in pc_cov.index:
    linreg = hpf.linear_regression(yrs, pc_cov.loc[iso3, yrs].to_list())
    pd_series[iso3] = linreg[-1].slope

#annotation = '\nSlope of linear regression to part of national Kyoto GHG emissions ' + \
#    '(excl. LULUCF and bunkers) covered by an (I)NDC (2010 - ' + \
#    str(meta.primap.last_year) + ').\nShare of emissions in %. Based on PRIMAP-hist v2.1 HISTCR.'

path_to_file = Path(path_to_folder, 'ndc_pc_cov_linreg_2010_2017.png')

hpf.plot_maps_bins(pd_series, path_to_file, 
    colours=pd.DataFrame([[.3, 0, 0], [.5, 0, 0], [.7, 0, 0], [0, 0, .7], [0, 0, .5], [0, 0, .3]]), 
    bounds=[-1.5, -.1, 0, .1, 1.5], nr_instances=True, plot_pdf=True)

pd_series_linreg_pc_cov = pd_series

# %%
emi_tot = 100. * hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', f"KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv")). \
    data.reindex(columns=yrs)

pd_series = pd.Series(index=emi_tot.index, dtype='float64')

for iso3 in pc_cov.index:
    linreg = hpf.linear_regression(yrs, (100*emi_tot.loc[iso3, :]/emi_tot.loc[iso3, :].sum()).to_list())
    pd_series[iso3] = linreg[-1].slope

#annotation = \
#    '\nSlope of linear regression to national Kyoto GHG emissions ' + \
#    f'(excl. LULUCF and bunkers; {yrs[0]} - {yrs[-1]}),' + \
#    f'\nnormalised by the average national emissions for {yrs[0]} - {yrs[-1]}.' + \
#    '\nBased on PRIMAP-hist v2.1 HISTCR.'

path_to_file = Path(meta.path.main, 'plots', 'maps', 'emi_tot_linreg_2010_2017.png')

hpf.plot_maps_bins(pd_series, path_to_file, 
    colours=pd.DataFrame(np.flipud([[.3, 0, 0], [.5, 0, 0], [.7, 0, 0], [.9, 0, 0], [0, 0, .9], [0, 0, .7]])), 
    bounds=[-.1, 0, .1, .25, .5], nr_instances=True, plot_pdf=True)

pd_series_linreg_emi_tot = pd_series

# %%