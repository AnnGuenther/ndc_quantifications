# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
import sys
from helpers_functions.units.get_units_and_operators import get_units_and_operators

# %%
# Only works for population, gdp (in GKD 2005 or 2011), and emissions (gramms or tons have to be in the unitFrom).

# %%
def get_baseunit(unitFrom):
    baseunit = unitFrom
    units, operators = get_units_and_operators(unitFrom)
    families = []
    for ind in range(len(units)):
        unit_act = units[ind]
        if 'Pers' in unit_act:
            baseunit = unitFrom.replace(unit_act, 'Pers')
            families += ['pop']
        elif 'GKD' in unit_act:
            if '2005' in unit_act:
                baseunit = unitFrom.replace(unit_act, '2005GKD')
                families += ['gdp']
            elif '2011' in unit_act:
                baseunit = unitFrom.replace(unit_act, '2011GKD')
                families += ['gdp']
            else:
                sys.exit("get_conversion_to_nice_unit.py: the unitFrom is not supported.")
            #endif
        elif any([xx in units[ind] for xx in ['g', 't']]):
            families += ['emi']
            if 'CO2eq' in unitFrom:
                baseunit = unitFrom.replace(unit_act, 'tCO2eq')
            else:
                baseunit = unitFrom.replace(unit_act, 't')
                # Something can slip through here, if one has units that are neither Pers nor GKD
                # but have a g or a t in them.
        else:
            sys.exit("get_conversion_to_baseunit.py: the unitFrom is not supported.")
        #endif
    #endfor
    
    return baseunit, families
#enddef

# %%