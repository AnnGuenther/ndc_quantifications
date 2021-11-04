# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
import pandas as pd
import os
from pathlib import Path

# %%
def get_members_of_basket(basket, **kwargs):
    # kwargs: all=True or all=False
    # If it is not given, all single gases are returned.
        
    if 'all' in kwargs.keys():
        get_all = kwargs['all']
    
    if basket in ['HFCS', 'PFCS']:
        gases = [str(xx[0]) for xx in 
                 pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), basket.lower() + '.csv')).values]
    elif basket in ['FGASES', 'KYOTOGHG']:
        if not get_all:
            gases = [str(xx[0]) for xx in 
                pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), basket.lower() + '.csv')).values]
        else:
            gases = [str(xx[0]) for xx in 
                pd.read_csv(Path(os.path.dirname(os.path.realpath(__file__)), basket.lower() + '_single_gases.csv')).values]
    
    # Gives error if the basket is not in ['HFCS', 'PFCS', 'FGASES', 'KYOTOGHG'].
    return gases
#enddef
# %%
