# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
KOR
"""

emi_2030 = 850.6 # MtCO2eq, p. 1.
RBU = -.37

print(f"ABU: {emi_2030 * RBU :.1f} MtCO2eq")
print(f"ABS: {emi_2030 * (1+RBU) :.1f} MtCO2eq")

# %%
