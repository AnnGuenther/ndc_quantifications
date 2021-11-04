# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Updated: 06/2021
"""

# %%
import helpers_functions as hpf

# %%
"""
CPV
"""

# %%
# NDC2021

bau_2030 = 1.006 # p. 19, Table 3, inclLU
abs_2030 = 0.764# p. 19, Table 4, inclLU

abu_2030 = abs_2030 - bau_2030
print(f"ABU 2030 inclLU: {hpf.rnd(abu_2030, 3)} MtCO2eq")
# In line with numbers given on p. 21!

abu_uncondi = -0.180000 # p. 21
abu_condi = -0.242000 #  p. 21
abs_uncondi = bau_2030 + abu_uncondi
abs_condi = bau_2030 + abu_condi
print(f"ABS uncondi: {hpf.rnd(abs_uncondi, 6)} MtCO2eq")
print(f"ABS condi: {hpf.rnd(abs_condi, 6)} MtCO2eq")
# The above given are "condi"!

# %%