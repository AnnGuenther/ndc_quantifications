# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
AGO
"""
bau = {2025: 155.819, 2030: 193.250}
ABS = {2025: {'uncondi': 124.656, 'condi': 113.748},
       2030: {'uncondi': 125.612, 'condi': 96.625}}
for year in bau.keys():
    for condi in ABS[year].keys():
        print(f"{year} {condi}: {ABS[year][condi] - bau[year] :.3f} MtCO2eq")

# %%
# NDC2021


# p. 42 (probably in MtCO2eq ...)
emi_2015_inclLU = 99.992231
emi_2015_onlyLU = 70.360442

emi_2015_exclLU = emi_2015_inclLU- emi_2015_onlyLU
print(f"EMI 2015 exclLU: {hpf.rnd(emi_2015_exclLU, 6)} MtCO2eq")

emi_bau_2025 = 108.47339
rbu_uncondi = -.14
abs_uncondi = emi_bau_2025 * (1+rbu_uncondi)
print(f"ABS uncondi 2025: {hpf.rnd(abs_uncondi, 6)} MtCO2eq")

# %%