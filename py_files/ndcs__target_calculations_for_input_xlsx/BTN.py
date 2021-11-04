# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
BTN
"""

emi = {2000: 1.6, 2013: 2.2} # MtCO2eq
sequestration = {2000: -6.3, 2013: -6.3}

for yr in emi.keys():
    print(f"IPC0 {yr}: {emi[yr] + sequestration[yr] :.1f} MtCO2eq")

# %%
