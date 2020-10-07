

## tar_type_used: RBY, refyr: 1990, taryr: 2030, unconditional_best
- ndc_value_exclLU: -35.0 (-35%)
- ndc_value_inclLU: -35.0 (-35%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [73.86158731         nan]
  - ndcs_emi_exclLU for refyr and taryr: [77.77521947         nan]
  - ndcs_emi_onlyLU for refyr and taryr: [-3.91363216         nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -35.0 / 100. = 0.65
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -35.0 / 100. = 0.65
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 1990: ndcs_emi_onlyLU used (-3.913632158886837).
    - bl_onlyLU_refyr = -3.913632158886837
    - emi_onlyLU 2030: external_emi_onlyLU used (-5.621175).
    - bl_onlyLU_taryr = -5.621175
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 77.7572 * 1.0 = 77.7572
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 80.6796 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.65 * 77.7572 + 0.0 = 50.54218
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.65 * 77.7572 + -3.913632158886837 + 0.0 = 46.62854784111317
- tar_emi_exclLU = ndc_value_exclLU = 50.54218
- tar_emi_inclLU = ndc_value_inclLU = 46.62854784111317
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 50.54218
- tar_emi_inclLU = 46.62854784111317

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 50.55373356459108 (47.665 MtCO2eq_SAR)
- ndc_value_inclLU: 48.01040296377519 (45.267 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-5.621175).
    - bl_onlyLU_refyr = -5.621175
    - emi_onlyLU 2030: external_emi_onlyLU used (-5.621175).
    - bl_onlyLU_taryr = -5.621175
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 50.55373356459108
- tar_emi_inclLU = ndc_value_inclLU = 48.01040296377519
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 50.55373356459108
- tar_emi_inclLU = 48.01040296377519