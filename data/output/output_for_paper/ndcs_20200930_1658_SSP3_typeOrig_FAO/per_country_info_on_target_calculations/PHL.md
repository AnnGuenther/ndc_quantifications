

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -70.0 (-70%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -70.0 / 100. = 0.30000000000000004
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-47.10218371428571).
    - bl_onlyLU_refyr = -47.10218371428571
    - emi_onlyLU 2030: external_emi_onlyLU used (-47.10218371428571).
    - bl_onlyLU_taryr = -47.10218371428571
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 290.7093 * 0.774533375 = 225.16405527288748
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 290.7093 * (1 - 0.774533375) = 65.5452447271125
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 225.16405527288748 + 65.5452447271125 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.30000000000000004 * 225.16405527288748 + -47.10218371428571 + 65.5452447271125 = 85.99227759469306
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 85.99227759469306
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([85.99227759469306, - -47.10218371428571]) = 133.09446130897877.
- tar_emi_exclLU = 133.09446130897877
- tar_emi_inclLU = 85.99227759469306