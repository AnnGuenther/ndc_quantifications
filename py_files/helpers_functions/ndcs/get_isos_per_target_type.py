# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last update in 04/2020.
"""

# %%
def get_isos_per_target_type(targets, baseyears, **kwargs):
    """
    Get the iso3s per target type.
    
    Input:
        targets: pd.Series with target types per iso3 (index).
        baseyears: pd.Series with base years per iso3 (index).
        Optional:
            dtype (output type: 'series')
            split_REI (if dtype == 'series', one can chose to split REI - split_REI == True - 
                into REI_RBY and REI_RBU, else it will just be REI).
    Output:
        dictionary with target types as keys and lists of iso3s as values.
        Or pd.Series, if dtype='series'.
    """
    
    # %%
    from setup_metadata import setup_metadata
    import numpy as np
    import pandas as pd
    
    # %%
    meta = setup_metadata()
    
    targets = targets.reindex(index=meta.isos.EARTH)
    # Replace nans by 'NAN'.
    targets.loc[targets.isnull()] = 'NAN'
    
    isos_per_type = {}
    
    tpes = meta.ndcs.types + ['NAN']
    
    for tpe in tpes:
        
        isos = targets.index[targets == tpe].to_list()
        
        if tpe == 'REI':
            
            # Check if it is compared to base year or target year.
            isos_REI_RBY = []
            isos_REI_RBU = []
            
            for iso3 in isos:
                
                base_yr = baseyears[iso3]
                
                if (type(base_yr) != str and not np.isnan(base_yr)):
                    # REI_RBY.
                    isos_REI_RBY += [iso3]
                else:
                    isos_REI_RBU += [iso3]
            
            isos_per_type['REI_RBY'] = isos_REI_RBY
            isos_per_type['REI_RBU'] = isos_REI_RBU
        
        isos_per_type[tpe] = isos
    
    if ('dtype' in kwargs.keys() and 'SERIES' in kwargs['dtype'].upper()):
        
        series = pd.Series(index=meta.isos.EARTH)
        
        if ('split_REI' in kwargs.keys() and kwargs['split_REI']):
            tpes = set(set(isos_per_type.keys()) - set(['REI']))
        else:
            tpes = set(set(isos_per_type.keys()) - set(['REI_RBY', 'REI_RBU']))
        
        for tpe in tpes:
            
            series[isos_per_type[tpe]] = tpe
        
        isos_per_type = series
    
    return isos_per_type

# %%
