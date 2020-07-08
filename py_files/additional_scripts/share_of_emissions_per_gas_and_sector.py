# -*- coding: utf-8 -*-
"""
Author: Annika Günther
Last update in 05/2020.
"""

# %%
"""
Global share of emissions per sector, per gas, and per combination of sector and gas.
Share compared to EARTH KYOTOGHG_IPCM0EL.
For PRIMAP-hist.
"""

# %%
import pandas as pd
from pathlib import Path
from warnings import warn
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def get_table(path_to_file, unit, gwp, meta):
    # Get table and convert the units.
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        path_to_file)
    
    table.ent = table.entity.replace('AR4', '')
    table.cat = table.category
    table.__convert_unit__(unit, entity=table.ent, gwp=gwp)
    
    table.__reindex__(isos=meta.isos.EARTH)
    
    table.data.loc['EARTH', :] = table.data.reindex(index=meta.isos.EARTH).sum(axis=0)
    table.data.loc['EU28', :] = table.data.reindex(index=meta.isos.EU28).sum(axis=0)
    
    return table
    
# %%
def calc_share(gas, cat, meta, output, unit, gwp, table_tot_act, year):
    
    path_to_file = Path(meta.path.matlab, '_'.join([gas, cat, 'TOTAL', 'NET', 'HISTCR',
        meta.primap.current_version['emi']]) + '.csv')
    
    if path_to_file.exists():
        table = get_table(path_to_file, unit, gwp, meta)
        
        share = 100 * table.data.reindex(index=meta.isos.EARTH + ['EARTH', 'EU28']).reindex(columns=[year]).div(table_tot_act)
        
        output.loc[share.index, table.ent + '_' + table.cat] = share.loc[:, year]
    
    return output

# %%
# Get metadata.
meta = setup_metadata()

unit, gwp = 'MtCO2eq', 'AR4'

# Get the total emissions.
path_to_file=Path(meta.path.matlab, 'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_' + 
    meta.primap.current_version['emi'] + '.csv')
table_tot = get_table(path_to_file, unit, gwp, meta).data

for year in [2017]:
    
    # Setup output DataFrame.
    output = pd.DataFrame(index=meta.isos.EARTH + ['EU28', 'EARTH'], dtype='float64')
    
    table_tot_act = table_tot.reindex(index=meta.isos.EARTH).reindex(columns=[year]).sum()
    
    # Get the 'national' share for 2017 per gas.
    cat = 'IPCM0EL'
    for gas in [xx + 'AR4' for xx in meta.gases.kyotoghg] + ['FGASESAR4', 'KYOTOGHGAR4']:
        output = calc_share(gas, cat, meta, output, unit, gwp, table_tot_act, year)
    
    # Get the global share for 2017 per category.
    gas = 'KYOTOGHGAR4'
    for cat in meta.categories.main.exclLU:
        output = calc_share(gas, cat, meta, output, unit, gwp, table_tot_act, year)
    
    for gas in [xx + 'AR4' for xx in meta.gases.kyotoghg] + ['FGASESAR4', 'KYOTOGHGAR4']:
        for cat in meta.categories.main.exclLU:
            output = calc_share(gas, cat, meta, output, unit, gwp, table_tot_act, year)
    
    test = output.loc[meta.isos.EARTH, [xx for xx in output.columns 
        if not ('FGASES' in xx or 'KYOTOGHG' in xx or 'IPCM0EL' in xx)]].sum().sum()
    if abs(100 - test) > 1e-4:
        warn("something went wrong (test).")
    
    output.index.name = f"{year}_MtCO2eq_AR4"
    
    # Write out the data.
    output.to_csv(Path(meta.path.main, 'data', 'other', 'share_per_gas_and_sector_' + 
        meta.primap.current_version['emi'] + '_HISTCR_' + str(year) + '.csv'))
    
# %%