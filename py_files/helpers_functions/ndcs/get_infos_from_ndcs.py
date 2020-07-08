# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
def get_infos_from_ndcs(meta, **kwargs):
    """
    Gets information from infos_from_ndcs_default.xlsx and writes out the important information to
    'ndcs_info.csv' in meta.path.preprocess.
    
    INPUT: meta
    kwargs: write_out_data (if False nothing is written out)
    """
    # %%
    import pandas as pd
    import numpy as np
    import json
    from pathlib import Path

    # %%
    # Get information from NDCs (only the rows with ".mod" in the name):
    infos_from_ndcs = pd.read_excel(Path(meta.path.main, 'data', 'input', 'infos_from_ndcs_default.xlsx'), 
        sheet_name='Overview', index_col=0, header=None).astype('str')
    
    # Only keep the rows ending with ".mod"
    infos_from_ndcs = infos_from_ndcs.loc[[xx for xx in infos_from_ndcs.index 
        if (type(xx) == str and '.mod' in xx)], :]
    infos_from_ndcs.index = [xx.replace('.mod', '').upper() for xx in infos_from_ndcs.index]
    
    # Check for the base year entries to be integers or NaN. Will give an error if it cannot be converted to int.
    infos_from_ndcs.loc['BASEYEAR', :] = [int(xx) if xx != 'nan' else np.nan for xx in infos_from_ndcs.loc['BASEYEAR', :]]    
    
    # ISO3s as index.
    infos_from_ndcs.columns = infos_from_ndcs.loc['ISO3', :]
    infos_from_ndcs = infos_from_ndcs.reindex(columns=meta.isos.EARTH_EU28)
    infos_from_ndcs.drop(index=['ISO3'], inplace=True)
    infos_from_ndcs = infos_from_ndcs.transpose()
    
    # Use EU28 information for all EU28 countries.
    cols = list(set(set(infos_from_ndcs.columns) - set(['ISO2', 'COUNTRYNAME'])))
    infos_from_ndcs.loc[meta.isos.EU28, cols] = infos_from_ndcs.loc['EU28', cols].values
    
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
            if type(cov_act) == str:
                cov_json = json.loads(cov_act)
                for case in cov_json.keys():
                    infos_from_ndcs.loc[iso3, [f"{xx.upper()}_{name}" for xx in cov_json[case]]] = case
    
    # Targets
    targets = [xx for xx in meta.ndcs.types if xx != 'NGT']
    
    for col in targets:
        infos_from_ndcs.loc[:, col] = np.nan
    
    for iso3 in infos_from_ndcs.index:
        tars_act = infos_from_ndcs.loc[iso3, 'TARGETS']
        if type(tars_act) == str:
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
        infos_from_ndcs.to_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'))
    
    return infos_from_ndcs

# %%