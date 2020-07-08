# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
import pandas as pd
import os
from copy import deepcopy
from pathlib import Path
from time import gmtime, strftime

import helpers_functions as hpf
import preprocessing as prep
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

# Path to output-folders.
meta.date_time = strftime("%Y%m%d_%H%M", gmtime()) # Current date and time.
meta.path.pc_cov = Path(meta.path.preprocess, 'pc_cov_' + meta.date_time)

# Create folders.
Path(meta.path.pc_cov).mkdir(parents=True, exist_ok=True)

# How many years should be used when calculating the mean over the last available years.
nrvalues = 6

# Have one pd.DataFrame, where the per-country information on modified data / dataseries is put to.
# E.g., which LULUCF data are used, and which coverages were modified, etc.
info_per_country = pd.DataFrame(index=meta.isos.EARTH)

# Simply add needed columns on the go (info_per_country.loc[:, 'newcolumn'] = whatever).

# %% Read in tables from meta.path.preprocess/tables.

"""
Read in all datatables in folder meta.path.preprocess/tables.

All read into class 'database', with the tablenames as attributes.
The attributes are classes again, with attributes entity, category, 
data, family, etc. (see meta.nomenclature.attrs).
"""

print("Read in all datatables in folder preprocess/tables.")

database = hpf.create_table(name='database')
# All files in matlab_tables.
path_to_files = Path(meta.path.preprocess, 'tables')
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

# %% Covered part of emissions - matrix on covered gases / sectors.

# TODO: update the text where there are questionmarks.

"""
Calculate the part of historical emissions that is covered by an NDC.

- If the country does not have an (I)NDC: nothing is covered.
Else:
- Assessment based on PRIMAP-hist HISTCR emissions time series.
- Categories and gases assessed (per country):
  - Main categories (IPC1, IPC2, IPCMAG, IPC4 and IPC5; namely Energy, IPPU, Agriculture, Waste and Other; excludes LULUCF).
  - Kyoto GHGs: CO$_2$, CH$_4$, N$_2$O, HFCS, PFCS, SF$_6$, NF$_3$.
- For each of these categories / gases, the information on whether they are covered by the country's NDC is provided (csv-input, assessed by A. Günther).
- If no information is available for all gases: only CO$_2$ assumed to be covered (in the csv-file already?!).
- If no information is available for all sectors: only energy assumed to be covered. Case never happened.
- If any of HFCS, PFCS, SF6 or NF3 is covered, put IPPU to covered (F-gases only relevant in IPC2).
- If all sectors (IPC1, 2, MAG, 4) are covered ('YES'), the category "Other" (IPC5) is set to "YES" (in the csv-file already?!).
- For all category + gas combinations, the emissions are counted as covered, if neither the category nor the gas are assumed not to be covered (neither category nor gas can contain a "NO").

Here, matrices on the coverage (Yes: covered, No: not-covered) are created.

We do not include the information on the EU28, but put the information into each of the member-states.
"""

print("Covered part of emissions.")

infos_from_ndcs = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0)

coverage, info_per_country = prep.prep_coverage(meta, infos_from_ndcs, info_per_country)

#%% Chose different coverage if wanted.
"""
You can chose to setup your own coverage.used_per_gas_per_sec.
If you do so, write out a file to say what you have chosen!!!

E.g. put all Energy and CO2 to covered ('YES'), and the rest to 'NO'.
Or: all ANNEX-I parties cover everything, and the rest only Energy and CO2.
"""

#coverage, txt_for_logfile = \
#    prep.prep_chose_covered_gases_and_sectors_if_wanted(meta, coverage, txt_for_logfile)

# %% Covered part of historical emissions (KYOTOGHG_IPCM0EL).

"""
The covered part of emissions (in 'emissions') is calculated here for historical years, 
for which data per sector and gas combination are available.
The assessment is based on the information in coverage.used_per_combi (all entries are 'YES' or 'NO').
All combinations with 'YES' are summed up to emicov_his, and all combinations with 'NO' are summed up to eminotcov_his.

For KYOTOGHG_IPCM0EL, excluding LULUCF.
"""

print("    Historical (IPCM0EL)")

database, coverage = prep.prep_covered_emissions_his(database, coverage, meta, primap)

"""
Additionally calculate the historical emissions not-/covered for perGas_IPCM0EL and KYOTOGHG_perCategory.
These values are not needed in further calculations, but nice to have.
"""

database = prep.prep_covered_emissions_his_additional_data(meta, database, primap)

