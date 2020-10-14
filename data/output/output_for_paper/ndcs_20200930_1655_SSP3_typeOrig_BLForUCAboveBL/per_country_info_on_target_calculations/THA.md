

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -111.0 (-111 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [555. 555.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_refyr = 15.342237142857142
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_taryr = 15.342237142857142
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 555.0
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 555.0 + -111.0 = 444.0 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 444.0
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([444.0, 15.342237142857142]) = 459.34223714285713
- tar_emi_exclLU = 444.0
- tar_emi_inclLU = 459.34223714285713

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -139.0 (-139 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [555. 555.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_refyr = 15.342237142857142
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_taryr = 15.342237142857142
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 555.0
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 555.0 + -139.0 = 416.0 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 416.0
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([416.0, 15.342237142857142]) = 431.34223714285713
- tar_emi_exclLU = 416.0
- tar_emi_inclLU = 431.34223714285713

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 444.0 (444 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [555. 555.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_refyr = 15.342237142857142
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_taryr = 15.342237142857142
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 444.0
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([444.0, 15.342237142857142]) = 459.34223714285713
- tar_emi_exclLU = 444.0
- tar_emi_inclLU = 459.34223714285713

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 416.0 (416 MtCO2eq_AR4)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [555. 555.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_refyr = 15.342237142857142
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_taryr = 15.342237142857142
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 416.0
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([416.0, 15.342237142857142]) = 431.34223714285713
- tar_emi_exclLU = 416.0
- tar_emi_inclLU = 431.34223714285713

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -20.0 (-20%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [555. 555.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -20.0 / 100. = 0.8
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_refyr = 15.342237142857142
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_taryr = 15.342237142857142
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 574.6514 * 1.0 = 574.6514
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 574.6514 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8 * 574.6514 + 0.0 = 459.72112
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (574.6514 + 15.342237142857142) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 459.72112
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([459.72112, 15.342237142857142]) = 475.0633571428571
- tar_emi_exclLU = 459.72112
- tar_emi_inclLU = 475.0633571428571

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -25.0 (-25%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [555. 555.]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -25.0 / 100. = 0.75
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_refyr = 15.342237142857142
    - emi_onlyLU 2030: external_emi_onlyLU used (15.342237142857142).
    - bl_onlyLU_taryr = 15.342237142857142
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 574.6514 * 1.0 = 574.6514
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 574.6514 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.75 * 574.6514 + 0.0 = 430.98855
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (574.6514 + 15.342237142857142) + 0.0 = nan
- tar_emi_exclLU = ndc_value_exclLU = 430.98855
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([430.98855, 15.342237142857142]) = 446.3307871428571
- tar_emi_exclLU = 430.98855
- tar_emi_inclLU = 446.3307871428571