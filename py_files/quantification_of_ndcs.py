# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
from warnings import warn
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%

meta = setup_metadata()
gwp_default = meta.gwps.default
database = hpf.create_class()

# %%
"""
Read in historical non-LULUCF emissions.
"""

def matlab_table(table):
    
    table.__attrs_primap_to_ndcs__()
    table.__tablename_to_standard__()
    table.__name_to_standard__()
    
    if table.unit != meta.units.default[table.family]:
        warn(f"Wrong unit for {table.code}!")
    
    if (table.family == 'emi' and table.gwp != meta.gwps.default):
        warn(f"Wrong GWP for {table.code}!")

primap_name = "_".join([meta.primap.emi[xx] for xx in ['clss', 'tpe', 'scen', 'srce']])

for cat in meta.categories.main.exclLU:
    
    for ent in (meta.gases.main if cat != 'IPC2' else meta.gases.kyotoghg):
        
        table = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.matlab, f"{ent}{gwp_default}_{cat}_" + primap_name + ".csv"))
        matlab_table(table)
        setattr(database, f"{ent}_{cat}", table)

ent, cat = f"KYOTOGHG{gwp_default}", "IPCM0EL"
table = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.matlab, f"{ent}{gwp_default}_{cat}_" + primap_name + ".csv"))
matlab_table(table)
setattr(database, f"{ent}_{cat}", table)

# %%
"""
Read in SSP emissions, population and GDP (PPP).
"""

for scen in meta.ssps.scens.long:
    
    cat = 'IPCM0EL'
    clss, tpe, srce = [meta.ssps.emi[xx] for xx in ['clss', 'tpe', 'srce']]
    
    for ent in meta.gases.main + ['FGASES']:
        
        table = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.matlab, f"{ent}{gwp_default}_{cat}_{clss}_{tpe}_{scen}_{srce}.csv"))
        matlab_table(table)
        setattr(database, f"{ent}_{cat}_{scen}", table)
    
    ent, cat = f"KYOTOGHG{gwp_default}", "IPCM0EL"
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.matlab, f"{ent}{gwp_default}_{cat}_" + primap_name + ".csv"))
    matlab_table(table)
    setattr(database, f"{ent}_{cat}_{scen}", table)
    
    for what in ['pop', 'gdp']:
        
        ent, cat, clss, tpe, srce = [getattr(meta.ssps, what)[xx] 
            for xx in ['ent', 'cat', 'clss', 'tpe', 'srce']]
        
        table = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.matlab, f"{ent}_{cat}_{clss}_{tpe}_{scen}_{srce}.csv"))
        matlab_table(table)
        setattr(database, f"{ent}_{cat}_{scen}", table)

# %%
"""
Read in LULUCF emissions.
"""

# %%
"""
NDC info from csv-file.
"""

hpf.get_infos_from_ndcs(meta)

# %%
"""
Fill SSPs.
"""

# %%
"""
Select and interpolate national LULUCF emissions.
"""

# %%
