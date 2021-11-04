# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 01/2021
"""

# %%
import helpers_functions as hpf

# %%
"""
RUS
"""

# %%
# NDC2020
emi_1990 = 3100
tar_rby = -.3
print(f"ABS: {hpf.rnd(emi_1990 * (1+tar_rby), 0)} MtCO2eq")

# %%