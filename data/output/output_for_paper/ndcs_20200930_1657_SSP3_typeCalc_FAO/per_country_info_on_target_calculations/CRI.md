

## tar_type_used: RBY, refyr: 2012, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -25.0 (-25%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [12.44126 16.739  ]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -25.0 / 100. = 0.75
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2012: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 12.44126 - 15.1463 = -2.7050400000000003
    - bl_onlyLU_refyr = -2.7050400000000003
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 16.739 - 24.0567 = -7.3176999999999985
    - bl_onlyLU_taryr = -7.3176999999999985
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 15.1463 * 1.0 = 15.1463
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 24.0567 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 15.1463 + 0.0 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.75 * 15.1463 + -2.7050400000000003 + 0.0 = 8.654685
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 8.654685
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([8.654685, - -7.3176999999999985]) = 15.972385.
- tar_emi_exclLU = 15.972385
- tar_emi_inclLU = 8.654685

## tar_type_used: AEI, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 1.19 (1.19 tCO2eq/cap)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: external_emi_onlyLU used (-10.581491385714283).
    - bl_onlyLU_refyr = -10.581491385714283
    - emi_onlyLU 2050: external_emi_onlyLU used (-10.581491385714283).
    - bl_onlyLU_taryr = -10.581491385714283
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 6978880.6794
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 1.19 * 1e-6 * 6978880.6794 = 8.304868008485998
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 8.304868008485998
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([8.304868008485998, - -10.581491385714283]) = 18.886359394200284.
- tar_emi_exclLU = 18.886359394200284
- tar_emi_inclLU = 8.304868008485998

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -7.365 (-7.365 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [16.739 16.739]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 16.739 - 24.0567 = -7.3176999999999985
    - bl_onlyLU_refyr = -7.3176999999999985
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 16.739 - 24.0567 = -7.3176999999999985
    - bl_onlyLU_taryr = -7.3176999999999985
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 16.739
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 16.739 + -7.365 = 9.374
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 9.374
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([9.374, - -7.3176999999999985]) = 16.691699999999997.
- tar_emi_exclLU = 16.691699999999997
- tar_emi_inclLU = 9.374

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 9.374 (9.374000 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [16.739 16.739]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 16.739 - 24.0567 = -7.3176999999999985
    - bl_onlyLU_refyr = -7.3176999999999985
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 16.739 - 24.0567 = -7.3176999999999985
    - bl_onlyLU_taryr = -7.3176999999999985
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 9.374
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([9.374, - -7.3176999999999985]) = 16.691699999999997.
- tar_emi_exclLU = 16.691699999999997
- tar_emi_inclLU = 9.374

## tar_type_used: ABS, refyr: 2050, taryr: 2050, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 5.964988 (5.964988 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: external_emi_onlyLU used (-10.581491385714283).
    - bl_onlyLU_refyr = -10.581491385714283
    - emi_onlyLU 2050: external_emi_onlyLU used (-10.581491385714283).
    - bl_onlyLU_taryr = -10.581491385714283
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 5.964988
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([5.964988, - -10.581491385714283]) = 16.546479385714285.
- tar_emi_exclLU = 16.546479385714285
- tar_emi_inclLU = 5.964988

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -44.0 (-44%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [16.739 16.739]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -44.0 / 100. = 0.56
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 16.739 - 24.0567 = -7.3176999999999985
    - bl_onlyLU_refyr = -7.3176999999999985
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 16.739 - 24.0567 = -7.3176999999999985
    - bl_onlyLU_taryr = -7.3176999999999985
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 24.0567 * 1.0 = 24.0567
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 24.0567 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 24.0567 + 0.0 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.56 * 24.0567 + -7.3176999999999985 + 0.0 = 6.154052000000002
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 6.154052000000002
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([6.154052000000002, - -7.3176999999999985]) = 13.471752.
- tar_emi_exclLU = 13.471752
- tar_emi_inclLU = 6.154052000000002