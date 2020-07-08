# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""

# %%
def prep_chose_covered_gases_and_sectors_if_wanted(meta, coverage, txt_for_logfile):
    
    """
    You can chose to setup your own coverage.used_per_gas_per_sec.
    If you do so, write out a file to say what you have chosen!!!
    
    E.g. put all Energy and CO2 to covered ('YES'), and the rest to 'NO'.
    Or: all ANNEX-I parties cover everything, and the rest only Energy and CO2.
    """
    
    # %%
    from copy import deepcopy
    import pandas as pd
    from pathlib import Path
    import helpers_functions as hpf
    
    # %%
    txt_for_logfile += (
        "\n### Coverage used in this preprocessing"
        "\nThe coverage used in this preprocessing is not based on the 'real' coverage provided by NDCs." +
        "\nOnly Energy and CO2 are covered, for all countries.")
    
    # %%
    # e.g. put all Energy and CO2 to covered ('YES'), and the rest to 'NO'.
    # Set all to 'NO', and then Energy & CO2 to 'YES'.
    #coverage.used_per_gas_per_sec.loc[:, :] = 'NO'
    #coverage.used_per_gas_per_sec.loc[:, ['ENERGY', 'CO2']] = 'YES'
    
    # %%
    # or: all ANNEX-I parties cover everything, and the rest only Energy and CO2.
    ctrs = hpf.get_isos_for_groups(['ANNEXI'], 'ISO3')
    if 'EU28' in ctrs:
        ctrs = sorted(set(ctrs + meta.isos.EU28))
        ctrs.remove('EU28')
    
    ctrs = [xx for xx in ctrs if xx in meta.isos.EARTH]
    
    # Set all to 'NO', and then Energy & CO2 to 'YES'. And then everything for 'ctrs' to 'YES'.
    coverage.used_per_gas_per_sec.loc[:, :] = 'NO'
    coverage.used_per_gase_per_sec.loc[:, ['ENERGY', 'CO2']] = 'YES'
    coverage.used_per_gase_per_sec.loc[ctrs, :] = 'YES'
    
    # %%
    for iso3 in meta.isos.EARTH:
        
        info_cov = coverage.used_per_gas_per_sec.loc[iso3, :]
        
        # For all the combis between gas and category define whether they are covered or not (YES / NO):
        for check_combi in meta.combis_gas_cat:
            
            check_gas, check_cat = check_combi.split('_')
            
            # combis_used.
            if 'NO' in list(info_cov[[check_gas, meta.categories.main.cat_to_sec[check_cat]]]):
                coverage.used_per_combi.loc[iso3, check_combi] = 'NO'
            else:
                coverage.used_per_combi.loc[iso3, check_combi] = 'YES'
            
            # combis_orig.
            cov_orig_case = [coverage.orig_per_gas_per_sec.loc[iso3, check_gas], 
                        coverage.orig_per_gas_per_sec.loc[iso3, meta.categories.main.cat_to_sec[check_cat]]]
            if cov_orig_case == ['YES', 'YES']:
                coverage.orig_per_combi.loc[iso3, check_combi] = 'YES'
            elif cov_orig_case == ['NO', 'NO']:
                coverage.orig_per_combi.loc[iso3, check_combi] = 'NO'
            elif cov_orig_case == ['NAN', 'NAN']:
                coverage.orig_per_combi.loc[iso3, check_combi] = 'NAN'
            else:
                coverage.orig_per_combi.loc[iso3, check_combi] = '/'.join(cov_orig_case)
    
    # Write out data.
    # Replace the sectors by categories.
    cov_used_cols = deepcopy(coverage.used_per_gas_per_sec)
    cov_used_cols.columns = [meta.sectors.main.sec_to_cat[xx] 
        if xx in meta.sectors.main.sec_to_cat.keys() else xx for xx in cov_used_cols.columns]
    pd.concat([cov_used_cols, coverage.used_per_combi], axis=1). \
        to_csv(Path(meta.path.preprocess, 'coverage_used_per_gas_and_per_sector_and_combi.csv'))
    
    return coverage, txt_for_logfile

# %%
