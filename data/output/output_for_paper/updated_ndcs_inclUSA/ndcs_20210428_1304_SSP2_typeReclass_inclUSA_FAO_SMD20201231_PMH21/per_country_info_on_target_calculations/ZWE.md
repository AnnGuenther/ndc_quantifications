## ['Zimbabwe']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | nan | nan | nan | nan |
| Used | yes | no | no | no | no | no |



## Target type used: AEI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 2.3 (2.3 tCO2eq/capita (energy CO2), from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (36.385291714285714 MtCO2eq).
    - bl_onlyLU_refyr = 36.385291714285714 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (36.385291714285714 MtCO2eq).
    - bl_onlyLU_taryr = 36.385291714285714 MtCO2eq
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 14682511.4263 Pers
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 2.3 * 1e-6 * 14682511.4263 = 33.76977628048999 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 33.76977628048999 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([33.76977628048999, 36.385291714285714]) = 70.1550679947757 MtCO2eq
- tar_emi_exclLU = 33.76977628048999 MtCO2eq
- tar_emi_inclLU = 70.1550679947757 MtCO2eq



## Target type used: REI, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -33.0 (-33%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -33.0 / 100. = 0.6699999999999999
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (36.385291714285714 MtCO2eq).
    - bl_onlyLU_refyr = 36.385291714285714 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (36.385291714285714 MtCO2eq).
    - bl_onlyLU_taryr = 36.385291714285714 MtCO2eq
### tar_type_used = REI
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 29.3464 * 0.4527119946675885 = 13.285467280312918 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 29.3464 * (1 - 0.4527119946675885) = 16.06093271968708 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.6699999999999999 * 13.285467280312918 + 16.06093271968708 = 24.962195797496733 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (13.285467280312918 + 36.385291714285714) + 16.06093271968708 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 24.962195797496733 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([24.962195797496733, 36.385291714285714]) = 61.34748751178245 MtCO2eq
- tar_emi_exclLU = 24.962195797496733 MtCO2eq
- tar_emi_inclLU = 61.34748751178245 MtCO2eq