# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
SYC
"""

# p. 8
ipc0_2000 = -0.564232
ipcmlulucf_2000 = 0.012540 - 0.837380
ipcm0el_2000 = ipc0_2000 - ipcmlulucf_2000
print(f"IPC0 2000: {ipc0_2000 :.6f} MtCO2eq")
print(f"IPCMLULUCF 2000: {ipcmlulucf_2000 :.6f} MtCO2eq")
print(f"IPCM0EL 2000: {ipcm0el_2000 :.6f} MtCO2eq")

# p. 11
ipc0_2005 = -0.502964
ipcm0el_2005 = 0.0310816
ipcmlulucf_2005 = ipc0_2005 - ipcm0el_2005
print(f"\nIPC0 2005: {ipc0_2005 :.6f} MtCO2eq")
print(f"IPCMLULUCF 2005: {ipcmlulucf_2005 :.6f} MtCO2eq")
print(f"IPCM0EL 2005: {ipcm0el_2005 :.6f} MtCO2eq")

# p. 11
emi = {2005: .310816, 2030: .911985}
removal  = {2005: -.813780, 2030: -.773896}

ipc0 = {}
for yr in emi.keys():
    ipc0[yr] = emi[yr] + removal[yr]
    print(f"IPC0 {yr}: {ipc0[yr] :.6f} MtCO2eq")

red = -.188
tar_ipc0 = ipc0[2030] + red
print(f"ABS IPC0: {tar_ipc0 :.6f} MtCO2eq")

# %%
