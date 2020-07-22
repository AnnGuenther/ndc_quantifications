# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
CRI
"""

ABS = 9.374000 # MtCO2eq
RBU = -.44
bau = 1/(1+RBU)*ABS
ABU = RBU*bau
print(f"2030 BAU: {bau :.3f} MtCO2eq")
print(f"2030 ABU: {ABU :.3f} MtCO2eq")

# %%