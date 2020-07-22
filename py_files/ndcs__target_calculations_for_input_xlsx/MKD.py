# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
MKD
"""

emi_bau = 17.663 # MtCO2eq
ABS = {'worst': 12.435, 'best': 11.359}

for rge in ABS.keys():
    print(f"{rge}: {ABS[rge] - emi_bau :.3f} MtCO2eq")

# %%
