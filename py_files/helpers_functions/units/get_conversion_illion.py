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
from warnings import warn
import os
from pathlib import Path

# %%
def get_conversion_illion(illionFrom, illionTo):
    # kwargs can only be GWP
    illion_multipliers = pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), 
                            'illion_multipliers.csv'), index_col=0)
    # Multiplier: multiplier for illionFrom divided by multiplier for illionTo.
    # E.g., from Thousand (1e3) to M (1e6), the multiplier is 1e3/1e6=1e-3.
    # E.g., 3 Thousand in M: 3*1e3/1e6 = 0.003M
    # E.g., 3 Thousand in M: 3*1e3/1e6 = 0.003M
    illionFrom = (illion_multipliers.loc[illionFrom] if illionFrom in list(illion_multipliers.index) else [False])
    illionTo = (illion_multipliers.loc[illionTo] if illionTo in list(illion_multipliers.index) else [False])
    if any(illionFrom) and any(illionTo):
        return (illionFrom/illionTo)[0]
    else:
        warn("get_illion_multiplier.py: the given illionFrom and / or illionTo are not valid.")
    #endif
#enddef

# %%
