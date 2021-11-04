# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2021
"""

# %%

import helpers_functions as hpf

# %%
"""
NPL
"""

# %%
# NDC2020

#[p. 3] conditional: "This target will reduce emissions from a projected BAU of 2,988 Gg CO2 eq. in 2025 to 2,734 Gg CO2 eq., 
# which is around 8% decrease in emissions."
#[p. 3] conditional: "This target will reduce emissions from a projected BAU of 3,640 Gg CO2 eq. in 2030 to 2,619 Gg CO2 eq., 
# which is around 28% decrease in emissions."
#[p. 4] conditional: "These three combined targets can reduce emissions from approximately 1,999 Gg CO2 eq. in BAU in 2025 to 
# approximately 1,774 Gg CO2 eq. This is around 11% reduction in emissions from the cooking sector. For 2030, 
# these three targets can reduce emissions from approximately 2,064 Gg CO2 eq. from BAU to 1,599 Gg CO2 eq., 
# which is around 23% reduction in emissions."
#[p. 4] conditional: "By 2025 ... These two activities will reduce around 258 Gg CO2 eq. compared to BAU."

lower_lim_bau_2025 = 2.988 + 1.999
lower_lim_bau_2030 = 3.640 + 2.064
print(f"BAU 2025 lower limit: {hpf.rnd(lower_lim_bau_2025, 3)} MtCO2eq")
print(f"BAU 2030 lower limit: {hpf.rnd(lower_lim_bau_2030, 3)} MtCO2eq")

abu_2025 = - ((2.988-2.734) + (1.999-1.774) + .258)
abu_2030 = - ((3.640-2.619) + (2.064-1.599))
print(f"ABU 2025: {hpf.rnd(abu_2025, 3)} MtCO2eq")
print(f"ABU 2030: {hpf.rnd(abu_2030, 3)} MtCO2eq")

# %%