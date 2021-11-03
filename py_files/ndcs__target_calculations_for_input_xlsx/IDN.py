# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 10/2021.
"""

# %%
import numpy as np
import helpers_functions as hpf

# %%
"""
IDN
"""

# p. 3.
inclLU_2005 = 1800 # MtCO2eq
inclLU_2000 = inclLU_2005 - 400
print(f"inclLU 2000: {inclLU_2000} MtCO2eq")
inclLU_2012 = 1453

pc_lu_2005 = .63
pc_lu_2012 = .478
lu_2005 = pc_lu_2005*inclLU_2005
lu_2012 = pc_lu_2012*inclLU_2012
print(f"IPCMLULUCF 2005: {lu_2005} MtCO2eq")
print(f"IPCMLULUCF 2012: {lu_2012} MtCO2eq")

exclLU_2005 = inclLU_2005 - lu_2005
exclLU_2012 = inclLU_2012 - lu_2012
print(f"exclLU 2005: {exclLU_2005} MtCO2eq")
print(f"exclLU 2012: {exclLU_2012} MtCO2eq")

# Table 1 [p. 10]
emi = {
    2010: {'IPC1': 453.2, 'IPC4': 88, 'IPC2': 36, 'IPCMAG': 110.5, 'IPCMLULUCF': 647},
    2030: {'IPC1': 1669, 'IPC4': 296, 'IPC2': 69.6, 'IPCMAG': 119.66, 'IPCMLULUCF': 714}}

# EMI exclLU.
for year in emi.keys():
    data = sum([emi[year][xx] for xx in emi[year].keys() if xx != 'IPCMLULUCF'])
    print(f"exclLU {year}: {data :.3f} MtCO2eq")

# ABS exclLU.
print(f"ABS unconditional exclLU 2030: {2034 - 217} MtCO2eq") # Table 1.
print(f"ABS conditional exclLU 2030: {1787 - 64} MtCO2eq")

# ABU exclLU.
ABU_exclLU = {'uncondi': -834 + 497, 'condi': -1081 + 650}
print(f"ABU unconditional exclLU 2030: {ABU_exclLU['uncondi']} MtCO2eq") # Table 1.
print(f"ABU conditional exclLU 2030: {ABU_exclLU['condi']} MtCO2eq")

bau_inclLU = 2869
bau_LU = 714
bau_exclLU = bau_inclLU - bau_LU
# RBU exclLU.
for condi in ABU_exclLU.keys():
    print(f"RBU {condi} exclLU 2030: {ABU_exclLU[condi]/bau_exclLU*100 :.1f}%")

# We calculate the 41% (inclLU) reduction assuming that the additional reductions (compared to the 
# 38% reduction) are in the Energy and Forestry sectors only, and in equal parts.
ABS_inclLU_41 = bau_inclLU * (1-.41)
ABU_inclLU_41 = bau_inclLU * -.41
print(f"\nABS 41% inclLU: {ABS_inclLU_41 :.3f} MtCO2eq")
print(f"ABU 41% inclLU: {ABU_inclLU_41 :.3f} MtCO2eq")
ABS_inclLU_38 = 1787
additional_red_exclLU_41 = - (ABS_inclLU_38 - ABS_inclLU_41)/2
ABS_exclLU_38 = 1723
ABS_exclLU_41 = ABS_exclLU_38 + additional_red_exclLU_41
ABU_exclLU_41 = ABS_exclLU_41 - bau_exclLU
print(f"ABS 41% exclLU: {ABS_exclLU_41 :.3f} MtCO2eq")
print(f"ABU 41% exclLU: {ABU_exclLU_41 :.3f} MtCO2eq")

# Calculate RBU condi_worst exclLU from the given uncondi_best and condi_best (inclLU and exclLU).
# Assuming linear relation.
print(f"RBU condi_worst exclLU: {-np.interp(38.24, [29, 41], [15.60, 20.00]) :.1f}%")
# Or from ABS: print(f"RBU condi_worst exclLU: {-np.interp(1723, [1817, 1675.855], [15.6, 20]) :.1f}%")

# %%
# NDC 07/2021

# MtCO2eq, p. 22
inclLU_2010 = 1334
inclLU_2030 = 2869
ipcmlulucf_2010 = 647
ipcmlulucf_2030 = 714

exclLU_2010 = inclLU_2010 - ipcmlulucf_2010
exclLU_2030 = inclLU_2030 - ipcmlulucf_2030

print(f"\nexclLU 2010: {hpf.rnd(exclLU_2010, 0)} MtCO2eq_AR4")
print(f"exclLU 2030: {hpf.rnd(exclLU_2030, 0)} MtCO2eq_AR4")

inclLU_abs_2030_uncondi = 2034
inclLU_abs_2030_condi = 1927
exclLU_abs_2030_uncondi = 1355 + 285 + 66.85 + 110.39
exclLU_abs_2030_condi = (1669-441) + 270 + 66.35 + 115.86
# In Table 1 there seems to be an error for the CM2 Energy and FOLU level...
inclLU_abs_2030_condi = (1669-441) + 270 + 66.35 + 115.86 + (714-692)
# That does not give the same result as CM2 1927...

# Table 1, p. 22:

# 2010 emissions
exclLU = 453.2+88+36+110.5
inclLU = exclLU + 647
print(f'\nexclLU 2010: {hpf.rnd(exclLU, 2)}')
print(f'inclLU 2010: {hpf.rnd(inclLU, 2)}') # as in table

# BAU 2030
bau_exclLU = 1669+296+69.6+119.66
bau_inclLU = bau_exclLU + 714
print(f'\nexclLU 2030: {hpf.rnd(bau_exclLU, 2)}')
print(f'inclLU 2030: {hpf.rnd(bau_inclLU, 2)}') # as in table

# CM1 emi
exclLU = 1355+285+66.85+110.39
inclLU = exclLU + 217
print(f'\nexclLU CM1 2030: {hpf.rnd(exclLU, 2)}')
print(f'inclLU CM1 2030: {hpf.rnd(inclLU, 2)}') # as in table

# CM2 emi
exclLU = 1407+270+66.35+115.86
inclLU = exclLU + 68
print(f'\nexclLU CM2 2030: {hpf.rnd(exclLU, 2)}')
print(f'inclLU CM2 2030: {hpf.rnd(inclLU, 2)}') # as in table

# GHG reduction, emi, CM1
exclLU = 314+11+2.75+9
inclLU = exclLU + 497
print(f'\nexclLU CM1 2030: {hpf.rnd(exclLU, 2)}')
print(f'inclLU CM1 2030: {hpf.rnd(inclLU, 2)}') # as in table

# GHG reduction, emi, CM2
exclLU = 441+26+3.25+4
inclLU = exclLU + 692
print(f'\nexclLU CM2 2030: {hpf.rnd(exclLU, 2)}')
print(f'inclLU CM2 2030: {hpf.rnd(inclLU, 2)}') # as in table

# GHG reduction, %, CM1
exclLU = 11+0.38+0.10+0.32
inclLU = exclLU + 17.2
print(f'\nexclLU CM1 2030: {hpf.rnd(exclLU, 2)}')
print(f'inclLU CM1 2030: {hpf.rnd(inclLU, 2)}') # as in table

# GHG reduction, %, CM2
exclLU = 15.5+1.0+0.11+0.13
inclLU = exclLU + 24.5
print(f'\nexclLU CM1 2030: {hpf.rnd(exclLU, 2)}')
print(f'inclLU CM1 2030: {hpf.rnd(inclLU, 2)}') # as in table

print(f'\nrbu_energy: {hpf.rnd(100*314/2869, 0)}%') # as in table, 11%
print(f'rbu_waste: {hpf.rnd(100*11/2869, 2)}%') # as in table, 0.38%
print(f'rbu_ippu: {hpf.rnd(100*2.75/2869, 2)}%') # as in table, 1.0%
print(f'rbu_agri: {hpf.rnd(100*9/2869, 2)}%') # as in table, 0.31% (table 0.32%)
print(f'rbu_folu: {hpf.rnd(100*497/2869, 1)}%') # as in table, 17.3% (table 17.3%)

# We assume the values for the emission reduction (absolute and %) as correct.
# The Energy CM2 emissions level should probably be
print(f'\nenergy CM2 emissions level should probably be: {hpf.rnd(1669-441, 0)} instead of 1407')
# The FOLU CM2 emissions level should probably be
print(f'folu CM2 emissions level should probably be: {hpf.rnd(714-692, 0)} instead of 68')
# The total CM2 emissions level should probably be
# exclLU
cm2_abs_exclLU = (1669 - 441) + (296 - 26) + (69.6 - 3.25) + (119.66 - 4)
cm2_abs_inclLU = cm2_abs_exclLU + (714 - 692)
cm2_rbu_exclLU = -(100 - cm2_abs_exclLU/bau_exclLU*100)
cm2_rbu_inclLU = -(100 - cm2_abs_inclLU/bau_inclLU*100)
cm2_abu_exclLU = cm2_rbu_exclLU/100 * bau_exclLU
cm2_abu_inclLU = cm2_rbu_inclLU/100 * bau_inclLU

print(f'\ncm2 abs exclLU: {hpf.rnd(cm2_abs_exclLU, 0)} MtCO2eq') # 1680
print(f'cm2 abs inclLU: {hpf.rnd(cm2_abs_inclLU, 0)} MtCO2eq instead of 1927') # 1702
print(f'cm2 rbu exclLU: {hpf.rnd(cm2_rbu_exclLU, 0)}%') # 22%
print(f'cm2 rbu inclLU: {hpf.rnd(cm2_rbu_inclLU, 0)}%') # 41%, as in table
print(f'cm2 abu exclLU: {hpf.rnd(cm2_abu_exclLU, 0)} MtCO2eq') # -474
print(f'cm2 abu inclLU: {hpf.rnd(cm2_abu_inclLU, 0)} MtCO2eq') # -1166, as in table

#########
cm1_abs_exclLU = (1669 - 314) + (296 - 11) + (69.6 - 2.75) + (119.66 - 9)
cm1_abs_inclLU = cm1_abs_exclLU + (714 - 497)
cm1_rbu_exclLU = -(100 - cm1_abs_exclLU/bau_exclLU*100)
cm1_rbu_inclLU = -(100 - cm1_abs_inclLU/bau_inclLU*100)
cm1_abu_exclLU = cm1_rbu_exclLU/100 * bau_exclLU
cm1_abu_inclLU = cm1_rbu_inclLU/100 * bau_inclLU

print(f'\ncm1 abs exclLU: {hpf.rnd(cm1_abs_exclLU, 0)} MtCO2eq') # 1680
print(f'cm1 abs inclLU: {hpf.rnd(cm1_abs_inclLU, 0)} MtCO2eq instead of 1927') # 1702
print(f'cm1 rbu exclLU: {hpf.rnd(cm1_rbu_exclLU, 0)}%') # 22%
print(f'cm1 rbu inclLU: {hpf.rnd(cm1_rbu_inclLU, 0)}%') # 41%, as in table
print(f'cm1 abu exclLU: {hpf.rnd(cm1_abu_exclLU, 0)} MtCO2eq') # -474
print(f'cm1 abu inclLU: {hpf.rnd(cm1_abu_inclLU, 0)} MtCO2eq') # -1166, as in table

# %%