

## tar_type_used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 2.8765466805339517 (2.7 tCO2eq_SAR/capita)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-8.686782928571429).
    - bl_onlyLU_refyr = -8.686782928571429
    - emi_onlyLU 2030: external_emi_onlyLU used (-8.686782928571429).
    - bl_onlyLU_taryr = -8.686782928571429
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 11150583.1929
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 2.8765466805339517 * 1e-6 * 11150583.1929 = 32.07517306955417
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 32.07517306955417
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([32.07517306955417, - -8.686782928571429]) = 40.7619559981256.
- tar_emi_exclLU = 40.7619559981256
- tar_emi_inclLU = 32.07517306955417

## tar_type_used: REI, refyr: 2010, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -25.0 (-25%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -25.0 / 100. = 0.75
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2010: external_emi_onlyLU used (-8.7073846).
    - bl_onlyLU_refyr = -8.7073846
    - emi_onlyLU 2030: external_emi_onlyLU used (-8.686782928571429).
    - bl_onlyLU_taryr = -8.686782928571429
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 27.491 * 1.0 = 27.491
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 48.8225 * (1 - 1.0) = 0.0
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 11150583.1929 / 9695121.0 = 1.1501231591539705
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.1501231591539705 * nan * 27.491 + 0.0 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.1501231591539705 * 0.75 * 27.491 + -8.7073846 + 0.0 = 15.00614222622635
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 15.00614222622635
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([15.00614222622635, - -8.686782928571429]) = 23.692925154797777.
- tar_emi_exclLU = 23.692925154797777
- tar_emi_inclLU = 15.00614222622635