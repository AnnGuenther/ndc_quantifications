# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
import helpers_functions as hpf

# %%
"""
MOZ
"""

# Cumulative reductions over 5 year periods given.
# [p. 9] "Based on the policy actions and programmes outlined above, the country estimates, 
# on a preliminary basis, the total reduction of about 76,5 MtCO2eq in the period 
# from 2020 to 2030, with 23,0 MtCO2eq by 2024 and 53,4 MtCO2eq from 2025 to 2030."
print(f"\nAssuming average per period (with 5 and then 6 years")
print(f"ABU 2024: {23/5} MtCO2eq")
print(f"ABU 2030: {53.4/6} MtCO2eq") # Not sures if it should be 5 years.

print(f"\nAssuming average per period (with 5 and then 5 years")
print(f"ABU 2025: {23/5} MtCO2eq")
print(f"ABU 2030: {53.4/5} MtCO2eq") # Not sures if it should be 5 years.

##########
# Other option: linear decrease per 5-year period.
# If I would use a 6 year period for the second period, emissions would increase again...

print("\nAssuming linear decrease per period)")
# first triangle (right angle, area = 1/2*side1*side2):
area = 23 # Mt
period = 5 # years
side2 = abu_2025 = (area * 2) / period
print(f"ABU 2025: {abu_2025} MtCO2eq")

# second period has square and triangle
# square
period = 5 # years
# side2 stays the same
area = period * side2

# area second triangle:
area = 53.4 - area
# side1 stays the same
side2 = (area * 2) / period
abu_2030 = abu_2025 + side2
print(f"ABU 2030: {hpf.rnd(abu_2030, 1)} MtCO2eq")

# %%
