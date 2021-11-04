# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
MDG
"""

ABS_emissions = 214.206-30
ABS_absorptions = -192.111-61 # MtCO2eq, p. 2

print(f"ABS (incl. LULUCF): {ABS_emissions + ABS_absorptions :.3f} MtCO2eq")
print(f"ABS (emissions, might include some LULUCF emissions): {ABS_emissions :.3f} MtCO2eq")

# %%
