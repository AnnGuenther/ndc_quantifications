

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 42.6029
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 42.6029 + -42.31412061078264 = 0.28877938921736046 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -48.79077172467794 = 38.644018312908614
- tar_emi_exclLU = ndc_value_exclLU = 0.28877938921736046
- tar_emi_inclLU = ndc_value_inclLU = 38.644018312908614
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.28877938921736046
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 42.6029
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 42.6029 + -45.336557797267105 = -2.7336577972671066 # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-45.337 MtCO2eq) is < 0 (-2.734 MtCO2eq, compared to baseline 42.603 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -51.813208911162405 = 35.62158112642415
- tar_emi_exclLU = ndc_value_exclLU = -2.7336577972671066
- tar_emi_inclLU = ndc_value_inclLU = 35.62158112642415
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -2.7336577972671066
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 0.999973818 = 28.3998564154908
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 42.6029 * (1 - 0.992709416) = 0.31060002109360185
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 94486128818.1051 / 27592626953.125 = 3.4243252365430936
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.4243252365430936 * 0.51 * 28.3998564154908 + 0.31060002109360185 = 49.90827599035397
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.4243252365430936 * nan * (28.3998564154908 + 0.7069) + 0.31060002109360185 = nan
- tar_emi_exclLU = ndc_value_exclLU = 49.90827599035397
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([49.90827599035397, 44.831890037586554]) = 94.74016602794052
- tar_emi_exclLU = 49.90827599035397
- tar_emi_inclLU = 94.74016602794052

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 0.999973818 = 28.3998564154908
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 42.6029 * (1 - 0.992709416) = 0.31060002109360185
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 94486128818.1051 / 27592626953.125 = 3.4243252365430936
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.4243252365430936 * 0.48 * 28.3998564154908 + 0.31060002109360185 = 46.990765639220996
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.4243252365430936 * nan * (28.3998564154908 + 0.7069) + 0.31060002109360185 = nan
- tar_emi_exclLU = ndc_value_exclLU = 46.990765639220996
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([46.990765639220996, 44.831890037586554]) = 91.82265567680756
- tar_emi_exclLU = 46.990765639220996
- tar_emi_inclLU = 91.82265567680756

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 42.6029 * 0.992709416 = 42.2922999789064
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 42.6029 * (1 - 0.992709416) = 0.31060002109360185
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.516 * 42.2922999789064 + 0.31060002109360185 = 22.133426810209304
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.44200000000000006 * (42.2922999789064 + 44.831890037586554) + 0.31060002109360185 = 38.819492008383484
- tar_emi_exclLU = ndc_value_exclLU = 22.133426810209304
- tar_emi_inclLU = ndc_value_inclLU = 38.819492008383484
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 22.133426810209304
- tar_emi_inclLU = 38.819492008383484

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 42.6029 * 0.992709416 = 42.2922999789064
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 42.6029 * (1 - 0.992709416) = 0.31060002109360185
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.481 * 42.2922999789064 + 0.31060002109360185 = 20.65319631094758
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.40700000000000003 * (42.2922999789064 + 44.831890037586554) + 0.31060002109360185 = 35.77014535780623
- tar_emi_exclLU = ndc_value_exclLU = 20.65319631094758
- tar_emi_inclLU = ndc_value_inclLU = 35.77014535780623
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 20.65319631094758
- tar_emi_inclLU = 35.77014535780623

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 42.6029
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 42.6029 + -42.31412061078264 = 0.28877938921736046 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -48.79077172467794 = 38.644018312908614
- tar_emi_exclLU = ndc_value_exclLU = 0.28877938921736046
- tar_emi_inclLU = ndc_value_inclLU = 38.644018312908614
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 0.28877938921736046
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 42.6029
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 42.6029 + -45.336557797267105 = -2.7336577972671066 # ndc_value is negative for a reduction ...
  - ABS_exclLU from ABU_exclLU (-45.337 MtCO2eq) is < 0 (-2.734 MtCO2eq, compared to baseline 42.603 MtCO2eq) and will be set to 0 MtCO2eq.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 87.43479003758655
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 87.43479003758655 + -51.813208911162405 = 35.62158112642415
- tar_emi_exclLU = ndc_value_exclLU = -2.7336577972671066
- tar_emi_inclLU = ndc_value_inclLU = 35.62158112642415
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = -2.7336577972671066
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 0.999973818 = 28.3998564154908
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 42.6029 * (1 - 0.992709416) = 0.31060002109360185
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 94486128818.1051 / 27592626953.125 = 3.4243252365430936
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.4243252365430936 * 0.51 * 28.3998564154908 + 0.31060002109360185 = 49.90827599035397
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.4243252365430936 * nan * (28.3998564154908 + 0.7069) + 0.31060002109360185 = nan
- tar_emi_exclLU = ndc_value_exclLU = 49.90827599035397
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([49.90827599035397, 44.831890037586554]) = 94.74016602794052
- tar_emi_exclLU = 49.90827599035397
- tar_emi_inclLU = 94.74016602794052

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 28.4006 * 0.999973818 = 28.3998564154908
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 42.6029 * (1 - 0.992709416) = 0.31060002109360185
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 94486128818.1051 / 27592626953.125 = 3.4243252365430936
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.4243252365430936 * 0.48 * 28.3998564154908 + 0.31060002109360185 = 46.990765639220996
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 3.4243252365430936 * nan * (28.3998564154908 + 0.7069) + 0.31060002109360185 = nan
- tar_emi_exclLU = ndc_value_exclLU = 46.990765639220996
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([46.990765639220996, 44.831890037586554]) = 91.82265567680756
- tar_emi_exclLU = 46.990765639220996
- tar_emi_inclLU = 91.82265567680756

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 42.6029 * 0.992709416 = 42.2922999789064
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 42.6029 * (1 - 0.992709416) = 0.31060002109360185
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.516 * 42.2922999789064 + 0.31060002109360185 = 22.133426810209304
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.44200000000000006 * (42.2922999789064 + 44.831890037586554) + 0.31060002109360185 = 38.819492008383484
- tar_emi_exclLU = ndc_value_exclLU = 22.133426810209304
- tar_emi_inclLU = ndc_value_inclLU = 38.819492008383484
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 22.133426810209304
- tar_emi_inclLU = 38.819492008383484

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_refyr = 44.831890037586554
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 87.43479003758655 - 42.6029 = 44.831890037586554
    - bl_onlyLU_taryr = 44.831890037586554
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 42.6029 * 0.992709416 = 42.2922999789064
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 42.6029 * (1 - 0.992709416) = 0.31060002109360185
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.481 * 42.2922999789064 + 0.31060002109360185 = 20.65319631094758
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.40700000000000003 * (42.2922999789064 + 44.831890037586554) + 0.31060002109360185 = 35.77014535780623
- tar_emi_exclLU = ndc_value_exclLU = 20.65319631094758
- tar_emi_inclLU = ndc_value_inclLU = 35.77014535780623
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 20.65319631094758
- tar_emi_inclLU = 35.77014535780623