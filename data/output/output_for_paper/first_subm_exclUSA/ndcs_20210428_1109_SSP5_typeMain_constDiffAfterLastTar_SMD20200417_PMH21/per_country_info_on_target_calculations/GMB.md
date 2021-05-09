## ['Gambia']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | yes | yes | yes |
| Used | yes | yes | yes | yes | yes | yes | yes |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | no |
| Used | yes | yes | yes | yes | yes | no |



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -1.443 (-1.443 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 3.25 MtCO2eq, 3.25 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_refyr = -0.3544705714285715 MtCO2eq
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_taryr = -0.3544705714285715 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 3.25 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 3.25 + -1.443 = 1.807 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 1.807 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([1.807, -0.3544705714285715]) = 1.4525294285714283 MtCO2eq
- tar_emi_exclLU = 1.807 MtCO2eq
- tar_emi_inclLU = 1.4525294285714283 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -1.748 (-1.748 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 3.85 MtCO2eq, 3.85 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_refyr = -0.3544705714285715 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_taryr = -0.3544705714285715 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 3.85 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 3.85 + -1.748 = 2.1020000000000003 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 2.1020000000000003 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([2.1020000000000003, -0.3544705714285715]) = 1.7475294285714287 MtCO2eq
- tar_emi_exclLU = 2.1020000000000003 MtCO2eq
- tar_emi_inclLU = 1.7475294285714287 MtCO2eq



## Target type used: RBU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -0.444 (-0.444%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 3.25 MtCO2eq, 3.25 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -0.444 / 100. = 0.99556
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_refyr = -0.3544705714285715 MtCO2eq
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_taryr = -0.3544705714285715 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 3.4625 * 1.0 = 3.4625 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 3.4625 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.99556 * 3.4625 + 0.0 = 3.4471265 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 3.4625 + -0.3544705714285715 + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 3.4471265 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([3.4471265, -0.3544705714285715]) = 3.0926559285714283 MtCO2eq
- tar_emi_exclLU = 3.4471265 MtCO2eq
- tar_emi_inclLU = 3.0926559285714283 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -0.454 (-0.454%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 3.85 MtCO2eq, 3.85 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -0.454 / 100. = 0.99546
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_refyr = -0.3544705714285715 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_taryr = -0.3544705714285715 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 4.4862 * 1.0 = 4.4862 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 4.4862 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.99546 * 4.4862 + 0.0 = 4.4658326520000005 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 4.4862 + -0.3544705714285715 + 0.0 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 4.4658326520000005 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([4.4658326520000005, -0.3544705714285715]) = 4.111362080571429 MtCO2eq
- tar_emi_exclLU = 4.4658326520000005 MtCO2eq
- tar_emi_inclLU = 4.111362080571429 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 1.807 (1.807 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 3.25 MtCO2eq, 3.25 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_refyr = -0.3544705714285715 MtCO2eq
    - emi_onlyLU 2025: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_taryr = -0.3544705714285715 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 1.807 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([1.807, -0.3544705714285715]) = 1.4525294285714283 MtCO2eq
- tar_emi_exclLU = 1.807 MtCO2eq
- tar_emi_inclLU = 1.4525294285714283 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 2.102 (2.102 MtCO2eq_AR4, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 3.85 MtCO2eq, 3.85 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_refyr = -0.3544705714285715 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.3544705714285715 MtCO2eq).
    - bl_onlyLU_taryr = -0.3544705714285715 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 2.102 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([2.102, -0.3544705714285715]) = 1.7475294285714282 MtCO2eq
- tar_emi_exclLU = 2.102 MtCO2eq
- tar_emi_inclLU = 1.7475294285714282 MtCO2eq