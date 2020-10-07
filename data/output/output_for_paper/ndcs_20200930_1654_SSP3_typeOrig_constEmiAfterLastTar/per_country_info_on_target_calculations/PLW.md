

## tar_type_used: RBY, refyr: 2005, taryr: 2025, conditional_best
- ndc_value_exclLU: -22.0 (-22%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -22.0 / 100. = 0.78
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2005: external_emi_onlyLU used (-0.14667).
    - bl_onlyLU_refyr = -0.14667
    - emi_onlyLU 2025: external_emi_onlyLU used (0.0).
    - bl_onlyLU_taryr = 0.0
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.26287 * 0.990571773 = 0.26039160196850997
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.28117000000000003 * (1 - 0.9905651329999999) = 0.0026528015543900198
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.78 * 0.26039160196850997 + 0.0026528015543900198 = 0.2057582510898278
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 0.26039160196850997 + -0.14667 + 0.0026528015543900198 = nan
- tar_emi_exclLU = ndc_value_exclLU = 0.2057582510898278
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.2057582510898278, 0.0]) = 0.2057582510898278
- tar_emi_exclLU = 0.2057582510898278
- tar_emi_inclLU = 0.2057582510898278