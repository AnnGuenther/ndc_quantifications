# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
COL
"""

# %%
# NDC2015

emi_bau = 335
pc_red = {'unconditional': -.2, 'conditional': -.3}

# ABS.
# -20% on BAU [e.g., p. 8]
for condi in pc_red.keys():
    print(f"ABS 2030 {condi}: {emi_bau * (1 + pc_red[condi]) :.3f} MtCO2eq")

# ABU.
# -20% on BAU [e.g., p. 8]
for condi in pc_red.keys():
    print(f"ABU 2030 {condi}: {pc_red[condi] * emi_bau :.3f} MtCO2eq")

# %%
# NDC2020

# p. 31
bau_inclLU = {2015: 233.58, 2020: 291.30, 2025: 332.70, 2030: 345.80}
# p. 32
bau_onlyLU = {2015: 61.65 + 16.91, 2020: 102.31 + 19.37, 2025: 111.80 + 19.95, 2030: 97.36 + 20.58}
for year in bau_onlyLU.keys():
    print(f"\n{year} onlyLU: {hpf.rnd(bau_onlyLU[year], 2)} MtCO2eq")
    print(f"{year} exclLU: {hpf.rnd(bau_inclLU[year] - bau_onlyLU[year], 2)} MtCO2eq")

abu = 169.44 - 345.442 # p. 34 and p. 31.
print(f"\nABU 2030: {abu} MtCO2eq")

# %%
