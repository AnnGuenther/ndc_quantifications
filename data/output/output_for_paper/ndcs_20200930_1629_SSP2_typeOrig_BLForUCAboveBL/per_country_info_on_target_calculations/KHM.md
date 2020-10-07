

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -3.449878268339869 (-3.100 MtCO2eq_SAR)
- ndc_value_inclLU: -15.240671898359519 (-13.695 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [4.12093523 4.12093523]
  - ndcs_emi_exclLU for refyr and taryr: [12.90922191 12.90922191]
  - ndcs_emi_onlyLU for refyr and taryr: [-8.78828667 -8.78828667]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-8.788286672606434).
    - bl_onlyLU_refyr = -8.788286672606434
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-8.788286672606434).
    - bl_onlyLU_taryr = -8.788286672606434
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 12.909221907336285
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 12.909221907336285 + -3.449878268339869 = 9.459343638996415 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 4.12093523472985
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 4.12093523472985 + -15.240671898359519 = -11.11973666362967
- tar_emi_exclLU = ndc_value_exclLU = 9.459343638996415
- tar_emi_inclLU = ndc_value_inclLU = -11.11973666362967
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 9.459343638996415
- tar_emi_inclLU = -11.11973666362967

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -27.0 (-27%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [4.12093523 4.12093523]
  - ndcs_emi_exclLU for refyr and taryr: [12.90922191 12.90922191]
  - ndcs_emi_onlyLU for refyr and taryr: [-8.78828667 -8.78828667]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -27.0 / 100. = 0.73
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-8.788286672606434).
    - bl_onlyLU_refyr = -8.788286672606434
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-8.788286672606434).
    - bl_onlyLU_taryr = -8.788286672606434
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 43.2219 * 0.256687382 = 11.0945163560658
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 43.2219 * (1 - 0.256687382) = 32.1273836439342
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.73 * 11.0945163560658 + 32.1273836439342 = 40.22638058386224
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 11.0945163560658 + -8.788286672606434 + 32.1273836439342 = nan
- tar_emi_exclLU = ndc_value_exclLU = 40.22638058386224
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([40.22638058386224, -8.788286672606434]) = 31.438093911255805
- tar_emi_exclLU = 40.22638058386224
- tar_emi_inclLU = 31.438093911255805