# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020.
"""

# %%
"""
Case sensitive (upper / lower).
Only checks for 2005GKD, 2011GDK, Pers, and CO2eq.
Can have entity and gwp as kwargs.
No combined units (such as MtCO2eq/Pers).
If you want to calculate MtCO2eq/Pers into tCO2eq/ThousandPers use:
    multiplier = get_conversion_illion('M', 'One')/get_conversion_illion('One', 'Thousand')

With wrong inputs the module will just stop working (error).
Unless unitFrom == unitTo.

kwargs:
    entity
    gwps:
        gwp only
        or gwpFrom only
        or gwpTo only
        or gwpFrom and gwpTo
        or gwp and gwpFrom
        or gwp and gwpTo
"""

# %%
from warnings import warn
import sys
from helpers_functions.units.get_gwps_for_gases import get_gwps_for_gases
from helpers_functions.units.get_conversion_illion import get_conversion_illion
from helpers_functions.units.get_conversion_gwp import get_conversion_gwp
from helpers_functions.units.get_units_and_operators import get_units_and_operators

# %%
def get_conversion_unit(unitFrom, unitTo, **kwargs):
    unitFrom, unitFrom_operator = get_units_and_operators(unitFrom)
    unitTo, unitTo_operator = get_units_and_operators(unitTo)
    if (len(unitFrom) != len(unitFrom) or unitFrom_operator != unitTo_operator):
        sys.exit("get_conversion_unit.py: unitFrom and unitTo do not have the same number of 'composites'.")
    #endif
    multiplier_total = 1.
    for ind in range(len(unitFrom)):
        multiplier = get_conversion_unit_simple(unitFrom[ind], unitTo[ind], kwargs)
        if unitFrom_operator[ind] == '/':
            multiplier_total = multiplier_total / multiplier
        elif unitFrom_operator[ind] == '*':
            multiplier_total = multiplier_total * multiplier
        #endif
    #endfor
    
    return multiplier_total

# %%
def get_conversion_unit_simple(unitFrom, unitTo, kwargs):
    # kwargs can be entity and gwp (or gwpFrom / gwpTo).
    warning = False
    if (unitFrom == unitTo and 'CO2eq' not in unitFrom):
        # For CO2eq a conversion from one GWP to another might be wanted.
        multiplier = 1.
    else:
        # Remove white spaces.
        unitFrom = ''.join([xx if xx != ' ' else '' for xx in unitFrom])
        unitTo = ''.join([xx if xx != ' ' else '' for xx in unitTo])
        
        # Set default multipliers, as these values will only be set for gases.
        multiplier_SI = 1.
        multiplier_gwp = 1.
        
        # kwargs can be entity and gwp.
        if 'entity' in kwargs.keys():
            entity = kwargs['entity']
        else:
            entity = '' # Cannot be None.
        #endif
        
        if ('POP' in entity) or ('Pers' in unitFrom) or ('Pers' in unitTo):
            if ('Pers' not in unitFrom) or ('Pers' not in unitTo):
                sys.exit("get_conversion_unit.py: something is wrong.")
            else:
                # Only illion multiplier intersting.
                unitFrom = unitFrom.replace('Pers', '')
                unitTo = unitTo.replace('Pers', '')
            #endif
        elif ('GDP' in entity) or ('GKD' in unitFrom) or ('GDK' in unitTo):
            if ('GKD' not in unitFrom) or ('GKD' not in unitTo):
                sys.exit("get_conversion_unit.py: something is wrong.")
            else:
                for yr in ['2005', '2011']:
                    # Only illion multiplier intersting.
                    warning = (True if warning or (yr in unitFrom) and (yr not in unitTo) else False)
                    unitFrom = unitFrom.replace(yr + 'GKD', '')
                    unitTo = unitTo.replace(yr + 'GKD', '')
                #endfor
            #endfor
        else:
            # Assuming that it is a gas or gas-basket.
            # g (gramm) or t (ton) has to be in unitFrom and unitTo.
            if ('g' not in unitFrom and 't' not in unitFrom) or \
                ('g' not in unitTo and 't' not in unitTo):
                sys.exit("get_conversion_unit.py: assuming that it is a gas, but the unit does not contain 'g', nor 't'.")
            # GWP only useful when entity is given, and when it is a gas.
            else:
                if (entity == '' and ('CO2eq' in unitFrom or 'CO2eq' in unitTo)):
                    multiplier_gwp = 1.
                    warn("get_conversion_unit.py: assuming that it is a gas. As no entity is given, no gwp conversion is performed, even if GWPs are given.")
                else:
                    if 'CO2eq' in unitFrom:
                        gwpFrom = (kwargs['gwpFrom'] if 'gwpFrom' in kwargs.keys() else kwargs['gwp'])
                        # Will give error if neither of them is in kwargs.
                    #endif
                    if 'CO2eq' in unitTo:
                        gwpTo = (kwargs['gwpTo'] if 'gwpTo' in kwargs.keys() else kwargs['gwp'])
                    #endif
                    if ('CO2eq' in unitFrom and 'CO2eq' in unitTo):
                        if any([xx in entity for xx in ['HFCS', 'PFCS', 'FGASES', 'KYOTOGHG']]):
                            if gwpFrom != gwpTo:
                                sys.exit("get_conversion_unit.py: something went wrong for the basket.")
                            else:
                                multiplier_gwp = 1.
                            #endif
                        else:
                            multiplier_gwp = get_conversion_gwp(gwpFrom, gwpTo, entity)
                        #endif
                    else:
                        if ('CO2eq' in unitFrom and 'CO2eq' not in unitTo):
                            multiplier_gwp = 1. / get_gwps_for_gases(entity, gwpFrom)
                        elif ('CO2eq' in unitTo and 'CO2eq' not in unitFrom):
                            multiplier_gwp = get_gwps_for_gases(entity, gwpTo)
                        #endif
                    #endif
                #endif
                unitFrom = (unitFrom.replace('CO2eq', '') if 'CO2eq' in unitFrom else unitFrom)
                unitTo = (unitTo.replace('CO2eq', '') if 'CO2eq' in unitTo else unitTo)
                # Get the SI multiplier.
                # 1 t is 1000 kg, and 1 kg is 1000 g.
                if unitFrom[-1] == unitTo[-1]:
                    multiplier_SI = 1.
                elif (unitFrom[-1] == 't' and unitTo[-1] == 'g'):
                    multiplier_SI = 1e6
                elif (unitFrom[-1] == 'g' and unitTo[-1] == 't'):
                    multiplier_SI = 1e-6
                else:
                    warning = True
                    multiplier_SI = None
                #endif
                unitFrom = unitFrom[:-1]
                unitTo = unitTo[:-1]
            #endif
        #endif
        # Get the illionFrom and illionTo.
        # What remains should be the illion.
        if len(unitFrom) > 0:
            illionFrom = unitFrom
        else:
            illionFrom = 'One'
        #endif
        if len(unitTo) > 0:
            illionTo = unitTo
        else:
            illionTo = 'One'
        #endif
        multiplier_illion = get_conversion_illion(illionFrom, illionTo)
        multiplier = multiplier_gwp * multiplier_illion * multiplier_SI
    #endif
    if warning:
        warn("get_conversion_unit.py: something went wrong. The output is None.")
        return None
    else:
        return multiplier
    #endif
#enddef

# %%
