# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
GIN
"""

emi_bau = 55 # MtCO2eq
RBU = -.3
ABU = emi_bau * RBU
ABS = emi_bau + ABU
print(f"ABU: {ABU} MtCO2eq")
print(f"ABS: {ABS} MtCO2eq")

# %%
