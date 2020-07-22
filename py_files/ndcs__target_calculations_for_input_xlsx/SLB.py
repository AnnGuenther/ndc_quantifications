# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
SLB
"""

ABU = {'uncondi': {2025: -0.008, 2030: -0.008}, 'condi': {2025: -0.018800, 2030: -0.031125}}
RBU = {'uncondi': {2025: -.12, 2030: -.3}, 'condi': {2025: -.27, 2030: -.45}}

for condi in ABU.keys():
    for yr in ABU[condi].keys():
        emi_bau = 1/RBU[condi][yr]*ABU[condi][yr]
        ABS = emi_bau * (1+RBU[condi][yr])
        print(f"\nBAU {condi} {yr}: {emi_bau :.3f} MtCO2eq")
        print(f"ABS {condi} {yr}: {ABS :.3f} MtCO2eq")
        print(f"ABU {condi} {yr}: {ABU[condi][yr] :.3f} MtCO2eq")
        print(f"RBU {condi} {yr}: {100 * RBU[condi][yr] :.0f}%")

# %%
