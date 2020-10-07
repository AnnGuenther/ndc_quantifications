

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -0.055065 (-0.055065 MtCO2eq)
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
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.07765624285714287).
    - bl_onlyLU_refyr = -0.07765624285714287
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.07765624285714287).
    - bl_onlyLU_taryr = -0.07765624285714287
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = nan
  - np.isnan(bl_exclLU_taryr), so bl_exclLU_taryr = ict['emi_bl_exclLU_taryr'] = 0.45251
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.45251 + -0.055065 = 0.39744500000000005 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 0.39744500000000005
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.39744500000000005, -0.07765624285714287]) = 0.31978875714285715
- tar_emi_exclLU = 0.39744500000000005
- tar_emi_inclLU = 0.31978875714285715

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -13.0 (-13%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [nan nan]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -13.0 / 100. = 0.87
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.07765624285714287).
    - bl_onlyLU_refyr = -0.07765624285714287
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.07765624285714287).
    - bl_onlyLU_taryr = -0.07765624285714287
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.45251 * 0.513624008 = 0.23241999986008
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.45251 * (1 - 0.513624008) = 0.22009000013992003
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.87 * 0.23241999986008 + 0.22009000013992003 = 0.42229540001818966
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 0.23241999986008 + -0.07765624285714287 + 0.22009000013992003 = nan
- tar_emi_exclLU = ndc_value_exclLU = 0.42229540001818966
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.42229540001818966, -0.07765624285714287]) = 0.34463915716104676
- tar_emi_exclLU = 0.42229540001818966
- tar_emi_inclLU = 0.34463915716104676