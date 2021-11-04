# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
def get_isos_earth_only_independent():
        
    # %%
    import os
    from pathlib import Path
    from helpers_functions.import_export.read_text_from_file import read_text_from_file
    
    # %%
    path_file = Path(os.path.dirname(os.path.realpath(__file__)), 'iso3_EARTH_exclEU28_exclDependent.csv')
    isos = read_text_from_file(path_file).split(',\n')
    
    return sorted(isos)
    
#enddef

# %% Based on:
"""
# ISO3s of EARTH and EU28.
EARTH = sorted(hpf.get_isos_for_groups('EARTH', 'ISO3'))
EU28 = sorted(hpf.get_isos_for_groups('EU28', 'ISO3'))
# ISO3s of data included in other ISO3 data (PRIMAPHIST, non-independent data):
no_independent_data = [
    'NFK', 'CXR', 'CCK', 'HMD', 'FRO', 'GRL', 'PSE', 
    'BLM', 'GLP', 'GUF', 'MAF', 'MTQ', 'MYT', 'NCL', 'PYF', 'REU', 'SPM', 
    'WLF', 'ATF', 'ALA', 'ESH', 'SJM', 'BMU', 'CYM', 'FLK', 'GIB', 
    'GGY', 'IMN', 'JEY', 'GUM', 'MNP', 'PRI', 'ASM', 'VIR']

# All EARTH isos, excluding the no_independent_data and excluding 'EU28' (but with single EU countries).
independent_data_exclEU28 = sorted(set(set(EARTH) - set(no_independent_data)))

# Write out isos.
hpf.write_text_to_file(',\n'.join(independent_data_exclEU28),
    Path(what_ever_path, 'iso3_EARTH_exclEU28_exclDependent.csv'))
"""

# %%
