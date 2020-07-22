# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
MDV
"""

emi_bau_energy_consumption = 3.3 # MtCO2eq, p. 2.
RBU = {'uncondi': -.1, 'condi': -.24}

for condi in RBU.keys():
    print(f"\n{condi} ABS (only energy consumption): {emi_bau_energy_consumption * (1+RBU[condi]) :.1f} MtCO2eq")
    print(f"{condi} ABU: {emi_bau_energy_consumption * RBU[condi] :.1f} MtCO2eq")

# %%
