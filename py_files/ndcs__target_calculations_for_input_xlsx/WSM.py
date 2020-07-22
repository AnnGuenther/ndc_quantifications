# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
WSM
"""

# Electricity subsector in 2014 was 13% of total:
elec = 0.055065 # MtCO2eq
pc = .13

print(f"Total emissions in 2014: {1/pc*elec :.6f} MtCO2eq")

# %%
