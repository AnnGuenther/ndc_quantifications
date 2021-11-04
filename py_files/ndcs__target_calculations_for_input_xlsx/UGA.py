# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
UGA
"""

ipc0_2000 = 36.5 # MtCO2eq.
ipcmlulucf_2000 = 10.6
ipcm0el_2000 = ipc0_2000 - ipcmlulucf_2000
print(f"IPCM0EL 2000: {ipcm0el_2000 :.1f} MtCO2eq")

ipc0_2030 = 77.3 # MtCO2eq, p. 17.
ipcmlulucf_2030 = 8 # p. 18.
ipcm0el_2030 = ipc0_2030 - ipcmlulucf_2030
print(f"IPCM0EL 2030: {ipcm0el_2030 :.1f} MtCO2eq")

RBU_inclLU = -.22
ABS_inclLU = ipc0_2030*(1+RBU_inclLU)
ABU_inclLU = ABS_inclLU - ipc0_2030
print(f"ABS inclLU 2030: {ABS_inclLU} MtCO2eq")
print(f"ABU inclLU 2030: {ABU_inclLU} MtCO2eq")

RBU_inclLU_uncondi = RBU_inclLU * .3
ABS_inclLU_uncondi = ipc0_2030*(1+RBU_inclLU_uncondi)
ABU_inclLU_uncondi = ABS_inclLU_uncondi - ipc0_2030
print(f"RBU inclLU_uncondi 2030: {hpf.rnd(100*RBU_inclLU_uncondi, 1)}%")
print(f"ABS inclLU_uncondi 2030: {hpf.rnd(ABS_inclLU_uncondi, 1)} MtCO2eq")
print(f"ABU inclLU_uncondi 2030: {hpf.rnd(ABU_inclLU_uncondi, 1)} MtCO2eq")

# [p. 4]: 70% through international finance. 6.6% reduction unconditional?


# ABU_energy = -3.2 # p. 18
# ABU_forestry = -(16.9+22.2)/2
# ABU_wetlands = -.4

# ABU_ipcm0el = ABU_energy
# ABU_ipc0 = ABU_energy + ABU_forestry + ABU_wetlands
# print(f"ABU IPCM0EL: {ABU_ipcm0el :.1f} MtCO2eq")
# print(f"ABU IPC0: {ABU_ipc0 :.1f} MtCO2eq")

# ABS_ipcm0el = ipcm0el_2030 + ABU_ipcm0el
# ABS_ipc0 = ipc0_2030 + ABU_ipc0
# print(f"ABS IPCM0EL: {ABS_ipcm0el :.1f} MtCO2eq")
# print(f"ABS IPC0: {ABS_ipc0 :.1f} MtCO2eq")

# RBU_ipcm0el = ABU_ipcm0el/ipcm0el_2030*100
# RBU_ipc0 = ABU_ipc0/ipc0_2030*100
# print(f"RBU IPCM0EL: {RBU_ipcm0el :.1f}%")
# print(f"RBU IPC0: {RBU_ipc0 :.1f}%")

# # The given RBU is 22%, which is by how much ABS_ipc0 is smaller than ipc0_2030.
# # But: the values are more in line with a 30% reduction...

# %%
