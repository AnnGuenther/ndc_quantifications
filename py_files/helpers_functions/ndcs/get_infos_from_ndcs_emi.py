# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
def get_infos_from_ndcs_emi():
    """
    Get the NDC emissions data.
    Converted from AR2 to AR4 if necessary.
    """
    
    # %%
    import json
    import pandas as pd
    from pathlib import Path
    from warnings import warn
    import helpers_functions as hpf
    from setup_metadata import setup_metadata
    
    # %%
    meta = setup_metadata()
    
    ndcs_all = hpf.get_infos_from_ndcs(meta, write_out_data=False)
    ndcs = ndcs_all.loc[:, 'EMI_POP_GDP']
    
    years = range(1990, 2051)
    emi_ndcs = {}
    emi_ndcs['inclLU'] = pd.DataFrame(index=ndcs.index, columns=years)
    emi_ndcs['exclLU'] = pd.DataFrame(index=ndcs.index, columns=years)
    emi_ndcs['onlyLU'] = pd.DataFrame(index=ndcs.index, columns=years)
    
    for iso3 in ndcs.index:
        
        ndc_info = ndcs_all.loc[iso3, 'EMI_POP_GDP']
        
        if (type(ndc_info) == str and ndc_info.upper() != 'NAN'):
            
            ndc_json = json.loads(ndc_info)['EMI']
            
            for case in ndc_json.keys():
                
                if case not in ['inclLU', 'exclLU', 'onlyLU']:
                    warn(f"Something went wrong for {iso3} {case}!")
                
                for year in ndc_json[case].keys():
                    
                    val = ndc_json[case][year]
                    
                    if ('AR2' in val or 'SAR' in val):
                        conversion_gwp = hpf.get_conversion_gwp_national([iso3], 'SAR', 'AR4').values[0]
                    else:
                        conversion_gwp = 1.
                    
                    emi_ndcs[case].loc[iso3, int(year)] = hpf.get_numerical_value_from_ndcval(val) * conversion_gwp
    
    for case in emi_ndcs.keys():
        emi_ndcs[case].to_csv(
            Path(meta.path.preprocess, f'infos_from_ndcs_emi_{case}.csv'))
    
    # %%
    return emi_ndcs

# %%