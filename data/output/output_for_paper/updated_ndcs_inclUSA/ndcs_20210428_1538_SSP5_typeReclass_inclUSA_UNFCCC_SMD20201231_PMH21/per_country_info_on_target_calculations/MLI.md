## ['Mali']



| Covered gases | CO2 | CH4 | N2O | HFCS | PFCS | SF6 | NF3 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | yes | yes | nan | nan | nan | nan |
| Used | yes | yes | yes | no | no | no | no |

| Covered sectors | ENERGY | IPPU | AGRICULTURE | WASTE | OTHER | LULUCF |
| ---- | ---- | ---- | ---- | ---- | ---- | ----  |
| NDC | yes | nan | yes | nan | nan | yes |
| Used | yes | yes | yes | yes | yes | yes |



## Target type used: ABU, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -10.399183 (-10.399183 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -69.327889 MtCO2eq, -69.327889 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 85.096 MtCO2eq, 85.096 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -154.424 MtCO2eq, -154.424 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-154.424 MtCO2eq).
    - bl_onlyLU_refyr = -154.424 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-154.424 MtCO2eq).
    - bl_onlyLU_taryr = -154.424 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -69.327889 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -69.327889 + -10.399183 = -79.72707199999999 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -79.72707199999999 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-79.72707199999999, - -154.424]) = 74.69692800000001 MtCO2eq.
- tar_emi_exclLU = 74.69692800000001 MtCO2eq
- tar_emi_inclLU = -79.72707199999999 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -4.386362 (-4.386362 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -29.242409999999996 MtCO2eq, -29.242409999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 97.346 MtCO2eq, 97.346 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -126.588 MtCO2eq, -126.588 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_refyr = -126.588 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_taryr = -126.588 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -29.242409999999996 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -29.242409999999996 + -4.386362 = -33.628772 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -33.628772 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-33.628772, - -126.588]) = 92.959228 MtCO2eq.
- tar_emi_exclLU = 92.959228 MtCO2eq
- tar_emi_inclLU = -33.628772 MtCO2eq



## Target type used: ABU, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: -10.318 (-10.318 MtCO2eq, from NDC)
- ndc_value_inclLU: -26.166416 (-26.166416 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -69.327889 MtCO2eq, -69.327889 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 85.096 MtCO2eq, 85.096 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -154.424 MtCO2eq, -154.424 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-154.424 MtCO2eq).
    - bl_onlyLU_refyr = -154.424 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-154.424 MtCO2eq).
    - bl_onlyLU_taryr = -154.424 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 85.096 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 85.096 + -10.318 = 74.778 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -69.327889 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -69.327889 + -26.166416 = -95.494305 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 74.778 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -95.494305 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 74.778 MtCO2eq
- tar_emi_inclLU = -95.494305 MtCO2eq



## Target type used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: -27.248 (-27.248 MtCO2eq, from NDC)
- ndc_value_inclLU: -55.694677 (-55.694677 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -29.242409999999996 MtCO2eq, -29.242409999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 97.346 MtCO2eq, 97.346 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -126.588 MtCO2eq, -126.588 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_refyr = -126.588 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_taryr = -126.588 MtCO2eq
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 97.346 MtCO2eq
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 97.346 + -27.248 = 70.098 MtCO2eq # ndc_value is negative for a reduction ...
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = -29.242409999999996 MtCO2eq
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = -29.242409999999996 + -55.694677 = -84.93708699999999 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = 70.098 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -84.93708699999999 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 70.098 MtCO2eq
- tar_emi_inclLU = -84.93708699999999 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -79.727072 (-79.727072 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -69.327889 MtCO2eq, -69.327889 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 85.096 MtCO2eq, 85.096 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -154.424 MtCO2eq, -154.424 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-154.424 MtCO2eq).
    - bl_onlyLU_refyr = -154.424 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-154.424 MtCO2eq).
    - bl_onlyLU_taryr = -154.424 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -79.727072 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-79.727072, - -154.424]) = 74.696928 MtCO2eq.
- tar_emi_exclLU = 74.696928 MtCO2eq
- tar_emi_inclLU = -79.727072 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -33.628772 (-33.628772 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -29.242409999999996 MtCO2eq, -29.242409999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 97.346 MtCO2eq, 97.346 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -126.588 MtCO2eq, -126.588 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_refyr = -126.588 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_taryr = -126.588 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -33.628772 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-33.628772, - -126.588]) = 92.959228 MtCO2eq.
- tar_emi_exclLU = 92.959228 MtCO2eq
- tar_emi_inclLU = -33.628772 MtCO2eq



## Target type used: ABS, refyr: 2025, taryr: 2025, conditional_best
- ndc_value_exclLU: 72.332 (72.332 MtCO2eq, from NDC)
- ndc_value_inclLU: -95.494305 (-95.494305 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -69.327889 MtCO2eq, -69.327889 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 85.096 MtCO2eq, 85.096 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -154.424 MtCO2eq, -154.424 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-154.424 MtCO2eq).
    - bl_onlyLU_refyr = -154.424 MtCO2eq
    - emi_onlyLU 2025: ndcs_emi_onlyLU used (-154.424 MtCO2eq).
    - bl_onlyLU_taryr = -154.424 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 72.332 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -95.494305 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 72.332 MtCO2eq
- tar_emi_inclLU = -95.494305 MtCO2eq



## Target type used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: 68.142 (68.142 MtCO2eq, from NDC)
- ndc_value_inclLU: -84.937087 (-84.937087 MtCO2eq, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -29.242409999999996 MtCO2eq, -29.242409999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 97.346 MtCO2eq, 97.346 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -126.588 MtCO2eq, -126.588 MtCO2eq
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_refyr = -126.588 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_taryr = -126.588 MtCO2eq
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 68.142 MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -84.937087 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU = 68.142 MtCO2eq
- tar_emi_inclLU = -84.937087 MtCO2eq



## Target type used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan, from NDC)
- ndc_value_inclLU: -27.0 (-27%, from NDC)
- lulucf_first_try: True
(first try: subtracting the bl_onlyLU_taryr from tar_emi_inclLU to get tar_emi_exclLU;
second try if some tar_exclLU values for iso_act are < 0: splitting the absolute reduction into onlyLU and exclLU parts, based on contributions of onlyLU and exclLU in the target year)
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: -29.242409999999996 MtCO2eq, -29.242409999999996 MtCO2eq
  - ndcs_emi_exclLU for refyr and taryr: 97.346 MtCO2eq, 97.346 MtCO2eq
  - ndcs_emi_onlyLU for refyr and taryr: -126.588 MtCO2eq, -126.588 MtCO2eq
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -27.0 / 100. = 0.73
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_refyr = -126.588 MtCO2eq
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (-126.588 MtCO2eq).
    - bl_onlyLU_taryr = -126.588 MtCO2eq
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 97.346 * 0.9999991434102552 = 97.3459166144147 MtCO2eq
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 97.346 * (1 - 0.9999991434102552) = 8.338558529750251e-05 MtCO2eq
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 97.3459166144147 + 8.338558529750251e-05 = nan MtCO2eq
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.73 * 97.3459166144147 + -126.588 + 8.338558529750251e-05 = -55.52539748589196 MtCO2eq
- tar_emi_exclLU = ndc_value_exclLU = nan MtCO2eq
- tar_emi_inclLU = ndc_value_inclLU = -55.52539748589196 MtCO2eq
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([-55.52539748589196, - -126.588]) = 71.06260251410804 MtCO2eq.
- tar_emi_exclLU = 71.06260251410804 MtCO2eq
- tar_emi_inclLU = -55.52539748589196 MtCO2eq