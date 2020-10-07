

## tar_type_used: AEI, refyr: 2050, taryr: 2050, unconditional_best
- ndc_value_exclLU: 2.0 (2 tCO2eq/cap)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2050: external_emi_onlyLU used (-0.3431753).
    - bl_onlyLU_refyr = -0.3431753
    - emi_onlyLU 2050: external_emi_onlyLU used (-0.3431753).
    - bl_onlyLU_taryr = -0.3431753
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2815458.1959
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 2.0 * 1e-6 * 2815458.1959 = 5.6309163918000005
- tar_emi_exclLU = ndc_value_exclLU = 5.6309163918000005
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([5.6309163918000005, -0.3431753]) = 5.2877410918
- tar_emi_exclLU = 5.6309163918000005
- tar_emi_inclLU = 5.2877410918

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -0.7353077255002235 (-0.708 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [6.39447693 6.39447693]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3431753).
    - bl_onlyLU_refyr = -0.3431753
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3431753).
    - bl_onlyLU_taryr = -0.3431753
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 6.394476929244176
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 6.394476929244176 + -0.7353077255002235 = 5.659169203743953 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 5.659169203743953
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([5.659169203743953, -0.3431753]) = 5.315993903743952
- tar_emi_exclLU = 5.659169203743953
- tar_emi_inclLU = 5.315993903743952

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 5.659169203743952 (5.449 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [6.39447693 6.39447693]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3431753).
    - bl_onlyLU_refyr = -0.3431753
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3431753).
    - bl_onlyLU_taryr = -0.3431753
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 5.659169203743952
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([5.659169203743952, -0.3431753]) = 5.315993903743951
- tar_emi_exclLU = 5.659169203743952
- tar_emi_inclLU = 5.315993903743951

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -11.5 (-11.5%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [6.39447693 6.39447693]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -11.5 / 100. = 0.885
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3431753).
    - bl_onlyLU_refyr = -0.3431753
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3431753).
    - bl_onlyLU_taryr = -0.3431753
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 11.4927 * 0.628183206 = 7.219521131596199
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 11.4927 * (1 - 0.628183206) = 4.2731788684038
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.885 * 7.219521131596199 + 4.2731788684038 = 10.662455069866436
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 7.219521131596199 + -0.3431753 + 4.2731788684038 = nan
- tar_emi_exclLU = ndc_value_exclLU = 10.662455069866436
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([10.662455069866436, -0.3431753]) = 10.319279769866435
- tar_emi_exclLU = 10.662455069866436
- tar_emi_inclLU = 10.319279769866435