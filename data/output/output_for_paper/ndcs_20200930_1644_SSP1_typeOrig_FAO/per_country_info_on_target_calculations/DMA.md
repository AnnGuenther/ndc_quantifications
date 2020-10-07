

## tar_type_used: RBY, refyr: 2014, taryr: 2025, conditional_best
- ndc_value_exclLU: -39.2 (-39.2%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [0.16944374        nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -39.2 / 100. = 0.608
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2014: external_emi_onlyLU used (0.11).
    - bl_onlyLU_refyr = 0.11
    - emi_onlyLU 2025: external_emi_onlyLU used (0.17285714285714288).
    - bl_onlyLU_taryr = 0.17285714285714288
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.21986 * 0.7990897159999999 = 0.17568786495975997
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.22354166666666667 * (1 - 0.797148401) = 0.04534578452645834
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.608 * 0.17568786495975997 + 0.04534578452645834 = 0.1521640064219924
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (0.17568786495975997 + 0.11) + 0.04534578452645834 = nan
- tar_emi_exclLU = ndc_value_exclLU = 0.1521640064219924
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.1521640064219924, 0.17285714285714288]) = 0.3250211492791353
- tar_emi_exclLU = 0.1521640064219924
- tar_emi_inclLU = 0.3250211492791353

## tar_type_used: RBY, refyr: 2014, taryr: 2030, conditional_best
- ndc_value_exclLU: -44.7 (-44.7%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [0.16944374        nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -44.7 / 100. = 0.5529999999999999
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2014: external_emi_onlyLU used (0.11).
    - bl_onlyLU_refyr = 0.11
    - emi_onlyLU 2030: external_emi_onlyLU used (0.17285714285714288).
    - bl_onlyLU_taryr = 0.17285714285714288
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.21986 * 0.7990897159999999 = 0.17568786495975997
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.22354166666666667 * (1 - 0.797148401) = 0.04534578452645834
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.5529999999999999 * 0.17568786495975997 + 0.04534578452645834 = 0.1425011738492056
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (0.17568786495975997 + 0.11) + 0.04534578452645834 = nan
- tar_emi_exclLU = ndc_value_exclLU = 0.1425011738492056
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.1425011738492056, 0.17285714285714288]) = 0.3153583167063485
- tar_emi_exclLU = 0.1425011738492056
- tar_emi_inclLU = 0.3153583167063485

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 0.10300531065904409 (0.100 MtCO2eq_SAR)
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
    - emi_onlyLU 2025: external_emi_onlyLU used (0.17285714285714288).
    - bl_onlyLU_refyr = 0.17285714285714288
    - emi_onlyLU 2025: external_emi_onlyLU used (0.17285714285714288).
    - bl_onlyLU_taryr = 0.17285714285714288
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 0.10300531065904409
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.10300531065904409, 0.17285714285714288]) = 0.275862453516187
- tar_emi_exclLU = 0.10300531065904409
- tar_emi_inclLU = 0.275862453516187

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 0.09373483269973011 (0.091 MtCO2eq_SAR)
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
    - emi_onlyLU 2030: external_emi_onlyLU used (0.17285714285714288).
    - bl_onlyLU_refyr = 0.17285714285714288
    - emi_onlyLU 2030: external_emi_onlyLU used (0.17285714285714288).
    - bl_onlyLU_taryr = 0.17285714285714288
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 0.09373483269973011
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.09373483269973011, 0.17285714285714288]) = 0.266591975556873
- tar_emi_exclLU = 0.09373483269973011
- tar_emi_inclLU = 0.266591975556873