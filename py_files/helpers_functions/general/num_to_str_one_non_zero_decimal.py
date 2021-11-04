# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 09/2020.
"""

# %%
def num_to_str_one_non_zero_decimal(number, **kwargs):
    
    """
    Convert number to string, leaving one non-zero decimal only.
    Only for numbers that are 0.xxx. Else the value is given with one digit.
    kwargs:
        maximal (if given, not more decimals than maximal are returned).
        nr_non_zero (if given, not one but nr_non_zero decimals are returned).
    """
    
    if (f"{number :.0f}" == '0' or 'nr_non_zero' in kwargs.keys()):
        
        string = f"{number :.20f}"
        
        if string != 'nan':
            
            point = [xx for xx in range(len(string)) if string[xx] == '.']
            non_zero = [xx for xx in range(point[0], len(string)) if string[xx] not in ['0', '.']]
    
            if len(non_zero) == 0:
                
                out = '0.0'
            
            else:
                
                if 'nr_non_zero' not in kwargs.keys():
                    nr_non_zero = 1
                else:
                    nr_non_zero = kwargs['nr_non_zero']
                
                if 'maximal' not in kwargs.keys():
                    end = non_zero[0] + nr_non_zero
                else:
                    end = min([non_zero[0] + nr_non_zero, point[0]+kwargs['maximal']+1])
                
                out = string[:end]
        
        else:
        
            out = 'NaN'
    
    else:
        
        out = f"{number :.1f}"
    
    if out.replace('0', '').replace('.', '') == '':
        out = '0.0'
    
    return out

# %%
