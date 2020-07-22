# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
ERI
"""

# p. 20
bau = {2025: 9379, 2030: 11466} # ktCO2eq
ABU = {'uncondi': {2025: -376, 2030: -982},
       'condi': {2025: -1518, 2030: -3152}}

for condi in ABU.keys():
    for yr in bau.keys():
        print(f"ABS {condi} {yr}: {0.001*(bau[yr]+ABU[condi][yr])} MtO2eq")

# %%
