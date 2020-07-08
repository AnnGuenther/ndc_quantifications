# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:17:54 2020

@author: annikag
"""

# %%
def get_targets_from_json(ndc_values_all_json, tar_type, iso3):
    """
    Get all the targets for a target type, as stored in infos_from_ndcs_default.xlsx.
    ndc_values_all_json is what is stored in a cell in infos_from_ndcs_default.xlsx.
    """
    
    # %%
    import pandas as pd
    import json
    import sys
    
    # %%
    ndc_values_all = pd.DataFrame(columns=['inclLU', 'exclLU', 'condi', 'rge', 'taryr'])
    ndc_values_all_json = json.loads(ndc_values_all_json)
    
    # Get all values (ndc_values_all), stored in a dictionary with keys 
    # ['inclLU/exclLU']['un/conditional']['best/worst']['year 20xx']
    # and put them into 'ndc_values_all'.
    for llcf in ndc_values_all_json[tar_type].keys(): # inclLU/exclLU
        if llcf not in ['inclLU', 'exclLU']:
            sys.exit(f"There is an error in the input data for {iso3} for {tar_type} (error in incl/exclLU).")
        
        for condi in ndc_values_all_json[tar_type][llcf].keys(): # un/conditional
            if condi not in ['unconditional', 'conditional']:
                sys.exit(f"There is an error in the input data for {iso3} for {tar_type} (error in un/conditional).")
            
            for rge in ndc_values_all_json[tar_type][llcf][condi].keys(): # best/worst
                if rge not in ['best', 'worst']:
                    sys.exit(f"There is an error in the input data for {iso3} for {tar_type} (error in best/worst).")
                
                for yr in ndc_values_all_json[tar_type][llcf][condi][rge].keys(): # e.g., 2030
                    
                    row_act = condi + '_' + rge + '_' + yr
                    ndc_values_all.loc[row_act, llcf] = ndc_values_all_json[tar_type][llcf][condi][rge][yr]
                    ndc_values_all.loc[row_act, ['condi', 'rge', 'taryr']] = [condi, rge, yr]
    
    return ndc_values_all

# %%