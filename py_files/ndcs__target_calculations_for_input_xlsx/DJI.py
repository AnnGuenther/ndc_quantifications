# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
DJI
"""

emi_bau = 4.475 # MtCO2eq
ABS_uncondi = 2.685
ABS_condi = 1.790
print(f"ABU uncondi: {ABS_uncondi - emi_bau :.3f} MtCO2eq")
print(f"ABU condi: {ABS_condi - emi_bau :.3f} MtCO2eq")

# %%
