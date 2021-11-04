# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
MKD
"""

# %%
# NDC2015

emi_bau = 17.663 # MtCO2eq
ABS = {'worst': 12.435, 'best': 11.359}

for rge in ABS.keys():
    print(f"{rge}: {ABS[rge] - emi_bau :.3f} MtCO2eq")

# %%
# NDC2021

# p. 9, MtCO2eq
emi_1990_exclLU = 12.478
emi_1990_inclLU = 12.271

emi_1990_onlyLU = emi_1990_inclLU - emi_1990_exclLU
print(f"EMI 1990 onlyLU: {hpf.rnd(emi_1990_onlyLU, 3)} MtCO2eq")

# %%
