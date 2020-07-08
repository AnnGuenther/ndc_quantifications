# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020
"""

# %%
import pandas as pd
from pathlib import Path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
"""
Global bunkers fuels.
"""

meta = setup_metadata()

# First three: shipping. Last: aviation.
files = ['CO2AR4_CM5_TOTAL_NET_SSP370BLAIMCGE_SSPC6BUNK.csv',
         'CH4AR4_CM5_TOTAL_NET_SSP370BLAIMCGE_SSPC6BUNK.csv',
         'N2OAR4_CM5_TOTAL_NET_SSP370BLAIMCGE_SSPC6BUNK.csv',
         'CO2AR4_CM4_TOTAL_NET_SSP370BLAIMCGE_SSPC6BUNK.csv']

bunkers = 0.
year = 2017
bunkers_ts = pd.Series(dtype='float64')
for file in files:
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.matlab, file)).data
    bunkers += table.loc[:, year].reindex(index=['EARTH']).values[0]
    bunkers_ts = bunkers_ts.add(table, fill_value=0)

print(f"Bunker fuels emissions in {year}: {bunkers} MtCO2eq")

bunkers_table = hpf.create_table(
    data=bunkers_ts, ent='KYOTOGHG', cat='BUNKERS', clss='TOTAL', tpe='NET',
    scen='SSP370BLAIMCGE', srce='SSPC6BUNK', gwp='AR4', unit='MtCO2eq',
    note=f"Sum over {', '.join(files)}.")
bunkers_table.__tablename_to_standard__()
hpf.write_table_from_class_metadata_country_year_matrix(bunkers_table, 
    Path(meta.path.main, 'data', 'other'))

# %%