# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
LCA
"""

# %%
# NDC2016

# ABS.
# From values given on p. 5.
bl = {2025: 0.758, 2030: 0.816}
abu = {2025: -0.121, 2030: -0.188}

for year in bl.keys():
    print(f"ABS {year}: {bl[year] + abu[year] :.3f} MtCO2eq")

# %%
# NDC2021

emi_exclLU_2010 = 0.643 # p. 11
emi_inclLU_2010 = 0.572 # p. 11
emi_onlyLU_2010 = emi_inclLU_2010 - emi_exclLU_2010

print(f"EMI onlyLU 2010: {hpf.rnd(emi_onlyLU_2010, 3)} MtCO2eq")

# 2010 energy emissions: 505 GgCO2eq, reduction: 7.2% or 37 GgCO2eq. p. 4+11
aby = 0.037
abs_2030_exclLU = emi_exclLU_2010 - aby

print(f"ABS exclLU 2030: {hpf.rnd(abs_2030_exclLU, 3)} MtCO2eq")

# %%