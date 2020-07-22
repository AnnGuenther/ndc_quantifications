# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
ZMB
"""

RBU = {'worst': -.25, 'best': -.47}
ABU = {'worst': -20, 'best': -38}

for rge in RBU.keys():
    emi_bau = 1/RBU[rge]*ABU[rge]
    print(f"{rge} BAU: {emi_bau :.1f} MtCO2eq")
    ABS = emi_bau + ABU[rge]
    print(f"{rge} ABS: {ABS :.1f} MtCO2eq")

# %%