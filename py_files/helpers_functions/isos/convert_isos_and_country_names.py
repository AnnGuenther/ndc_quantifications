# -*- coding: utf-8 -*-
"""
Author: Annika GÜnther, annika.guenther@pik-potsdam.de
Last update: 02/2021
"""

# %%
#####
# Convert:
# - list of ISO2s to ISO3s. Input: From='ISO2', To='ISO3'.
# - list of ISO3s to ISO2s. Input: From='ISO3', To='ISO2'.
# - list of ISO2s to CountryNames. Input: From='ISO2', To='ShortName' or To='LongName'.
# - list of ISO3s to CountryNames. Input: From='ISO3', To='ShortName' or To='LongName'.

# Example:
#from py_Functions.func_ISOs_To_ISOs_Or_CountryNames import *
#func_ISOs_To_ISOs_Or_CountryNames(['DE'], 'ISO2', 'ISO3')
# --> ['DEU']
#####

# %%
def convert_isos_and_country_names(ISOs, From, To, **kwargs):
    
    """
    Convert between ISOs and country names.
    
    Chose between 'ISO2', 'ISO3', 'ShortName', 'LongName'.
    
    kwargs:
        the = 'The' or 'the' (if To == 'ShortName' one can chose to get it 
        including an upper- or lowerase 'the' where applicable).
    """
    
    # %%
    import pandas as pd
    import numpy as np
    import os
    from pathlib import Path
    
    # %%
    file = 'iso3_iso2_countrynames.csv'
    
    data = pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), file))
    
    # NA for Namibia is treated as nan, replace it by the string NA.
    data.loc[data.ISO3 == 'NAM', 'ISO2'] = 'NA'
    
    if ('the' in kwargs.keys() and To == 'ShortName'):
        
        if kwargs['the'] == 'The':
            # Capitalize all
            the = pd.Series(
                [f'{xx.capitalize()} ' if type(xx) == str else '' for xx in data.the],
                index=data.loc[:, From])
        
        elif kwargs['the'] == 'the':
            # Leave it as is
            the = pd.Series(
                [f'{xx} ' if type(xx) == str else '' for xx in data.the],
                index=data.loc[:, From])
    
    if 'the' not in locals():
        the = pd.Series(
            '',
            index=data.loc[:, From])
    
    data.index = data.loc[:, From]
    data = data.loc[:, To]
    
    Out = []
    
    if type(ISOs) != list:
        
        ISOs = [ISOs]
    
    for xx1 in range(len(ISOs)):
        
        act = ISOs[xx1]
        
        if act in list(data.index):
            
            Out.append(f'{the[act]}{data[act]}')
        
        else:
            
            Out.append(np.nan)
            print('WARNING: ' + act + ' not in ' + file + '.')
    #
    return Out

# %%