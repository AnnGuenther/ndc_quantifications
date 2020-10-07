

## tar_type_used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -42.31412061078264 (-39.2 MtCO2eq_AR2)
- ndc_value_inclLU: -48.79077172467794 (-45.2 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 41.0635
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 41.0635 + -42.31412061078264 = -1.25062061078264 # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-42.314 MtCO2eq) is < 0 (-1.251 MtCO2eq, compared to baseline 41.063 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -48.79077172467794 = 38.644018312908614
- tar_emi_exclLU = ndc_value_exclLU = -1.25062061078264
- tar_emi_inclLU = ndc_value_inclLU = 38.644018312908614
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -1.25062061078264
- tar_emi_inclLU = 38.644018312908614

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -45.336557797267105 (-42.0 MtCO2eq_AR2)
- ndc_value_inclLU: -51.813208911162405 (-48.0 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 41.0635
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 41.0635 + -45.336557797267105 = -4.273057797267107 # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-45.337 MtCO2eq) is < 0 (-4.273 MtCO2eq, compared to baseline 41.063 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -51.813208911162405 = 35.62158112642415
- tar_emi_exclLU = ndc_value_exclLU = -4.273057797267107
- tar_emi_inclLU = ndc_value_inclLU = 35.62158112642415
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -4.273057797267107
- tar_emi_inclLU = 35.62158112642415

## tar_type_used: REI, refyr: 1990, taryr: 2025, unconditional_best
- ndc_value_exclLU: -49.0 (-49% (SAR))
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [        nan 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -49.0 / 100. = 0.51
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (0.7069).
    - bl_onlyLU_refyr = 0.7069
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 0.999973818 = 28.3998564154908
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 41.0635 * (1 - 0.9896063409999999) = 0.4268000163465045
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 95988171752.5413 / 27592626953.125 = 3.4787616240964754
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.4787616240964754 * 0.51 * 28.3998564154908 + 0.4268000163465045 = 50.81292863665684
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.4787616240964754 * nan * (28.3998564154908 + 0.7069) + 0.4268000163465045 = nan
- tar_emi_exclLU = ndc_value_exclLU = 50.81292863665684
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([50.81292863665684, 46.371290037586554]) = 97.1842186742434
- tar_emi_exclLU = 50.81292863665684
- tar_emi_inclLU = 97.1842186742434

## tar_type_used: REI, refyr: 1990, taryr: 2025, conditional_best
- ndc_value_exclLU: -52.0 (-52% (SAR))
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [        nan 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -52.0 / 100. = 0.48
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (0.7069).
    - bl_onlyLU_refyr = 0.7069
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 0.999973818 = 28.3998564154908
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 41.0635 * (1 - 0.9896063409999999) = 0.4268000163465045
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 95988171752.5413 / 27592626953.125 = 3.4787616240964754
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.4787616240964754 * 0.48 * 28.3998564154908 + 0.4268000163465045 = 47.84903871781505
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.4787616240964754 * nan * (28.3998564154908 + 0.7069) + 0.4268000163465045 = nan
- tar_emi_exclLU = ndc_value_exclLU = 47.84903871781505
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([47.84903871781505, 46.371290037586554]) = 94.2203287554016
- tar_emi_exclLU = 47.84903871781505
- tar_emi_inclLU = 94.2203287554016

## tar_type_used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 45.12066942680393 (41.8 MtCO2eq_AR2)
- ndc_value_inclLU: 38.64401831290863 (35.8 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 45.12066942680393
- tar_emi_inclLU = ndc_value_inclLU = 38.64401831290863
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 45.12066942680393
- tar_emi_inclLU = 38.64401831290863

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 42.098232240319454 (39.0 MtCO2eq_AR2)
- ndc_value_inclLU: 35.621581126424154 (33.0 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 42.098232240319454
- tar_emi_inclLU = ndc_value_inclLU = 35.621581126424154
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 42.098232240319454
- tar_emi_inclLU = 35.621581126424154

## tar_type_used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -48.4 (-48.4%)
- ndc_value_inclLU: -55.8 (-55.8%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -48.4 / 100. = 0.516
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -55.8 / 100. = 0.44200000000000006
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 41.0635 * 0.9896063409999999 = 40.63669998365349
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 41.0635 * (1 - 0.9896063409999999) = 0.4268000163465045
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.516 * 40.63669998365349 + 0.4268000163465045 = 21.39533720791171
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.44200000000000006 * (40.63669998365349 + 46.371290037586554) + 0.4268000163465045 = 38.88433160573461
- tar_emi_exclLU = ndc_value_exclLU = 21.39533720791171
- tar_emi_inclLU = ndc_value_inclLU = 38.88433160573461
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 21.39533720791171
- tar_emi_inclLU = 38.88433160573461

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -51.9 (-51.9%)
- ndc_value_inclLU: -59.3 (-59.3%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -51.9 / 100. = 0.481
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -59.3 / 100. = 0.40700000000000003
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 41.0635 * 0.9896063409999999 = 40.63669998365349
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 41.0635 * (1 - 0.9896063409999999) = 0.4268000163465045
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.481 * 40.63669998365349 + 0.4268000163465045 = 19.973052708483834
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.40700000000000003 * (40.63669998365349 + 46.371290037586554) + 0.4268000163465045 = 35.839051954991206
- tar_emi_exclLU = ndc_value_exclLU = 19.973052708483834
- tar_emi_inclLU = ndc_value_inclLU = 35.839051954991206
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 19.973052708483834
- tar_emi_inclLU = 35.839051954991206

## tar_type_used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -42.31412061078264 (-39.2 MtCO2eq_AR2)
- ndc_value_inclLU: -48.79077172467794 (-45.2 MtCO2eq_SAR)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 41.0635
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 41.0635 + -42.31412061078264 = -1.25062061078264 # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-42.314 MtCO2eq) is < 0 (-1.251 MtCO2eq, compared to baseline 41.063 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -48.79077172467794 = 38.644018312908614
- tar_emi_exclLU = ndc_value_exclLU = -1.25062061078264
- tar_emi_inclLU = ndc_value_inclLU = 38.644018312908614
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -1.25062061078264
- tar_emi_inclLU = 38.644018312908614

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -45.336557797267105 (-42.0 MtCO2eq_AR2)
- ndc_value_inclLU: -51.813208911162405 (-48.0 MtCO2eq_SAR)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 41.0635
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 41.0635 + -45.336557797267105 = -4.273057797267107 # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-45.337 MtCO2eq) is < 0 (-4.273 MtCO2eq, compared to baseline 41.063 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -51.813208911162405 = 35.62158112642415
- tar_emi_exclLU = ndc_value_exclLU = -4.273057797267107
- tar_emi_inclLU = ndc_value_inclLU = 35.62158112642415
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -4.273057797267107
- tar_emi_inclLU = 35.62158112642415

## tar_type_used: REI, refyr: 1990, taryr: 2025, unconditional_best
- ndc_value_exclLU: -49.0 (-49% (SAR))
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [        nan 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -49.0 / 100. = 0.51
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (0.7069).
    - bl_onlyLU_refyr = 0.7069
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 0.999973818 = 28.3998564154908
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 41.0635 * (1 - 0.9896063409999999) = 0.4268000163465045
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 95988171752.5413 / 27592626953.125 = 3.4787616240964754
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.4787616240964754 * 0.51 * 28.3998564154908 + 0.4268000163465045 = 50.81292863665684
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.4787616240964754 * nan * (28.3998564154908 + 0.7069) + 0.4268000163465045 = nan
- tar_emi_exclLU = ndc_value_exclLU = 50.81292863665684
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([50.81292863665684, 46.371290037586554]) = 97.1842186742434
- tar_emi_exclLU = 50.81292863665684
- tar_emi_inclLU = 97.1842186742434

## tar_type_used: REI, refyr: 1990, taryr: 2025, conditional_best
- ndc_value_exclLU: -52.0 (-52% (SAR))
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [        nan 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -52.0 / 100. = 0.48
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: external_emi_onlyLU used (0.7069).
    - bl_onlyLU_refyr = 0.7069
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 0.999973818 = 28.3998564154908
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 41.0635 * (1 - 0.9896063409999999) = 0.4268000163465045
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 95988171752.5413 / 27592626953.125 = 3.4787616240964754
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.4787616240964754 * 0.48 * 28.3998564154908 + 0.4268000163465045 = 47.84903871781505
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.4787616240964754 * nan * (28.3998564154908 + 0.7069) + 0.4268000163465045 = nan
- tar_emi_exclLU = ndc_value_exclLU = 47.84903871781505
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([47.84903871781505, 46.371290037586554]) = 94.2203287554016
- tar_emi_exclLU = 47.84903871781505
- tar_emi_inclLU = 94.2203287554016

## tar_type_used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 45.12066942680393 (41.8 MtCO2eq_AR2)
- ndc_value_inclLU: 38.64401831290863 (35.8 MtCO2eq_SAR)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 45.12066942680393
- tar_emi_inclLU = ndc_value_inclLU = 38.64401831290863
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 45.12066942680393
- tar_emi_inclLU = 38.64401831290863

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 42.098232240319454 (39.0 MtCO2eq_AR2)
- ndc_value_inclLU: 35.621581126424154 (33.0 MtCO2eq_SAR)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 42.098232240319454
- tar_emi_inclLU = ndc_value_inclLU = 35.621581126424154
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 42.098232240319454
- tar_emi_inclLU = 35.621581126424154

## tar_type_used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -48.4 (-48.4%)
- ndc_value_inclLU: -55.8 (-55.8%)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -48.4 / 100. = 0.516
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -55.8 / 100. = 0.44200000000000006
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 41.0635 * 0.9896063409999999 = 40.63669998365349
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 41.0635 * (1 - 0.9896063409999999) = 0.4268000163465045
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.516 * 40.63669998365349 + 0.4268000163465045 = 21.39533720791171
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.44200000000000006 * (40.63669998365349 + 46.371290037586554) + 0.4268000163465045 = 38.88433160573461
- tar_emi_exclLU = ndc_value_exclLU = 21.39533720791171
- tar_emi_inclLU = ndc_value_inclLU = 38.88433160573461
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 21.39533720791171
- tar_emi_inclLU = 38.88433160573461

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -51.9 (-51.9%)
- ndc_value_inclLU: -59.3 (-59.3%)
- lulucf_first_try: False
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [87.43479004 87.43479004]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -51.9 / 100. = 0.481
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -59.3 / 100. = 0.40700000000000003
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_refyr = 46.371290037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 41.0635 = 46.371290037586554
    - bl_onlyLU_taryr = 46.371290037586554
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 41.0635 * 0.9896063409999999 = 40.63669998365349
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 41.0635 * (1 - 0.9896063409999999) = 0.4268000163465045
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.481 * 40.63669998365349 + 0.4268000163465045 = 19.973052708483834
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.40700000000000003 * (40.63669998365349 + 46.371290037586554) + 0.4268000163465045 = 35.839051954991206
- tar_emi_exclLU = ndc_value_exclLU = 19.973052708483834
- tar_emi_inclLU = ndc_value_inclLU = 35.839051954991206
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 19.973052708483834
- tar_emi_inclLU = 35.839051954991206