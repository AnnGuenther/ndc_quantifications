

## tar_type_used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -0.387 (-0.387 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [9.379 9.379]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 9.379
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 9.379 + -0.387 = 8.991999999999999 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 8.991999999999999
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([8.991999999999999, 0.6548442857142857]) = 9.646844285714284
- tar_emi_exclLU = 8.991999999999999
- tar_emi_inclLU = 9.646844285714284

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -0.982 (-0.982 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [11.466 11.466]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 11.466
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 11.466 + -0.982 = 10.484 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 10.484
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([10.484, 0.6548442857142857]) = 11.138844285714285
- tar_emi_exclLU = 10.484
- tar_emi_inclLU = 11.138844285714285

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -1.518 (-1.518 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [9.379 9.379]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 9.379
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 9.379 + -1.518 = 7.861 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 7.861
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([7.861, 0.6548442857142857]) = 8.515844285714286
- tar_emi_exclLU = 7.861
- tar_emi_inclLU = 8.515844285714286

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -3.152 (-3.152 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [11.466 11.466]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 11.466
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 11.466 + -3.152 = 8.314 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 8.314
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([8.314, 0.6548442857142857]) = 8.968844285714285
- tar_emi_exclLU = 8.314
- tar_emi_inclLU = 8.968844285714285

## tar_type_used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 9.003 (9.003 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [9.379 9.379]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 9.003
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([9.003, 0.6548442857142857]) = 9.657844285714285
- tar_emi_exclLU = 9.003
- tar_emi_inclLU = 9.657844285714285

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 10.484 (10.484 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [11.466 11.466]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 10.484
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([10.484, 0.6548442857142857]) = 11.138844285714285
- tar_emi_exclLU = 10.484
- tar_emi_inclLU = 11.138844285714285

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 7.861 (7.861 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [9.379 9.379]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 7.861
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([7.861, 0.6548442857142857]) = 8.515844285714286
- tar_emi_exclLU = 7.861
- tar_emi_inclLU = 8.515844285714286

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 8.314 (8.314 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [11.466 11.466]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 8.314
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([8.314, 0.6548442857142857]) = 8.968844285714285
- tar_emi_exclLU = 8.314
- tar_emi_inclLU = 8.968844285714285

## tar_type_used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -6.2 (-6.2%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [9.379 9.379]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -6.2 / 100. = 0.938
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 6.1204 * 0.159251254 = 0.9746813749816
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 6.1204 * (1 - 0.159251254) = 5.1457186250184
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.938 * 0.9746813749816 + 5.1457186250184 = 6.059969754751141
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (0.9746813749816 + 0.6548442857142857) + 5.1457186250184 = nan
- tar_emi_exclLU = ndc_value_exclLU = 6.059969754751141
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([6.059969754751141, 0.6548442857142857]) = 6.714814040465427
- tar_emi_exclLU = 6.059969754751141
- tar_emi_inclLU = 6.714814040465427

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -12.0 (-12%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [11.466 11.466]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -12.0 / 100. = 0.88
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 6.4733 * 0.164434023 = 1.0644307610859
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 6.4733 * (1 - 0.164434023) = 5.4088692389141
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.88 * 1.0644307610859 + 5.4088692389141 = 6.345568308669693
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (1.0644307610859 + 0.6548442857142857) + 5.4088692389141 = nan
- tar_emi_exclLU = ndc_value_exclLU = 6.345568308669693
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([6.345568308669693, 0.6548442857142857]) = 7.000412594383978
- tar_emi_exclLU = 6.345568308669693
- tar_emi_inclLU = 7.000412594383978

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -24.9 (-24.9%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [9.379 9.379]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -24.9 / 100. = 0.751
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 6.1204 * 0.159251254 = 0.9746813749816
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 6.1204 * (1 - 0.159251254) = 5.1457186250184
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.751 * 0.9746813749816 + 5.1457186250184 = 5.877704337629582
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (0.9746813749816 + 0.6548442857142857) + 5.1457186250184 = nan
- tar_emi_exclLU = ndc_value_exclLU = 5.877704337629582
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([5.877704337629582, 0.6548442857142857]) = 6.532548623343867
- tar_emi_exclLU = 5.877704337629582
- tar_emi_inclLU = 6.532548623343867

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -38.5 (-38.5%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [11.466 11.466]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -38.5 / 100. = 0.615
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_refyr = 0.6548442857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (0.6548442857142857).
    - bl_onlyLU_taryr = 0.6548442857142857
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 6.4733 * 0.164434023 = 1.0644307610859
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 6.4733 * (1 - 0.164434023) = 5.4088692389141
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.615 * 1.0644307610859 + 5.4088692389141 = 6.063494156981928
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (1.0644307610859 + 0.6548442857142857) + 5.4088692389141 = nan
- tar_emi_exclLU = ndc_value_exclLU = 6.063494156981928
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([6.063494156981928, 0.6548442857142857]) = 6.718338442696214
- tar_emi_exclLU = 6.063494156981928
- tar_emi_inclLU = 6.718338442696214