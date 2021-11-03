# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2021

03/2021: moved the NDC-specific parts from preprocessing_general.py to here.
"""

# %%
"""
**Preprocessing to calculate the part of emissions covered by national mitigation targets.**
"""

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
meta.path.pc_cov = Path(meta.path.preprocess, 
    f'pc_cov_{meta.date_time}_SMD{meta.ndcs.submissions_until}_{meta.primap.current_primap}')

# Create folders.
Path(meta.path.pc_cov).mkdir(parents=True, exist_ok=True)

# Have one pd.DataFrame, where the per-country information on modified data / dataseries is put to.
# E.g., which LULUCF data are used, and which coverages were modified, etc.
# Simply add needed columns on the go (info_per_country.loc[:, 'newcolumn'] = whatever).
info_per_country = pd.DataFrame(index=meta.isos.EARTH)

# %%

"""
Load and write out *information retrieved from NDCs* to ``ndcs_info.csv`` into folder 
meta.path.pc_cov.
Includes information on Parties' target types, years, conditionality, range, coverage.
Takes into account targets up to a certain given submission date (meta.ndcs.submissions_until).
"""
infos_from_ndcs = hpf.get_infos_from_ndcs(meta)

"""
Get the emission data that were retrieved from the NDCs and write them to csv-files.
"""
_ = hpf.get_infos_from_ndcs_emi(meta)

# %%
# Moved here from preprocessing_general.py (03/2021)

"""
*Create NDC exclLU pathways.*

*Use PRIMAP-hist v2.1 HISTCR up to 2017 and then use given ndcs_emi['exclLU'] when available, 
with linear interpolation between values.*
*These pathways are used for type_reclass when creating the mitigated pathways (growth rates),
and when calculating the targets for countries without ABS as type_reclass.*

*For the countries without exclLU values check if they have inclLU values.*
*If so use the onlyLU data from the NDC (or other options, as used in the NDC quantifications) 
to derive exclLU emissions.*
*Use the given inclLU values and the corresponding onlyLU values to derive exclLU, 
and then interpolate linearly between them (again, with PRIMAP-hist for KYOTOGHG_IPCM0EL up to 2017).*
"""
ndcs_emi = {}

for what in ['exclLU', 'inclLU', 'onlyLU']:
    
    ndcs_emi[what] = pd.read_csv(Path(meta.path.pc_cov,
        f"infos_from_ndcs_emi_{what}_{meta.units.default['emi']}_{meta.gwps.default}_SMD{meta.ndcs.submissions_until}.csv"), index_col=0)
    ndcs_emi[what].columns = [int(xx) for xx in ndcs_emi[what].columns]

yrs_fut = list(range(meta.primap.last_year+1, 2051))
yrs_primap = list(range(1990, meta.primap.last_year+1))

path_tables = Path(meta.path.preprocess, f'tables_{meta.primap.current_primap}')

txt = ''

plot_data = False

fig = plt.figure(figsize=(7, 7))

for ssp in meta.ssps.scens.long:
    
    # onlyLU.
    for lu_table in ['', 'FAO', 'UNFCCC']:
        
        """
        EMI onlyLU.
        """
        
        tablename_onlyLU = f'KYOTOGHG{meta.gwps.default}_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS{lu_table}'
        table_onlyLU = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(path_tables, f'{tablename_onlyLU}.csv'))
        table_onlyLU.data = table_onlyLU.data.reindex(index=meta.isos.EARTH)
        
        # exclLU
        tablename_exclLU = f'KYOTOGHG{meta.gwps.default}_IPCM0EL_TOTAL_NET_' \
            f'{meta.primap.current_primap}{ssp}FILLED_{meta.primap.current_primap}SSPBIE'
        table_exclLU = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(path_tables, f'{tablename_exclLU}.csv'))
        table_exclLU.data = table_exclLU.data.reindex(index=meta.isos.EARTH)
        
        for iso3 in meta.isos.EARTH:
            
            ndc_onlyLU_act = ndcs_emi['onlyLU'].loc[iso3, :]
            ndc_inclLU_act = ndcs_emi['inclLU'].loc[iso3, :]
            ndc_exclLU_act = ndcs_emi['exclLU'].loc[iso3, :]
            
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
            If there are onlyLU values available for 2010 or later, use them for 
            constant extrapolation (use their average) if no future values are available.
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
            bl_onlyLU can have missing values before 2018 (and is nan if all values in 2010-2017 are nan).
            It is constantly the average of 2010-2017 for years > 2017.
            """
            
            """
            EMI exclLU.
            
            Check if there is exclLU data available from the NDC for years > 2017.
            If so, use them with linear interpolation from PRIMAP-hist to the first year, and inbetween.
            After last year: use SSP growth rates.
            
            - If ndc_exclLU available: use ndc_exclLU.
            - If ndc_inclLU available: use ndc_inclLU - onlyLU.
            - Else: use external_exclLU.
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
        setattr(table_onlyLU, 'scen', f'NDC{meta.primap.current_primap}{ssp}')
        setattr(table_onlyLU, 'srce', f'NDC{meta.primap.current_primap}SSPBIE{lu_table}')
        setattr(table_onlyLU, 'note', getattr(table_onlyLU, 'note') + 
                ' For countries without emissions provided in the NDC but with inclLU emissions provided, ' +
                'the onlyLU emissions were calculated based on NDC_inclLU minus SSP_exclLU. ' +
                f'For countries without emissions provided in the NDC the {tablename_onlyLU} values are used.')
        table_onlyLU.__tablename_to_standard__()
        table_onlyLU.__name_to_standard__()
        hpf.write_table_from_class_metadata_country_year_matrix(table_onlyLU,
            meta.path.pc_cov)
        
        setattr(table_exclLU, 'cat', 'IPCM0EL')
        setattr(table_exclLU, 'scen', f'NDC{meta.primap.current_primap}{ssp}')
        setattr(table_exclLU, 'srce', f'NDC{meta.primap.current_primap}SSPBIE{lu_table}')
        setattr(table_exclLU, 'note', getattr(table_exclLU, 'note') + 
                ' For countries without emissions provided in the NDC but with inclLU emissions provided, ' +
                'the exclLU emissions were calculated based on NDC_inclLU minus {table_onlyLU.tablename}. ' +
                f'For countries without emissions provided in the NDC the {tablename_exclLU} values are used.')
        table_exclLU.__tablename_to_standard__()
        table_exclLU.__name_to_standard__()
        hpf.write_table_from_class_metadata_country_year_matrix(table_exclLU,
            meta.path.pc_cov)

plt.close(fig)
hpf.write_text_to_file(txt, Path(meta.path.pc_cov, 'info_onlyLU_exclLU_fromNDCs.txt'))

# %% Read in tables from meta.path.preprocess/tables.

"""
Read in all datatables in folder meta.path.preprocess/tables_PMHxx.

