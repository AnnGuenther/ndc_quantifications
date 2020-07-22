# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
GMB
"""

# GgCO2eq
red = {
    'uncondi':
        {'RE': {2025: 78.5, 2030: 104},
         'afforestation': {2025: 275.4, 2030: 330.5}},
    'condi':
        {'nerica': {2025: 397.7, 2030: 397.7},
         'SRI': {2025: 707.0, 2030: 707.0},
         'transmission': {2025: 69.6, 2030: 98.7},
         'lighting': {2025: 42.9, 2030: 41.7},
         'heating': {2025: 19.3, 2030: 36.4},
         'RE_EE': {2025: 121.7, 2030: 174.4},
         'cook_stoves': {2025: 287.6, 2030: 278.4},
         'vehicle': {2025: 114.5, 2030: 193.3},
         'waste': {2025: 239.7, 2030: 413.7}}}

for yr in [2025, 2030]:
    sum_yr = 0.
    for condi in red.keys():
        sum_condi = 0.
        for sec in red[condi].keys():
            sum_yr += red[condi][sec][yr]
            sum_condi += red[condi][sec][yr]
        
        print(f"{yr} {condi}: {sum_condi :.1f} GgCO2eq")
    
    print(f"{yr} total: {sum_yr :.1f} GgCO2eq")

# Values do not fit to Figure 1. The reductions are way too high.

bau = {2025: 3.250, 2030: 3.850} # MtCO2eq, read from Figure 1.
RBU = {2025: -.444, 2030: -.454}
for yr in bau.keys():
    print(f"{yr} ABS: {bau[yr]*(1+RBU[yr]) :.3f} MtCO2eq")
    print(f"{yr} ABU: {bau[yr]*RBU[yr] :.3f} MtCO2eq")

# %%
