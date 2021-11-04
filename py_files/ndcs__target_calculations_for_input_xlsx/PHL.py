# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
PHL
"""

# %%
# NDC2021

bau = 3340.3 # MtCO2eq, p. 4

# p. 4: avoidance of 75%, of which 2.71% is unconditional and 72.29% is conditional
rbu_uncondi = -.75*(2.71/75)
rbu_condi = -.75

abu_uncondi = bau*rbu_uncondi
abu_condi = bau*rbu_condi

abs_uncondi = bau + abu_uncondi
abs_condi = bau + abu_condi

print(f"ABS uncondi: {hpf.rnd(abs_uncondi, 1)} MtCO2eq")
print(f"ABS condi: {hpf.rnd(abs_condi, 1)} MtCO2eq")

print(f"RBU uncondi: {hpf.rnd(rbu_uncondi*100, 2)}%")
print(f"RBU condi: {hpf.rnd(rbu_condi*100, 2)}%")

print(f"ABU uncondi: {hpf.rnd(abu_uncondi, 1)} MtCO2eq")
print(f"ABU condi: {hpf.rnd(abu_condi, 1)} MtCO2eq")

# %%