All read into class 'database', with the tablenames as attributes.
The meta-data are classes again, with attributes entity, category, data, unit, etc. 
(see meta.nomenclature.attrs).
"""

print("Read in all datatables in folder preprocess/tables_PMHxx.")

database = hpf.create_table(name='database')

# All files in matlab_tables.
path_to_files = Path(meta.path.preprocess, f'tables_{meta.primap.current_primap}')
files = os.listdir(path_to_files)

for file in files:
    
    if file.endswith('.csv'):
        
        database = prep.prep_read_in_tables(file, path_to_files, database, meta)

# %%
# Get PRIMAP emissions for KYOTOGHG_IPCM0EL, POP and GDPPPP. For easier use.

primap = {}

meta.primap.emi['ent'] = meta.primap.emi['ent'] + meta.gwps.default

for tpe in ['emi', 'pop', 'gdp']:
    
    primap[tpe] =  deepcopy(getattr(database, '_'.join([getattr(meta.primap, tpe)[xx] 
        for xx in ['ent', 'cat', 'clss', 'tpe', 'scen', 'srce']]).
        replace(getattr(meta.primap, tpe)['srce'], getattr(meta.primap, tpe)['srcepmh'])).data)

# %% Covered part of emissions - matrix on covered gases / sectors.

# TODO: update the text where there are questionmarks.

"""
*Calculate the part of historical emissions that is covered by an NDC.*

*If the country does not have an (I)NDC: nothing is covered.*

Else:

- Assessment based on *PRIMAP-hist HISTCR* emissions time series.
- Categories and gases assessed (per country):
  
  - *Main categories* (IPC1, IPC2, IPCMAG, IPC4 and IPC5; namely Energy, IPPU, Agriculture, Waste and Other; excludes LULUCF).
  - *Kyoto GHGs*: CO2, CH4, N2O, HFCS, PFCS, SF6, NF3.

