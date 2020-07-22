# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
BEN
"""

ABS = {'uncondi': 37, 'condi': 32.5}
bau = 38.5

for condi in ABS.keys():
    ABU = ABS[condi] - bau
    print(f"\nABU {condi}: {ABU} MtCO2eq")
    print(f"RBU {condi}: {ABU/bau*100 :.1f}%")

# %%
