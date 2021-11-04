# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020.
"""

# %%
"""
Case sensitive (upper / lower).
E.g., get_conversion_illion('Thousand', 'M')
or get_conversion_illion('M', 'One')
Check illion_multipliers.csv for available inputs.
"""

# %%
import pandas as pd
import os
from pathlib import Path

# %%
def get_illion_from_power(power, illion):
    # illion is 'long' or 'short'. long means e.g. Million, short means e.g. M.
    illion_multipliers = pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), 
                            'illion_multipliers.csv'))
    get_illions = illion_multipliers.loc[illion_multipliers.value == 10**power, 'code']
    illion_name = get_illions[get_illions.index[0]]
    for xx in get_illions[get_illions.index[1:]]:
        if illion == 'long':
            illion_name = (illion_name if len(illion_name) > len(xx) else xx)
        if illion == 'short':
            illion_name = (illion_name if len(illion_name) < len(xx) else xx)
        #endif
    #endfor
    
    return illion_name
#enddef

# %%
