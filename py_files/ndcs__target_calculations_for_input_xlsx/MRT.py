# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
MRT
"""

# 12% of the given 22.3% reduction are unconditional.
uncondi = -22.3 * .12
print(f"RBU uncondi: {uncondi :.1f}%")
emi_bau = 18.84 # MtCO2eq
ABU_uncondi = uncondi/100 * emi_bau
print(f"ABU uncondi: {ABU_uncondi :.3f} MtCO2eq")
print(f"ABS uncondi: {emi_bau + ABU_uncondi :.3f} MtCO2eq")

ABU_condi = -4.2 # MtCO2eq (given)
print(f"ABS condi: {emi_bau + ABU_condi :.3f} MtCO2eq")

# Cumulated emissions per sector given [p. 4]
energy_ippu_dechets = 12711.1 + 30.5 + 386.1
agriculture_lulucf = 20431

# %%
