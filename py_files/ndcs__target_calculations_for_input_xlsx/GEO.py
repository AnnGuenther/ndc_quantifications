# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
GEO
"""

bau_2030 = 38.42 # MtCO2eq
ABS = {'uncondi': 32.66, 'condi': 28.31} # MtCO2eq

for condi in ABS.keys():
    print(f"ABU {condi}: {ABS[condi] - bau_2030 :.2f} MtCO2eq")

# %%
