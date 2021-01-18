# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 01/2021
"""

# %%
import helpers_functions as hpf

# %%
"""
GRD
"""

# NDC2020
emi_inclLU_2010 = 0.2169 # MtCO2eq, p. 4
tar_rby = -.4 # p. 4
tar_abs = emi_inclLU_2010 * (1+tar_rby)
print(f"absolute target inclLU: {hpf.rnd(tar_abs, 4)} MtCO2eq")

# %%