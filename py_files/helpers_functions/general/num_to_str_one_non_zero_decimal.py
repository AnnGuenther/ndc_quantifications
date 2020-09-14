# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 09/2020.
"""

# %%
def num_to_str_one_non_zero_decimal(number):
    
    """
    Convert number to string, leaving one non-zero decimal only.
    """
    
    string = f"{number :f}"
    point = [xx for xx in range(len(string)) if string[xx] == '.']
    decimals = string[point[0]+1:]
    non_zero = [point[0]+1 + xx for xx in range(len(decimals)) if string[xx] not in ['0', '.']]
    
    return string[:non_zero[0]+1]

# %%
