# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2021.

03/2021:
    moved the NDC-specific parts to preprocessing_current_pc_cov.py;
    changed naming for SSP output files (PMSSP to PMH21SSP, to include the PRIMAP-hist version);
    changed naming for PRIMAPHIST -> PMH.
"""

# %%
"""
**General preprocessing.**

**Fill missing data, SSPs (emi, pop, gdp).**

**Parts of LULUCF emissions preprocessing here, other part depends on NDC info (in preprocessing_current_pccov.py).**

**Covered part of emissions in preprocessing_current_pccov.py.**
"""

# %%
import pandas as pd
import os
from copy import deepcopy
from pathlib import Path
import helpers_functions as hpf
import preprocessing as prep
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

# Create folder & sub-folders.
Path(meta.path.preprocess).mkdir(parents=True, exist_ok=True)
# Output tables.
path_tables = Path(meta.path.preprocess, f'tables_{meta.primap.current_primap}')
path_tables.mkdir(parents=True, exist_ok=True)

# Have one pd.DataFrame, where the per-country information on modified data / dataseries is put to.
# E.g., which LULUCF data are used, and which coverages were modified, etc.
# Simply add needed columns on the go (info_per_country.loc[:, 'newcolumn'] = whatever).
info_per_country = pd.DataFrame(index=meta.isos.EARTH)

# %% Read in tables from meta.path.matlab.

"""
Read in *all datatables from folder matlab_tables.*

All tables are read into the class 'database', with the tablenames as main-attributes.
The table meta-data are classes again, with attributes 'entity', 'category', 
'data', 'unit', etc. (see meta.nomenclature.attrs).

As we only use one GWP, replace the AR4 strings by ''
(e.g., ``KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTORY_CRF2019.csv`` is read in 
with tablename 'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTORY_CRF2019').
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
# Get PRIMAP data for KYOTOGHG_IPCM0EL, POP and GDPPPP. For easier use.

primap = {}

meta.primap.emi['ent'] = meta.primap.emi['ent'] + meta.gwps.default

for tpe in ['emi', 'pop', 'gdp']:
    
    primap[tpe] =  deepcopy(getattr(database, '_'.join([getattr(meta.primap, tpe)[xx] 
        for xx in ['ent', 'cat', 'clss', 'tpe', 'scen', 'srce']])).data)

# %% SSPs.
"""
*SSPs: check if there are countries that do have data in some SSPs but not in others 
and use the average over the available SSPs for the non-available SSPs.*
*For countries that have PRIMAP-hist data but no SSP data at all 
(for marker scenarios of SSP1 to SSP5), use the PRIMAP-hist data and 
use the linear regression over the last 6 available years as future estimates.*
Only happens for countries with very low emissions.
"""

print("Preprocessing of SSPs.")

database, info_per_country = prep.prep_ssps_fill_gaps(
    database, info_per_country, meta, meta.average_nrvalues)

"""
*The SSPs only have data for FGASES*, not separated into HFCS, PFCS, SF6 and NF3.
For the calculation of the future pc_cov, a *split into the four subgroups is performed*.
The historical share per gas/basket is kept constant and applied to the future FGASES-basket.
The mean over the last 6 available years is used.
"""

print("SSPs: splitting the F-gases.")

database = prep.prep_ssps_split_fgases(meta, database, meta.average_nrvalues)

"""
Check if the SSPs (KYOTOGHG_IPCM0EL per SSP scenario) are consistent with the given PRIMAP-hist data.
"""
# Only gives out a warning if not.
# Only tests the 'main' data (kyotoghg_ipcm0el, pop and gdp).

prep.prep_ssps_test(database, meta, primap)

# %%
# Calculate the covered part of emissions for certain cases (not using NDC-input, for the NDC-input go to preprocessing_current_pc_cov.py):
#     All NaNs set to Nos.
#     Only cover CO2_ENERGY, CO2_CH4_N2O_ENERGY, CO2_CH4_N2O_ENERGY_AGRICULTURE,
#     CO2_CH4_N2O_ENERGY_AGRICULTURE_IPPU, CO2_CH4_N2O_HFCS_PFCS_SF6_NF3_ENERGY_AGRICULTURE_IPPU.

# #preference_pccov_fut = 'mean'
# preference_pccov_fut = 'corr'

# first_year_for_slope = 2010
# slope_lim = 1./100. 
# rvalue_lim = .85

# hpf.write_text_to_file(f"preference\_pccov\_fut is set to {preference_pccov_fut}\n" +
#     f"first\_year\_for\_slope is set to {first_year_for_slope}\n" +
#     f"slope\_lim is set to {slope_lim}\n" +
#     f"rvalue\_lim is set to {rvalue_lim}",
#     Path(meta.path.preprocess, 'preference_pc_cov_fut.md'))

