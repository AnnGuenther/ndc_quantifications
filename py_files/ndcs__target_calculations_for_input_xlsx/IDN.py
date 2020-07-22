# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import numpy as np

# %%
"""
IDN
"""

# p. 3.
ipc0_2005 = 1800 # MtCO2eq
ipc0_2000 = ipc0_2005 - 400
print(f"IPC0 2000: {ipc0_2000} MtCO2eq")
ipc0_2012 = 1453

pc_lu_2005 = .63
pc_lu_2012 = .478
lu_2005 = pc_lu_2005*ipc0_2005
lu_2012 = pc_lu_2012*ipc0_2012
print(f"IPCMLULUCF 2005: {lu_2005} MtCO2eq")
print(f"IPCMLULUCF 2012: {lu_2012} MtCO2eq")

ipcm0el_2005 = ipc0_2005 - lu_2005
ipcm0el_2012 = ipc0_2012 - lu_2012
print(f"IPCM0EL 2005: {ipcm0el_2005} MtCO2eq")
print(f"IPCM0EL 2012: {ipcm0el_2012} MtCO2eq")

# Table 1 [p. 10]
emi = {
    2010: {'IPC1': 453.2, 'IPC4': 88, 'IPC2': 36, 'IPCMAG': 110.5, 'IPCMLULUCF': 647},
    2030: {'IPC1': 1669, 'IPC4': 296, 'IPC2': 69.6, 'IPCMAG': 119.66, 'IPCMLULUCF': 714}}

# EMI IPCM0EL.
for year in emi.keys():
    data = sum([emi[year][xx] for xx in emi[year].keys() if xx != 'IPCMLULUCF'])
    print(f"IPCM0EL {year}: {data :.3f} MtCO2eq")

# ABS IPCM0EL.
print(f"ABS unconditional IPCM0EL 2030: {2034 - 217} MtCO2eq") # Table 1.
print(f"ABS conditional IPCM0EL 2030: {1787 - 64} MtCO2eq")

# ABU IPCM0EL.
ABU_ipcm0el = {'uncondi': -834 + 497, 'condi': -1081 + 650}
print(f"ABU unconditional IPCM0EL 2030: {ABU_ipcm0el['uncondi']} MtCO2eq") # Table 1.
print(f"ABU conditional IPCM0EL 2030: {ABU_ipcm0el['condi']} MtCO2eq")

bau_inclLU = 2869
bau_LU = 714
bau_exclLU = bau_inclLU - bau_LU
# RBU IPCM0EL.
for condi in ABU_ipcm0el.keys():
    print(f"RBU {condi} IPCM0EL 2030: {ABU_ipcm0el[condi]/bau_exclLU*100 :.1f}%")

# We calculate the 41% (inclLU) reduction assuming that the additional reductions (compared to the 
# 38% reduction) are in the Energy and Forestry sectors only, and in equal parts.
ABS_inclLU_41 = bau_inclLU * (1-.41)
ABU_inclLU_41 = bau_inclLU * -.41
print(f"\nABS 41% inclLU: {ABS_inclLU_41 :.3f} MtCO2eq")
print(f"ABU 41% inclLU: {ABU_inclLU_41 :.3f} MtCO2eq")
ABS_inclLU_38 = 1787
additional_red_IPCM0EL_41 = - (ABS_inclLU_38 - ABS_inclLU_41)/2
ABS_exclLU_38 = 1723
ABS_exclLU_41 = ABS_exclLU_38 + additional_red_IPCM0EL_41
ABU_exclLU_41 = ABS_exclLU_41 - bau_exclLU
print(f"ABS 41% exclLU: {ABS_exclLU_41 :.3f} MtCO2eq")
print(f"ABU 41% exclLU: {ABU_exclLU_41 :.3f} MtCO2eq")

# Calculate RBU condi_worst exclLU from the given uncondi_best and condi_best (inclLU and exclLU).
# Assuming linear relation.
print(f"RBU condi_worst exclLU: {-np.interp(38.24, [29, 41], [15.60, 20.00]) :.1f}%")
# Or from ABS: print(f"RBU condi_worst exclLU: {-np.interp(1723, [1817, 1675.855], [15.6, 20]) :.1f}%")

# %%