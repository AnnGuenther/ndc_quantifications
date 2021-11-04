# -*- coding: utf-8 -*-
"""
Author: Annika Günther
Last update in 03/2020.
"""

# %%
"""
Global share of emissions per sector, per gas, and per combination of sector and gas.
For PRIMAP-hist.
"""

# %%
import pandas as pd
from pathlib import Path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
def calc_share():
    
    path_file = Path(meta.path.matlab, '_'.join([gas, cat, 'TOTAL', 'NET', 'HISTCR',
        meta.primap.current_version['emi']]) + '.csv')
    
    if path_file.exists():
        table = hpf.import_table_to_class_metadata_country_year_matrix(path_file)
        
        output.loc[:, table.entity + '_' + table.category] = \
            100 * table.__global_share__(isos=meta.isos.EARTH, years=year)
    
    return output

# %%
# Get metadata.
meta = setup_metadata()

for year in [2017]:
    
    # Setup output DataFrame.
    output = pd.DataFrame(index=meta.isos.EARTH, dtype='float64')
    
    # Get the global share for 2017 per gas (F-gases as one).
    for gas in [xx + 'AR4' for xx in meta.gases.kyotoghg] + ['FGASESAR4', 'KYOTOGHGAR4']:
        cat = 'IPCM0EL'
        output = calc_share()
    
    # Get the global share for 2017 per category.
    for cat in meta.categories.main.exclLU:
        gas = 'KYOTOGHGAR4'
        output = calc_share()
    
    # Get the global share for 2017 per gas + category combination.
    for gas in [xx + 'AR4' for xx in meta.gases.kyotoghg] + ['FGASESAR4', 'KYOTOGHGAR4']:
        for cat in meta.categories.main.exclLU:
            output = calc_share()
    
    output.index.name = f"{year}_MtCO2eq_AR4"
    
    # Write out the data.
    output.to_csv(Path(meta.path.main, 'data', 'other', 'global_share_per_gas_and_sector_' + 
        meta.primap.current_version['emi'] + '_HISTCR_' + str(year) + '.csv'))

# %%
