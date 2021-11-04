# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
# If gas == 'all' give out the GWPs for all gases in the csv-files.
# If gwp == 'all' give out all available GWPS for the wanted gas.

# %%
import pandas as pd
from warnings import warn
import os
from pathlib import Path

# %%
def get_gwps_for_gases(gas, gwp):
    warning = False
    warning = (True if type(gas) != str else False)
    warning = (True if (warning or type(gwp) != str) else False)
    warning = (True if (warning or gwp.upper() not in ['ALL', 'SAR', 'AR2', 'AR4', 'AR5', 'AR5', 'AR5CCF']) else False)
    gwp = ('AR2' if gwp.upper() == 'SAR' else gwp)
    if not warning:
        if gwp.upper() != 'ALL':
            gwps = pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), 
                                    'gwps_' + gwp.lower() + '.csv'), index_col='entity')
            if gas.upper() == 'ALL':
                return gwps.loc[:, 'gwp']
            else:
                warning = (True if (warning or gas.upper() not in list(gwps.index)) else False)
                if not warning:
                    return gwps.loc[gas.upper(), 'gwp']
                #endif
            #endif
        else:
            gwps = pd.DataFrame(columns=['AR2', 'AR4', 'AR5', 'AR5CCF'])
            for gwp in gwps.index:
                gwps.loc[:, gwp] = pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), 
                        'gwps_' + gwp.lower() + '.csv'), index_col='entity').loc[:, 'gwp']
            #endfor
            if gas.upper() == 'ALL':
                return gwps
            else:
                warning = (True if (warning or gas.upper() not in list(gwps.index)) else False)
                if not warning:
                    return gwps.loc[gas.upper(), :]
                #endif
            #endif
        #endif
    #endif
    if warning:
        warn("get_gwp_for_gas.py: the input for gas or GWP is not supported, or no conversion factor is available.")
        return None
    #endif
#enddef
# %%
