# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam
Last updated in 02/2020
"""

# %%
def timeseries_interpolate(df, method):
    """
    Linear interpolation or filling with constant values (forward filling has priority).
    
    INPUT:
    df is pd.DataFrame (columns are years as integers) or pd.Series (indices are years as integers)
    method = 'linear' or 'constant'
    
    OUTPUT:
    pd.DataFrame (even if you hand over a pd.Series ...)
    """
    
    # %%
    import pandas as pd
    import numpy as np
    import copy
    from warnings import warn
    
    # %%
    # Add the missing years (columns with nans)
    calculate = True
    
    if isinstance(df, pd.Series):
        df = df.to_frame().transpose()
    elif isinstance(df, pd.DataFrame):
        df = df.reindex(columns=range(min(df.columns), max(df.columns)+1))
    else:
        warn("timeseries_interpolate.py: the given df is neither a pd.DataFrame, nor a pd.Series. Nothing was calculated.")
        calculate = False
    
    df = df.astype('float64')
    
    if method not in ['linear', 'constant']:
        warn("timeseries_interpolate.py: the given method is not valid. Nothing was calculated.")
        calculate = False
    
    # If nothing is calculated, it hands back a pd.DataFrame with the original df
    # (even if the input was a pd.Series).
    df_copy = copy.deepcopy(df)
    
    if calculate:
        # Both methods used here (for linear and constant) basically also extrapolate the timeseries.
        # So remember the NaNs at the edges, and put them back after applying interpolate or ffill and bfill.
        df_notnan = ~df.isnull()
        df_nan = df.isnull()
        # Only do it for rows that contain some values.
        isos_to_fill = [xx for xx in df_notnan.index if ((df_notnan.loc[xx, :].any()) and ~(df_nan.loc[xx, :].all()))]
        first_available = [[xx for xx in df_notnan.columns if df_notnan.loc[yy, xx]][0] for yy in isos_to_fill]
        last_available = [[xx for xx in df_notnan.columns if df_notnan.loc[yy, xx]][-1] for yy in isos_to_fill]
        first_available = pd.DataFrame(first_available, isos_to_fill)
        last_available = pd.DataFrame(last_available, isos_to_fill)
        
        if method == 'linear':
            # If you first fill the missing years, then it does not matter if the method is
            # 'linear', 'time', or 'index'.
            df.interpolate(method='linear', limit_area='inside', axis=1, inplace=True)
            
        elif method == 'constant':
            # Filling with constant values (first fill forward, then backward, 
            # so that the first available value is used before its year).
            # Code could be improved ...
            df = df.ffill(axis=1) # Forward
            df = df.bfill(axis=1) # Backward
        
        for row in isos_to_fill:
            df.loc[row, df.columns < first_available.loc[row].values[0]] = np.NaN
            df.loc[row, df.columns > last_available.loc[row].values[0]] = np.NaN
        
        return df
    
    else:
        return df_copy

# %%