# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
CUB
"""

# %%
# NDC2016

# p. 16
emi_brutto_2010 = 40 # MtCO2eq
emi_brutto_1990 = 100/84*emi_brutto_2010
print(f"emi brutto 1990: {emi_brutto_1990 :.1f} MtCO2eq")
emi_energy_2010 = .76*emi_brutto_2010
emi_agri_2010 = .15*emi_brutto_2010
emi_waste_ippu = .09*emi_brutto_2010

# %%
# NDC2020

# p. 14: It is estimated that the contribution will avoid the
# emission of 30.6 million ktCO2eq. into the
# atmosphere in the period 2014 – 2030.
# p. 16: It is estimated that the contribution will avoid the
# emission of 700 thousand ktCO2eq. into the
# atmosphere in the period 2014 – 2030.
# p. 17: It is estimated that the contribution will avoid the
# emission of one million ktCO2eq. annually.
# p. 18: Removing 169,9 million tons of atmospheric CO2 in the period 2019-2030.
# p. 19: ... reducing 8 million ktCO2eq. in emissions annually in the period of 2020-2030.

# Assuming the same annual removal:
removal = 30.6e6/(2030-2014) + 700e3/(2030-2014) + 1e6 + 169.9e3*(2030-2019) + 8e6*(2030-2020) # ktCO2eq
# in 2016: CUB emissions of 23 MtCO2eq.
# not sure about the given units ...
removal = 30.6e6/(2030-2014) + 700e3/(2030-2014) + 1e6 + 169.9e6*(2030-2019) + 8e6*(2030-2020) # ktCO2eq
# Does not really seem to make sense ...

# %%