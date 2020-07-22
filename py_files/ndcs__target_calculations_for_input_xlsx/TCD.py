# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
TCD
"""

emi = {2010: {'energy': 0.66520, 'agri': 18.44800, 'lu': -10.90877, 'waste': 0.17519},
       2030: {'energy': 2.16500, 'agri': 43.42600, 'lu': -17.38748, 'waste': 0.45585},
       'uncondi': {'energy': 2.16500, 'agri': 38.21570, 'lu': -17.38748, 'waste': 0.45585},
       'condi': {'energy': 1.84025, 'agri': 30.39883, 'lu': -24.34248, 'waste': 0.40285}} # MtCO2eq, p. 12

emi_sum_ipcm0el = {}
for yr_condi in emi.keys():
    emi_tot = 0
    for cat in emi[yr_condi].keys():
        if cat != 'lu':
            emi_tot += emi[yr_condi][cat]
    
    emi_sum_ipcm0el[yr_condi] = emi_tot
    
    print(f"{yr_condi} IPCM0EL: {emi_tot :.5f} MtCO2eq")

emi_2030 = emi[2030]
emi_ipcm0el = sum([emi_2030[xx] for xx in emi_2030.keys() if xx != 'lu'])
emi_ipc0 = sum([emi_2030[xx] for xx in emi_2030.keys()])

print(f"ABU uncondi IPC0: {23.44907 - emi_ipc0 :.4f} MtCO2eq")
print(f"ABU condi IPC0: {8.22945 - emi_ipc0 :.4f} MtCO2eq")

ABU_uncondi = emi_sum_ipcm0el['uncondi'] - emi_ipcm0el
ABU_condi = emi_sum_ipcm0el['condi'] - emi_ipcm0el
print(f"ABU uncondi IPCM0EL: {ABU_uncondi :.4f} MtCO2eq")
print(f"ABU condi IPCM0EL: {ABU_condi :.4f} MtCO2eq")

print(f"RBU uncondi IPCM0EL: {ABU_uncondi / emi_ipcm0el * 100 :.1f}%")
print(f"RBU condi IPCM0EL: {ABU_condi / emi_ipcm0el * 100 :.1f}%")

# %%
