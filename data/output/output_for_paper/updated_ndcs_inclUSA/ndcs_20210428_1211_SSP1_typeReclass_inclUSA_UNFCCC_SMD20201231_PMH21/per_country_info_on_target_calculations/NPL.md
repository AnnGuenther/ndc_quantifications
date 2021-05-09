## ['Nepal']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -0.737 (-0.737 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (7.238065714285715 MtCO2eq).
    - bl_onlyLU_refyr = 7.238065714285715 MtCO2eq
    - emi_onlyLU 2025: external_emi_onlyLU used (7.238065714285715 MtCO2eq).
    - bl_onlyLU_taryr = 7.238065714285715 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([42.1229, 7.238065714285715]) = 49.36096571428572 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 49.36096571428572 + -0.737 = 48.62396571428572 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 48.62396571428572 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([48.62396571428572, - 7.238065714285715]) = 41.3859 MtCO2eq.
- tar_emi_exclLU = 41.3859 MtCO2eq
- tar_emi_inclLU = 48.62396571428572 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -1.486 (-1.486 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (7.238065714285715 MtCO2eq).
    - bl_onlyLU_refyr = 7.238065714285715 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (7.238065714285715 MtCO2eq).
    - bl_onlyLU_taryr = 7.238065714285715 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([46.4334, 7.238065714285715]) = 53.671465714285716 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 53.671465714285716 + -1.486 = 52.18546571428572 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 52.18546571428572 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([52.18546571428572, - 7.238065714285715]) = 44.9474 MtCO2eq.
- tar_emi_exclLU = 44.9474 MtCO2eq
- tar_emi_inclLU = 52.18546571428572 MtCO2eq