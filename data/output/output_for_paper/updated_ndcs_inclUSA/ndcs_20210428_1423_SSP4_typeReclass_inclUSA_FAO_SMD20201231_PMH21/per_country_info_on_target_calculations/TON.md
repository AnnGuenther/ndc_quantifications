## ['Tonga']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | nan | nan | nan | nan |
| Used | yes | nan | nan | nan | nan | nan |



## Target type used: RBY, refyr: 2006, taryr: 2030, conditional_best
- ndc_value_exclLU: -13.0 (-13%, from NDC)
- ndc_value_inclLU: nan (nan, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: 0.3104 MtCO2eq, nan MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 0.1228 MtCO2eq, nan MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: 0.1874 MtCO2eq, nan MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -13.0 / 100. = 0.87
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2006: ndcs_emi_onlyLU used (0.1874 MtCO2eq).
    - bl_onlyLU_refyr = 0.1874 MtCO2eq
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.07333285714285716 MtCO2eq).
    - bl_onlyLU_taryr = -0.07333285714285716 MtCO2eq
### tar_type_used = RBY
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.23209000000000002 * 0.5605100275577031 = 0.13008877229586732 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.2372083333333333 * (1 - 0.5312108915098042) = 0.11120068310977853 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.87 * 0.13008877229586732 + 0.11120068310977853 = 0.2243779150071831 MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * nan * (0.13008877229586732 + 0.1874) + 0.11120068310977853 = nan MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 0.2243779150071831 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = nan MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.2243779150071831, -0.07333285714285716]) = 0.15104505786432593 MtCO2eq
- tar_emi_exclLU = 0.2243779150071831 MtCO2eq
- tar_emi_inclLU = 0.15104505786432593 MtCO2eq