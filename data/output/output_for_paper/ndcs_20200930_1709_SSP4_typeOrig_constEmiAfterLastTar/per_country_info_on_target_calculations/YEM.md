

## tar_type_used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: -0.18526554155481048 (-0.18 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.84075938 40.84075938]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2025: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 40.840759382749326
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.840759382749326 + -0.18526554155481048 = 40.65549384119451 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 40.65549384119451
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([40.65549384119451, -1.7134999999999998]) = 38.94199384119452
- tar_emi_exclLU = 40.65549384119451
- tar_emi_inclLU = 38.94199384119452

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -0.47345638397340456 (-0.46 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [45.09157431 45.09157431]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 45.0915743084236
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 45.0915743084236 + -0.47345638397340456 = 44.618117924450196 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 44.618117924450196
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([44.618117924450196, -1.7134999999999998]) = 42.90461792445019
- tar_emi_exclLU = 44.618117924450196
- tar_emi_inclLU = 42.90461792445019

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -3.0260038453952376 (-2.94 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.84075938 40.84075938]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2025: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 40.840759382749326
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 40.840759382749326 + -3.0260038453952376 = 37.81475553735409 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 37.81475553735409
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([37.81475553735409, -1.7134999999999998]) = 36.10125553735409
- tar_emi_exclLU = 37.81475553735409
- tar_emi_inclLU = 36.10125553735409

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -6.309320942949935 (-6.13 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [45.09157431 45.09157431]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 45.0915743084236
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 45.0915743084236 + -6.309320942949935 = 38.782253365473665 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 38.782253365473665
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([38.782253365473665, -1.7134999999999998]) = 37.06875336547367
- tar_emi_exclLU = 38.782253365473665
- tar_emi_inclLU = 37.06875336547367

## tar_type_used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: 40.65549384119452 (39.5 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.84075938 40.84075938]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2025: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 40.65549384119452
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([40.65549384119452, -1.7134999999999998]) = 38.94199384119452
- tar_emi_exclLU = 40.65549384119452
- tar_emi_inclLU = 38.94199384119452

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 44.61811792445019 (43.35 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [45.09157431 45.09157431]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 44.61811792445019
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([44.61811792445019, -1.7134999999999998]) = 42.90461792445019
- tar_emi_exclLU = 44.61811792445019
- tar_emi_inclLU = 42.90461792445019

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 37.814755537354095 (36.74 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [40.84075938 40.84075938]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2025: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 37.814755537354095
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([37.814755537354095, -1.7134999999999998]) = 36.10125553735409
- tar_emi_exclLU = 37.814755537354095
- tar_emi_inclLU = 36.10125553735409

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 38.77196083538728 (37.67 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [45.09157431 45.09157431]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 38.77196083538728
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([38.77196083538728, -1.7134999999999998]) = 37.05846083538728
- tar_emi_exclLU = 38.77196083538728
- tar_emi_inclLU = 37.05846083538728

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -1.0 (-1%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [45.09157431 45.09157431]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -1.0 / 100. = 0.99
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 76.3199 * 0.942275555 = 71.9143761300445
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 76.3199 * (1 - 0.942275555) = 4.405523869955497
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.99 * 71.9143761300445 + 4.405523869955497 = 75.60075623869956
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 71.9143761300445 + -1.7134999999999998 + 4.405523869955497 = nan
- tar_emi_exclLU = ndc_value_exclLU = 75.60075623869956
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([75.60075623869956, -1.7134999999999998]) = 73.88725623869956
- tar_emi_exclLU = 75.60075623869956
- tar_emi_inclLU = 73.88725623869956

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -14.0 (-14%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [45.09157431 45.09157431]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -14.0 / 100. = 0.86
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_refyr = -1.7134999999999998
    - emi_onlyLU 2030: external_emi_onlyLU used (-1.7134999999999998).
    - bl_onlyLU_taryr = -1.7134999999999998
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 76.3199 * 0.942275555 = 71.9143761300445
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 76.3199 * (1 - 0.942275555) = 4.405523869955497
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.86 * 71.9143761300445 + 4.405523869955497 = 66.25188734179378
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 71.9143761300445 + -1.7134999999999998 + 4.405523869955497 = nan
- tar_emi_exclLU = ndc_value_exclLU = 66.25188734179378
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([66.25188734179378, -1.7134999999999998]) = 64.53838734179378
- tar_emi_exclLU = 66.25188734179378
- tar_emi_inclLU = 64.53838734179378