# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
SEN
"""

bau = {2025: 30.0, 2030: 37.5} # MtCO2eq, read from Figure 1, p. 14.
RBU = {'uncondi': {2025: -.04, 2030: -.05},
       'condi': {2025: -.15, 2030: -.21}}
for yr in bau.keys():
    for condi in RBU.keys():
        print(f"\n{yr} {condi} ABS: {bau[yr] * (1+RBU[condi][yr]) :.1f} MtCO2eq")
        print(f"{yr} {condi} ABU: {bau[yr] * RBU[condi][yr] :.1f} MtCO2eq")

# %%