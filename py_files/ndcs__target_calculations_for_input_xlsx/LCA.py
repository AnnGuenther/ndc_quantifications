# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
LCA
"""

# ABS.
# From values given on p. 5.
bl = {2025: 0.758, 2030: 0.816}
abu = {2025: -0.121, 2030: -0.188}

for year in bl.keys():
    print(f"ABS {year}: {bl[year] + abu[year] :.3f} MtCO2eq")

# %%
