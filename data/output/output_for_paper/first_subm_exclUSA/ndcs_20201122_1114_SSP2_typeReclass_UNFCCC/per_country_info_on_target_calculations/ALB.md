## ['Albania']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | no | no | no | no | no | no |
| Used | yes | no | no | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | no | no | nan | no |
| Used | yes | yes | no | no | no | no |



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 5.659169203743952 (5.449 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 6.394476929244176 MtCO2eq, 6.394476929244176 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.911 MtCO2eq).
    - bl_onlyLU_refyr = 0.911 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (0.911 MtCO2eq).
    - bl_onlyLU_taryr = 0.911 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 5.659169203743952 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([5.659169203743952, 0.911]) = 6.570169203743951 MtCO2eq
- tar_emi_exclLU = 5.659169203743952 MtCO2eq
- tar_emi_inclLU = 6.570169203743951 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -0.7353077255002235 (-0.708 MtCO2eq_SAR, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 6.394476929244176 MtCO2eq, 6.394476929244176 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.911 MtCO2eq).
    - bl_onlyLU_refyr = 0.911 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (0.911 MtCO2eq).
    - bl_onlyLU_taryr = 0.911 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 6.394476929244176 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 6.394476929244176 + -0.7353077255002235 = 5.659169203743953 MtCO2eq # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 5.659169203743953 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([5.659169203743953, 0.911]) = 6.570169203743953 MtCO2eq
- tar_emi_exclLU = 5.659169203743953 MtCO2eq
- tar_emi_inclLU = 6.570169203743953 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -11.5 (-11.5%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 6.394476929244176 MtCO2eq, 6.394476929244176 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: nan MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -11.5 / 100. = 0.885
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (0.911 MtCO2eq).
    - bl_onlyLU_refyr = 0.911 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (0.911 MtCO2eq).
    - bl_onlyLU_taryr = 0.911 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 6.394476929244176 * 0.6281832063568606 = 4.016903020387579 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 6.394476929244176 * (1 - 0.6281832063568606) = 2.377573908856597 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.885 * 4.016903020387579 + 2.377573908856597 = 5.932533081899605 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (4.016903020387579 + 0.911) + 2.377573908856597 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 5.932533081899605 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([5.932533081899605, 0.911]) = 6.843533081899604 MtCO2eq
- tar_emi_exclLU = 5.932533081899605 MtCO2eq
- tar_emi_inclLU = 6.843533081899604 MtCO2eq



## Target type used: AEI, refyr: 2050, taryr: 2050, unconditional_best
- ndc_value_exclLU: 2.0 (2 tCO2eq/cap, from NDC)
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
    - emi_onlyLU 2050: external_emi_onlyLU used (0.911 MtCO2eq).
    - bl_onlyLU_refyr = 0.911 MtCO2eq
    - emi_onlyLU 2050: external_emi_onlyLU used (0.911 MtCO2eq).
    - bl_onlyLU_taryr = 0.911 MtCO2eq
### tar_type_used = AEI
tar_emi is the given absolute emissions intensity multiplied by the target year GDP or POP.
- 'CAP' in ndc_value_excl/inclLU: ref_act = ict['pop_taryr'] = 2815458.1959 Pers
- tar_emi_exclLU = ndc_value_exclLU * 1e-6 * ref_act = 2.0 * 1e-6 * 2815458.1959 = 5.6309163918000005 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 5.6309163918000005 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([5.6309163918000005, 0.911]) = 6.541916391800001 MtCO2eq
- tar_emi_exclLU = 5.6309163918000005 MtCO2eq
- tar_emi_inclLU = 6.541916391800001 MtCO2eq