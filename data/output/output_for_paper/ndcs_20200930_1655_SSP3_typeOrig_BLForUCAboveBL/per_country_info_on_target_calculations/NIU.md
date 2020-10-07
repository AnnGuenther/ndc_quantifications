

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -0.0012 (-0.0012 MtCO2eq)
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
    - emi_onlyLU 2030: external_emi_onlyLU used (0.03666685714285715).
    - bl_onlyLU_refyr = 0.03666685714285715
    - emi_onlyLU 2030: external_emi_onlyLU used (0.03666685714285715).
    - bl_onlyLU_taryr = 0.03666685714285715
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 0.01631516666666667
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.01631516666666667 + -0.0012 = 0.015115166666666669 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 0.015115166666666669
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.015115166666666669, 0.03666685714285715]) = 0.05178202380952382
- tar_emi_exclLU = 0.015115166666666669
- tar_emi_inclLU = 0.05178202380952382

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -0.0031 (-0.0031 MtCO2eq)
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
    - emi_onlyLU 2030: external_emi_onlyLU used (0.03666685714285715).
    - bl_onlyLU_refyr = 0.03666685714285715
    - emi_onlyLU 2030: external_emi_onlyLU used (0.03666685714285715).
    - bl_onlyLU_taryr = 0.03666685714285715
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 0.01631516666666667
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.01631516666666667 + -0.0031 = 0.013215166666666668 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 0.013215166666666668
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.013215166666666668, 0.03666685714285715]) = 0.049882023809523814
- tar_emi_exclLU = 0.013215166666666668
- tar_emi_inclLU = 0.049882023809523814