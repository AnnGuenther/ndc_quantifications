

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -12.76311169038518 (-12 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [360.6961723 360.6961723]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_refyr = 19.250258428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_taryr = 19.250258428571428
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 360.6961722966939
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 360.6961722966939 + -12.76311169038518 = 347.9330606063087 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 347.9330606063087
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([347.9330606063087, 19.250258428571428]) = 367.1833190348801
- tar_emi_exclLU = 347.9330606063087
- tar_emi_inclLU = 367.1833190348801

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -38.28933507115554 (-36 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [360.6961723 360.6961723]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_refyr = 19.250258428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_taryr = 19.250258428571428
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 360.6961722966939
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 360.6961722966939 + -38.28933507115554 = 322.4068372255383 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 322.4068372255383
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([322.4068372255383, 19.250258428571428]) = 341.65709565410975
- tar_emi_exclLU = 322.4068372255383
- tar_emi_inclLU = 341.65709565410975

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 347.9330606063087 (327.130 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [360.6961723 360.6961723]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_refyr = 19.250258428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_taryr = 19.250258428571428
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 347.9330606063087
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([347.9330606063087, 19.250258428571428]) = 367.1833190348801
- tar_emi_exclLU = 347.9330606063087
- tar_emi_inclLU = 367.1833190348801

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 322.4068372255383 (303.130 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [360.6961723 360.6961723]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_refyr = 19.250258428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_taryr = 19.250258428571428
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 322.4068372255383
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([322.4068372255383, 19.250258428571428]) = 341.65709565410975
- tar_emi_exclLU = 322.4068372255383
- tar_emi_inclLU = 341.65709565410975

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -5.0 (-5%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [360.6961723 360.6961723]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -5.0 / 100. = 0.95
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_refyr = 19.250258428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_taryr = 19.250258428571428
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 360.6961722966939 * 0.657172077 = 237.0394527141682
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 360.6961722966939 * (1 - 0.657172077) = 123.6567195825257
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.95 * 237.0394527141682 + 123.6567195825257 = 348.84419966098545
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (237.0394527141682 + 19.250258428571428) + 123.6567195825257 = nan
- tar_emi_exclLU = ndc_value_exclLU = 348.84419966098545
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([348.84419966098545, 19.250258428571428]) = 368.0944580895569
- tar_emi_exclLU = 348.84419966098545
- tar_emi_inclLU = 368.0944580895569

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -15.0 (-15%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [360.6961723 360.6961723]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -15.0 / 100. = 0.85
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_refyr = 19.250258428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (19.250258428571428).
    - bl_onlyLU_taryr = 19.250258428571428
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 360.6961722966939 * 0.657172077 = 237.0394527141682
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 360.6961722966939 * (1 - 0.657172077) = 123.6567195825257
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.85 * 237.0394527141682 + 123.6567195825257 = 325.14025438956867
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (237.0394527141682 + 19.250258428571428) + 123.6567195825257 = nan
- tar_emi_exclLU = ndc_value_exclLU = 325.14025438956867
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([325.14025438956867, 19.250258428571428]) = 344.3905128181401
- tar_emi_exclLU = 325.14025438956867
- tar_emi_inclLU = 344.3905128181401