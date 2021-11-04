# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last update: 2/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
NIC
"""

# %%
# NDC2020

# p. 61
bau = 77.331
abs_best = 69.573
abs_worst = 71.231

print(f"ABU best: {hpf.rnd(abs_best - bau, 3)} MtCO2eq")
print(f"ABU worst: {hpf.rnd(abs_worst - bau, 3)} MtCO2eq")

# %%
