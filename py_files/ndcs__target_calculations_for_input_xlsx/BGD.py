# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
BGD
"""

# p. 3
# 69% of BAU in 2030 is 234 MtCO2eq.
bau_2030 = 100/69*234
print(f"BAU in 2030 (IPCM0EL): {bau_2030 :.3f} MtCO2eq")

# ABS from BAU and given ABU. [p. 3].
print(f"ABS unconditional: {bau_2030 - 12 :.3f} MtCO2eq")
print(f"ABS conditional: {bau_2030 - 36 :.3f} MtCO2eq")

# %%
