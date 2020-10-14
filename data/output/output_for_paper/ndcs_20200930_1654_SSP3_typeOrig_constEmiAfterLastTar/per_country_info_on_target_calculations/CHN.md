

## tar_type_used: REI, refyr: 2005, taryr: 2030, unconditional_worst
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -60.0 (-60%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -60.0 / 100. = 0.4
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: external_emi_onlyLU used (-420.6954).
    - bl_onlyLU_refyr = -420.6954
    - emi_onlyLU 2030: external_emi_onlyLU used (-553.3526571428571).
    - bl_onlyLU_taryr = -553.3526571428571
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 7808.0066 * 0.779733188 = 6088.161878143041
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 17717.0259 * (1 - 0.8097411940000001) = 3370.8201936050737
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 33402740259393.24 / 8456687000000.0 = 3.949861247009998
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.949861247009998 * nan * 6088.161878143041 + 3370.8201936050737 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 3.949861247009998 * 0.4 * 6088.161878143041 + -420.6954 + 3370.8201936050737 = 12569.082660805394
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 12569.082660805394
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([12569.082660805394, - -553.3526571428571]) = 13122.435317948251.
- tar_emi_exclLU = 13122.435317948251
- tar_emi_inclLU = 12569.082660805394

## tar_type_used: REI, refyr: 2005, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -65.0 (-65%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -65.0 / 100. = 0.35
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: external_emi_onlyLU used (-420.6954).
    - bl_onlyLU_refyr = -420.6954
    - emi_onlyLU 2030: external_emi_onlyLU used (-553.3526571428571).
    - bl_onlyLU_taryr = -553.3526571428571
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 7808.0066 * 0.779733188 = 6088.161878143041
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 17717.0259 * (1 - 0.8097411940000001) = 3370.8201936050737
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 33402740259393.24 / 8456687000000.0 = 3.949861247009998
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.949861247009998 * nan * 6088.161878143041 + 3370.8201936050737 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 3.949861247009998 * 0.35 * 6088.161878143041 + -420.6954 + 3370.8201936050737 = 11366.712927405355
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 11366.712927405355
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([11366.712927405355, - -553.3526571428571]) = 11920.065584548212.
- tar_emi_exclLU = 11920.065584548212
- tar_emi_inclLU = 11366.712927405355