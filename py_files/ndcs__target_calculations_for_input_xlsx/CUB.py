# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
CUB
"""

# p. 16
emi_brutto_2010 = 40 # MtCO2eq
emi_brutto_1990 = 100/84*emi_brutto_2010
print(f"emi brutto 1990: {emi_brutto_1990 :.1f} MtCO2eq")
emi_energy_2010 = .76*emi_brutto_2010
emi_agri_2010 = .15*emi_brutto_2010
emi_waste_ippu = .09*emi_brutto_2010

# %%
