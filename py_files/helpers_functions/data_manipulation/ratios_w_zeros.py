# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
def ratios_w_zeros(numerator, denominator, **kwargs):
    """
    Calculate ratios from two inputs (same shape), where the denominator can have zeros.
    Zeros in the denominator are first replaced by NaNs, and then NaNs where the 
    numerator or denominator had zeros and none had NaN are replaced by zeros.
    
    Input: numerator and denominator.
    Output is a np.array or what is chosen as dtype.
    kwargs: dtype = 'np.array', 'pd.DataFrame', 'pd.Series', 'list' or 'tuple'
    """
    # %%
    import pandas as pd
    import numpy as np
    from warnings import warn
    import sys
    from copy import deepcopy
    
    # %%
    
    if isinstance(numerator, pd.Series):
        
        numerator_index = numerator.index
        if any(numerator_index != denominator.index):
            sys.exit("ratios_w_zeros.py: indices of numerator and denominator are not the same.")
        
    elif isinstance(numerator, pd.DataFrame):
        
        numerator_index = numerator.index
        if any(numerator_index != denominator.index):
            sys.exit("ratios_w_zeros.py: indices of numerator and denominator are not the same.")
        
        numerator_columns = numerator.columns
        if any(numerator_columns != denominator.columns):
            sys.exit("ratios_w_zeros.py: columns of numerator and denominator are not the same.")
      
    numerator = np.array(numerator, dtype=np.float64)
    denominator = np.array(denominator, dtype=np.float64)
    
    if (numerator.size != denominator.size):
        warn("ratios_w_zeros.py: the input does not have the same size. Nothing was calculated.")
    
    # Save where there are zeros.
    numerator_iszero = numerator == 0.
    # Save where there are NaN.
    numerator_isnan = np.isnan(numerator)
    # Replace the zeros by NaNs.
    numerator[numerator_iszero] = np.nan
    
    denominator_iszero = denominator == 0.
    denominator[denominator_iszero] = np.nan
    denominator_isnan = np.isnan(denominator)
    
    ratio = numerator / denominator
    
    # Where numerator or denominator had zeros: replace the NaNs by zeros.
    ratio[numerator_iszero | denominator_iszero] = 0.
    # Where numerator or denominator had NaNs: replace the values by NaNs.
    ratio[numerator_isnan | denominator_isnan] = np.nan
    
    if 'dtype' in kwargs.keys():
        
        if kwargs['dtype'] == 'pd.DataFrame':
            ratio = pd.DataFrame(ratio)
            if 'numerator_index' in locals():
                ratio.index = numerator_index
            if 'numerator_columns' in locals():
                ratio.columns = numerator_columns
       
        elif kwargs['dtype'] == 'pd.Series': # Only works with 'one row'.
            ratio = pd.Series(ratio)
            if 'numerator_index' in locals():
                ratio.index = numerator_index
        
        elif kwargs['dtype'] == 'list':
            ratio = list(ratio)
        
        elif kwargs['dtype'] == 'tuple':
            ratio = tuple(ratio)
        
        elif kwargs['dtype'] == 'np.array':
            ratio = ratio
    
    return ratio

# %%