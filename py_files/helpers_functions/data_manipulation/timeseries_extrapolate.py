# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam
Last updated in 02/2020
"""

# %%
def timeseries_extrapolate(df, method, direction, **kwargs):
    """
    With regression or with mean over last/first values or with last/first value.
    One can chose how many values to use, or a starting/ending year.
    Has to be used twice if you want to extrapolate into the future and the past.
    
    For mean or lin_reg, the extrapolated values can have quite a jump between the 
    first/last available value, and the following ones...
    
    INPUT:
    df is pd.DataFrame (columns are years as integers) or pd.Series (indices are years as integers)
    method = 'constant' (use the last / first available value)
    method = 'lin_reg' (use a linear regression, give period or nrvalues)
    method = 'mean' (use the mean over some values, give period or nrvalues)
    direction = 'forward' or 'backward' (towards future or past)
    
    kwargs
    period = range(2010, 2017), if you want to have the lin_reg or mean over 2010 to 2016.
    nrvalues = 6, if you want to use the last 6 available values.
    
    OUTPUT:
    pd.DataFrame (even if you hand over a pd.Series ...)
    """
    
    # %%
    import pandas as pd
    import numpy as np
    import copy
    from warnings import warn
    import helpers_functions as hpf
    
    # %%
    # Add the missing years (columns with nans)
    calculate = True
    
    if isinstance(df, pd.Series):
        df = df.to_frame().transpose()
    elif isinstance(df, pd.DataFrame):
        df = df.reindex(columns=range(min(df.columns), max(df.columns)+1))
    else:
        warn("timeseries_extrapolate.py: the given df is neither a pd.DataFrame, nor a pd.Series. Nothing was calculated.")
        calculate = False
    
    if method not in ['constant', 'mean', 'lin_reg']:
        warn("timeseries_extrapolate.py: the given method is not valid. Nothing was calculated.")
        calculate = False
    
    if direction not in ['backward', 'forward']:
        warn("timeseries_extrapolate.py: the given direction is not valid. Nothing was calculated.")
        calculate = False
    
    # Get the kwargs:
    if kwargs != None:
        if 'period' in kwargs.keys():
            period = kwargs['period']
        else:
            period = None
        
        if 'nrvalues' in kwargs.keys():
            nrvalues = kwargs['nrvalues']
        else:
            nrvalues = None
    
    # If nothing is calculated, it hands back a pd.DataFrame with the original df
    # (even if the input was a pd.Series ...).
    df_copy = copy.deepcopy(df)
    df_notnan = ~df.isnull()
    
    if calculate:
        
        for row in df.index:
            
            df_row = df.loc[row, :]
            available_years = np.array(sorted(df_row.index[df_notnan.loc[row, :]]))
            missing_years = np.array(sorted(df_row.index[~df_notnan.loc[row, :]]))
            
            if (len(available_years) > 0) and (len(missing_years) > 0):
                
                # Only calculate something if needed:
                if ((direction == 'backward') and (min(missing_years) < min(available_years))) or \
                    ((direction == 'forward') and (max(missing_years) > max(available_years))):
                    
                    if method == 'constant':
                        
                        if direction == 'backward':
                            fill_val = df_row[available_years[0]]
                        
                        elif direction == 'forward':
                            fill_val = df_row[available_years[-1]]
                    
                    if method in ['mean', 'lin_reg']:
                        
                        # If both, period and nrvalues are given.
                        # Use the df from the period, or the nrvalues, if less values are available in the period, 
                        # or if values are available in the direction of extrapolation, 
                        # which lie outside the period.
                        # Do not overwrite available years.
                        
                        if (period != None) and (nrvalues != None):
                            
                            if direction == 'backward':
                                
#                                period_extended = range(min([min(period), available_years[0]]), 
#                                                        max(period)+1)
                                period_extended = range(min([min(period), available_years[0]]), 
                                                        max([max(period)+1, available_years[0]+1])) # !TODO check if that works
                                available_years_in_period = \
                                    available_years[(available_years >= min(period_extended)) & 
                                                    (available_years <=max(period_extended))]
                                years_for_mean_or_reg = available_years_in_period[:nrvalues]
                            
                            elif direction == 'forward':
                                
#                                period_extended = range(min(period), 
#                                                        max([max(period), available_years[-1]])+1)
                                period_extended = range(min([min(period), available_years[-1]]),  # !TODO check if that works
                                                        max([max(period), available_years[-1]])+1)
                                available_years_in_period = \
                                    available_years[(available_years >= min(period_extended)) & 
                                                    (available_years <= max(period_extended))]
                                years_for_mean_or_reg = available_years_in_period[-nrvalues:]
                                      
                        # If only period is given.
                        # period = range(2010, 2017), if you want to have the lin_reg or mean over 2010 to 2016.
                        # Do not overwrite available years.
                        elif period != None:
                            
                            if direction == 'backward':
                                
                                period_extended = range(min([min(period), available_years[0]]), 
                                                        max([max(period)+1, available_years[0]+1])) # !TODO check if that works
                                available_years_in_period = \
                                    available_years[(available_years >= min(period_extended)) & 
                                                    (available_years <= max(period_extended))]
                                years_for_mean_or_reg = available_years_in_period
                            
                            elif direction == 'forward':
                                
                                period_extended = range(min([min(period), available_years[-1]]),  # !TODO check if that works
                                                        max([max(period), available_years[-1]])+1)
                                available_years_in_period = \
                                    available_years[(available_years >= min(period_extended)) & 
                                                    (available_years <= max(period_extended))]
                                years_for_mean_or_reg = available_years_in_period
                        
                        # If only nrvalues is given.
                        # nrvalues = 6, if you want to use the last 6 available values.
                        # Do not overwrite available years.
                        elif nrvalues != None:
                            
                            if direction == 'backward':
                                years_for_mean_or_reg = available_years[:nrvalues]
                            
                            elif direction == 'forward':
                                years_for_mean_or_reg = available_years[-nrvalues:]
                        
                        if method == 'mean':
                            fill_val = df_row[years_for_mean_or_reg].mean()
                    
                    if method in ['constant', 'mean']:
                        
                        if direction == 'backward':
                            df.loc[row, df.columns < available_years[0]] = fill_val
                        elif direction == 'forward':
                            df.loc[row, df.columns > available_years[-1]] = fill_val
                    
                    elif method == 'lin_reg':
                        
                        xx, yy, linreg = hpf.linear_regression(years_for_mean_or_reg, df_row[years_for_mean_or_reg])
                        
                        if direction == 'backward':
                            xx_to_fill = range(missing_years[0], years_for_mean_or_reg[0])
                        elif direction == 'forward':
                            xx_to_fill = range(years_for_mean_or_reg[-1]+1, missing_years[-1]+1)
                        
                        yy_to_fill = [linreg.slope * xx + linreg.intercept 
                                 for xx in xx_to_fill]
                        df.loc[row, xx_to_fill] = yy_to_fill
        
        if len(years_for_mean_or_reg) == 0:
            print("Warning: no years available for years_for_mean_or_reg!")
        
        return df
    
    else:
        return df_copy

# %%