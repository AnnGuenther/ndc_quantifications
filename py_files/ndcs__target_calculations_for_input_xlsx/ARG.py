# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
ARG
"""

# %%
# NDC2016

# ABU.
bau = 592
ABS_uncondi = 483
ABS_condi = 369

print(f"ABU unconditional: {ABS_uncondi - bau} MtCO2eq")
print(f"ABU conditional: {ABS_condi - bau} MtCO2eq")

# %%
# NDC2020

emi_inclLU_2016 = 364.44 # MtCO2eq, p. 13
share_onlyLU_2016 = .098 # Figura 3: Cambio de uso de suelos y silvicultura: 9,8%
# Not sure if that's correct ...
emi_onlyLU_2016 = emi_inclLU_2016 * share_onlyLU_2016
emi_exclLU_2016 = emi_inclLU_2016 - emi_onlyLU_2016
print(f"emi onlyLU 2016: {hpf.rnd(emi_onlyLU_2016, 2)} MtCO2eq")
print(f"emi exclLU 2016: {hpf.rnd(emi_exclLU_2016, 2)} MtCO2eq")

# %%