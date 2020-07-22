# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
ECU
"""

bau_ipcm0el = 76.904
ABS_ipcm0el = {'uncondi': 67.774, 'condi': 60.824}

for condi in ABS_ipcm0el.keys():
    print(f"ABU {condi}: {ABS_ipcm0el[condi] - bau_ipcm0el :.3f} MtCO2eq")

ref_lu = 100/80*35 # p. 17, mitigated by 20% is 35 MtCO2eq/yr.
# Nivel de referencia 2000 - 2008. But here used as BAU ...
print(f"\nBAU LULUCF: {ref_lu} MtCO2eq")

ABS_lu = {'uncondi': ref_lu * (1-.04), 'condi': ref_lu * (1-.2)} # p. 17.

for condi in ABS_lu.keys():
    ABS_ipc0 = ABS_ipcm0el[condi] + ABS_lu[condi]
    print(f"ABS IPC0 {condi}: {ABS_ipc0 :.3f} MtCO2eq")
    # We just assume that the 2000-2008 reference for LULUCF would be the BAU LULUCF emissions.
    print("Assuming the reference LULUCF emissions to be the BAU emissions:")
    ABU_ipc0 = ABS_ipc0 - (bau_ipcm0el + ref_lu)
    print(f"ABU IPC0 {condi}: {ABU_ipc0 :.3f} MtCO2eq")
    RBU_ipc0 = ABU_ipc0/ABS_ipc0*100.
    print(f"RBU IPC0 {condi}: {RBU_ipc0 :.0f}%")    

# %%
