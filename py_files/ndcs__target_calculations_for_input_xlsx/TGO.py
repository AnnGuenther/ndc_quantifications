# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
TGO
"""

bau = 38.86136 # MtCO2eq
ABS = {'uncondi': 34.53328, 'condi': 27.62662}

for condi in ABS.keys():
    print(f"ABU {condi}: {ABS[condi] - bau :.5f} MtCO2eq")

# %%
