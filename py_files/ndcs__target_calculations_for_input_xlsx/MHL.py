# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
MHL
"""

# %%
# NDC20xx

emi_2010 = .185 # MtCO2eq, p. 3
RBU = {2025: -.32, 2030: -.45, 2035: -.58}

for yr in RBU.keys():
    print(f"ABS {yr}: {emi_2010 * (1+RBU[yr]) :.3f} MtCO2eq")

# %%
# NDC2020

emi_2010 = .168 # MtCO2eq, p. 72 Climate Strategy
RBU = {2025: -.32, 2030: -.45, 2035: -.58}

for yr in RBU.keys():
    print(f"ABS {yr}: {hpf.rnd(emi_2010 * (1+RBU[yr]), 3)} MtCO2eq")

# %%