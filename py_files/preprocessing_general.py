# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
import pandas as pd
import numpy as np
import os
from copy import deepcopy
from pathlib import Path
import matplotlib.pyplot as plt
import helpers_functions as hpf
import preprocessing as prep
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

# Create folder & sub-folders.
Path(meta.path.preprocess).mkdir(parents=True, exist_ok=True)
# Output tables.
Path(meta.path.preprocess, 'tables').mkdir(parents=True, exist_ok=True)

# Also writes out information to 'ndcs_info.csv' in meta.path.preprocess.
infos_from_ndcs = hpf.get_infos_from_ndcs(meta)

# How many years should be used when calculating the mean over the last available years.
nrvalues = 6

# Have one pd.DataFrame, where the per-country information on modified data / dataseries is put to.
# E.g., which LULUCF data are used, and which coverages were modified, etc.
info_per_country = pd.DataFrame(index=meta.isos.EARTH)

# Simply add needed columns on the go (info_per_country.loc[:, 'newcolumn'] = whatever).

# %% Read in tables from meta.path.matlab.

"""
Read in all datatables in folder matlab_tables.

All read into class 'database', with the tablenames as attributes.
Replace the AR4 strings by ''
(e.g., KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTORY_CRF2019.csv is read in 
with tablename 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTORY_CRF2019').
The attributes are classes again, with attributes entity, category, 
data, family, etc. (see meta.nomenclature.attrs).
"""

print("Read in all datatables in folder matlab_tables.")

database = hpf.create_table(name='database')
# All files in matlab_tables.
path_to_files = meta.path.matlab
files = os.listdir(path_to_files)
for file in files:
    if file.endswith('.csv'):
        
        database = prep.prep_read_in_tables(file, path_to_files, database, meta)

# %%
"""
Get PRIMAP emissions for KYOTOGHG_IPCM0EL, POP and GDPPPP. For easier use.
"""

primap = {}
for tpe in ['emi', 'pop', 'gdp']:
    primap[tpe] =  deepcopy(getattr(database, '_'.join([getattr(meta.primap, tpe)[xx] 
        for xx in getattr(meta.primap, tpe).keys()])).data)

# %% SSPs.
"""
SSPs: check if there are countries that do have data in some SSPs but not in others and
use the average over the available SSPs for the non-available SSPs.
For countries that have PRIMAP-hist data but no SSP data at all (for SSP1 to SSP5), 
use the PRIMAP-hist data and use the linear regression over the last 6 available years 
as future estimates.
Only happens for countries with very low emissions.
"""

print("Preprocessing of SSPs.")

database, info_per_country = prep.prep_ssps_fill_gaps(database, info_per_country, meta, nrvalues)
    
"""
The SSPs only have data for FGASES, not separated into HFCS, PFCS, SF6 and NF3.
For the calculation of the future pc_cov, a split into the four subgroups is performed.
The historical share per gas/basket is kept constant and applied to the future FGASES-basket.
The mean over the last 6 available years is used.
"""

print("SSPs: splitting the F-gases.")

database = prep.prep_ssps_split_fgases(meta, database, nrvalues)

"""
Check if the SSPs (KYOTOGHG_IPCM0EL per SSP scenario) are consistent with the given PRIMAP-hist data.
Only gives out a warning if not.
Only tests the 'main' data (kyotoghg_ipcm0el, pop and gdp).
"""

prep.prep_ssps_test(database, meta, primap)

# %%
"""
Calculate the covered part of emissions for certain cases (not using NDC-input, for the NDC-input go to preprocessing_current_pc_cov.py):
    All NaNs set to Nos.
    Only cover CO2_ENERGY, CO2_CH4_N2O_ENERGY, CO2_CH4_N2O_ENERGY_AGRICULTURE,
    CO2_CH4_N2O_ENERGY_AGRICULTURE_IPPU, CO2_CH4_N2O_HFCS_PFCS_SF6_NF3_ENERGY_AGRICULTURE_IPPU.
"""

