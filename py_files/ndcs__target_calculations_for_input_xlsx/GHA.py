# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
GHA
"""

emi_bau = {2025: 53.5, 2030: 73.95}
RBU = {'uncondi': {2025: -.12, 2030: -.15},
       'condi': {2025: -.27, 2030: -.45}}

for condi in RBU.keys():
    print(f"\n{condi}")
    for yr in emi_bau.keys():
        print(f"{yr}")
        print(f"ABS: {emi_bau[yr]*(1+RBU[condi][yr]) :.2f} MtCO2eq")
        print(f"ABU: {emi_bau[yr]*RBU[condi][yr] :.2f} MtCO2eq")

# %%
