# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
COK
"""

emi_tot = 0.069574 # MtCO2eq

pc_electricity = .34
emi_electricity = emi_tot * pc_electricity
print(f"emi electricity: {emi_electricity :.6f} MtCO2eq") # Fits to values in Figure 2, p. 1.

pc_energy = .79
emi_energy = emi_tot * pc_energy
print(f"emi Energy: {emi_energy :.6f} MtCO2eq")

RBY = {2020: -.38, 2030: -.81} # Only electricity

for yr in RBY.keys():
    ABY = emi_electricity * RBY[yr]
    print(f"\nABY {yr}: {ABY :.6f} MtCO2eq")
    print(f"ABS {yr}: {emi_tot + ABY :.6f} MtCO2eq")
    print(f"RBY {yr} compared to emi_energy: {100.*ABY/emi_energy :.1f}%")
    print(f"\nABS {yr} only electricity (comparison with Figure 2): {emi_electricity + ABY :.6f} MtCO2eq")

# %%
