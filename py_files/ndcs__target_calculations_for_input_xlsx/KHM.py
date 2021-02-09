# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
KHM
"""

# %%
# NDC2016

# EMI IPCM0EL from data given on p. 5.
ipcm0el = 11.600
ipcmlulucf = -7.897
ipc0 = ipcm0el + ipcmlulucf

emi_exclLU = ipc0 - ipcmlulucf
print(f"EMI IPCM0EL 2030: {emi_exclLU :.6f} MtCO2eq")

ABU_ipcm0el = -3.100 # MtCO2eq, this is compared to BAU.
ABU_lulucf = 7.897 - 18.492 # This is compared to 2010, not to BAU! We ignore that...
ABU_ipc0 = ABU_ipcm0el + ABU_lulucf
print(f"ABU IPC0: {ABU_ipc0} MtCO2eq")

# %%
# NDC2020

# p. 11
bau_2016_exclLU = 15.1 + 21.2 + 9.9 + 2.7
bau_2016_onlyLU = 76.3
bau_2016_inclLU = bau_2016_exclLU + bau_2016_onlyLU
print(f"\nBAU 2016 exclLU: {hpf.rnd(bau_2016_exclLU, 1)} MtCO2eq")
print(f"BAU 2016 inclLU: {hpf.rnd(bau_2016_inclLU, 1)} MtCO2eq")

bau_2030_exclLU = 34.3 + 27.1 + 13.9 + 3.3
bau_2030_onlyLU = 76.3
bau_2030_inclLU = bau_2030_exclLU + bau_2030_onlyLU
print(f"\nBAU 2030 exclLU: {hpf.rnd(bau_2030_exclLU, 1)} MtCO2eq")
print(f"BAU 2030 inclLU: {hpf.rnd(bau_2030_inclLU, 1)} MtCO2eq")

abs_2030_exclLU = 20.7 + 20.9 + 8.0 + 2.7
abs_2030_onlyLU = 38.2
abs_2030_inclLU = abs_2030_exclLU + abs_2030_onlyLU
print(f"\nABS 2030 exclLU: {hpf.rnd(abs_2030_exclLU, 1)} MtCO2eq")
print(f"ABS 2030 inclLU: {hpf.rnd(abs_2030_inclLU, 1)} MtCO2eq")

abu_2030_exclLU = -13.7 -6.2 -5.9 -0.6
abu_2030_onlyLU = -38.1
abu_2030_inclLU = abu_2030_exclLU + abu_2030_onlyLU
print(f"\nABU 2030 exclLU: {hpf.rnd(abu_2030_exclLU, 1)} MtCO2eq")
print(f"ABU 2030 inclLU: {hpf.rnd(abu_2030_inclLU, 1)} MtCO2eq")

rbu_2030_exclLU = 100 * abu_2030_exclLU / bau_2030_exclLU
rbu_2030_inclLU = 100 * abu_2030_inclLU / bau_2030_inclLU
print(f"\nRBU 2030 exclLU: {hpf.rnd(rbu_2030_exclLU, 1)} MtCO2eq")
print(f"RBU 2030 inclLU: {hpf.rnd(rbu_2030_inclLU, 1)} MtCO2eq")

# %%