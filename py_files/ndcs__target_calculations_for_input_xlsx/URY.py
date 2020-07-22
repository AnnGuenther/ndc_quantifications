# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
URY
"""

# ABU.
# Based on counterfactual scenario and un/conditional scenarios [p. 28].
# AR2.

print(f"ABU IPCM0EL unconditional: {41.8 - 81} MtCO2eq_SAR")
print(f"ABU IPCM0EL conditional: {39.0 - 81} MtCO2eq_SAR")
print(f"ABU IPC0 unconditional: {35.8 - 81} MtCO2eq_SAR")
print(f"ABU IPC0 conditional: {33.0 - 81} MtCO2eq_SAR")

print(f"RBU IPCM0EL unconditional: {100*(41.8 - 81)/81 :.1f}%")
print(f"RBU IPCM0EL conditional: {100*(39.0 - 81)/81 :.1f}%")
print(f"RBU IPC0 unconditional: {100*(35.8 - 81)/81 :.1f}%")
print(f"RBU IPC0 conditional: {100*(33.0 - 81)/81 :.1f}%")

# %%
