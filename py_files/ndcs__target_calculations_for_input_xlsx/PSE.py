# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
PSE
"""

# Status quo scenario.
bau = 9.1 # MtCO2eq
RBU = -.128
print(f"ABS: {bau*(1+RBU) :.1f} MtCO2eq")
print(f"ABU: {bau*RBU :.1f} MtCO2eq")

# %%
