# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
HND
"""

# ABS.
emi_bau = 28.922
red = -.15
print(f"ABS target: {emi_bau * (1+red) :.3f} MtCO2eq")
print(f"ABU target: {emi_bau * red :.3f} MtCO2eq")

# %%
