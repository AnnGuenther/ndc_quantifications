

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -2.1 (-2.100 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [7. 7.]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 7.0 - 16.3831 = -9.383099999999999
    - bl_onlyLU_refyr = -9.383099999999999
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 7.0 - 16.3831 = -9.383099999999999
    - bl_onlyLU_taryr = -9.383099999999999
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 7.0
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 7.0 + -2.1 = 4.9
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 4.9
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([4.9, - -9.383099999999999]) = 14.2831.
- tar_emi_exclLU = 14.2831
- tar_emi_inclLU = 4.9

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 4.9 (4.900 MtCO2eq)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [7. 7.]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 7.0 - 16.3831 = -9.383099999999999
    - bl_onlyLU_refyr = -9.383099999999999
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 7.0 - 16.3831 = -9.383099999999999
    - bl_onlyLU_taryr = -9.383099999999999
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 4.9
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([4.9, - -9.383099999999999]) = 14.2831.
- tar_emi_exclLU = 14.2831
- tar_emi_inclLU = 4.9

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -30.0 (-30%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [7. 7.]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -30.0 / 100. = 0.7
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_refyr'] = 7.0 - 16.3831 = -9.383099999999999
    - bl_onlyLU_refyr = -9.383099999999999
    - emi_onlyLU 2030: ndcs_emi_inclLU minus external_emi_exclLU used. ndcs_emi_inclLU[yr_int] - ict[f'emi_bl_exclLU_taryr'] = 7.0 - 16.3831 = -9.383099999999999
    - bl_onlyLU_taryr = -9.383099999999999
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 16.3831 * 0.376900587 = 6.1748000068797
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 16.3831 * (1 - 0.376900587) = 10.208299993120301
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 6.1748000068797 + 10.208299993120301 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.7 * 6.1748000068797 + -9.383099999999999 + 10.208299993120301 = 5.147559997936091
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 5.147559997936091
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([5.147559997936091, - -9.383099999999999]) = 14.530659997936091.
- tar_emi_exclLU = 14.530659997936091
- tar_emi_inclLU = 5.147559997936091