- For each of these categories / gases, the information on whether they are covered by the country's NDC is provided (csv-input, assessed by A. Günther).
- If *no information is available for all gases: CO2, CH4, and N2O are assumed to be covered* (in the csv-file already).
- If *any of HFCS, PFCS, SF6 or NF3 is covered, put IPPU to covered* (F-gases only relevant in IPC2).
- If *all sectors (IPC1, 2, MAG, 4) are covered, the category "Other" (IPC5) is set to "YES"* (in the csv-file already).
- For *all category + gas combinations*, the *emissions are counted as covered, if neither the category nor the gas are assumed not to be covered* (neither category nor gas can contain a "NO").

Here, matrices on the coverage (Yes: covered, No: not-covered) are created.

We do not include the information on the EU, but put the information into each of the member-states.
"""

print("Covered part of emissions.")

infos_from_ndcs = pd.read_csv(Path(meta.path.pc_cov, f'infos_from_ndcs_SMD{meta.ndcs.submissions_until}.csv'), index_col=0)

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
The covered part of emissions (in 'emissions') is calculated here for *historical years, for which data per sector and gas combination are available*.
The assessment is based on the information in coverage.used_per_combi (all entries are already 'YES' or 'NO', no 'NAN' entries).
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
Calculate the part of *future emissions covered by an NDC (KYOTOGHG_IPCM0EL)*

- For countries that *cover everything: set pccov_fut to 1 (100%)*.
- For countries that *cover nothing: set pccov_fut to 0 (0%)*.
- For countries that *cover all sectors (excl. LULUCF), but not all gases:* 
    the *SSP entity_IPCM0EL emissions per gas are used to calculate pc\_cov\_fut.*
  
    - SSP data are available for KYOTOGHG, CO2, CH4, N2O and FGASES:

        - For *countries that cover only some FGASES, the \% share between HFCS, PFCS, SF6 and NF3 is kept constant* (at mean over last 6 available PRIMAP-hist values).
        - The share per gas is applied to the future KYOTOGHG\_IPCM0EL emissions data.

- For countries that do *not cover all sectors*:
    
    - Calculate the *slope of pc\_cov\_his* (2010 to most recent year with available data ("mry")).
        
        - If *abs(slope) < lim_slope: use the mean over 2010 to mry*.
        - If *abs(slope) > lim_slope: calculate pc\_cov\_fut from the correlation between emi\_tot\_his and emi\_cov\_his. For 2010 to mry.*
            
            - If any(pc\_cov\_fut) > 90\%, but not all(pc\_cov\_fut) > 90\% --> set the pc\_cov\_fut > 90\% to 90\%.
            - If any(pc\_cov\_fut) < 10\%, but not all(pc\_cov\_fut) < 10\% --> set the pc\_cov\_fut < 10\% to 10\%.
            - If any(pc\_cov\_fut) > 100\% or < 0\% use the mean instead.

- If no future emissions data are available: use the mean over 2010 to mry.

The future emicov / pccov values depend on the chosen SSP scenario.

One can give a *preference for the calculation method of pccov_fut.
preference_pccov_fut can be 'mean' or 'corr'.*

'mean':
    Check for the countries for which the slope of a regression to the last available years of pccov_his is less than slope_lim.
    Use the mean over the years as pccov_fut.
    For the others check the correlation between emitot and emicov and decide whether to better use this correlation for pccov_fut.
'corr':
    Take the correlation between emitot and emicov, unless it is too 'bad', then take the mean.

Default: 'corr'.
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

# Also calculate the pc_cov_fut using the growth rates of the last available historical years
# per gas+sector combi.
# Results are not great ...

# Results aren't great:
#database, info_per_country, coverage = \
#    prep.prep_covered_emissions_fut_by_growth(database, meta, coverage, info_per_country, primap,
#    first_year_for_slope)

# %%
# Calculate LULUCF emissions covered by an NDC.

# Based on KYOTOGHG_IPCMLULUCF_INTEREXTRAPOL_VARIOUS emissions time series (1990 - 2050).
# If LULUCF and CO$_2$ are not "NO", put KYOTOGHG_IPCMLULUCF to covered. Ignoring the information on CH4 and N2O.

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

"""
**Update the current pc_cov-folder in setup_metadata after running preprocessing_current_pc_cov.py.**
"""

# %%