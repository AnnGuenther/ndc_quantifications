## ['Mongolia']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | nan | nan |
| Used | yes | yes | yes | yes | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -17.772680446598812 (-16.9 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 75.4024371610139 MtCO2eq, 75.4024371610139 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 78.13669569125987 MtCO2eq, 78.13669569125987 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -2.7342585302459703 MtCO2eq, -2.7342585302459703 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_refyr = -2.7342585302459703 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_taryr = -2.7342585302459703 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 78.13669569125987 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 78.13669569125987 + -17.772680446598812 = 60.36401524466106 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 60.36401524466106 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([60.36401524466106, -2.7342585302459703]) = 57.629756714415095 MtCO2eq
- tar_emi_exclLU = 60.36401524466106 MtCO2eq
- tar_emi_inclLU = 57.629756714415095 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -21.243085504218698 (-20.2 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: -41.75002448106349 (-39.7 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 75.4024371610139 MtCO2eq, 75.4024371610139 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 78.13669569125987 MtCO2eq, 78.13669569125987 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -2.7342585302459703 MtCO2eq, -2.7342585302459703 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_refyr = -2.7342585302459703 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_taryr = -2.7342585302459703 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 78.13669569125987 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 78.13669569125987 + -21.243085504218698 = 56.893610187041176 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 75.4024371610139 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 75.4024371610139 + -41.75002448106349 = 33.652412679950416 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 56.893610187041176 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 33.652412679950416 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 56.893610187041176 MtCO2eq
- tar_emi_inclLU = 33.652412679950416 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 60.364015244661054 (57.4 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 75.4024371610139 MtCO2eq, 75.4024371610139 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 78.13669569125987 MtCO2eq, 78.13669569125987 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -2.7342585302459703 MtCO2eq, -2.7342585302459703 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_refyr = -2.7342585302459703 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_taryr = -2.7342585302459703 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 60.364015244661054 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([60.364015244661054, -2.7342585302459703]) = 57.62975671441508 MtCO2eq
- tar_emi_exclLU = 60.364015244661054 MtCO2eq
- tar_emi_inclLU = 57.62975671441508 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 56.893610187041176 (54.1 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: 33.652412679950416 (32.0 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 75.4024371610139 MtCO2eq, 75.4024371610139 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 78.13669569125987 MtCO2eq, 78.13669569125987 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -2.7342585302459703 MtCO2eq, -2.7342585302459703 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_refyr = -2.7342585302459703 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_taryr = -2.7342585302459703 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 56.893610187041176 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 33.652412679950416 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 56.893610187041176 MtCO2eq
- tar_emi_inclLU = 33.652412679950416 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -22.7 (-22.7%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 75.4024371610139 MtCO2eq, 75.4024371610139 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 78.13669569125987 MtCO2eq, 78.13669569125987 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -2.7342585302459703 MtCO2eq, -2.7342585302459703 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -22.7 / 100. = 0.773
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_refyr = -2.7342585302459703 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_taryr = -2.7342585302459703 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 80.0186 * 0.9999997500581114 = 80.01858 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 80.0186 * (1 - 0.9999997500581114) = 2.0000000009557908e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.773 * 80.01858 + 2.0000000009557908e-05 = 61.85438234000001 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 80.01858 + -2.7342585302459703 + 2.0000000009557908e-05 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 61.85438234000001 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([61.85438234000001, -2.7342585302459703]) = 59.120123809754034 MtCO2eq
- tar_emi_exclLU = 61.85438234000001 MtCO2eq
- tar_emi_inclLU = 59.120123809754034 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -27.2 (-27.2%, from NDC)
- ndc_value_inclLU: -44.9 (-44.9%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 75.4024371610139 MtCO2eq, 75.4024371610139 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 78.13669569125987 MtCO2eq, 78.13669569125987 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -2.7342585302459703 MtCO2eq, -2.7342585302459703 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -27.2 / 100. = 0.728
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -44.9 / 100. = 0.5509999999999999
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_refyr = -2.7342585302459703 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-2.7342585302459703 MtCO2eq).
    - bl_onlyLU_taryr = -2.7342585302459703 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 80.0186 * 0.9999997500581114 = 80.01858 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 80.0186 * (1 - 0.9999997500581114) = 2.0000000009557908e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.728 * 80.01858 + 2.0000000009557908e-05 = 58.253546240000006 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.5509999999999999 * 80.01858 + -2.7342585302459703 + 2.0000000009557908e-05 = 41.35599904975403 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 58.253546240000006 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 41.35599904975403 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 58.253546240000006 MtCO2eq
- tar_emi_inclLU = 41.35599904975403 MtCO2eq