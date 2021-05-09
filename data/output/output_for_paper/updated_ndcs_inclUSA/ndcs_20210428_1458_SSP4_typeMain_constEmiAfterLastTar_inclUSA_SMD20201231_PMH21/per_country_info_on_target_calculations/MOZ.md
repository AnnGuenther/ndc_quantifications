## ['Mozambique']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | nan | yes | nan | yes |
| Used | yes | no | no | yes | no | yes |



## Target type used: ABU, refyr: 2024, taryr: 2024, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -9.2 (-9.2 MtCO2eq, from NDC)
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
    - emi_onlyLU 2024: external_emi_onlyLU used (38.377205714285715 MtCO2eq).
    - bl_onlyLU_refyr = 38.377205714285715 MtCO2eq
    - emi_onlyLU 2024: external_emi_onlyLU used (38.377205714285715 MtCO2eq).
    - bl_onlyLU_taryr = 38.377205714285715 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([54.2667, 38.377205714285715]) = 92.64390571428572 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 92.64390571428572 + -9.2 = 83.44390571428572 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 83.44390571428572 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([83.44390571428572, - 38.377205714285715]) = 45.066700000000004 MtCO2eq.
- tar_emi_exclLU = 45.066700000000004 MtCO2eq
- tar_emi_inclLU = 83.44390571428572 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -12.2 (-12.2 MtCO2eq, from NDC)
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
    - emi_onlyLU 2030: external_emi_onlyLU used (38.377205714285715 MtCO2eq).
    - bl_onlyLU_refyr = 38.377205714285715 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (38.377205714285715 MtCO2eq).
    - bl_onlyLU_taryr = 38.377205714285715 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan MtCO2eq
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([64.4694, 38.377205714285715]) = 102.84660571428572 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 102.84660571428572 + -12.2 = 90.64660571428571 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 90.64660571428571 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([90.64660571428571, - 38.377205714285715]) = 52.2694 MtCO2eq.
- tar_emi_exclLU = 52.2694 MtCO2eq
- tar_emi_inclLU = 90.64660571428571 MtCO2eq