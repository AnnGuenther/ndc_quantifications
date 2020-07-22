# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
LBN
"""

# ABS.
emi_bau = 43.5 # MtCO2eq
red = {'uncondi': -.15, 'condi': -.3}

for condi in red.keys():
    ABS = emi_bau * (1+red[condi])
    print(f"ABS {condi}: {ABS :.3f} MtCO2eq")
    print(f"ABU {condi}: {ABS - emi_bau :.3f} MtCO2eq")

# %%
