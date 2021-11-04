# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
VCT
"""

emi_bau = 0.6 # MtCO2eq
RBU = -.22
print(f"ABS: {emi_bau * (1+RBU) :.3f} MtCO2eq")
print(f"ABU: {emi_bau * RBU :.3f} MtCO2eq")

# %%
