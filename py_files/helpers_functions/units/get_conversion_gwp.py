# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020.
"""

# %%
"""
Case sensitive (upper / lower).
Only for CO2eq to CO2eq, with a change of GWP.
Can handle GWPs SAR, AR2, AR4, AR5, AR5CCF.
"""

# %%
from .get_gwps_for_gases import get_gwps_for_gases

# %%
def get_conversion_gwp(gwpFrom, gwpTo, entity):
    gwpFrom = get_gwps_for_gases(entity, gwpFrom)
    gwpTo = get_gwps_for_gases(entity, gwpTo)
    multiplier = 1./gwpFrom * gwpTo
    return multiplier
#enddef

# %%