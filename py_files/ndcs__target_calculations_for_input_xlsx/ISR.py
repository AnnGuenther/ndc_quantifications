# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
ISR
"""

emi_2030 = 105.5 # MtCO2eq
ABU_2030 = -23.85
print(f"RBU 2030: {100*ABU_2030/emi_2030 :.1f}%")

AEI = {2025: 8.8, 2030: 7.7}
emi_per_cap_2005 = 10.4

for yr in AEI.keys():
    print(f"REI {yr}: {(AEI[yr]/emi_per_cap_2005 - 1) * 100. :.1f}%")

# %%