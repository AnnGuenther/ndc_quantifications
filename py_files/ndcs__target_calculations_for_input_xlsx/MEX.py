# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
MEX
"""

# ABS.
emi_2030 = 973 # MtCO2eq
red = {'uncondi': -.22, 'condi': -.36}

for condi in red.keys():
    ABS = emi_2030 * (1+red[condi])
    print(f"ABS {condi}: {ABS :.3f} MtCO2eq")
    print(f"ABU {condi}: {ABS - emi_2030 :.3f} MtCO2eq")

# %%
