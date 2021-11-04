# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated: 01/2021
"""

# %%
def join_list_but_last_element_different(list_of_elements, **kwargs):
    
    # %%
    import helpers_functions as hpf
    
    # %%
    try:
        separator = kwargs['separator']
    except:
        separator = 'and'
    
    try:
        precision = kwargs['precision']
    except:
        precision = 1
    
    list_of_elements_new = [xx if type(xx) == str else hpf.rnd(xx, precision) for xx in list_of_elements]
    
    len_list = len(list_of_elements_new)
    if len_list == 0:
        joined = ''
    elif len_list == 1:
        joined = list_of_elements_new[0]
    else:
        joined = ', '.join(list_of_elements_new[:-1]) + f' {separator} ' + list_of_elements_new[-1]
    
    return joined

# %%