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
import pandas as pd
import numpy as np
import os
from pathlib import Path

# %%
def convert_isos_and_country_names(ISOs, From, To):
    File = 'iso3_iso2_countrynames.csv'
    Data = pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), File))
    # NA for Namibia is treated as nan, replace it by the string NA.
    Data.loc[Data.ISO3 == 'NAM', 'ISO2'] = 'NA'
    Data.index = Data.loc[:, From]
    Data = Data.loc[:, To]
    Out = []
    if type(ISOs) != list:
        ISOs = [ISOs]
    
    for xx1 in range(len(ISOs)):
        Act = ISOs[xx1]
        if Act in list(Data.index):
            Out.append(Data[Act])
        else:
            Out.append(np.nan)
            print('WARNING: ' + Act + ' not in ' + File + '.')
    #
    return Out
