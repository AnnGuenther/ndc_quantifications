# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
CHE
"""

# %%
# NDC2015

ipcm0el_1990 = 53.3
red = {'best': {2025: -.35, 2030: -.5, 2050: -.85}, 'worst': {2050: -.7}}

for rge in red.keys():
    data = red[rge]
    for year in data.keys():
        print(f"{rge} {year}: {ipcm0el_1990 * (1 + data[year]) :.3f}")

# %%
# NDC2020

emi_exclLU_1990= 54.15892
tar_rby = -.5
tar_abu = tar_rby*emi_exclLU_1990
tar_abs = (1+tar_rby)*emi_exclLU_1990
print(f"ABU: {hpf.rnd(tar_abu, 5)} MtCO2eq")
print(f"ABS: {hpf.rnd(tar_abs, 5)} MtCO2eq")

# %%