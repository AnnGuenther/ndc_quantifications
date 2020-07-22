# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
KEN
"""

# ABS
emi_bau = 143 # MtCO2eq
red = -.3
print(f"ABS: {emi_bau * (1+red)} MtCO2eq")
print(f"ABU: {emi_bau * red} MtCO2eq")

# %%