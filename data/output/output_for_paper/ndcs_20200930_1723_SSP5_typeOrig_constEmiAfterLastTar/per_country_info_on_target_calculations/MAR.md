

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
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_refyr = -12.890396209275707
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_taryr = -12.890396209275707
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 36377206.7894
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 3.0654590829752513 * 1e-6 * 36377206.7894 = 111.51283896583519
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 2.656731205245218 * 1e-6 * 36377206.7894 = 96.64446043705716
- tar_emi_exclLU = ndc_value_exclLU = 111.51283896583519
- tar_emi_inclLU = ndc_value_inclLU = 96.64446043705716
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 111.51283896583519
- tar_emi_inclLU = 96.64446043705716

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_refyr = -9.944529619810595
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_taryr = -9.944529619810595
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 155.7582
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 155.7582 + -23.09312509174689 = 132.6650749082531 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 145.8136703801894
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 145.8136703801894 + -26.567312052452177 = 119.24635832773721
- tar_emi_exclLU = ndc_value_exclLU = 132.6650749082531
- tar_emi_inclLU = ndc_value_inclLU = 119.24635832773721
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 132.6650749082531
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
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_refyr = -12.890396209275707
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_taryr = -12.890396209275707
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 187.4172
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 187.4172 + -25.545492358127092 = 161.87170764187292 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 174.5268037907243
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 174.5268037907243 + -30.04149901315746 = 144.48530477756685
- tar_emi_exclLU = ndc_value_exclLU = 161.87170764187292
- tar_emi_inclLU = ndc_value_inclLU = 144.48530477756685
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 161.87170764187292
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_refyr = -9.944529619810595
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_taryr = -9.944529619810595
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 155.7582
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 155.7582 + -45.879704275196254 = 109.87849572480374 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 145.8136703801894
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 145.8136703801894 + -52.21498638001178 = 93.59868400017761
- tar_emi_exclLU = ndc_value_exclLU = 109.87849572480374
- tar_emi_inclLU = ndc_value_inclLU = 93.59868400017761
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 109.87849572480374
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
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_refyr = -12.890396209275707
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_taryr = -12.890396209275707
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 187.4172
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 187.4172 + -64.5790046813453 = 122.83819531865471 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 174.5268037907243
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 174.5268037907243 + -73.46883602197352 = 101.05796776875079
- tar_emi_exclLU = ndc_value_exclLU = 122.83819531865471
- tar_emi_inclLU = ndc_value_inclLU = 101.05796776875079
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 122.83819531865471
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_refyr = -9.944529619810595
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_taryr = -9.944529619810595
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
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_refyr = -12.890396209275707
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_taryr = -12.890396209275707
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_refyr = -9.944529619810595
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_taryr = -9.944529619810595
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
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_refyr = -12.890396209275707
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_taryr = -12.890396209275707
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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_refyr = -9.944529619810595
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_taryr = -9.944529619810595
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 155.7582 * 1.0 = 155.7582
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 155.7582 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.842 * 155.7582 + 0.0 = 131.14840439999998
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8180000000000001 * 155.7582 + -9.944529619810595 + 0.0 = 117.4656779801894
- tar_emi_exclLU = ndc_value_exclLU = 131.14840439999998
- tar_emi_inclLU = ndc_value_inclLU = 117.4656779801894
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 131.14840439999998
- tar_emi_inclLU = 117.4656779801894

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
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_refyr = -12.890396209275707
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_taryr = -12.890396209275707
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 187.4172 * 1.0 = 187.4172
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 187.4172 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.854 * 187.4172 + 0.0 = 160.0542888
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8280000000000001 * 187.4172 + -12.890396209275707 + 0.0 = 142.29104539072432
- tar_emi_exclLU = ndc_value_exclLU = 160.0542888
- tar_emi_inclLU = ndc_value_inclLU = 142.29104539072432
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 160.0542888
- tar_emi_inclLU = 142.29104539072432

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
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_refyr = -9.944529619810595
    - emi_onlyLU 2025: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 145.8136703801894 - 155.7582 = -9.944529619810595
    - bl_onlyLU_taryr = -9.944529619810595
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 155.7582 * 1.0 = 155.7582
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 155.7582 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.685 * 155.7582 + 0.0 = 106.694367
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.642 * 155.7582 + -9.944529619810595 + 0.0 = 90.0522347801894
- tar_emi_exclLU = ndc_value_exclLU = 106.694367
- tar_emi_inclLU = ndc_value_inclLU = 90.0522347801894
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 106.694367
- tar_emi_inclLU = 90.0522347801894

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
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_refyr = -12.890396209275707
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 174.5268037907243 - 187.4172 = -12.890396209275707
    - bl_onlyLU_taryr = -12.890396209275707
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 187.4172 * 1.0 = 187.4172
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 187.4172 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.63 * 187.4172 + 0.0 = 118.07283600000001
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.579 * 187.4172 + -12.890396209275707 + 0.0 = 95.6241625907243
- tar_emi_exclLU = ndc_value_exclLU = 118.07283600000001
- tar_emi_inclLU = ndc_value_inclLU = 95.6241625907243
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 118.07283600000001
- tar_emi_inclLU = 95.6241625907243