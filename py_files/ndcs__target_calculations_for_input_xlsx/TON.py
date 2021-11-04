# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last update: 11/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
TON
"""

# %%
# NDC2020

energy_2006 = 0.1204 # p. 26
aby_2025 = -0.016 # p. 27, absolute reduction compared to 2006
# Convert ABY into RBY (for energy sector only).
print(f"RBY (energy sector): {hpf.rnd(100*aby_2025/energy_2006, 1)}%")

# %%