# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
VNM
"""

emi_bau = 787.4 # MtCO2eq
red = {'uncondi': -.08, 'condi': -.25}

for condi in red.keys():
    ABU = emi_bau * red[condi]
    print(f"ABU {condi}: {ABU} MtCO2eq")
    print(f"ABS {condi}: {emi_bau + ABU} MtCO2eq")

# %%
