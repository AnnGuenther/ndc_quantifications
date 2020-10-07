

## tar_type_used: ABU, refyr: 2024, taryr: 2024, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -4.6 (-4.6 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2024: external_emi_onlyLU used (38.377205714285715).
    - bl_onlyLU_refyr = 38.377205714285715
    - emi_onlyLU 2024: external_emi_onlyLU used (38.377205714285715).
    - bl_onlyLU_taryr = 38.377205714285715
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([55.3383, 38.377205714285715]) = 93.71550571428571
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 93.71550571428571 + -4.6 = 89.11550571428572
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 89.11550571428572
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([89.11550571428572, - 38.377205714285715]) = 50.7383.
- tar_emi_exclLU = 50.7383
- tar_emi_inclLU = 89.11550571428572

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -8.9 (-8.9 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (38.377205714285715).
    - bl_onlyLU_refyr = 38.377205714285715
    - emi_onlyLU 2030: external_emi_onlyLU used (38.377205714285715).
    - bl_onlyLU_taryr = 38.377205714285715
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = nan
  - np.isnan(bl_inclLU_taryr), so bl_inclLU_taryr = np.nansum([ict['emi_bl_exclLU_taryr'], bl_onlyLU_taryr]) = np.nansum([66.2762, 38.377205714285715]) = 104.65340571428573
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 104.65340571428573 + -8.9 = 95.75340571428572
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 95.75340571428572
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([95.75340571428572, - 38.377205714285715]) = 57.376200000000004.
- tar_emi_exclLU = 57.376200000000004
- tar_emi_inclLU = 95.75340571428572