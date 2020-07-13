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
    from helpers_functions.units.get_illion_from_power import get_illion_from_power
    from helpers_functions.units.get_conversion_illion import get_conversion_illion
    from helpers_functions.units.get_conversion_unit import get_conversion_unit
    from helpers_functions.units.get_baseunit import get_baseunit
    from helpers_functions.units.get_units_and_operators import get_units_and_operators
    from helpers_functions.data_manipulation.format_sci_multipliers_of_3 import format_sci_multipliers_of_3
    
    # %%
    unitBase, families = get_baseunit(unitFrom)
    data = (pd.DataFrame(np.array(data)) if not isinstance(data, pd.DataFrame) else data)
    data = data.abs() * get_conversion_unit(unitFrom, unitBase)
    units, operators = get_units_and_operators(unitBase)
    if 'numerator_or_denominator' in kwargs.keys():
        numerator_or_denominator = kwargs['numerator_or_denominator']
    #endif
    if 'length' in kwargs.keys():
        length = kwargs['length']
    #endif
    if 'numerator_or_denominator' not in locals():
        # Check if the gdp or pop are numerator or denominator, else put numerator_or_denominator = 'numerator'.
        check_gdp = [operators[xx] for xx in range(len(families)) if 'gdp' in families[xx]]
        check_pop = [operators[xx] for xx in range(len(families)) if 'pop' in families[xx]]
        if len(check_gdp) > 0:
            numerator_or_denominator = ( 'denominator' if check_gdp[-1] == '/' else 'numerator')
            if 'length' not in locals():
                length = 'long'
            #endif
        elif len(check_pop) > 0:
            numerator_or_denominator = ( 'denominator' if check_pop[-1] == '/' else 'numerator')
            if 'length' not in locals():
                length = 'long'
            #endif
        else:
            numerator_or_denominator = 'numerator'
            if 'length' not in locals():
                length = 'short' # Assuming it is gas.
            #endif
        #endif
    #endif
    
    maxi = data.max().max()
    if not np.isnan(maxi):
        sciformat = format_sci_multipliers_of_3(maxi)[0]
        sci_split = [float(xx) for xx in sciformat.split('e')]
        if len(sci_split) > 1:
            if numerator_or_denominator == 'numerator':
                power = sci_split[-1]
                if abs(power) > 1:
                    illion_new = get_illion_from_power(power, length)
                    multiplier = get_conversion_illion('One', illion_new)
                    if any(['Pers' in unitBase, 'GKD' in unitBase]):
                        unit_new = illion_new + ' ' + unitBase
                    else:
                        unit_new = illion_new + unitBase
                    #endif
                #endif
            elif numerator_or_denominator == 'denominator':
                power = -1 * sci_split[-1]
                if abs(power) > 1:
                    illion_new = get_illion_from_power(power, length)
                    multiplier = 1. / get_conversion_illion('One', illion_new)
                    unit_act = unitBase.split('/')
                    if any(['Pers' in unit_act[1], 'GKD' in unit_act[1]]):
                        unit_new = unit_act[0] + ' / ' + illion_new + ' ' + unit_act[1]
                    else:
                        unit_new = unit_act[0] + ' / ' + illion_new + unit_act[1]
                    #endif
                #endif
            #endif
        #endif
    #endif
    unit_new = (unit_new if 'unit_new' in locals() else unitBase)
    unit_new = (unit_new.replace(' ', '') if ' ' in unit_new else unit_new)
    multiplier = (1. if unit_new == unitBase.replace(' ', '') else multiplier)
    unit_new = (unit_new.replace('/', ' / ') if '/' in unit_new else unit_new)
    unit_new = (unit_new.replace('CO2eq', ' CO2eq') if 'CO2eq' in unit_new else unit_new)
    
    return unit_new, multiplier
# %%
