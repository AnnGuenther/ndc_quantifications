# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
LAO
"""

# p. 4+5

ABU = -(0.063 + 0.033 + 0.158 + 16.284)
print(f"ABU: {ABU} MtCO2eq")

# If we include No 1 and 2, the ABU would be by far higher than the given 2000 emissions of 51,000 Gg.
print(f"Probably too high: {ABU - (60.000 + 69.000)/2 - 1468.000} MtCO2eq")

# %%
