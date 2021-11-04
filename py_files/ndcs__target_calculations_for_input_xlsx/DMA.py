# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
DMA
"""

emi = .1645 # MtCO2eq
red = {2025: -.392, 2030: -.447}

for yr in red.keys():
    print(f"\n{yr}")
    print(f"ABS: {emi*(1+red[yr]) :.3f} MtCO2eq")
    print(f"ABU: {emi*red[yr] :.3f} MtCO2eq")

# %%
