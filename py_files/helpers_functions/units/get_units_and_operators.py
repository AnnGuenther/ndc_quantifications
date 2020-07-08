# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def get_units_and_operators(unit):
    # Check if the unit is a 'composite' unit.
    #unitFrom = 'MtCO2eq/Pers'
    unit = '*' + unit
    splitter = [xx for xx in range(len(unit)) if unit[xx] in '/*']
    splitter = splitter + [len(unit)]
    unit_split = []
    for ind in range(len(splitter[:-1])):
        unit_split.append(unit[splitter[ind] : splitter[ind+1]])
    #endfor
    units = [xx[1:] for xx in unit_split]
    operators = [xx[0] for xx in unit_split]
    
    return units, operators
#enddef

# %%