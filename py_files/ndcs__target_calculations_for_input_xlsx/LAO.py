# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
LAO
"""

# %%
# NDC2016

# p. 4+5

ABU = -(0.063 + 0.033 + 0.158 + 16.284)
print(f"ABU: {ABU} MtCO2eq")

# If we include No 1 and 2, the ABU would be by far higher than the given 2000 emissions of 51,000 Gg.
print(f"Probably too high: {ABU - (60.000 + 69.000)/2 - 1468.000} MtCO2eq")

# %%
# NDC2021

# p. 7
uncondi_exclLU = -(2500+50+25+300)
uncondi_inclLU = uncondi_exclLU - 1100
print(f"exclLU: unconditional average abatement between 2020 and 2030 (ktCO2e/y): {uncondi_exclLU}")
print(f"inclLU: nconditional average abatement between 2020 and 2030 (ktCO2e/y): {uncondi_inclLU}")

# p. 8
rbu_uncondi = -.6
abu_uncondi = -62.000 # is "around 62,000 ktCO2e in absolute terms"
bau_2030 = 104.000 # ktCO2e
print(hpf.rnd(abu_uncondi/bau_2030*100, 0), "%")
# 62000 is 60% of the given 2030 BAU.

abs_uncondi = bau_2030 + abu_uncondi
print(f"ABS uncondi 2030: {hpf.rnd(abs_uncondi, 3)} MtCO2eq")

abs_condi = 35.000 # read from Figure 1 (approx.)
abu_condi = abs_condi - bau_2030
rbu_condi = abu_condi/bau_2030
print(f"ABS condi 2030: {hpf.rnd(abs_condi, 3)} MtCO2eq")
print(f"RBU condi 2030: {hpf.rnd(rbu_condi, 1)} %")
print(f"ABU condi 2030: {hpf.rnd(abu_condi, 3)} MtCO2eq")

# %%