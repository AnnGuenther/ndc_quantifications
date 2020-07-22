# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
DOM
"""

emi_2010 = 3.6 # tCO2eq per capita, p. 2
REI = -.25

print(f"AEI: {emi_2010 * (1+REI) :.1f} tCO2eq/capita")

# %%