# %% Covered part of future emissions (KYOTOGHG_IPCM0EL).

# TODO: check the last option if it is still an issue.

"""
Calculate the part of future emissions covered by an NDC (KYOTOGHG_IPCM0EL)

- For countries that cover everything: set pccov_fut to 1 (100%).
- For countries that cover nothing: set pccov_fut to 0 (0%).
- For countries that cover all sectors (excl. LULUCF), but not all gases: 
    the SSP entity_IPCM0EL emissions per gas are used to calculate pc\_cov\_fut.
  - SSP data are available for KYOTOGHG, CO$_2$, CH$_4$, N$_2$O and FGASES:
    - For countries that cover only some FGASES, the \% share between HFCS, PFCS, 
        SF$_6$ and NF$_3$ is kept constant (at mean over last 6 available values).
    - The share per gas is applied to the future KYOTOGHG\_IPCM0EL emissions data.
- For countries that do not cover all sectors:
  - Calculate the slope of pc\_cov\_his (2010 to most recent year with available data ("mry")).
    - If abs(slope) < lim_slope: use the mean over 2010 to mry.
    - If abs(slope) > lim_slope: calculate pc\_cov\_fut from the correlation between emi\_tot\_his and emi\_cov\_his. For 2010 to mry.
        - If any(pc\_cov\_fut) > 90\%, but not all(pc\_cov\_fut) > 90\% --> set the pc\_cov\_fut > 90\% to 90\%.
        - If any(pc\_cov\_fut) < 10\%, but not all(pc\_cov\_fut) < 10\% --> set the pc\_cov\_fut < 10\% to 10\%.
        - Set min(pc\_cov\_fut) to 0\% and max(pc\_cov\_fut) to 100\%.
- If no future emissions data are available: use the mean over 2010 to mry?!

The future emicov / pccov values depend on the chosen SSP scenario.

One can give a preference for the calculation method of pccov_fut.
preference_pccov_fut can be 'mean' or 'corr'.

'mean':
    Check for the countries for which the slope of a regression to the last available 
    years of pccov_his is less than slope_lim.
    Use the mean over the years as pccov_fut.
    For the others check the correlation between emitot and emicov and decide 
    whether to better use this correlation for pccov_fut.
'corr':
    Take the correlation between emitot and emicov, unless it is too 'bad', then take the mean.
"""

print("    Future (IPCM0EL)")

#preference_pccov_fut = 'mean'
preference_pccov_fut = 'corr'

first_year_for_slope = 2010
slope_lim = 1./100. 
rvalue_lim = .85

hpf.write_text_to_file(f"preference\_pccov\_fut is set to {preference_pccov_fut}\n" +
    f"first\_year\_for\_slope is set to {first_year_for_slope}\n" +
    f"slope\_lim is set to {slope_lim}\n" +
    f"rvalue\_lim is set to {rvalue_lim}",
    Path(meta.path.pc_cov, 'preference_pc_cov_fut.md'))

database, info_per_country, coverage = \
    prep.prep_covered_emissions_fut(database, meta, coverage, info_per_country, preference_pccov_fut, primap,
    first_year_for_slope, slope_lim, rvalue_lim)

"""
Also calculate the pc_cov_fut using the growth rates of the last available historical years
per gas+sector combi.
"""

# Results aren't great:
#database, info_per_country, coverage = \
#    prep.prep_covered_emissions_fut_by_growth(database, meta, coverage, info_per_country, primap,
#    first_year_for_slope)

# %%
"""
Calculate LULUCF emissions covered by an NDC.

Based on KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTEREXTRAPOL_VARIOUS emissions time series (1990 - 2050).
If LULUCF and CO$_2$ are not "NO", put KYOTOGHG_IPCMLULUCF to covered. Ignoring the information on CH4 and N2O.
"""

#database = prep.prep_lulucf_covered_emissions(database, coverage, 'constant')
#database = prep.prep_lulucf_covered_emissions(database, coverage, 'linear')

# %%
# Write out the tables including 'COV' from database.
for tablename in hpf.get_all_attributes_of_class(database):
    
    if 'COV' in tablename:
        hpf.write_table_from_class_metadata_country_year_matrix(
            getattr(database, tablename), meta.path.pc_cov)

# %%
info_per_country.to_csv(Path(meta.path.pc_cov, 'info_per_country_pccov.csv'))

print("##### UPDATE the current pc_cov-folder to " + str(meta.path.pc_cov) + 
      " in setup_metadata.py (if this pc_cov should be used)! #####")

# %%