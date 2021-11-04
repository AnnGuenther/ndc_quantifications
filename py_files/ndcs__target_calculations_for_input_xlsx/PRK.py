# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2021.
"""

# %%
print('PRK')

# %%
# NDC2019

bau_2030 = 218
# Given as 218,000,000 tons, and as "CO2 emission". p 2.
# But then always refer to GHG emissions.
# Not a lot of information in that updated NDC (no real NDC document).

abu_uncondi = -35.800 # p. 2
abu_condi = abu_uncondi - 78.800 # p. 2
print(f"ABU condi: {abu_condi} MtCO2eq")
rbu_uncondi = -.164 # p. 2
rbu_condi = -.52 # p. 3

abs_uncondi = bau_2030 + abu_uncondi
abs_condi = bau_2030 + abu_condi
print(f"ABS uncondi: {abs_uncondi} MtCO2eq")
print(f"ABS condi: {abs_condi} MtCO2eq")

# %%