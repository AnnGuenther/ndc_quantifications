

## tar_type_used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 3.0654590829752513 (3 tCO2eq_SAR/capita)
- ndc_value_inclLU: 2.656731205245218 (2.6 tCO2eq_SAR/capita)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [174.52680379 174.52680379]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_refyr = 2.6997037907243
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_taryr = 2.6997037907243
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 41377674.6435
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 3.0654590829752513 * 1e-6 * 41377674.6435 = 126.8415685683118
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 2.656731205245218 * 1e-6 * 41377674.6435 = 109.92935942587023
- tar_emi_exclLU = ndc_value_exclLU = 126.8415685683118
- tar_emi_inclLU = ndc_value_inclLU = 109.92935942587023
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 126.8415685683118
- tar_emi_inclLU = 109.92935942587023

## tar_type_used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -23.09312509174689 (-22.6 MtCO2eq_SAR)
- ndc_value_inclLU: -26.567312052452177 (-26.0 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [145.81367038 145.81367038]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_refyr = -2.664329619810559
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_taryr = -2.664329619810559
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 148.47799999999995
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 148.47799999999995 + -23.09312509174689 = 125.38487490825307 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 145.8136703801894
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 145.8136703801894 + -26.567312052452177 = 119.24635832773721
- tar_emi_exclLU = ndc_value_exclLU = 125.38487490825307
- tar_emi_inclLU = ndc_value_inclLU = 119.24635832773721
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 125.38487490825307
- tar_emi_inclLU = 119.24635832773721

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -25.545492358127092 (-25.0 MtCO2eq_SAR)
- ndc_value_inclLU: -30.04149901315746 (-29.4 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [174.52680379 174.52680379]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_refyr = 2.6997037907243
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_taryr = 2.6997037907243
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 171.8271
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 171.8271 + -25.545492358127092 = 146.2816076418729 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 174.5268037907243
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 174.5268037907243 + -30.04149901315746 = 144.48530477756685
- tar_emi_exclLU = ndc_value_exclLU = 146.2816076418729
- tar_emi_inclLU = ndc_value_inclLU = 144.48530477756685
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 146.2816076418729
- tar_emi_inclLU = 144.48530477756685

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -45.879704275196254 (-44.9 MtCO2eq_SAR)
- ndc_value_inclLU: -52.21498638001178 (-51.1 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [145.81367038 145.81367038]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_refyr = -2.664329619810559
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_taryr = -2.664329619810559
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 148.47799999999995
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 148.47799999999995 + -45.879704275196254 = 102.5982957248037 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 145.8136703801894
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 145.8136703801894 + -52.21498638001178 = 93.59868400017761
- tar_emi_exclLU = ndc_value_exclLU = 102.5982957248037
- tar_emi_inclLU = ndc_value_inclLU = 93.59868400017761
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 102.5982957248037
- tar_emi_inclLU = 93.59868400017761

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -64.5790046813453 (-63.2 MtCO2eq_SAR)
- ndc_value_inclLU: -73.46883602197352 (-71.9 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [174.52680379 174.52680379]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_refyr = 2.6997037907243
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_taryr = 2.6997037907243
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 171.8271
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 171.8271 + -64.5790046813453 = 107.2480953186547 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 174.5268037907243
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 174.5268037907243 + -73.46883602197352 = 101.05796776875079
- tar_emi_exclLU = ndc_value_exclLU = 107.2480953186547
- tar_emi_inclLU = ndc_value_inclLU = 101.05796776875079
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 107.2480953186547
- tar_emi_inclLU = 101.05796776875079

## tar_type_used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 102.07978746307586 (99.9 MtCO2eq_SAR)
- ndc_value_inclLU: 119.24635832773727 (116.7 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [145.81367038 145.81367038]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_refyr = -2.664329619810559
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_taryr = -2.664329619810559
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 102.07978746307586
- tar_emi_inclLU = ndc_value_inclLU = 119.24635832773727
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 102.07978746307586
- tar_emi_inclLU = 119.24635832773727

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 126.39909618801285 (123.7 MtCO2eq_SAR)
- ndc_value_inclLU: 144.48530477756682 (141.4 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [174.52680379 174.52680379]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_refyr = 2.6997037907243
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_taryr = 2.6997037907243
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 126.39909618801285
- tar_emi_inclLU = ndc_value_inclLU = 144.48530477756682
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 126.39909618801285
- tar_emi_inclLU = 144.48530477756682

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 58.14154060709726 (56.9 MtCO2eq_SAR)
- ndc_value_inclLU: 93.59868400017766 (91.6 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [145.81367038 145.81367038]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_refyr = -2.664329619810559
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_taryr = -2.664329619810559
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 58.14154060709726
- tar_emi_inclLU = ndc_value_inclLU = 93.59868400017766
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 58.14154060709726
- tar_emi_inclLU = 93.59868400017766

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 51.090984716254184 (50.0 MtCO2eq_SAR)
- ndc_value_inclLU: 101.05796776875079 (98.9 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [174.52680379 174.52680379]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_refyr = 2.6997037907243
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_taryr = 2.6997037907243
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 51.090984716254184
- tar_emi_inclLU = ndc_value_inclLU = 101.05796776875079
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 51.090984716254184
- tar_emi_inclLU = 101.05796776875079

## tar_type_used: RBU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -15.8 (-15.8%)
- ndc_value_inclLU: -18.2 (-18.2%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [145.81367038 145.81367038]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -15.8 / 100. = 0.842
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -18.2 / 100. = 0.8180000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_refyr = -2.664329619810559
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_taryr = -2.664329619810559
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 148.47799999999995 * 1.0 = 148.47799999999995
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 148.47799999999995 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.842 * 148.47799999999995 + 0.0 = 125.01847599999995
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8180000000000001 * 148.47799999999995 + -2.664329619810559 + 0.0 = 118.79067438018942
- tar_emi_exclLU = ndc_value_exclLU = 125.01847599999995
- tar_emi_inclLU = ndc_value_inclLU = 118.79067438018942
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 125.01847599999995
- tar_emi_inclLU = 118.79067438018942

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -14.6 (-14.6%)
- ndc_value_inclLU: -17.2 (-17.2%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [174.52680379 174.52680379]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -14.6 / 100. = 0.854
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -17.2 / 100. = 0.8280000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_refyr = 2.6997037907243
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_taryr = 2.6997037907243
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 171.8271 * 1.0 = 171.8271
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 171.8271 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.854 * 171.8271 + 0.0 = 146.7403434
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.8280000000000001 * (171.8271 + 2.6997037907243) + 0.0 = 144.50819353871972
- tar_emi_exclLU = ndc_value_exclLU = 146.7403434
- tar_emi_inclLU = ndc_value_inclLU = 144.50819353871972
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 146.7403434
- tar_emi_inclLU = 144.50819353871972

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -31.5 (-31.5%)
- ndc_value_inclLU: -35.8 (-35.8%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [145.81367038 145.81367038]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -31.5 / 100. = 0.685
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -35.8 / 100. = 0.642
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_refyr = -2.664329619810559
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 148.47799999999995 = -2.664329619810559
    - bl_onlyLU_taryr = -2.664329619810559
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 148.47799999999995 * 1.0 = 148.47799999999995
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 148.47799999999995 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.685 * 148.47799999999995 + 0.0 = 101.70742999999997
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.642 * 148.47799999999995 + -2.664329619810559 + 0.0 = 92.6585463801894
- tar_emi_exclLU = ndc_value_exclLU = 101.70742999999997
- tar_emi_inclLU = ndc_value_inclLU = 92.6585463801894
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 101.70742999999997
- tar_emi_inclLU = 92.6585463801894

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -37.0 (-37.0%)
- ndc_value_inclLU: -42.1 (-42.1%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [174.52680379 174.52680379]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -37.0 / 100. = 0.63
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -42.1 / 100. = 0.579
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_refyr = 2.6997037907243
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 171.8271 = 2.6997037907243
    - bl_onlyLU_taryr = 2.6997037907243
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 171.8271 * 1.0 = 171.8271
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 171.8271 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.63 * 171.8271 + 0.0 = 108.251073
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.579 * (171.8271 + 2.6997037907243) + 0.0 = 101.05101939482937
- tar_emi_exclLU = ndc_value_exclLU = 108.251073
- tar_emi_inclLU = ndc_value_inclLU = 101.05101939482937
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 108.251073
- tar_emi_inclLU = 101.05101939482937