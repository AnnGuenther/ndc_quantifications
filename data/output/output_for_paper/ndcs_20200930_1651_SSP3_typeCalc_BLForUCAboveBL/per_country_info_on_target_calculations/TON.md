

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -0.27 (-0.27 MtCO2eq)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.07333285714285716).
    - bl_onlyLU_refyr = -0.07333285714285716
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.07333285714285716).
    - bl_onlyLU_taryr = -0.07333285714285716
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 0.2372083333333333
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.2372083333333333 + -0.27 = -0.03279166666666672 # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-0.270 MtCO2eq) is < 0 (-0.033 MtCO2eq, compared to baseline 0.237 MtCO2eq) and will be set to 0 MtCO2eq.
- tar_emi_exclLU = ndc_value_exclLU = -0.03279166666666672
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([-0.03279166666666672, -0.07333285714285716]) = -0.10612452380952388
- tar_emi_exclLU = -0.03279166666666672
- tar_emi_inclLU = -0.10612452380952388

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -0.27 (-0.27 MtCO2eq)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.07333285714285716).
    - bl_onlyLU_refyr = -0.07333285714285716
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.07333285714285716).
    - bl_onlyLU_taryr = -0.07333285714285716
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 0.2372083333333333
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.2372083333333333 + -0.27 = -0.03279166666666672 # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-0.270 MtCO2eq) is < 0 (-0.033 MtCO2eq, compared to baseline 0.237 MtCO2eq) and will be set to 0 MtCO2eq.
- tar_emi_exclLU = ndc_value_exclLU = -0.03279166666666672
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([-0.03279166666666672, -0.07333285714285716]) = -0.10612452380952388
- tar_emi_exclLU = -0.03279166666666672
- tar_emi_inclLU = -0.10612452380952388