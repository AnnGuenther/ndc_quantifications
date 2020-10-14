

## tar_type_used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 1.1 (1.1 tCO2eq/cap)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [400. 400.]
  - ndcs_emi_exclLU for refyr and taryr: [310. 310.]
  - ndcs_emi_onlyLU for refyr and taryr: [90. 90.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (90.0).
    - bl_onlyLU_refyr = 90.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (90.0).
    - bl_onlyLU_taryr = 90.0
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 142052893.7391
- tar_emi_inclLU = ndc_value_inclLU * 1e-6 * ref_act = 1.1 * 1e-6 * 142052893.7391 = 156.25818311301
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 156.25818311301
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([156.25818311301, - 90.0]) = 66.25818311301.
- tar_emi_exclLU = 66.25818311301
- tar_emi_inclLU = 156.25818311301

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -125.0 (-125 MtCO2eq_AR4)
- ndc_value_inclLU: -255.0 (-255 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [400. 400.]
  - ndcs_emi_exclLU for refyr and taryr: [310. 310.]
  - ndcs_emi_onlyLU for refyr and taryr: [90. 90.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (90.0).
    - bl_onlyLU_refyr = 90.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (90.0).
    - bl_onlyLU_taryr = 90.0
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 310.0
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 310.0 + -125.0 = 185.0 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 400.0
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 400.0 + -255.0 = 145.0
- tar_emi_exclLU = ndc_value_exclLU = 185.0
- tar_emi_inclLU = ndc_value_inclLU = 145.0
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 185.0
- tar_emi_inclLU = 145.0

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 185.0 (185 MtCO2eq_AR4)
- ndc_value_inclLU: 145.0 (145 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [400. 400.]
  - ndcs_emi_exclLU for refyr and taryr: [310. 310.]
  - ndcs_emi_onlyLU for refyr and taryr: [90. 90.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (90.0).
    - bl_onlyLU_refyr = 90.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (90.0).
    - bl_onlyLU_taryr = 90.0
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 185.0
- tar_emi_inclLU = ndc_value_inclLU = 145.0
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 185.0
- tar_emi_inclLU = 145.0

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -40.0 (-40%)
- ndc_value_inclLU: -64.0 (-64%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [400. 400.]
  - ndcs_emi_exclLU for refyr and taryr: [310. 310.]
  - ndcs_emi_onlyLU for refyr and taryr: [90. 90.]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -40.0 / 100. = 0.6
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -64.0 / 100. = 0.36
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (90.0).
    - bl_onlyLU_refyr = 90.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (90.0).
    - bl_onlyLU_taryr = 90.0
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 310.0 * 0.998703865 = 309.59819815
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 310.0 * (1 - 0.998703865) = 0.4018018500000098
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.6 * 309.59819815 + 0.4018018500000098 = 186.16072074
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.36 * (309.59819815 + 90.0) + 0.4018018500000098 = 144.25715318399997
- tar_emi_exclLU = ndc_value_exclLU = 186.16072074
- tar_emi_inclLU = ndc_value_inclLU = 144.25715318399997
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 186.16072074
- tar_emi_inclLU = 144.25715318399997