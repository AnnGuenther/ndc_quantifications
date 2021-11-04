# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 07/2020.
"""

# %%
"""
COM
"""

# p. 18+22, emissions per sector.
# IPC0 is given in the tables.
ipcm0el = {2000: 0.106600 + 0.053000 + 0.026300,
           2005: 0.025600 + 0.057000 + 0.029900,
           2010: 0.149700 + 0.070600 + 0.034200,
           2015: 0.181300 + 0.081400 + 0.039100,
           2020: 0.219100 + 0.085600 + 0.044700,
           2025: 0.266500 + 0.089800 + 0.050800,
           2030: 0.319200 + 0.094100 + 0.056000}
ipcmlulucf = {2000: 0.061500 - 0.315200 + 0.024600,
              2005: 0.061500 - 0.268800 + 0.027300,
              2010: 0.061500 - 0.209300 + 0.034900,
              2015: 0.061500 - 0.175100 + 0.041200,
              2020: 0.050000 - 0.085200 + 0.043600,
              2025: 0.059600 - 0.078300 + 0.046100,
              2030: 0.069100 - 0.068900 + 0.048500}
for yr in ipcm0el.keys():
    print(f"\nipcm0el {yr}: {ipcm0el[yr] :.6f} MtCO2eq")
    print(f"ipcmlulucf {yr}: {ipcmlulucf[yr] :.6f} MtCO2eq")


ipc0 = {2025: .434500, 2030: .523000} # MtCO2eq, p. 9
ABU_inclLU = {2025: -.301500, 2030: -.441700} # 2020 values ignored.
RBU_inclLU = {2025: -.69, 2030: -.84}
ABS_inclLU = {}
for yr in ipc0.keys():
    ABS_inclLU[yr] = ipc0[yr] + ABU_inclLU[yr]
    print(f"ABS_inclLU {yr}: {ABS_inclLU[yr] :.6f} MtCO2eq")

# Target year onlyLU is positive.
# Calculate the ABS exclLU as ABS inclLU minus the target year LULUCF emissions.
for yr in ipc0.keys():
    ABS_exclLU = ABS_inclLU[yr] - ipcmlulucf[yr]
    ABU_exclLU = ABS_exclLU - ipcm0el[yr]
    RBU_exclLU = ABU_exclLU/ipcm0el[yr]*100
    print(f"\n{yr} ABS exclLU: {ABS_exclLU :.6f} MtCO2eq")
    print(f"{yr} ABU exclLU: {ABU_exclLU :.6f} MtCO2eq")
    print(f"{yr} RBU exclLU: {RBU_exclLU :.1f}%")

# %%