

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -0.057 (-0.057 MtCO2eq)
- ndc_value_inclLU: -0.057 (-0.057 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-0.39 -0.39]
  - ndcs_emi_exclLU for refyr and taryr: [0.24 0.24]
  - ndcs_emi_onlyLU for refyr and taryr: [-0.63 -0.63]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63).
    - bl_onlyLU_refyr = -0.63
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63).
    - bl_onlyLU_taryr = -0.63
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 0.24
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.24 + -0.057 = 0.183 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -0.39
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -0.39 + -0.057 = -0.447
- tar_emi_exclLU = ndc_value_exclLU = 0.183
- tar_emi_inclLU = ndc_value_inclLU = -0.447
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.183
- tar_emi_inclLU = -0.447

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 0.183 (0.183 MtCO2eq)
- ndc_value_inclLU: -0.447 (-0.447 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-0.39 -0.39]
  - ndcs_emi_exclLU for refyr and taryr: [0.24 0.24]
  - ndcs_emi_onlyLU for refyr and taryr: [-0.63 -0.63]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63).
    - bl_onlyLU_refyr = -0.63
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63).
    - bl_onlyLU_taryr = -0.63
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 0.183
- tar_emi_inclLU = ndc_value_inclLU = -0.447
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.183
- tar_emi_inclLU = -0.447

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -24.0 (-24%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [-0.39 -0.39]
  - ndcs_emi_exclLU for refyr and taryr: [0.24 0.24]
  - ndcs_emi_onlyLU for refyr and taryr: [-0.63 -0.63]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -24.0 / 100. = 0.76
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63).
    - bl_onlyLU_refyr = -0.63
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-0.63).
    - bl_onlyLU_taryr = -0.63
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.2085066666666667 * 0.9999952040000001 = 0.20850566666869338
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.2085066666666667 * (1 - 0.9999952040000001) = 9.999979733162543e-07
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.76 * 0.20850566666869338 + 9.999979733162543e-07 = 0.15846530666618028
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 0.20850566666869338 + -0.63 + 9.999979733162543e-07 = nan
- tar_emi_exclLU = ndc_value_exclLU = 0.15846530666618028
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.15846530666618028, -0.63]) = -0.4715346933338197
- tar_emi_exclLU = 0.15846530666618028
- tar_emi_inclLU = -0.4715346933338197