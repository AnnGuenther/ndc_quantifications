# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2021
"""

# %%
import helpers_functions as hpf

# %%
"""
ETH
"""

# NDC2020 (summary document)
bau_exclLU = {
    2025: 9.16 + 163.5 + 168.78 + 7.46 + 10.28,
    2030: 14.7 + 183.6 + 193 + 9.67 + 11.36} # MtCO2eq, Table1, p. 5
bau_onlyLU = {2025: -1.02, 2030: -0.27}
abu_exclLU_uncondi = {
    2025: - (-.15 + 20.37 + .87 + .02 + .89),
    2030: - (-.72 + 44.37 + 1.99 + .05 + 1.94)}
abu_onlyLU_uncondi = {2025: - 3.34, 2030: - 3.61}
abu_exclLU_condi = {
    2025: - (1.68 + 67.68 + 13.04 + .06 + 3.39),
    2030: - (-.13 + 117 + 28.41 + .16 + 6.54)}
abu_onlyLU_condi = {2025: - 9.25, 2030: - 17.11}

# tests (results given in Table1):
print(hpf.rnd(bau_exclLU[2025] + bau_onlyLU[2025], 2))
print(hpf.rnd(bau_exclLU[2030] + bau_onlyLU[2030], 2))
print(hpf.rnd(abu_exclLU_uncondi[2025] + abu_onlyLU_uncondi[2025], 2))
print(hpf.rnd(abu_exclLU_uncondi[2030] + abu_onlyLU_uncondi[2030], 2))
print(hpf.rnd(abu_exclLU_condi[2025] + abu_onlyLU_condi[2025], 2))
print(hpf.rnd(abu_exclLU_condi[2030] + abu_onlyLU_condi[2030], 2)) # is different than in table, but values are correct ...

years = [2025, 2030]

for year in years:
    print(f"BAU exclLU {year}: {hpf.rnd(bau_exclLU[year], 2)} MtCO2eq")

for condi in ['uncondi', 'condi']:
    
    print(f"\n{condi}")
    for year in years:
        
        if condi == 'uncondi':
            tar_abu_exclLU = abu_exclLU_uncondi[year]
            tar_abu_inclLU = abu_exclLU_uncondi[year] + abu_onlyLU_uncondi[year]
        elif condi == 'condi':
            tar_abu_exclLU = abu_exclLU_uncondi[year] + abu_exclLU_condi[year]
            tar_abu_inclLU = abu_exclLU_uncondi[year] + abu_onlyLU_uncondi[year] + abu_exclLU_condi[year] + abu_onlyLU_condi[year]
        
        tar_abs_exclLU = bau_exclLU[year] + tar_abu_exclLU
        tar_rbu_exclLU = 100*tar_abu_exclLU/bau_exclLU[year]
        
        bau_inclLU = bau_exclLU[year] + bau_onlyLU[year]
        tar_abs_inclLU = bau_inclLU + tar_abu_inclLU
        tar_rbu_inclLU = 100*tar_abu_inclLU/bau_inclLU
        
        print(f"\nABS exclLU {year}: {hpf.rnd(tar_abs_exclLU, 2)} MtCO2eq")
        print(f"RBU exclLU {year}: {hpf.rnd(tar_rbu_exclLU, 1)}%")
        print(f"ABU exclLU {year}: {hpf.rnd(tar_abu_exclLU, 2)} MtCO2eq")
        
        print(f"\nABS inclLU {year}: {hpf.rnd(tar_abs_inclLU, 2)} MtCO2eq")
        print(f"RBU inclLU {year}: {hpf.rnd(tar_rbu_inclLU, 1)}%")
        print(f"ABU inclLU {year}: {hpf.rnd(tar_abu_inclLU, 2)} MtCO2eq")

# %%