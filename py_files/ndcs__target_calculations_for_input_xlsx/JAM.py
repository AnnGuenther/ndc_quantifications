# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
JAM
"""

emi_bau = {2025: 13.443, 2030: 14.492} # MtCO2eq
emi_tar = {'uncondi': {2025: 12.370, 2030: 13.368}, 'condi': {2025: 12.099, 2030: 13.043}}

for condi in emi_tar.keys():
    for yr in emi_bau.keys():
        ABU = emi_tar[condi][yr] - emi_bau[yr]
        print(f"ABU {condi} {yr}: {ABU :.3f} MtCO2eq")
        print(f"RBU {condi} {yr}: {100*ABU/emi_bau[yr] :.1f}%")

# %%
