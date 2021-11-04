# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
NAM
"""

# Conditional
bau = 22.647 # MtCO2eq
RBU = -.1
print(f"ABU: {bau*RBU :.3f} MtCO2eq")
print(f"ABS: {bau*(1+RBU) :.3f} MtCO2eq")

# %%