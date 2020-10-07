

## tar_type_used: ABU, refyr: 2035, taryr: 2035, conditional_best
- ndc_value_exclLU: -33.0 (-33 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [104. 104.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143).
    - bl_onlyLU_refyr = 117.79018142857143
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143).
    - bl_onlyLU_taryr = 117.79018142857143
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 104.0
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 104.0 + -33.0 = 71.0 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 71.0
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([71.0, 117.79018142857143]) = 188.79018142857143
- tar_emi_exclLU = 71.0
- tar_emi_inclLU = 188.79018142857143

## tar_type_used: ABS, refyr: 2035, taryr: 2035, conditional_best
- ndc_value_exclLU: 71.0 (71 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [104. 104.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143).
    - bl_onlyLU_refyr = 117.79018142857143
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143).
    - bl_onlyLU_taryr = 117.79018142857143
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 71.0
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([71.0, 117.79018142857143]) = 188.79018142857143
- tar_emi_exclLU = 71.0
- tar_emi_inclLU = 188.79018142857143

## tar_type_used: RBU, refyr: 2035, taryr: 2035, conditional_best
- ndc_value_exclLU: -32.0 (-32%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [104. 104.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -32.0 / 100. = 0.6799999999999999
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143).
    - bl_onlyLU_refyr = 117.79018142857143
    - emi_onlyLU 2035: external_emi_onlyLU used (117.79018142857143).
    - bl_onlyLU_taryr = 117.79018142857143
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 104.0 * 0.990535707 = 103.015713528
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 104.0 * (1 - 0.990535707) = 0.9842864719999955
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.6799999999999999 * 103.015713528 + 0.9842864719999955 = 71.03497167104
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (103.015713528 + 117.79018142857143) + 0.9842864719999955 = nan
- tar_emi_exclLU = ndc_value_exclLU = 71.03497167104
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([71.03497167104, 117.79018142857143]) = 188.82515309961144
- tar_emi_exclLU = 71.03497167104
- tar_emi_inclLU = 188.82515309961144