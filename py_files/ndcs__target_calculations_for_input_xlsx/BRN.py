# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 01/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
BRN
"""

# %%
# NDC2020

emi_bau = 29.5 # MtCO2eq, p. 1
tar_rbu = -.2 # p. 1
tar_abu = emi_bau * tar_rbu
tar_abs = emi_bau + tar_abu
print(f"ABS: {hpf.rnd(tar_abs, 1)} MtCO2eq")
print(f"ABU: {hpf.rnd(tar_abu, 1)} MtCO2eq")

# %%