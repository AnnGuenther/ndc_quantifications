# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last update in 02/2020
"""

# %%
"""
Calculate nansum for numpy array or pandas.DataFrame or pandas.Series.
pandas.sum(skipna=True) does not work for me, and np.nansum neither ...
"""

# %%
import numpy as np
import pandas as pd
from warnings import warn

# %%
def nansum(matrix, **kwargs):
    
    # Get the kwargs:
    if kwargs != None:
        if 'axis' in kwargs.keys():
            axis = kwargs['axis']
        else:
            axis = 0 # Default: along index.
        #endif
    #endif
    
    tpe = None
    out = None
    if isinstance(matrix, pd.Series):
        tpe = 'series'
    elif isinstance(matrix, pd.DataFrame):
        tpe = 'df'
    elif isinstance(matrix, list):
        tpe = 'list'
    elif isinstance(matrix, tuple):
        tpe = 'tuple'
    elif isinstance(matrix, np.ndarray):
        tpe = 'np'
    else:
        warn("nansum.py: wrong input, nothing calculated.")
    #endif
    
    if tpe in ['series', 'df', 'list', 'tuple', 'np']:
        if tpe == 'series':
            if matrix.isnull().all():
                out = np.nan
        else:
            matrix = pd.DataFrame(matrix)
            # Along index.
            if axis == 0:
                all_nan= matrix.isnull().all(axis=0)
                out = matrix.sum(axis=0)
                out[all_nan] = np.nan
            # Along columns.
            else:
                all_nan = matrix.isnull().all(axis=1)
                out = matrix.sum(axis=1)
                out[all_nan] = np.nan
            #endif
            if tpe == 'list':
                out = list(out)
            elif tpe == 'tuple':
                out = tuple(out)
            elif tpe == 'np':
                out = np.array(out)
            #endif
        #endif
    #endif
    
    return out
#enddef

# %%