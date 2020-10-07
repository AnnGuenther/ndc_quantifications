

## tar_type_used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 2.3 (2.3 tCO2eq/capita (energy CO2))
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
    - emi_onlyLU 2030: external_emi_onlyLU used (-83.0).
    - bl_onlyLU_refyr = -83.0
    - emi_onlyLU 2030: external_emi_onlyLU used (-83.0).
    - bl_onlyLU_taryr = -83.0
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 14400150.0102
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 2.3 * 1e-6 * 14400150.0102 = 33.12034502345999
- tar_emi_exclLU = ndc_value_exclLU = 33.12034502345999
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([33.12034502345999, -83.0]) = -49.87965497654001
- tar_emi_exclLU = 33.12034502345999
- tar_emi_inclLU = -49.87965497654001

## tar_type_used: REI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -33.0 (-33%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -33.0 / 100. = 0.6699999999999999
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-83.0).
    - bl_onlyLU_refyr = -83.0
    - emi_onlyLU 2030: external_emi_onlyLU used (-83.0).
    - bl_onlyLU_taryr = -83.0
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 29.7289 * 0.452711995 = 13.4586296281555
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 29.7289 * (1 - 0.452711995) = 16.2702703718445
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.6699999999999999 * 13.4586296281555 + 16.2702703718445 = 25.287552222708683
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 13.4586296281555 + -83.0 + 16.2702703718445 = nan
- tar_emi_exclLU = ndc_value_exclLU = 25.287552222708683
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([25.287552222708683, -83.0]) = -57.71244777729132
- tar_emi_exclLU = 25.287552222708683
- tar_emi_inclLU = -57.71244777729132