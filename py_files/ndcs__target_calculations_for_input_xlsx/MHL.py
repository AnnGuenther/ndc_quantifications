# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
MHL
"""

emi_2010 = .185 # MtCO2eq, p. 3
RBU = {2025: -.32, 2030: -.45, 2035: -.58}

for yr in RBU.keys():
    print(f"ABS {yr}: {emi_2010 * (1+RBU[yr]) :.3f} MtCO2eq")

# %%
