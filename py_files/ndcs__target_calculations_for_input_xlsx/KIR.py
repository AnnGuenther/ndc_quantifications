# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import numpy as np

# %%
"""
KIR
"""

# p. 9.
ABU_uncondi = -0.010090
ABU = {}
ABU['uncondi'] = {2025: ABU_uncondi, 2030: ABU_uncondi}
ABU['condi'] = {2025: ABU_uncondi -0.035880, 2030: ABU_uncondi -0.038420}

RBU = {'uncondi': {2025: -.137, 2030: -.128},
       'condi': {2025: -.137-.488, 2030: -.128-.490}}

bau = {}
for yr in [2025, 2030]:
    bau_act = []
    for condi in ['uncondi', 'condi']:
        bau_act += [1/RBU[condi][yr]*ABU[condi][yr]]
    
    bau[yr] = np.average(bau_act)
    print(f"BAU {yr}: {bau[yr] :.6f} MtCO2eq (uncondi: {bau_act[0] :.6f}; condi: {bau_act[1] :.6f})")

for condi in ABU.keys():
    print(f"\n{condi}")
    for yr in ABU[condi].keys():
        print(f"\n{yr}")
        print(f"ABS: {bau[yr]*(1+RBU[condi][yr]) :.6f} MtCO2eq")
        print(f"ABU: {ABU[condi][yr] :.6f} MtCO2eq")
        print(f"RBU: {100.*RBU[condi][yr] :.1f}%")

# We use the mean over the calculated BAUs (per year).

# %%