"""
#preference_pccov_fut = 'mean'
preference_pccov_fut = 'corr'

first_year_for_slope = 2010
slope_lim = 1./100. 
rvalue_lim = .85

hpf.write_text_to_file(f"preference\_pccov\_fut is set to {preference_pccov_fut}\n" +
    f"first\_year\_for\_slope is set to {first_year_for_slope}\n" +
    f"slope\_lim is set to {slope_lim}\n" +
    f"rvalue\_lim is set to {rvalue_lim}",
    Path(meta.path.preprocess, 'preference_pc_cov_fut.md'))

# Tables written out in the function.
prep.prep_calculate_other_coverages(database, infos_from_ndcs, meta, primap, info_per_country)
"""

# %% LULUCF data.

"""
Prepare LULUCF data.

Make one LULUCF table, with the chosen KYOTOGHG_IPCMLULUCF time series.
Prioritisation of data-sources as given in meta.lulucf.source_prioritisation.
When a source has data, use them, and fill data gaps with 'constant filling' 
(interpolation & forward extrapolation: last value kept constant, 
backward extrapolation: first available value after 1990 used for 1990 to year of first available value).
Other option: linear interpolation, but constant extrapolation.
If KYOTOGHG is calculated here from CO2 + CH4 + N2O: sum up the already inter- & extrapolated time series.

Problems with LULUCF data: high inter-annual variability, negative / positive emissions, 
and the data we use are not consistent with the time series used in the pathway extension.
"""

print("LULUCF data.")

# TODO: somehow scale the LULUCF data we use (after filling the gaps) to the 
# regional time series used in the pathway extension?
# Problem: negative emissions (and different data sources).

nr_available_values_lulucf = 3

database, info_per_country = prep.prep_lulucf(database, meta, meta.lulucf.source_prioritisation,
    'VARIOUS', info_per_country, nr_available_values_lulucf, 'constant')
database, info_per_country = prep.prep_lulucf(database, meta, meta.lulucf.source_prioritisation,
    'VARIOUS', info_per_country, nr_available_values_lulucf, 'linear')

"""
Put FAO or UNFCCC to the first place in the LULUCF prioritisation, for a comparison run.
"""
for srce_lu in ['FAO', 'UNFCCC']:
    srce_act = [xx for xx in meta.lulucf.source_prioritisation if srce_lu in xx]
    lu_prios = srce_act + [xx for xx in meta.lulucf.source_prioritisation if srce_lu not in xx]
    database, info_per_country = prep.prep_lulucf(database, meta, lu_prios,
        f'VARIOUS{srce_lu}', info_per_country, nr_available_values_lulucf, 'constant')
    database, info_per_country = prep.prep_lulucf(database, meta, lu_prios,
        f'VARIOUS{srce_lu}', info_per_country, nr_available_values_lulucf, 'linear')

# %%
# Write out the tables from database.
for tablename in hpf.get_all_attributes_of_class(database):
    
    if 'COV' not in tablename: # The COV non-LULUCF was written out earlier.
        hpf.write_table_from_class_metadata_country_year_matrix(
            getattr(database, tablename), Path(meta.path.preprocess, 'tables'))

# Write out info_per_country.
info_per_country.to_csv(Path(meta.path.preprocess, 'info_per_country.csv'))

# %%
"""
Create NDC exclLU pathways.
Use PRIMAP-hist v2.1 HISTCR up to 2017 and then use given ndcs_emi_exclLU when available, 
with linear interpolation between values.

For the countries without exclLU values check if they have inclLU values.
If so use the onlyLU data from the NDC (or other options, as used in the NDC quantifications)
to derive onlyLU emissions.
Use the given inclLU values and the corresponding onlyLU values to derive exclLU, and
then interpolate linearly between them (again, with PRIMAP-hist for KYOTOGHG_IPCM0EL up to 2017).
"""
ndcs_emi_exclLU = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_exclLU.csv'), index_col=0)
ndcs_emi_exclLU.columns = [int(xx) for xx in ndcs_emi_exclLU.columns]
#
ndcs_emi_inclLU = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_inclLU.csv'), index_col=0)
ndcs_emi_inclLU.columns = [int(xx) for xx in ndcs_emi_inclLU.columns]
#
ndcs_emi_onlyLU = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_onlyLU.csv'), index_col=0)
ndcs_emi_onlyLU.columns = [int(xx) for xx in ndcs_emi_onlyLU.columns]

yrs_fut = list(range(2018, 2051))
yrs_primap = list(range(1990, 2018))

txt = ''

plot_data = False

