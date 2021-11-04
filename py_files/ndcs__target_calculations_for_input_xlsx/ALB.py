# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
ALB
"""

# 0.708 MtCO2eq = 11.5% reduction.
red = 0.708
bau = 100/11.5*red
print(f"BAU: {bau :.3f} MtCO2eq")
print(f"ABS: {bau - red :.3f} MtCO2eq")

# %%
