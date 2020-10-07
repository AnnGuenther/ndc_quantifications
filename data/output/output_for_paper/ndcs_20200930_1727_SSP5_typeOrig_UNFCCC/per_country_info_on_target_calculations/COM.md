

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -0.3015 (-0.301500 MtCO2eq)
- ndc_value_inclLU: -0.3015 (-0.301500 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [0.4345 0.4345]
  - ndcs_emi_exclLU for refyr and taryr: [0.4071 0.4071]
  - ndcs_emi_onlyLU for refyr and taryr: [0.0274 0.0274]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (0.0274).
    - bl_onlyLU_refyr = 0.0274
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (0.0274).
    - bl_onlyLU_taryr = 0.0274
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 0.4071
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.4071 + -0.3015 = 0.10560000000000003 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 0.4345
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 0.4345 + -0.3015 = 0.133
- tar_emi_exclLU = ndc_value_exclLU = 0.10560000000000003
- tar_emi_inclLU = ndc_value_inclLU = 0.133
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.10560000000000003
- tar_emi_inclLU = 0.133

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -0.4367 (-0.436700 MtCO2eq)
- ndc_value_inclLU: -0.4417 (-0.441700 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [0.5231 0.5231]
  - ndcs_emi_exclLU for refyr and taryr: [0.4693 0.4693]
  - ndcs_emi_onlyLU for refyr and taryr: [0.0487 0.0487]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (0.0487).
    - bl_onlyLU_refyr = 0.0487
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (0.0487).
    - bl_onlyLU_taryr = 0.0487
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 0.4693
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.4693 + -0.4367 = 0.03260000000000002 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 0.5231
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 0.5231 + -0.4417 = 0.08140000000000003
- tar_emi_exclLU = ndc_value_exclLU = 0.03260000000000002
- tar_emi_inclLU = ndc_value_inclLU = 0.08140000000000003
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.03260000000000002
- tar_emi_inclLU = 0.08140000000000003

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 0.1056 (0.105600 MtCO2eq)
- ndc_value_inclLU: 0.133 (0.133 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [0.4345 0.4345]
  - ndcs_emi_exclLU for refyr and taryr: [0.4071 0.4071]
  - ndcs_emi_onlyLU for refyr and taryr: [0.0274 0.0274]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (0.0274).
    - bl_onlyLU_refyr = 0.0274
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (0.0274).
    - bl_onlyLU_taryr = 0.0274
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 0.1056
- tar_emi_inclLU = ndc_value_inclLU = 0.133
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.1056
- tar_emi_inclLU = 0.133

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 0.0326 (0.032600 MtCO2eq)
- ndc_value_inclLU: 0.0813 (0.0813 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [0.5231 0.5231]
  - ndcs_emi_exclLU for refyr and taryr: [0.4693 0.4693]
  - ndcs_emi_onlyLU for refyr and taryr: [0.0487 0.0487]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (0.0487).
    - bl_onlyLU_refyr = 0.0487
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (0.0487).
    - bl_onlyLU_taryr = 0.0487
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 0.0326
- tar_emi_inclLU = ndc_value_inclLU = 0.0813
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.0326
- tar_emi_inclLU = 0.0813

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -74.1 (-74.1%)
- ndc_value_inclLU: -69.0 (-69%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [0.4345 0.4345]
  - ndcs_emi_exclLU for refyr and taryr: [0.4071 0.4071]
  - ndcs_emi_onlyLU for refyr and taryr: [0.0274 0.0274]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -74.1 / 100. = 0.259
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -69.0 / 100. = 0.31000000000000005
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (0.0274).
    - bl_onlyLU_refyr = 0.0274
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (0.0274).
    - bl_onlyLU_taryr = 0.0274
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1.053 * 1.0 = 1.053
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1.053 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.259 * 1.053 + 0.0 = 0.272727
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.31000000000000005 * (1.053 + 0.0274) + 0.0 = 0.33492400000000005
- tar_emi_exclLU = ndc_value_exclLU = 0.272727
- tar_emi_inclLU = ndc_value_inclLU = 0.33492400000000005
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.272727
- tar_emi_inclLU = 0.33492400000000005

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -93.1 (-93.1%)
- ndc_value_inclLU: -84.0 (-84%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [0.5231 0.5231]
  - ndcs_emi_exclLU for refyr and taryr: [0.4693 0.4693]
  - ndcs_emi_onlyLU for refyr and taryr: [0.0487 0.0487]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -93.1 / 100. = 0.06900000000000006
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -84.0 / 100. = 0.16000000000000003
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (0.0487).
    - bl_onlyLU_refyr = 0.0487
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (0.0487).
    - bl_onlyLU_taryr = 0.0487
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1.4744 * 1.0 = 1.4744
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1.4744 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.06900000000000006 * 1.4744 + 0.0 = 0.10173360000000009
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.16000000000000003 * (1.4744 + 0.0487) + 0.0 = 0.24369600000000002
- tar_emi_exclLU = ndc_value_exclLU = 0.10173360000000009
- tar_emi_inclLU = ndc_value_inclLU = 0.24369600000000002
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.10173360000000009
- tar_emi_inclLU = 0.24369600000000002