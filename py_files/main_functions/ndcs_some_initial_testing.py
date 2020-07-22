# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
def ndcs_some_initial_testing(database, meta):
    """
    Check input data for 'how many countries have no / missing data' and 'are the values of pc_cov/ncov between 0 and 1'.
    Does not check whether the emissions / pop / gdp data seem realistic.
    """
    
    # %%
    from copy import deepcopy
    import sys
    
    # %%
    # How many countries have no data. How many countries have missing data.
    for tablename in ['emi_bl_exclLU', 'emi_bl_LU', 'pc_cov_exclLU', 
                      'pop',  'gdp']:
        
        data = deepcopy(getattr(database, tablename).data)
        data_null = data.index[data.isnull().all(axis=1)]
        data.drop(index=data_null, inplace=True)
        data_missing = data.index[data.isnull().any(axis=1)]
        
        if len(data_null) > 0:
            print(f"{tablename} has no data for " + ", ".join(data_null) + ".")
        
        if len(data_missing) > 0:
            print(f"{tablename} has missing data for " + ", ".join(data_missing) + ".")
    
    # Are values of pc_n/cov between 0 and 1?
    tablename = 'pc_cov_exclLU'
    data = getattr(database, tablename).data
    
    if (data < 0.).any().any():
        sys(f"{tablename} has values below 0.")
    
    if (data > 1.).any().any():
        sys(f"{tablename} has values greater than 1.")

# %%