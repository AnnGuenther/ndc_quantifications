# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
TLS
"""

emi_2015 = {'CO2': 0.46687, 'CH4': .54856, 'N2O': .46718}
emi_tot = sum([emi_2015[xx] for xx in emi_2015.keys()])
print(f"emi: {emi_tot} MtCO2eq")

# %%
