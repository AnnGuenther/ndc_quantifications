

## tar_type_used: AEI, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 1.32 (1.32 tCO2eq/cap)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [18.92128781 18.92128781]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_refyr = 36.74402857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_taryr = 36.74402857142857
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 6120302.287000001
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 1.32 * 1e-6 * 6120302.287000001 = 8.078799018840002
- tar_emi_exclLU = ndc_value_exclLU = 8.078799018840002
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([8.078799018840002, 36.74402857142857]) = 44.822827590268574
- tar_emi_exclLU = 8.078799018840002
- tar_emi_inclLU = 44.822827590268574

## tar_type_used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 1.72 (1.72 tCO2eq/cap)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [38.46533822 38.46533822]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_refyr = 36.74402857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_taryr = 36.74402857142857
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 6774751.2178
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 1.72 * 1e-6 * 6774751.2178 = 11.652572094615998
- tar_emi_exclLU = ndc_value_exclLU = 11.652572094615998
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([11.652572094615998, 36.74402857142857]) = 48.39660066604457
- tar_emi_exclLU = 11.652572094615998
- tar_emi_inclLU = 48.39660066604457

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -9.125310201522707 (-8.191 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [18.92128781 18.92128781]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_refyr = 36.74402857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_taryr = 36.74402857142857
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 18.921287811337034
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 18.921287811337034 + -9.125310201522707 = 9.795977609814328 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 9.795977609814328
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([9.795977609814328, 36.74402857142857]) = 46.5400061812429
- tar_emi_exclLU = 9.795977609814328
- tar_emi_inclLU = 46.5400061812429

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -20.798488115276207 (-18.669 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [38.46533822 38.46533822]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_refyr = 36.74402857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_taryr = 36.74402857142857
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 38.465338216087716
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 38.465338216087716 + -20.798488115276207 = 17.66685010081151 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 17.66685010081151
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([17.66685010081151, 36.74402857142857]) = 54.41087867224008
- tar_emi_exclLU = 17.66685010081151
- tar_emi_inclLU = 54.41087867224008

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 9.795977609814326 (8.793 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [18.92128781 18.92128781]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_refyr = 36.74402857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_taryr = 36.74402857142857
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 9.795977609814326
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([9.795977609814326, 36.74402857142857]) = 46.5400061812429
- tar_emi_exclLU = 9.795977609814326
- tar_emi_inclLU = 46.5400061812429

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 17.66685010081151 (15.858 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [38.46533822 38.46533822]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_refyr = 36.74402857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_taryr = 36.74402857142857
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 17.66685010081151
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([17.66685010081151, 36.74402857142857]) = 54.41087867224008
- tar_emi_exclLU = 17.66685010081151
- tar_emi_inclLU = 54.41087867224008

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -48.0 (-48%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [18.92128781 18.92128781]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -48.0 / 100. = 0.52
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_refyr = 36.74402857142857
    - emi_onlyLU 2025: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_taryr = 36.74402857142857
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 18.921287811337034 * 0.9945941770000001 = 18.81900267849689
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 18.921287811337034 * (1 - 0.9945941770000001) = 0.1022851328401439
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.52 * 18.81900267849689 + 0.1022851328401439 = 9.888166525658528
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (18.81900267849689 + 36.74402857142857) + 0.1022851328401439 = nan
- tar_emi_exclLU = ndc_value_exclLU = 9.888166525658528
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([9.888166525658528, 36.74402857142857]) = 46.6321950970871
- tar_emi_exclLU = 9.888166525658528
- tar_emi_inclLU = 46.6321950970871

## tar_type_used: RBU, refyr: 2035, taryr: 2035, conditional_best
- ndc_value_exclLU: -54.0 (-54%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -54.0 / 100. = 0.45999999999999996
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2035: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_refyr = 36.74402857142857
    - emi_onlyLU 2035: external_emi_onlyLU used (36.74402857142857).
    - bl_onlyLU_taryr = 36.74402857142857
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.13363821608772 * 0.9860459020000001 = 39.573609495323886
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.13363821608772 * (1 - 0.9860459020000001) = 0.5600287207638298
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.45999999999999996 * 39.573609495323886 + 0.5600287207638298 = 18.763889088612814
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (39.573609495323886 + 36.74402857142857) + 0.5600287207638298 = nan
- tar_emi_exclLU = ndc_value_exclLU = 18.763889088612814
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([18.763889088612814, 36.74402857142857]) = 55.507917660041386
- tar_emi_exclLU = 18.763889088612814
- tar_emi_inclLU = 55.507917660041386