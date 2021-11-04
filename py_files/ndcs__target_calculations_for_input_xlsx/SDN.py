"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2021.
"""

# %%
import helpers_functions as hpf

# %%
"""
SDN
"""

# %%
# NDC2021

# p. 3-5, BAU for several sectors, and Targets (2021-2030) for these sectors.
energy = 3574580 + 1086360 + 26221 + 857506 + 463759 + 6449582 # tCO2
forestry = 35000000 + 12333267 + 2333503 + 1137405 + 19439790 # tCO2
waste = 1278822 # tCO2/year
abu = (energy + forestry)/(2030-2021) + waste
print(f"ABU: {hpf.rnd(abu, 0)} tCO2")

# %%