# # Tables written out in the function.
# prep.prep_calculate_other_coverages(database, infos_from_ndcs, meta, primap, info_per_country)

# %% LULUCF data.

"""
*Prepare LULUCF data.*

Problems with LULUCF data: high inter-annual variability, negative / positive emissions, 
and the data we use are not consistent with the time series used in the pathway extension.

*Make one LULUCF table, with the chosen KYOTOGHG_IPCMLULUCF time series.
Prioritisation of data-sources as given in meta.lulucf.source_prioritisation.
When a source has data, use them, and fill data gaps with 'constant filling'.*

Interpolation & forward extrapolation: last value kept constant.
Backward extrapolation: first available value after 1990 used for 1990 to year of 
first available value).

Other option: *linear interpolation, but constant extrapolation* (with mean over several years).

If KYOTOGHG is calculated here as sum over CO2 + CH4 + N2O: sum up the already 
inter- & extrapolated time series.
"""

print("LULUCF data.")

# TODO: somehow scale the LULUCF data we use (after filling the gaps) to the 
# regional time series used in the pathway extension?
# Problem: negative emissions (and different data sources).

database, info_per_country = prep.prep_lulucf(
    database, meta, meta.lulucf.source_prioritisation,
    'VARIOUS', info_per_country, 'constant')
database, info_per_country = prep.prep_lulucf(
    database, meta, meta.lulucf.source_prioritisation,
    'VARIOUS', info_per_country, 'linear')

"""
Additionally to prioritising CRF, BRU, UNFCCC, FAO in that order, put FAO or UNFCCC 
to the first place in the LULUCF prioritisation, for comparison runs.
"""
for srce_lu in ['FAO', 'UNFCCC']:
    
    srce_act = [xx for xx in meta.lulucf.source_prioritisation if srce_lu in xx]
    lu_prios = srce_act + [xx for xx in meta.lulucf.source_prioritisation if srce_lu not in xx]
    
    database, info_per_country = prep.prep_lulucf(database, meta, lu_prios,
        f'VARIOUS{srce_lu}', info_per_country, 'constant')
    database, info_per_country = prep.prep_lulucf(database, meta, lu_prios,
        f'VARIOUS{srce_lu}', info_per_country, 'linear')

# %%
# Write out the tables from database.

attrs = ['scen', 'srce', 'tablename']

for tablename in hpf.get_all_attributes_of_class(database):
    
    if 'COV' not in tablename:
        
        data = getattr(database, tablename)
        
        # Replace PRIMAPHIST/PMHSOCIOECO with PMH
        for attr in attrs:
            
            for tpe in ['emi', 'pop', 'gdp']:
                
                data.tablename = data.tablename.replace(getattr(meta.primap, tpe)['srce'], getattr(meta.primap, tpe)['srcepmh'])
                data.scen = data.scen.replace(getattr(meta.primap, tpe)['srce'], getattr(meta.primap, tpe)['srcepmh'])
                data.srce = data.srce.replace(getattr(meta.primap, tpe)['srce'], getattr(meta.primap, tpe)['srcepmh'])
        
        # Replace PRIMAPHIST and PMHSOCIOECO by PMH.
        
        data.tablename = data.tablename.replace('PRIMAPHIST', 'PMH')
        data.scen = data.scen.replace('PRIMAPHIST', 'PMH')
        data.srce = data.srce.replace('PRIMAPHIST', 'PMH')
        data.tablename = data.tablename.replace('PMHSOCIOECO', 'PMH')
        data.scen = data.scen.replace('PMHSOCIOECO', 'PMH')
        data.srce = data.srce.replace('PMHSOCIOECO', 'PMH')
        
        # Include the PRIMAP-hist version in the SSP names.
        
        data.tablename = data.tablename.replace('PMSSP', 'SSP')
        data.scen = data.scen.replace('PMSSP', 'SSP')
        data.srce = data.srce.replace('PMSSP', 'SSP')
        
        if 'SSP' in tablename:
            
            data.tablename = data.tablename.replace('SSP', f'{meta.primap.current_primap}SSP')
            data.scen = data.scen.replace('SSP', f'{meta.primap.current_primap}SSP')
            data.srce = data.srce.replace('SSP', f'{meta.primap.current_primap}SSP')
        
        for attr in ['family', 'ent', 'cat', 'clss', 'tpe', 'srce', 'scen', 'tablename']:
            
            if attr not in hpf.get_all_attributes_of_class(data):
            
                print(f"Missing attribute '{attr}' for {tablename}")
        
        if meta.gwps.default in data.ent:
            
            print(f"GWP in ent for {tablename}")
        
        hpf.write_table_from_class_metadata_country_year_matrix(
            data, path_tables)

# Write out info_per_country.
info_per_country.to_csv(Path(meta.path.preprocess, 'info_per_country.csv'))

# %%