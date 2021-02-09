# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def get_conversion_to_nice_unit(data, unitFrom, **kwargs):
    """
    Get a 'nicer looking' unit for emissions, population or GDP data, depending on the maximum of the data.
    Also handels composit-units (e.g., MtCO2eq/Pers).
    
    GIVES OUT CONVERSION FROM BASE UNIT, NOT FROM unitFrom!!!
    
    Parameters
    ----------
    data : list, array, df, etc.
        data in the unit unitFrom
    unitFrom: str.
        string with the data-unit (e.g., 'MtCO2eq/Pers')
    OPTIONAL
    ----------
    numerator_or_denominator : str
        'numerator' or 'denominator', indicating where to change the unit
        (e.g., t/Pers --> numerator changes to Mt/Pers, denominator changes to t/ThousandPers).
    length : str
        'short' or 'long'. E.g., 'short' results in 'M', 'long' in 'Million' 
    
    Returns
    -------
    unit_new, multiplier
        new unit (str), and multiplier (float)
    """
        
    # %%
    import numpy as np
    import pandas as pd
    import helpers_functions as hpf
    
    # %%
    unitBase, families = hpf.get_baseunit(unitFrom)
    
    data = (pd.DataFrame((np.array([data] * 2) if np.array(data).shape == () else np.array(data)))
        if not isinstance(data, pd.DataFrame) else data) # Stupid workaround, with data is number the rest would not work, and I don't want to do more recoding ...
    data = data.abs() * hpf.get_conversion_unit(unitFrom, unitBase)
    
    units, operators = hpf.get_units_and_operators(unitBase)
    
    if 'numerator_or_denominator' in kwargs.keys():
        
        numerator_or_denominator = kwargs['numerator_or_denominator']
    
    if 'length' in kwargs.keys():
        
        length = kwargs['length']
    
    if 'numerator_or_denominator' not in locals():
        
        # Check if the gdp or pop are numerator or denominator, else put numerator_or_denominator = 'numerator'.
        check_gdp = [operators[xx] for xx in range(len(families)) if 'gdp' in families[xx]]
        check_pop = [operators[xx] for xx in range(len(families)) if 'pop' in families[xx]]
        
        if len(check_gdp) > 0:
            
            numerator_or_denominator = ( 'denominator' if check_gdp[-1] == '/' else 'numerator')
            
            if 'length' not in locals():
                
                length = 'long'
        
        elif len(check_pop) > 0:
            
            numerator_or_denominator = ( 'denominator' if check_pop[-1] == '/' else 'numerator')
            
            if 'length' not in locals():
                
                length = 'long'
        
        else:
            
            numerator_or_denominator = 'numerator'
            
            if 'length' not in locals():
                
                length = 'short' # Assuming it is gas.
    
    maxi = data.max().max()
    
    if not np.isnan(maxi):
        
        sciformat = hpf.format_sci_multipliers_of_3(maxi)[0]
        sci_split = [float(xx) for xx in sciformat.split('e')]
        
        if len(sci_split) > 1:
            
            if numerator_or_denominator == 'numerator':
                
                power = sci_split[-1]
                
                if abs(power) > 1:
                    
                    illion_new = hpf.get_illion_from_power(power, length)
                    multiplier = hpf.get_conversion_illion('One', illion_new)
                    
                    if any(['Pers' in unitBase, 'GKD' in unitBase]):
                        
                        unit_new = illion_new + ' ' + unitBase
                    
                    else:
                        
                        unit_new = illion_new + unitBase
            
            elif numerator_or_denominator == 'denominator':
                
                power = -1 * sci_split[-1]
                
                if abs(power) > 1:
                    
                    illion_new = hpf.get_illion_from_power(power, length)
                    multiplier = 1. / hpf.get_conversion_illion('One', illion_new)
                    unit_act = unitBase.split('/')
                    
                    if any(['Pers' in unit_act[1], 'GKD' in unit_act[1]]):
                        
                        unit_new = unit_act[0] + ' / ' + illion_new + ' ' + unit_act[1]
                    
                    else:
                        
                        unit_new = unit_act[0] + ' / ' + illion_new + unit_act[1]
                        
    unit_new = (unit_new if 'unit_new' in locals() else unitBase)
    unit_new = (unit_new.replace(' ', '') if ' ' in unit_new else unit_new)
    multiplier = (1. if unit_new == unitBase.replace(' ', '') else multiplier)
    unit_new = (unit_new.replace('/', ' / ') if '/' in unit_new else unit_new)
    unit_new = (unit_new.replace('CO2eq', ' CO2eq') if 'CO2eq' in unit_new else unit_new)
    
    return unit_new, multiplier

# %%
