# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
BRB
"""

RBU = {2025: -.37, 2030: -.44}
emi_bau = {2025: 2.2822, 2030: 2.5025}

for yr in RBU.keys():
    print(f"\n{yr} ABS: {emi_bau[yr] * (1+RBU[yr]) :.4f} MtCO2eq")
    print(f"{yr} ABU: {emi_bau[yr] * RBU[yr] :.4f} MtCO2eq")

# %%
