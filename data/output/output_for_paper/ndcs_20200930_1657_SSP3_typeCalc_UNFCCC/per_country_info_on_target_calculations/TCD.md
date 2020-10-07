

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -5.2103 (-5.2103 MtCO2eq_AR4)
- ndc_value_inclLU: -5.2103 (-5.2103 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [28.65937 28.65937]
  - ndcs_emi_exclLU for refyr and taryr: [46.04685 46.04685]
  - ndcs_emi_onlyLU for refyr and taryr: [-17.38748 -17.38748]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_refyr = -17.38748
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_taryr = -17.38748
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 46.04685
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 46.04685 + -5.2103 = 40.83655 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 28.659370000000003
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 28.659370000000003 + -5.2103 = 23.449070000000003
- tar_emi_exclLU = ndc_value_exclLU = 40.83655
- tar_emi_inclLU = ndc_value_inclLU = 23.449070000000003
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 40.83655
- tar_emi_inclLU = 23.449070000000003

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -13.4049 (-13.4049 MtCO2eq_AR4)
- ndc_value_inclLU: -20.42992 (-20.42992 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [28.65937 28.65937]
  - ndcs_emi_exclLU for refyr and taryr: [46.04685 46.04685]
  - ndcs_emi_onlyLU for refyr and taryr: [-17.38748 -17.38748]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_refyr = -17.38748
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_taryr = -17.38748
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 46.04685
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 46.04685 + -13.4049 = 32.64195 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 28.659370000000003
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 28.659370000000003 + -20.42992 = 8.229450000000003
- tar_emi_exclLU = ndc_value_exclLU = 32.64195
- tar_emi_inclLU = ndc_value_inclLU = 8.229450000000003
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 32.64195
- tar_emi_inclLU = 8.229450000000003

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 40.83655 (40.83655 MtCO2eq_AR4)
- ndc_value_inclLU: 23.44907 (23.44907 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [28.65937 28.65937]
  - ndcs_emi_exclLU for refyr and taryr: [46.04685 46.04685]
  - ndcs_emi_onlyLU for refyr and taryr: [-17.38748 -17.38748]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_refyr = -17.38748
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_taryr = -17.38748
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 40.83655
- tar_emi_inclLU = ndc_value_inclLU = 23.44907
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 40.83655
- tar_emi_inclLU = 23.44907

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 32.64193 (32.64193 MtCO2eq_AR4)
- ndc_value_inclLU: 8.22945 (8.22945 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [28.65937 28.65937]
  - ndcs_emi_exclLU for refyr and taryr: [46.04685 46.04685]
  - ndcs_emi_onlyLU for refyr and taryr: [-17.38748 -17.38748]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_refyr = -17.38748
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_taryr = -17.38748
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 32.64193
- tar_emi_inclLU = ndc_value_inclLU = 8.22945
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 32.64193
- tar_emi_inclLU = 8.22945

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -11.3 (-11.3%)
- ndc_value_inclLU: -18.2 (-18.2%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [28.65937 28.65937]
  - ndcs_emi_exclLU for refyr and taryr: [46.04685 46.04685]
  - ndcs_emi_onlyLU for refyr and taryr: [-17.38748 -17.38748]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -11.3 / 100. = 0.887
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -18.2 / 100. = 0.8180000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_refyr = -17.38748
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_taryr = -17.38748
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 46.04685 * 0.9974660679999999 = 45.93017041328579
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 46.04685 * (1 - 0.9974660679999999) = 0.11667958671420331
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.887 * 45.93017041328579 + 0.11667958671420331 = 40.85674074329871
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8180000000000001 * 45.93017041328579 + -17.38748 + 0.11667958671420331 = 20.300078984781983
- tar_emi_exclLU = ndc_value_exclLU = 40.85674074329871
- tar_emi_inclLU = ndc_value_inclLU = 20.300078984781983
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 40.85674074329871
- tar_emi_inclLU = 20.300078984781983

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -29.1 (-29.1%)
- ndc_value_inclLU: -71.0 (-71%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [28.65937 28.65937]
  - ndcs_emi_exclLU for refyr and taryr: [46.04685 46.04685]
  - ndcs_emi_onlyLU for refyr and taryr: [-17.38748 -17.38748]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -29.1 / 100. = 0.709
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -71.0 / 100. = 0.29000000000000004
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_refyr = -17.38748
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-17.38748).
    - bl_onlyLU_taryr = -17.38748
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 46.04685 * 0.9974660679999999 = 45.93017041328579
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 46.04685 * (1 - 0.9974660679999999) = 0.11667958671420331
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.709 * 45.93017041328579 + 0.11667958671420331 = 32.68117040973383
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.29000000000000004 * 45.93017041328579 + -17.38748 + 0.11667958671420331 = -3.9510509934329154
- tar_emi_exclLU = ndc_value_exclLU = 32.68117040973383
- tar_emi_inclLU = ndc_value_inclLU = -3.9510509934329154
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 32.68117040973383
- tar_emi_inclLU = -3.9510509934329154