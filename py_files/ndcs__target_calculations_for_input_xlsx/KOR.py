# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
KOR
"""

# %%
# NDC2016
emi_2030 = 850.6 # MtCO2eq, p. 1.
RBU = -.37

print(f"ABU: {emi_2030 * RBU :.1f} MtCO2eq")
print(f"ABS: {emi_2030 * (1+RBU) :.1f} MtCO2eq")

# %%
# NDC2020
emi_2017 = 709.1 # MtCO2eq
RBY = -.244
print(f"ABS: {hpf.rnd(emi_2017*(1+RBY), 1)} MtCO2eq")

# %%