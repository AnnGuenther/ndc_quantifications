

## tar_type_used: REI, refyr: 2010, taryr: 2030, conditional_best
- ndc_value_exclLU: -10.0 (-10%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -10.0 / 100. = 0.9
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2010: external_emi_onlyLU used (-1.32).
    - bl_onlyLU_refyr = -1.32
    - emi_onlyLU 2030: external_emi_onlyLU used (-14.257551571428568).
    - bl_onlyLU_taryr = -14.257551571428568
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 219.5286 * 0.819244427 = 179.8475821171122
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 288.0084 * (1 - 0.7471198640000001) = 72.83160336114237
- intensity_growth = ict[ict['int_ref'].lower() + '\_taryr'] / ict[ict['int_ref'].lower() + '\_refyr'] = 650985182562.5647 / 179653937500.0 = 3.6235508757639376
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 3.6235508757639376 * 0.9 * 179.8475821171122 + 72.83160336114237 = 659.3497806771821
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 3.6235508757639376 * nan * 179.8475821171122 + -1.32 + 72.83160336114237 = nan
- tar_emi_exclLU = ndc_value_exclLU = 659.3497806771821
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([659.3497806771821, -14.257551571428568]) = 645.0922291057535
- tar_emi_exclLU = 659.3497806771821
- tar_emi_inclLU = 645.0922291057535