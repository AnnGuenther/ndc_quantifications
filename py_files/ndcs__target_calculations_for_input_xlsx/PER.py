# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
PER
"""

# %%
# NDC2015

# IPCMLULUCF
emi_2010_inclLU = 170.6 # MtCO2eq
emi_2010_exclLU = 78.0
emi_2010_onlyLU = emi_2010_inclLU - emi_2010_exclLU
print(f"IPCMLULUCF 2010: {emi_2010_onlyLU} MtCO2eq")
emi_2030_inclLU = 298.3
emi_2030_exclLU = 139.3
emi_2030_onlyLU = emi_2030_inclLU - emi_2030_exclLU
print(f"IPCMLULUCF 2030: {emi_2030_onlyLU} MtCO2eq")

# Targets
RBU = {'uncondi': -.2, 'condi': -.3} # inclLU

for condi in RBU.keys():
    ABS_exclLU = emi_2030_exclLU * (1+RBU[condi])
    ABS_onlyLU = emi_2030_onlyLU * (1+RBU[condi])
    ABS_inclLU = ABS_exclLU + ABS_onlyLU
    print(f"\n{condi} ABS IPC0: {ABS_inclLU :.1f} MtCO2eq")
    #print(f"{condi} ABS IPCM0EL: {ABS_exclLU :.1f} MtCO2eq")
    print(f"\n{condi} ABU IPC0: {ABS_inclLU - emi_2030_inclLU :.1f} MtCO2eq")
    #print(f"{condi} ABU IPCM0EL: {ABS_exclLU - emi_2030_exclLU :.1f} MtCO2eq")

# %%
# NDC2020

# BAU 2030: not given in new NDC, but the value is the same as in old NDC.
# The 30% reduction compared to BAU is the same in NDC2015 and NDC2020.
emi_2030_inclLU = 298.3 # MtCO2eq
abs_uncondi = 208.8
abs_condi = 179.0
print(f"ABU uncondi: {hpf.rnd(abs_uncondi - emi_2030_inclLU, 1)} MtCO2eq")
print(f"ABU condi: {hpf.rnd(abs_condi - emi_2030_inclLU, 1)} MtCO2eq")

# %%