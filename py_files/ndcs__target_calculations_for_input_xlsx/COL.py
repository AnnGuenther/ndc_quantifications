# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
COL
"""

emi_bau = 335
pc_red = {'unconditional': -.2, 'conditional': -.3}

# ABS.
# -20% on BAU [e.g., p. 8]
for condi in pc_red.keys():
    print(f"ABS 2030 {condi}: {emi_bau * (1 + pc_red[condi]) :.3f} MtCO2eq")

# ABU.
# -20% on BAU [e.g., p. 8]
for condi in pc_red.keys():
    print(f"ABU 2030 {condi}: {pc_red[condi] * emi_bau :.3f} MtCO2eq")

# %%
