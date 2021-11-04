# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
COG
"""

# ABU from given ABS and BAU.
ABS = {2025: 8.793, 2035: 15.858}
BAU = {2025: 16.984, 2035: 34.527}

for year in ABS.keys():
    print(f"ABU {year}: {ABS[year] - BAU[year] :.3f} MtCO2eq_SAR")

# %%
