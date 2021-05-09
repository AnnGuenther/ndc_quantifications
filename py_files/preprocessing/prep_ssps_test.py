# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""

# %%
def prep_ssps_test(database, meta, primap):
    
    """
    Check if the SSPs (KYOTOGHG_IPCM0EL per SSP scenario) are consistent with the given PRIMAP-hist data.
    Only gives out a warning if not.
    Only tests the 'main' data (kyotoghg_ipcm0el, pop and gdp).
    """
    
    # %%
    import sys
    import helpers_functions as hpf
    
    # %%    
    # Are there countries for which differences exceed 0.1%?
    for ssp in meta.ssps.scens.long:
        
        for tpe in ['emi', 'pop', 'gdp']:
            
            ssps_info = getattr(meta.ssps, tpe)
            ssp_table = hpf.copy_table(getattr(database, 
                '_'.join([ssps_info['ent'] + (meta.gwps.default if tpe == 'emi' else ''), 
                ssps_info['cat'], ssps_info['clss'], ssps_info['tpe'], ssp, ssps_info['srce']]))). \
                __reindex__(years=primap[tpe].columns.to_list()).data
            
            test = hpf.ratios_w_zeros(100. * ssp_table.add(-primap[tpe], fill_value=0), ssp_table, dtype='pd.DataFrame').abs()
            test = test.index[test[test > .1].any(axis=1)]
            
            if len(test) > 0:
                sys.exit("preprocessing.py: the difference between the new SSP data and the original SSP data is too high.")
    
# %%