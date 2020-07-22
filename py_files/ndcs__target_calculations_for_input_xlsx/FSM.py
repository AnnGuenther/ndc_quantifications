# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
FSM
"""

ABS = {'uncondi': 0.108, 'condi': 0.094} # MtCO2eq, p. 1
emi_2000 = 0.150 # p. 1

for condi in ABS.keys():
    print(f"ABU {condi}: {ABS[condi] - emi_2000 :.3f} MtCO2eq")

# %%
