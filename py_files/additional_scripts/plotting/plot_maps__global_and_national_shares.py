# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in April 2020.
"""

# %%
from pathlib import Path
import pandas as pd
from setup_metadata import setup_metadata
import helpers_functions as hpf

# %%
meta = setup_metadata()

# %%
# Plot the global share in 10 equally sized bins.
share = pd.read_csv(Path(meta.path.main, 'data', 'other',
    'global_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)

for ent_cat in share.columns:
    
    pd_series = share.loc[:, ent_cat]
    
    annotation = 'PRIMAP-hist v2.1 HISTCR ' + ent_cat.replace('AR4', '') + ' (AR4) for 2017.' + \
        " National totals: excl. LULUCF and bunkers."    
    ent, cat = ent_cat.split('_')
    title = 'Global share of ' + meta.gases.gas_to_label[ent.replace('AR4', '')] + \
        ' emissions (' + \
        (meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[cat]]
        if cat != 'IPCM0EL' else 'national totals') + ')'
    
    hpf.plot_maps_bins(pd_series, 
        Path(meta.path.main, 'plots', 'maps', 'global_share', 'global_share' + '_' + 
        ent_cat.replace('AR4', '') + '.png'), title=title, annotation=annotation, flipud=True, nr_instances=True)
    
    # For global share setting the limits to 0 - 100 does not make a lot of sense.
    if ent_cat == 'KYOTOGHGAR4_IPCM0EL':
        hpf.plot_maps_bins(pd_series, 
            Path(meta.path.main, 'plots', 'maps', 'global_share', 'global_share' + '_' + 
            ent_cat.replace('AR4', '') + '_better_limits.png'), title=title, annotation=annotation, 
            bounds=[.05, .1, .2, .4, .6, .8, 1, 1.5, 2.5, 10], flipud=True, nr_instances=True, plot_pdf=True)
        hpf.plot_maps_bins(pd_series, 
            Path(meta.path.main, 'plots', 'maps', 'global_share', 'global_share' + '_' + 
            ent_cat.replace('AR4', '') + '_better_limits.png'), 
            bounds=[.05, .1, .2, .4, .6, .8, 1, 1.5, 2.5, 10], flipud=True, nr_instances=True, plot_pdf=True)

# %%
# Plot the global share in 10 equally sized bins (2030, SSP2).
share = hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
    'KYOTOGHG_IPCM0EL_TOTAL_NET_' + meta.ssps.scens.long[1] + '_' + meta.ssps.emi['srce'] + '.csv'))
pd_series = 100. * share.__global_share__(years=[2030]).loc[:, 2030]

annotation = 'National share of Kyoto GHG emissions ' + meta.gwps.default + ' for 2030.' + \
    " National totals: excl. LULUCF and bunkers."
title = 'Global share of Kyoto GHG emissions (national totals)'

hpf.plot_maps_bins(pd_series, 
    Path(meta.path.main, 'plots', 'maps', 'global_share', 'global_share_KYOTOGHG_IPCM0EL_2030_' + 
         meta.ssps.scens.long[1] +'.png'), title=title, annotation=annotation, 
    bounds=[.05, .1, .2, .4, .6, .8, 1, 1.5, 2.5, 10], flipud=True, nr_instances=True)

# %%
# Plot the national share in 10 equally sized bins.
share = pd.read_csv(Path(meta.path.main, 'data', 'other',
    'national_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)

for ent_cat in [xx for xx in share.columns if xx != 'KYOTOGHG_IPCM0EL']:
    
    pd_series = share.loc[:, ent_cat]
    
    annotation = "PRIMAP-hist v2.1 HISTCR '" + ent_cat + " compared to KYOTOGHG_IPCM0EL' (AR4) for 2017." + \
        " National totals: excl. LULUCF and bunkers."
    ent, cat = ent_cat.split('_')
    title = 'National share of ' + meta.gases.gas_to_label[ent.replace('AR4', '')] + \
        ' emissions (' + \
        (meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[cat]]
        if cat != 'IPCM0EL' else 'national totals') + \
        ")\ncompared to national totals of Kyoto GHG emissions"
    
    hpf.plot_maps_bins(pd_series, 
            Path(meta.path.main, 'plots', 'maps', 'national_share', 'national_share' + '_' + ent_cat + '.png'),
            title=title, annotation=annotation, flipud=True, nr_instances=True)
    hpf.plot_maps_bins(pd_series, 
            Path(meta.path.main, 'plots', 'maps', 'national_share', 'limits_0_100',
            'national_share' + '_' + ent_cat + '.png'),
            title=title, annotation=annotation, val_min=0, val_max=100, flipud=True, nr_instances=True)

# %%
# Plot the sector with the highest share (per country).
share = pd.read_csv(Path(meta.path.main, 'data', 'other',
    'national_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)
share = share.reindex(columns=[xx for xx in share.columns if (xx != 'KYOTOGHG_IPCM0EL' and 'KYOTOGHG' in xx)])
pd_series = pd.Series(index=share.index, dtype='object')
for iso3 in share.index:
    pd_series.loc[iso3] = meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[
        share.loc[iso3, :].sort_values(ascending=False).index[0].split('_')[1]]]

colours = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
    'colours', 'colours_categories_ipc.csv'), index_col=0)
colours = colours.reindex(index=[xx.split('_')[1] for xx in share.columns])
colours.index = [meta.sectors.main.sec_to_label[meta.categories.main.cat_to_sec[xx]] for xx in colours.index]
colours_dict = dict(zip(colours.index, colours.values))

annotation = "PRIMAP-hist v2.1 HISTCR sector with highest share compared to KYOTOGHG_IPCM0EL' (AR4) for 2017." + \
    " National totals: excl. LULUCF and bunkers."
title = "Sectors with highest national share of emissions" + \
    "\ncompared to national totals of Kyoto GHG emissions"

hpf.plot_maps(pd_series, colours_dict,
    Path(meta.path.main, 'plots', 'maps', 'national_share_highest_sector.png'),
    title=title, annotation=annotation, colour_nan_countries=(.3, .3, .3), nr_instances=True)

# %%
# Plot the gases with the highest share (per country).
share = pd.read_csv(Path(meta.path.main, 'data', 'other',
    'national_share_per_gas_and_sector_PRIMAPHIST21_HISTCR_2017.csv'), index_col=0)
share = share.reindex(columns=[xx for xx in share.columns if (xx != 'KYOTOGHG_IPCM0EL' and 'IPCM0EL' in xx)])
pd_series = pd.Series(index=share.index, dtype='object')
for iso3 in share.index:
    pd_series.loc[iso3] = meta.gases.gas_to_label[
        share.loc[iso3, :].sort_values(ascending=False).index[0].split('_')[0]]

colours = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
    'colours', 'colours_gases.csv'), index_col=0)
colours = colours.reindex(index=[xx.split('_')[0] for xx in share.columns])
colours.index = [meta.gases.gas_to_label[xx] for xx in colours.index]
colours_dict = dict(zip(colours.index, colours.values))

annotation = "PRIMAP-hist v2.1 HISTCR gas with highest share compared to KYOTOGHG_IPCM0EL' (AR4) for 2017." + \
    " National totals: excl. LULUCF and bunkers."
title = "Gases with highest national share of emissions" + \
    "\ncompared to national totals of Kyoto GHG emissions"

hpf.plot_maps(pd_series, colours_dict,
    Path(meta.path.main, 'plots', 'maps', 'national_share_highest_gas.png'),
    title=title, annotation=annotation, colour_nan_countries=(.3, .3, .3), nr_instances=True)

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

hpf.plot_maps(pd_series, colours_dict, Path(meta.path.main, 'plots', 'maps', 'national_share_highest_gas_cat.png'),
    title=title, annotation=annotation, colour_nan_countries=(.3, .3, .3), nr_instances=True, plot_pdf=True)

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

hpf.plot_maps(pd_series, colours_dict_secs, Path(meta.path.main, 'plots', 'maps', 'national_share_highest_gas_sec.png'),
    colour_nan_countries=(.3, .3, .3), nr_instances=True, plot_pdf=True)

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

hpf.plot_maps(pd_series, colours_dict, Path(meta.path.main, 'plots', 'maps', 'national_share_second_highest_gas_cat.png'),
    title=title, annotation=annotation, colour_nan_countries=(.3, .3, .3), nr_instances=True, plot_pdf=True)

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

hpf.plot_maps(pd_series, colours_dict_secs, Path(meta.path.main, 'plots', 'maps', 'national_share_second_highest_gas_sec.png'),
    colour_nan_countries=(.3, .3, .3), nr_instances=True, plot_pdf=True)

# %%