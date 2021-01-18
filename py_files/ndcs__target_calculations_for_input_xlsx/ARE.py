# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 01/2021
"""

# %%
import helpers_functions as hpf

# %%
"""
ARE
"""

# %%
# NDC2020

bau_2030 = 310 # MtCO2eq
tar_rbu = -.235
tar_abu = bau_2030*tar_rbu
tar_abs = bau_2030+tar_abu
print(f"ABU: {hpf.rnd(tar_abu, 0)} MtCO2eq")
print(f"ABS: {hpf.rnd(tar_abs, 0)} MtCO2eq")

# %%

