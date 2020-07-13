# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:53:29 2020

@author: annikag
"""

# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
"""
Get scientific notation in steps of 3 (-6, -3, +3, +6, +9, etc.).
INPUT: numeric data (or strings).
OUTPUT: list of strings, all with the same power.
"""

# %%
def format_sci_multipliers_of_3(data_num_1d, **kwargs):
    if 'prec' in kwargs.keys():
        prec = kwargs['prec']
    else:
        prec = 3
    #endif
    if not isinstance(data_num_1d, list):
        data_num_1d = [data_num_1d]
    #endif
    data_num_1d = [float(xx) for xx in data_num_1d]
    # Get info on min and max.
    lowest = min(data_num_1d)
    highest = max(data_num_1d)
    get_pot_lowest = [float(xx) for xx in '{:.2e}'.format(lowest).split('e')]
    get_pot_lowest = get_pot_lowest[1] - get_pot_lowest[1] % 3
    get_pot_highest = [float(xx) for xx in '{:.2e}'.format(highest).split('e')]
    get_pot_highest = get_pot_highest[1] - get_pot_highest[1] % 3
    # Don't use 0.
    get_pot = [xx for xx in [get_pot_lowest, get_pot_highest] if xx != 0.]
    data_str = []
    if len(get_pot) > 0:
        get_pot = max(get_pot)
    else:
        get_pot = 0
    #endif
    if get_pot != 0:
        for val in data_num_1d:
            tick_str = '{:.2e}'.format(val)
            val_str_components = tick_str.split('e')
            val_num_components = [float(xx) for xx in val_str_components]
            val_num_components[0] = val_num_components[0]*(10**(val_num_components[1]-get_pot))
            val_num_components[1] = get_pot
            rest = val_num_components[1] % 3
            new_str = '{:.{prec}f}'.format(val_num_components[0] * 10**rest, prec=prec-2) + '1e' + '{:+}'.format(int(get_pot))
            data_str.append(new_str)
        #endfor
    else:
        for val in data_num_1d:
            data_str.append('{:.{prec}f}'.format(val, prec=prec-1))
        #endfor
    #endif
    return data_str
#enddef

# %%
