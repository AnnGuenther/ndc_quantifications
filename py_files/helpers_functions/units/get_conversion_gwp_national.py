# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020
"""

# %%
def get_conversion_gwp_national(list_of_iso3s, gwp_from, gwp_to):
    
    """
    Calculate conversion factors for GWPs.
    Per country use the mean over 2010-2017 of PRIMAPHIST21 KYOTOGHG_IPCM0EL data.
    There is no data available for AR5. And for the FGASES we cannot simply convert it...
    """
    
    # %%
    import pandas as pd
    from pathlib import Path
    import os
    from setup_metadata import setup_metadata
    import helpers_functions as hpf
    
    # %%
    meta = setup_metadata()
    
    path_to_file = Path(meta.path.py_files, 'helpers_functions', 'units',
        'national_conversion_factors_gwp_ar2_ar4.csv')
    
    if not os.path.isfile(path_to_file):
        
        data = {}
        
        for gwp in ['AR2', 'AR4']:
            
            data[gwp] = hpf.import_table_to_class_metadata_country_year_matrix(
                Path(meta.path.matlab, f'KYOTOGHG{gwp}_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
                data.loc[:, range(2010, meta.primap.last_year+1)].mean(axis=1)
        
        factors = pd.DataFrame(index=meta.isos.EARTH)
        factors.loc[:, 'AR2_to_AR4'] = data['AR4'].div(data['AR2'])
        factors.loc[:, 'AR4_to_AR2'] = data['AR2'].div(data['AR4'])
        factors.to_csv(path_to_file)
    
    else:
        
        factors = pd.read_csv(path_to_file, index_col=0)
    
    gwp_from = ('AR2' if gwp_from == 'SAR' else gwp_from)
    gwp_to = ('AR2' if gwp_to == 'SAR' else gwp_to)
    
    return factors.loc[:, f"{gwp_from}_to_{gwp_to}"].reindex(index=list_of_iso3s)

# %%