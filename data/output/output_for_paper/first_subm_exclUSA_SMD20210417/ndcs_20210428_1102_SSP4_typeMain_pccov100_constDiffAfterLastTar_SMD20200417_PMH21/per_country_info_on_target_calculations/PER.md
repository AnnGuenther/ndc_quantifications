## ['Peru']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | yes | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -61.97557278329763 (-59.7 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 309.6702405570801 MtCO2eq, 309.6702405570801 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 144.60966982769446 MtCO2eq, 144.60966982769446 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 165.06057072938563 MtCO2eq, 165.06057072938563 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_refyr = 165.06057072938563 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_taryr = 165.06057072938563 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 309.6702405570801 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 309.6702405570801 + -61.97557278329763 = 247.69466777378247 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 247.69466777378247 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([247.69466777378247, - 165.06057072938563]) = 82.63409704439684 MtCO2eq.
- tar_emi_exclLU = 82.63409704439684 MtCO2eq
- tar_emi_inclLU = 247.69466777378247 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -92.91145333509444 (-89.5 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 309.6702405570801 MtCO2eq, 309.6702405570801 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 144.60966982769446 MtCO2eq, 144.60966982769446 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 165.06057072938563 MtCO2eq, 165.06057072938563 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_refyr = 165.06057072938563 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_taryr = 165.06057072938563 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 309.6702405570801 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 309.6702405570801 + -92.91145333509444 = 216.75878722198564 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 216.75878722198564 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([216.75878722198564, - 165.06057072938563]) = 51.69821649260001 MtCO2eq.
- tar_emi_exclLU = 51.69821649260001 MtCO2eq
- tar_emi_inclLU = 216.75878722198564 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -20.0 (-20%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 309.6702405570801 MtCO2eq, 309.6702405570801 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 144.60966982769446 MtCO2eq, 144.60966982769446 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 165.06057072938563 MtCO2eq, 165.06057072938563 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -20.0 / 100. = 0.8
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_refyr = 165.06057072938563 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_taryr = 165.06057072938563 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 172.5189 * 1.0 = 172.5189 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 172.5189 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 172.5189 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.8 * (172.5189 + 165.06057072938563) + 0.0 = 270.06357658350856 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 270.06357658350856 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([270.06357658350856, - 165.06057072938563]) = 105.00300585412293 MtCO2eq.
- tar_emi_exclLU = 105.00300585412293 MtCO2eq
- tar_emi_inclLU = 270.06357658350856 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -30.0 (-30%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 309.6702405570801 MtCO2eq, 309.6702405570801 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 144.60966982769446 MtCO2eq, 144.60966982769446 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 165.06057072938563 MtCO2eq, 165.06057072938563 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -30.0 / 100. = 0.7
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_refyr = 165.06057072938563 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_taryr = 165.06057072938563 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 172.5189 * 1.0 = 172.5189 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 172.5189 * (1 - 1.0) = 0.0 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 172.5189 + 0.0 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.7 * (172.5189 + 165.06057072938563) + 0.0 = 236.30562951056996 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 236.30562951056996 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([236.30562951056996, - 165.06057072938563]) = 71.24505878118433 MtCO2eq.
- tar_emi_exclLU = 71.24505878118433 MtCO2eq
- tar_emi_inclLU = 236.30562951056996 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 247.69466777378247 (238.6 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 309.6702405570801 MtCO2eq, 309.6702405570801 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 144.60966982769446 MtCO2eq, 144.60966982769446 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 165.06057072938563 MtCO2eq, 165.06057072938563 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_refyr = 165.06057072938563 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_taryr = 165.06057072938563 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 247.69466777378247 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([247.69466777378247, - 165.06057072938563]) = 82.63409704439684 MtCO2eq.
- tar_emi_exclLU = 82.63409704439684 MtCO2eq
- tar_emi_inclLU = 247.69466777378247 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: 216.75878722198567 (208.8 MtCO2eq_SAR, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 309.6702405570801 MtCO2eq, 309.6702405570801 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 144.60966982769446 MtCO2eq, 144.60966982769446 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 165.06057072938563 MtCO2eq, 165.06057072938563 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_refyr = 165.06057072938563 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563 MtCO2eq).
    - bl_onlyLU_taryr = 165.06057072938563 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = 216.75878722198567 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([216.75878722198567, - 165.06057072938563]) = 51.69821649260004 MtCO2eq.
- tar_emi_exclLU = 51.69821649260004 MtCO2eq
- tar_emi_inclLU = 216.75878722198567 MtCO2eq