fig = plt.figure(figsize=(7, 7))
for ssp in meta.ssps.scens.long:
    
    # onlyLU.
    for lu_table in ['', 'FAO', 'UNFCCC']:
        tablename_onlyLU = f'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS{lu_table}'
        table_onlyLU = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', f'{tablename_onlyLU}.csv'))
        table_onlyLU.data = table_onlyLU.data.reindex(index=meta.isos.EARTH)
        
        # exclLU
        tablename_exclLU = f'KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp}FILLED_PMSSPBIE'
        table_exclLU = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', f'{tablename_exclLU}.csv'))
        table_exclLU.data = table_exclLU.data.reindex(index=meta.isos.EARTH)
        
        for iso3 in meta.isos.EARTH:
            
            ndc_onlyLU_act = ndcs_emi_onlyLU.loc[iso3, :]
            ndc_inclLU_act = ndcs_emi_inclLU.loc[iso3, :]
            ndc_exclLU_act = ndcs_emi_exclLU.loc[iso3, :]
            
            bl_onlyLU = pd.Series(index=ndc_onlyLU_act.index, dtype='float64')
            
            if (not ndc_onlyLU_act.isnull().all() or not ndc_inclLU_act.isnull().all()):
                if not ndc_onlyLU_act.isnull().all():
                    bl_onlyLU.loc[:] = ndc_onlyLU_act
                    if 'SSP2' in ssp:
                        txt += f"\n{iso3} onlyLU: ndc_onlyLU used."
                elif (not np.isnan(ndc_inclLU_act.isnull().all() and not np.isnan(ndc_exclLU_act.isnull().all()))):
                    inds = [xx for xx in ndc_inclLU_act.index
                        if (not np.isnan(ndc_inclLU_act[xx]) and not np.isnan(ndc_exclLU_act[xx]))]
                    if inds != []:
                        bl_onlyLU.loc[inds] = [ndc_inclLU_act[xx] - ndc_exclLU_act[xx] for xx in inds]
                        available_years = [xx for xx in ndc_onlyLU_act.index if not np.isnan(ndc_onlyLU_act[xx])]
                        if 'SSP2' in ssp:
                            txt += f"\n{iso3} onlyLU: ndc_inclLU - ndc_exclLU used."
                if bl_onlyLU.isnull().all():
                    if not np.isnan(ndc_inclLU_act.isnull().all()):
                        # Here, the bl_onlyLU depends on the chosen SSP ...
                        bl_onlyLU.loc[:] = ndc_inclLU_act.add(- table_exclLU.data.loc[iso3, :]) # Do not use fill_value=0!
                        if 'SSP2' in ssp:
                            txt += f"\n{iso3} onlyLU: ndc_inclLU - external_exclLU used."
            
            """
            If there are onlyLU values available for 2010 or later, use them for constant extrapolation 
            (use their average) if no future values are available.
            """
            if (not bl_onlyLU.loc[range(2010, 2018)].isnull().all() and bl_onlyLU.loc[range(2018, 2051)].isnull().all()):
                bl_onlyLU.loc[list(range(2018, 2051))] = bl_onlyLU.loc[range(2010, 2018)].mean()
            
            if bl_onlyLU.isnull().all():
                bl_onlyLU = table_onlyLU.data.loc[iso3, :]
                if 'SSP2' in ssp:
                    txt += f"\n{iso3} onlyLU: external_onlyLU used."
            
    #        if 'SSP1' in ssp:
    #            available_years = [str(xx) for xx in bl_onlyLU.index if not np.isnan(bl_onlyLU[xx])]
    #            txt += "\nAvailable years: " + ', '.join(available_years)
            
            table_onlyLU.data.loc[iso3, :] = bl_onlyLU
            
            """
            Check if there is exclLU data available from the NDC for years > 2017.
            If so, use them with linear interpolation from PRIMAP-hist to the first year, and inbetween.
            After last year: use SSP growth rates.
            
            If ndc_exclLU available: use ndc_exclLU.
            If ndc_inclLU available: use ndc_inclLU - onlyLU.
            Else: use external_exclLU.
            """
            
            if not ndc_exclLU_act.loc[yrs_fut].isnull().all():
                bl_exclLU = ndc_exclLU_act
                if 'SSP2' in ssp:
                    txt += f"\n{iso3} exclLU: data from NDC."
            
            elif not ndc_inclLU_act.loc[yrs_fut].isnull().all():
                bl_exclLU = ndc_inclLU_act.add(-bl_onlyLU) # Gives nans where no bl_onlyLU data are available!
                if 'SSP2' in ssp:
                    txt += f"\n{iso3} exclLU: inclLU data from NDC minus onlyLU."
            
            else:
                bl_exclLU = table_exclLU.data.loc[iso3, :]
                if 'SSP2' in ssp:
                    txt += f"\n{iso3} exclLU: external data."
            
            """
            Put in PRIMAP-hist data to 1990 - 2017.
            And interpolate linearly.
            Extrapolate with the SSP growth rates.
            """
            if ('SSP2' in ssp and plot_data):
                plt.plot(table_exclLU.data.columns, table_exclLU.data.loc[iso3, :])
                plt.scatter(bl_exclLU.index, bl_exclLU, 80, marker='s', color='r')
            bl_exclLU.loc[yrs_primap] = table_exclLU.data.loc[iso3, yrs_primap].to_list()
            if ('SSP2' in ssp and plot_data):
                plt.scatter(bl_exclLU.index, bl_exclLU, 60, marker='*')
            bl_exclLU.interpolate(limit_area='inside', inplace=True)
            if ('SSP2' in ssp and plot_data):
                plt.scatter(bl_exclLU.index, bl_exclLU, 40, marker = 'o')
            available_years = [xx for xx in bl_exclLU.index if not np.isnan(bl_exclLU[xx])]
            if (len(available_years) > 0 and available_years[-1] < 2050):
                missing_years = list(range(available_years[-1] + 1, 2051))
                bl_exclLU.loc[missing_years] = \
                    table_exclLU.data.loc[iso3, missing_years] - \
                        (table_exclLU.data.loc[iso3, available_years[-1]] - bl_exclLU[available_years[-1]])
            if ('SSP2' in ssp and plot_data):
                plt.scatter(bl_exclLU.index, bl_exclLU, 20, marker='<')
            
            table_exclLU.data.loc[iso3, :] = bl_exclLU
            if ('SSP2' in ssp and plot_data):
                plt.savefig(Path(meta.path.main, 'plots', 'time_series', 'ssp2_ndcs_exclLU_filled', f'NDC_exclLU_{iso3}.png'), dpi=300)
                plt.clf()
        
        setattr(table_onlyLU, 'cat', 'IPCMLULUCF')
        setattr(table_onlyLU, 'scen', f'NDC{ssp}')
        setattr(table_onlyLU, 'srce', f'NDCPMSSPBIE{lu_table}')
        setattr(table_onlyLU, 'note', getattr(table_onlyLU, 'note') + 
                ' For countries without emissions provided in the NDC but with inclLU emissions provided, ' +
                'the onlyLU emissions were calculated based on NDC_inclLU minus SSP_exclLU. ' +
                f'For countries without emissions provided in the NDC the {tablename_onlyLU} values are used.')
        table_onlyLU.__tablename_to_standard__()
        table_onlyLU.__name_to_standard__()
        hpf.write_table_from_class_metadata_country_year_matrix(table_onlyLU,
            Path(meta.path.preprocess, 'tables'))
        
        setattr(table_exclLU, 'cat', 'IPCM0EL')
        setattr(table_exclLU, 'scen', f'NDC{ssp}')
        setattr(table_exclLU, 'srce', f'NDCPMSSPBIE{lu_table}')
        setattr(table_exclLU, 'note', getattr(table_exclLU, 'note') + 
                ' For countries without emissions provided in the NDC but with inclLU emissions provided, ' +
                'the exclLU emissions were calculated based on NDC_inclLU minus {table_onlyLU.tablename}. ' +
                f'For countries without emissions provided in the NDC the {tablename_exclLU} values are used.')
        table_exclLU.__tablename_to_standard__()
        table_exclLU.__name_to_standard__()
        hpf.write_table_from_class_metadata_country_year_matrix(table_exclLU,
            Path(meta.path.preprocess, 'tables'))

plt.close(fig)
hpf.write_text_to_file(txt, Path(meta.path.preprocess, 'info_onlyLU_exclLU_fromNDCs.txt'))

# %%