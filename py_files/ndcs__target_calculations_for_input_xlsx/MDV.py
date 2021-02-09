# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
MDV
"""

# %%
# NDC2016
emi_bau_energy_consumption = 3.3 # MtCO2eq, p. 2.
RBU = {'uncondi': -.1, 'condi': -.24}

for condi in RBU.keys():
    print(f"\n{condi} ABS (only energy consumption): {emi_bau_energy_consumption * (1+RBU[condi]) :.1f} MtCO2eq")
    print(f"{condi} ABU: {emi_bau_energy_consumption * RBU[condi] :.1f} MtCO2eq")

# %%
# NDC2020
bau_2030 = 3.28492 # MtCO2eq
tar_rbu = -.26
tar_abu = bau_2030 * tar_rbu
tar_abs = bau_2030 + tar_abu
print(f"ABU {hpf.rnd(tar_abu, 5)} MtCO2eq")
print(f"ABS {hpf.rnd(tar_abs, 5)} MtCO2eq")

# %%