

## tar_type_used: RBY, refyr: 2006, taryr: 2030, conditional_best
- ndc_value_exclLU: -34.9 (-34.9%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [0.069574      nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -34.9 / 100. = 0.651
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2006: external_emi_onlyLU used (-0.036667).
    - bl_onlyLU_refyr = -0.036667
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.005238142857142857).
    - bl_onlyLU_taryr = -0.005238142857142857
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.08287699999999999 * 0.79842671 = 0.06617121044466999
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.09218483333333333 * (1 - 0.815742788) = 0.016985720378684666
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.651 * 0.06617121044466999 + 0.016985720378684666 = 0.06006317837816483
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 0.06617121044466999 + -0.036667 + 0.016985720378684666 = nan
- tar_emi_exclLU = ndc_value_exclLU = 0.06006317837816483
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.06006317837816483, -0.005238142857142857]) = 0.05482503552102197
- tar_emi_exclLU = 0.06006317837816483
- tar_emi_inclLU = 0.05482503552102197

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 0.050413 (0.050413 MtCO2eq)
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
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.005238142857142857).
    - bl_onlyLU_refyr = -0.005238142857142857
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.005238142857142857).
    - bl_onlyLU_taryr = -0.005238142857142857
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 0.050413
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.050413, -0.005238142857142857]) = 0.04517485714285714
- tar_emi_exclLU = 0.050413
- tar_emi_inclLU = 0.04517485714285714