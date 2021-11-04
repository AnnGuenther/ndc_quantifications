# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
TZA
"""

emi_bau = 145.5 # MtCO2eq
red = {'worst': -.1, 'best': -.2}

for tar in red.keys():
    ABS = emi_bau * (1 + red[tar])
    print(f"ABS {tar}: {ABS :.3f} MtCO2eq")
    print(f"ABU {tar}: {ABS - emi_bau :.3f} MtCO2eq")

# %%
