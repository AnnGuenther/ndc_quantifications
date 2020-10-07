

## tar_type_used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -1.4776926549090623 (-1.372950 MtCO2eq_SAR)
- ndc_value_inclLU: -1.4776818920068817 (-1.372940 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [57.23780262 57.23780262]
  - ndcs_emi_exclLU for refyr and taryr: [44.85218844 44.85218844]
  - ndcs_emi_onlyLU for refyr and taryr: [12.38562494 12.38562494]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675).
    - bl_onlyLU_refyr = 12.38562494256675
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675).
    - bl_onlyLU_taryr = 12.38562494256675
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 44.85218844341937
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 44.85218844341937 + -1.4776926549090623 = 43.37449578851031 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 57.23780262308392
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 57.23780262308392 + -1.4776818920068817 = 55.76012073107704
- tar_emi_exclLU = ndc_value_exclLU = 43.37449578851031
- tar_emi_inclLU = ndc_value_inclLU = 55.76012073107704
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 43.37449578851031
- tar_emi_inclLU = 55.76012073107704

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -6.71555586730128 (-6.239540 MtCO2eq_SAR)
- ndc_value_inclLU: -6.71555586730128 (-6.239540 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [65.69056624 65.69056624]
  - ndcs_emi_exclLU for refyr and taryr: [52.67314818 52.67314818]
  - ndcs_emi_onlyLU for refyr and taryr: [13.01741806 13.01741806]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234).
    - bl_onlyLU_refyr = 13.017418063480234
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234).
    - bl_onlyLU_taryr = 13.017418063480234
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 52.67314817919682
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 52.67314817919682 + -6.71555586730128 = 45.95759231189554 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 65.69056624267705
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 65.69056624267705 + -6.71555586730128 = 58.975010375375774
- tar_emi_exclLU = ndc_value_exclLU = 45.95759231189554
- tar_emi_inclLU = ndc_value_inclLU = 58.975010375375774
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 45.95759231189554
- tar_emi_inclLU = 58.975010375375774

## tar_type_used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 43.3744957885103 (40.3 MtCO2eq_SAR)
- ndc_value_inclLU: 55.76012073107705 (51.807700 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [57.23780262 57.23780262]
  - ndcs_emi_exclLU for refyr and taryr: [44.85218844 44.85218844]
  - ndcs_emi_onlyLU for refyr and taryr: [12.38562494 12.38562494]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675).
    - bl_onlyLU_refyr = 12.38562494256675
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675).
    - bl_onlyLU_taryr = 12.38562494256675
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 43.3744957885103
- tar_emi_inclLU = ndc_value_inclLU = 55.76012073107705
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 43.3744957885103
- tar_emi_inclLU = 55.76012073107705

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 45.95759231189553 (42.7 MtCO2eq_SAR)
- ndc_value_inclLU: 58.97501037537577 (54.794710 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [65.69056624 65.69056624]
  - ndcs_emi_exclLU for refyr and taryr: [52.67314818 52.67314818]
  - ndcs_emi_onlyLU for refyr and taryr: [13.01741806 13.01741806]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234).
    - bl_onlyLU_refyr = 13.017418063480234
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234).
    - bl_onlyLU_taryr = 13.017418063480234
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 45.95759231189553
- tar_emi_inclLU = ndc_value_inclLU = 58.97501037537577
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 45.95759231189553
- tar_emi_inclLU = 58.97501037537577

## tar_type_used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -3.3 (-3.3%)
- ndc_value_inclLU: -2.6 (-2.6%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [57.23780262 57.23780262]
  - ndcs_emi_exclLU for refyr and taryr: [44.85218844 44.85218844]
  - ndcs_emi_onlyLU for refyr and taryr: [12.38562494 12.38562494]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -3.3 / 100. = 0.967
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -2.6 / 100. = 0.974
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675).
    - bl_onlyLU_refyr = 12.38562494256675
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (12.38562494256675).
    - bl_onlyLU_taryr = 12.38562494256675
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 40.1317 * 1.0 = 40.1317
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 40.1317 * (1 - 1.0) = 0.0
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.967 * 40.1317 + 0.0 = 38.8073539
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.974 * (40.1317 + 12.38562494256675) + 0.0 = 51.15187449406002
- tar_emi_exclLU = ndc_value_exclLU = 38.8073539
- tar_emi_inclLU = ndc_value_inclLU = 51.15187449406002
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 38.8073539
- tar_emi_inclLU = 51.15187449406002

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -13.6 (-13.6%)
- ndc_value_inclLU: -10.2 (-10.2%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [65.69056624 65.69056624]
  - ndcs_emi_exclLU for refyr and taryr: [52.67314818 52.67314818]
  - ndcs_emi_onlyLU for refyr and taryr: [13.01741806 13.01741806]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -13.6 / 100. = 0.864
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -10.2 / 100. = 0.898
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234).
    - bl_onlyLU_refyr = 13.017418063480234
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (13.017418063480234).
    - bl_onlyLU_taryr = 13.017418063480234
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 44.6621 * 0.9999977609999999 = 44.6620000015581
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 44.6621 * (1 - 0.9999977609999999) = 9.999844190314824e-05
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.864 * 44.6620000015581 + 9.999844190314824e-05 = 38.5880679997881
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.898 * (44.6620000015581 + 13.017418063480234) + 9.999844190314824e-05 = 51.79621742084633
- tar_emi_exclLU = ndc_value_exclLU = 38.5880679997881
- tar_emi_inclLU = ndc_value_inclLU = 51.79621742084633
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 38.5880679997881
- tar_emi_inclLU = 51.79621742084633