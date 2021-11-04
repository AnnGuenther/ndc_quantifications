# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2021.

03/2021:
    store info in preprocess/pc_cov* instead of preprocess, as it depends on the NDCs.
04/2021:
    for submissions between 20201212 and 20201218: difficulty as GBR submitted on the 20201212,
    but EU27 submitted on the 20201218. So during these few days still use EU28 incl. GBR, and 
    not the separate GBR target information. No real change needed in code, as the routine
    already put the EU28 info into GBR if the meta.ndcs.submissions_until is earlier than
    20201218.
"""

# %%
def get_infos_from_ndcs(meta, **kwargs):
    """
    Gets information from meta.ndcs.path_to_infos_from_ndcs and writes out the important information to
    'ndcs_info.csv' in meta.path.pc_cov.
    Uses the submissions before a certain submission date (meta.ndcs.submissions_until)
    
    INPUT: meta
    kwargs:
        write_out_data (if False nothing is written out)
        get_all_rows (if True not only the ones ending with .mod are used)
    """
    # %%
    import pandas as pd
    import numpy as np
    import json
    from pathlib import Path

    # %%
    # Get information from NDCs (only the rows with ".mod" in the name):
    infos_from_ndcs = pd.read_excel(meta.ndcs.path_to_infos_from_ndcs, 
        sheet_name='Overview', index_col=0, header=None).astype('str')
    
    # Only keep the rows ending with ".mod"
    if 'get_all_rows' in kwargs.keys():
        
        get_all_rows = kwargs['get_all_rows']
        
        if get_all_rows not in [True, False]:
            
            print("The given value for get_all_rows is not supported and only rows ending with .mod are used.")
            get_all_rows = False
    
    else:
        get_all_rows = False
    
    if not get_all_rows:
        infos_from_ndcs = infos_from_ndcs.loc[[xx for xx in infos_from_ndcs.index 
            if (type(xx) == str and '.mod' in xx)], :]
    
    infos_from_ndcs.index = [xx.replace('.mod', '').upper() for xx in infos_from_ndcs.index]
    
    # Check for the base year entries to be integers or NaN. Will give an error if it cannot be converted to int.
    infos_from_ndcs.loc['BASEYEAR', :] = [int(xx) if xx != 'nan' else np.nan for xx in infos_from_ndcs.loc['BASEYEAR', :]]
    
    # Only use the entries (per country) before a certain submission date (meta.ndcs.submissions_until).
    use_cols = []
    
    # Don't use the 'wrong' EU (keep EU28 for meta.ndcs.submissions_until < submission of second NDC that is for EU27):
    for iso3 in set(set(infos_from_ndcs.loc['ISO3', :].unique()) - set([xx for xx in meta.EUs if xx != meta.EU])):
        
        cols = [
            xx 
            for xx in infos_from_ndcs.loc[:, infos_from_ndcs.columns[infos_from_ndcs.loc['ISO3'] == iso3]].columns 
            if int(infos_from_ndcs.loc['SUBMISSION_DATE', xx]) <= meta.ndcs.submissions_until]
        use_cols += [infos_from_ndcs.loc['SUBMISSION_DATE', cols].sort_values().index[-1]]
    
    infos_from_ndcs = infos_from_ndcs.loc[:, use_cols]
    
    # ISO3s as index.
    infos_from_ndcs.columns = infos_from_ndcs.loc['ISO3', :]
    infos_from_ndcs = infos_from_ndcs.reindex(columns=meta.isos.EARTH_EU)
    infos_from_ndcs.drop(index=['ISO3'], inplace=True)
    infos_from_ndcs = infos_from_ndcs.transpose()
    
    # Use EU information for all EU countries.
    cols = list(set(set(infos_from_ndcs.columns) - set(['ISO2', 'COUNTRYNAME'])))
    # For EU28 it will use the EU info for GBR as well, so it is not a real problem
    # that the GBR NDC was submitted on the 20201212, and the EU27 NDC only on the
    # 20201218.
    infos_from_ndcs.loc[meta.isos.EU, cols] = infos_from_ndcs.loc[meta.EU, cols].values
    
    """
    Replace the information on coverage by single entries.
    Replace the information on targets by single entries.
    """
    # Coverage
    sectors = ['ENERGY', 'IPPU', 'AGRICULTURE', 'LULUCF', 'WASTE', 'OTHER']
    gases = ['CO2', 'CH4', 'N2O', 'HFCS', 'PFCS', 'SF6', 'NF3']
    
    for what, name, ents in \
        ['COVERAGE_SECTORS_NDCS', 'NDCS', sectors], \
        ['COVERAGE_SECTORS_CALC', 'CALC', sectors], \
        ['COVERAGE_GASES_NDCS', 'NDCS', gases], \
        ['COVERAGE_GASES_CALC', 'CALC', gases]:
        
        for col in ents:
            
            infos_from_ndcs.loc[:, f"{col}_{name}"] = 'NAN'
        
        for iso3 in infos_from_ndcs.index:
            
            cov_act = infos_from_ndcs.loc[iso3, what]
            
            if (type(cov_act) == str and cov_act.upper() != 'NAN'):
                
                cov_json = json.loads(cov_act)
                
                for case in cov_json.keys():
                    
                    infos_from_ndcs.loc[iso3, [f"{xx.upper()}_{name}" for xx in cov_json[case]]] = case
    
    # Targets
    targets = [xx for xx in meta.ndcs.types if xx != 'NGT']
    
    for col in targets:
        
        infos_from_ndcs.loc[:, col] = np.nan
    
    for iso3 in infos_from_ndcs.index:
        
        tars_act = infos_from_ndcs.loc[iso3, 'TARGETS']
        
        if (type(tars_act) == str and tars_act.upper() != 'NAN'):
            
            tars_json = json.loads(tars_act)
            
            for tar in targets:
                
                if (type(tars_json[tar]) == float and np.isnan(tars_json[tar])):
                    pass
                
                else:
                    infos_from_ndcs.loc[iso3, tar] = '{"' + tar + '": ' + json.dumps(tars_json[tar]) + '}'
    
    # %%
    # Write out the file to the current preprocess folder.
    if ('write_out_data' in kwargs.keys() and not kwargs['write_out_data']):
        pass
    
    else:
        infos_from_ndcs.to_csv(Path(meta.path.pc_cov, f'infos_from_ndcs_SMD{meta.ndcs.submissions_until}.csv'))
    
    return infos_from_ndcs

# %%