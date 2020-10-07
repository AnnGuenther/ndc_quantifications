

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -337.0 (-337 MtCO2eq_AR4)
- ndc_value_inclLU: -834.0 (-834 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 2154.26
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 2154.26 + -337.0 = 1817.2600000000002 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 2869.0
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 2869.0 + -834.0 = 2035.0
- tar_emi_exclLU = ndc_value_exclLU = 1817.2600000000002
- tar_emi_inclLU = ndc_value_inclLU = 2035.0
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 1817.2600000000002
- tar_emi_inclLU = 2035.0

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -479.145 (-479.145 MtCO2eq_AR4)
- ndc_value_inclLU: -1176.29 (-1176.290 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 2154.26
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 2154.26 + -479.145 = 1675.1150000000002 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 2869.0
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 2869.0 + -1176.29 = 1692.71
- tar_emi_exclLU = ndc_value_exclLU = 1675.1150000000002
- tar_emi_inclLU = ndc_value_inclLU = 1692.71
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 1675.1150000000002
- tar_emi_inclLU = 1692.71

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_worst
- ndc_value_exclLU: -431.0 (-431 MtCO2eq_AR4)
- ndc_value_inclLU: -1081.0 (-1081 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 2154.26
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 2154.26 + -431.0 = 1723.2600000000002 # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 2869.0
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 2869.0 + -1081.0 = 1788.0
- tar_emi_exclLU = ndc_value_exclLU = 1723.2600000000002
- tar_emi_inclLU = ndc_value_inclLU = 1788.0
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 1723.2600000000002
- tar_emi_inclLU = 1788.0

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 1817.0 (1817 MtCO2eq_AR4)
- ndc_value_inclLU: 2034.0 (2034 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 1817.0
- tar_emi_inclLU = ndc_value_inclLU = 2034.0
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 1817.0
- tar_emi_inclLU = 2034.0

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 1675.855 (1675.855 MtCO2eq_AR4)
- ndc_value_inclLU: 1692.71 (1692.710 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 1675.855
- tar_emi_inclLU = ndc_value_inclLU = 1692.71
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 1675.855
- tar_emi_inclLU = 1692.71

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_worst
- ndc_value_exclLU: 1723.0 (1723 MtCO2eq_AR4)
- ndc_value_inclLU: 1788.0 (1788 MtCO2eq_AR4)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 1723.0
- tar_emi_inclLU = ndc_value_inclLU = 1788.0
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 1723.0
- tar_emi_inclLU = 1788.0

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -15.6 (-15.6%)
- ndc_value_inclLU: -29.0 (-29%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -15.6 / 100. = 0.844
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -29.0 / 100. = 0.71
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1172.2964 * 0.9843812540000001 = 1153.9866002916856
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1172.2964 * (1 - 0.9843812540000001) = 18.309799708314287
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.844 * 1153.9866002916856 + 18.309799708314287 = 992.2744903544968
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.71 * (1153.9866002916856 + 714.0) + 18.309799708314287 = 1344.580285915411
- tar_emi_exclLU = ndc_value_exclLU = 992.2744903544968
- tar_emi_inclLU = ndc_value_inclLU = 1344.580285915411
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 992.2744903544968
- tar_emi_inclLU = 1344.580285915411

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -20.0 (-20.0%)
- ndc_value_inclLU: -41.0 (-41%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -20.0 / 100. = 0.8
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -41.0 / 100. = 0.5900000000000001
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1172.2964 * 0.9843812540000001 = 1153.9866002916856
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1172.2964 * (1 - 0.9843812540000001) = 18.309799708314287
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.8 * 1153.9866002916856 + 18.309799708314287 = 941.4990799416628
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.5900000000000001 * (1153.9866002916856 + 714.0) + 18.309799708314287 = 1120.421893880409
- tar_emi_exclLU = ndc_value_exclLU = 941.4990799416628
- tar_emi_inclLU = ndc_value_inclLU = 1120.421893880409
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 941.4990799416628
- tar_emi_inclLU = 1120.421893880409

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_worst
- ndc_value_exclLU: -19.0 (-19.0%)
- ndc_value_inclLU: -38.24 (-38.24%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [2869. 2869.]
  - ndcs_emi_exclLU for refyr and taryr: [2154.26 2154.26]
  - ndcs_emi_onlyLU for refyr and taryr: [714. 714.]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -19.0 / 100. = 0.81
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -38.24 / 100. = 0.6175999999999999
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_refyr = 714.0
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (714.0).
    - bl_onlyLU_taryr = 714.0
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 1172.2964 * 0.9843812540000001 = 1153.9866002916856
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 1172.2964 * (1 - 0.9843812540000001) = 18.309799708314287
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.81 * 1153.9866002916856 + 18.309799708314287 = 953.0389459445796
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.6175999999999999 * (1153.9866002916856 + 714.0) + 18.309799708314287 = 1171.9783240484592
- tar_emi_exclLU = ndc_value_exclLU = 953.0389459445796
- tar_emi_inclLU = ndc_value_inclLU = 1171.9783240484592
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 953.0389459445796
- tar_emi_inclLU = 1171.9783240484592