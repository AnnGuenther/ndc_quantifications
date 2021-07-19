# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
HND
"""

# %%
# ABS.
emi_bau = 28.922
red = -.15
print(f"ABS target: {emi_bau * (1+red) :.3f} MtCO2eq")
print(f"ABU target: {emi_bau * red :.3f} MtCO2eq")

# %%
# ABS
emi_bau = 28.945
red = -.16
print(f"ABS target: {hpf.rnd(emi_bau * (1+red), 3)} MtCO2eq")
print(f"ABU target: {hpf.rnd(emi_bau * red, 3)} MtCO2eq")

# %%