# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
KEN
"""

# %%
# NDC2016

# ABS
emi_bau = 143 # MtCO2eq
red = -.3
print(f"ABS: {emi_bau * (1+red)} MtCO2eq")
print(f"ABU: {emi_bau * red} MtCO2eq")

# %%
# NDC2020
emi_bau = 143 # MtCO2eq, p. 1

tar_rbu_condi = -.32 # p. 1
tar_rbu_uncondi = tar_rbu_condi * .21 # p. 10: Subject to national circumstances, Kenya intends to bear 21% of the mitigation cost from domestic sources
print(f"RBU uncondi: {hpf.rnd(100*tar_rbu_uncondi, 2)}%")

print(f"ABU uncondi: {hpf.rnd(emi_bau * tar_rbu_uncondi, 0)} MtCO2eq")
print(f"ABU condi: {hpf.rnd(emi_bau * tar_rbu_condi, 0)} MtCO2eq")

print(f"ABS uncondi: {hpf.rnd(emi_bau * (1+tar_rbu_uncondi), 0)} MtCO2eq")
print(f"ABS condi: {hpf.rnd(emi_bau * (1+tar_rbu_condi), 0)} MtCO2eq")

# %%