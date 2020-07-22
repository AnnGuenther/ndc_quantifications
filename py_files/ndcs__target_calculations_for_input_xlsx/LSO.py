# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
LSO
"""

# p. 25.
bau = {2025: 4.822, 2030: 5.713} # MtCO2eq
ABS = {'uncondi': {2025: 4.332, 2030: 5.142}, 'condi': {2025: 3.653, 2030: 3.737}}

for condi in ABS.keys():
    print(f"\n{condi}")
    for yr in bau.keys():
        print(f"ABU {yr}: {ABS[condi][yr] - bau[yr] :.3f} MtCO2eq")

# %%
