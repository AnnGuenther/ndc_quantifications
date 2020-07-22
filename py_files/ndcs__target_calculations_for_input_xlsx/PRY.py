# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
PRY
"""

RBU = {'uncondi': -.1, 'condi': -.2} # p. 5
emi_bau_2030 = 416 # MtCo2eq

for condi in RBU.keys():
    print(f"ABU {condi}: {emi_bau_2030*RBU[condi] :.0f} MtCO2eq")
    print(f"ABS {condi}: {emi_bau_2030 * (1+RBU[condi]) :.0f} MtCO2eq")

# %%