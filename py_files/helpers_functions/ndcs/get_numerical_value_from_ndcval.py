# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
def get_numerical_value_from_ndcval(ndc_value):
    """
    Get the numerical value from ndc_value.
    """
    
    # %%
    from warnings import warn
    
    # %%
    ndc_value_new = ndc_value
    
    if type(ndc_value_new) != str:
        ndc_value_num = ndc_value_new
    
    else:
        # Prevent some 'numbers' that might be in ndc_value_new from interfering in getting the numerical value.
        for repl in ['CO2', 'AR2', 'AR4', 'AR5']:
            ndc_value_new = ndc_value_new.replace(repl, '')
        
        # If there is a space in ndc_value_new only use the first part, 
        # and give out a warning if there is a number in the rest of the string.
        if ' ' not in ndc_value_new:
            ndc_value_num = ndc_value_new
        
        else:
            ndc_value_num = ndc_value_new[:[xx for xx in range(len(ndc_value_new)) if ndc_value_new[xx] == ' '][0]]
            ndc_value_rest = ndc_value_new[[xx for xx in range(len(ndc_value_new)) if ndc_value_new[xx] == ' '][0]:]
            
            if any([True if xx in ndc_value_rest else False for xx in '0123456789']):
                warn(f"ndcs_calulate_targets.py get_numerical_values_from_ndcval: check the value '{ndc_value}'" +  
                     " from the ndc input table as it contains a numerical value after the first space.")
        
        ndc_value_num = float(''.join([xx for xx in ndc_value_num if xx in '0123456789eE.+-']))
    
    return ndc_value_num

# %%