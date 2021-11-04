# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import numpy as np

# %%
"""
CAF
"""

# p. 6, emissions per sector
print('\n', 2010)

emi_2010 = {'lu': 104.02897, 'agri': 6.12000, 'autr_ener': 0.33094, 
            'bois_ener': 5.70454, 'dechets': 0.10055, 'ippu': 0.00013} # MtCO2eq
emi_total_2010 = 116.2855 # excluding sequestration, p. 7
pc_lu_2010 = emi_2010['lu']/emi_total_2010
sequestration_2010 = -330.000

emi_ipcm0el_2010 = 0
for cat in [xx for xx in emi_2010.keys() if xx != 'lu']:
    emi_ipcm0el_2010 += emi_2010[cat]

print(f"IPCM0EL: {emi_ipcm0el_2010 :.4f} MtCO2eq")

emi_lu_2010 = emi_2010['lu'] + sequestration_2010
emi_ipc0_2010 = emi_ipcm0el_2010 + emi_lu_2010

print(f"IPC0: {emi_ipc0_2010 :.4f} MtCO2eq")
print(f"IPCMLULUCF: {emi_lu_2010 :.4f} MtCO2eq")

print('\n', 2050) # p. 7

pc_2050 = {'lu': .684, 'energy': .134, 'agri': .134, 'water': .032, 'ippu': .016}
emi_total_2050 = 189.2718 # excluding sequestration
pc_lu_2050 = pc_2050['lu']
sequestration_2050 = -310.14643
emi_2050 = {}
for cat in pc_2050.keys():
    emi_2050[cat] = pc_2050[cat] * emi_total_2050
    print(f"2050 {cat}: {emi_2050[cat] :.4f} MtCO2eq")

emi_ipcm0el_2050 = 0
for cat in [xx for xx in emi_2050.keys() if xx!= 'lu']:
    emi_ipcm0el_2050 += emi_2050[cat]

print(f"IPCM0EL: {emi_ipcm0el_2050 :.4f} MtCO2eq")

emi_lu_2050 = emi_2050['lu'] + sequestration_2050
emi_ipc0_2050 = emi_ipcm0el_2050 + emi_lu_2050

print(f"IPC0: {emi_ipc0_2050 :.4f} MtCO2eq")
print(f"IPCMLULUCF: {emi_lu_2050 :.4f} MtCO2eq")

sequestration_2030 = np.interp(2030, [2010, 2050], [sequestration_2010, sequestration_2050])
print(f"\nSequestration in 2030: {sequestration_2030} MtCO2eq")
pc_lu_2030 = np.interp(2030, [2010, 2050], [pc_lu_2010, pc_lu_2050])
# Not realistic total emissions:
test_2030 = 100/5*5.500
# Correct total emissions:
test_2050 = 100/25*47.320
# We use the linear interpolation between 2010 and 2050 for the 2030 total emissions.
emi_total_2030 = np.interp(2030, [2010, 2050], [emi_total_2010, emi_total_2050])
emi_ipc0_2030 = emi_total_2030 + sequestration_2030
emi_lu_2030 = sequestration_2030 + pc_lu_2030*emi_total_2030
emi_ipcm0el_2030 = emi_ipc0_2030 - emi_lu_2030
print(f"2030 IPC0: {emi_ipc0_2030 :.4f} MtCO2eq")
print(f"2030 IPCM0EL: {emi_ipcm0el_2030 :.4f} MtCO2eq")
print(f"2030 IPCMLULUCF: {emi_lu_2030 :.4f} MtCO2eq")

ABU_all = {'uncondi': {2030: -4.062, 2050: -10.410},
       'condi': {2030: -5.500, 2050: -47.320}} # MtCO2eq, p. 8
bau_ipc0 = {2030: emi_ipc0_2030, 2050: emi_ipc0_2050}
bau_ipcm0el = {2030: emi_ipcm0el_2030, 2050: emi_ipcm0el_2050}

for condi in ABU_all.keys():
    print(f"\n{condi}")
    for yr in ABU_all[condi].keys():
        bau = bau_ipc0[yr]
        ABU = ABU_all[condi][yr]
        #RBU = ABU/bau # 'Problem': bau and ABU negative.
        ABS = bau + ABU
        print(f"\nIPC0 {yr}")
        print(f"BAU: {bau :.4f} MtCO2eq")
        print(f"ABS: {ABS :.4f} MtCO2eq")
        print(f"ABU: {ABU :.4f} MtCO2eq")
        #print(f"RBU: {RBU*100 :.1f}%")
        
        #print(f"\nIPCM0EL {yr}")
        #print(f"\nBAU: {bau_ipcm0el[yr] :.4f} MtCO2eq")
        #print(f"ABS: {bau_ipcm0el[yr]*(1+RBU) :.4f} MtCO2eq")
        #print(f"ABU: {bau_ipcm0el[yr]*RBU :.4f} MtCO2eq")
        #print(f"RBU: {RBU*100 :.1f}%")

# ABS exclLU.
# Calculated based on given RBU and bau_exclLU.
bau_exclLU = {2030: 32.1905, 2050: 59.8099}
RBU_inclLU = {'uncondi': {2030: -.037, 2050: -.055},
              'condi': {2030: -.05, 2050: -.25}}

for yr in bau_exclLU.keys():
    for condi in RBU_inclLU.keys():
        print(f"\n{yr} {condi} exclLU ABS: {bau_exclLU[yr] * (1+RBU_inclLU[condi][yr]) :.4f} MtCO2eq")
        print(f"{yr} {condi} exclLU ABU: {bau_exclLU[yr] * RBU_inclLU[condi][yr] :.4f} MtCO2eq")

# %%
