

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -61.97557278329763 (-59.7 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [309.67024056 309.67024056]
  - ndcs_emi_exclLU for refyr and taryr: [144.60966983 144.60966983]
  - ndcs_emi_onlyLU for refyr and taryr: [165.06057073 165.06057073]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_refyr = 165.06057072938563
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_taryr = 165.06057072938563
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 309.6702405570801
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 309.6702405570801 + -61.97557278329763 = 247.69466777378247
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 247.69466777378247
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([247.69466777378247, - 165.06057072938563]) = 82.63409704439684.
- tar_emi_exclLU = 82.63409704439684
- tar_emi_inclLU = 247.69466777378247

## tar_type_used: ABU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -92.91145333509444 (-89.5 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [309.67024056 309.67024056]
  - ndcs_emi_exclLU for refyr and taryr: [144.60966983 144.60966983]
  - ndcs_emi_onlyLU for refyr and taryr: [165.06057073 165.06057073]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_refyr = 165.06057072938563
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_taryr = 165.06057072938563
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_inclLU_taryr = ndcs_emi_inclLU[taryr] = 309.6702405570801
- tar_emi_inclLU = bl_inclLU_taryr + ndc_value_inclLU = 309.6702405570801 + -92.91145333509444 = 216.75878722198564
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 216.75878722198564
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([216.75878722198564, - 165.06057072938563]) = 51.69821649260001.
- tar_emi_exclLU = 51.69821649260001
- tar_emi_inclLU = 216.75878722198564

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 247.69466777378247 (238.6 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [309.67024056 309.67024056]
  - ndcs_emi_exclLU for refyr and taryr: [144.60966983 144.60966983]
  - ndcs_emi_onlyLU for refyr and taryr: [165.06057073 165.06057073]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_refyr = 165.06057072938563
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_taryr = 165.06057072938563
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 247.69466777378247
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([247.69466777378247, - 165.06057072938563]) = 82.63409704439684.
- tar_emi_exclLU = 82.63409704439684
- tar_emi_inclLU = 247.69466777378247

## tar_type_used: ABS, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: 216.75878722198567 (208.8 MtCO2eq_SAR)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [309.67024056 309.67024056]
  - ndcs_emi_exclLU for refyr and taryr: [144.60966983 144.60966983]
  - ndcs_emi_onlyLU for refyr and taryr: [165.06057073 165.06057073]
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_refyr = 165.06057072938563
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_taryr = 165.06057072938563
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 216.75878722198567
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([216.75878722198567, - 165.06057072938563]) = 51.69821649260004.
- tar_emi_exclLU = 51.69821649260004
- tar_emi_inclLU = 216.75878722198567

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -20.0 (-20%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [309.67024056 309.67024056]
  - ndcs_emi_exclLU for refyr and taryr: [144.60966983 144.60966983]
  - ndcs_emi_onlyLU for refyr and taryr: [165.06057073 165.06057073]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -20.0 / 100. = 0.8
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_refyr = 165.06057072938563
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_taryr = 165.06057072938563
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 200.6261 * 0.985452042 = 197.7073999234962
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 200.6261 * (1 - 0.985452042) = 2.9187000765037947
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 197.7073999234962 + 2.9187000765037947 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.8 * (197.7073999234962 + 165.06057072938563) + 2.9187000765037947 = 293.1330765988093
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 293.1330765988093
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([293.1330765988093, - 165.06057072938563]) = 128.07250586942365.
- tar_emi_exclLU = 128.07250586942365
- tar_emi_inclLU = 293.1330765988093

## tar_type_used: RBU, refyr: 2030, taryr: 2030, conditional_best
- ndc_value_exclLU: nan (nan)
- ndc_value_inclLU: -30.0 (-30%)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [309.67024056 309.67024056]
  - ndcs_emi_exclLU for refyr and taryr: [144.60966983 144.60966983]
  - ndcs_emi_onlyLU for refyr and taryr: [165.06057073 165.06057073]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + nan / 100. = nan
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + -30.0 / 100. = 0.7
- LULUCF
  - is_LU_covered_valinfo: True
  - is_LU_covered_secinfo: True
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_refyr = 165.06057072938563
    - emi_onlyLU 2030: ndcs_emi_onlyLU used (165.06057072938563).
    - bl_onlyLU_taryr = 165.06057072938563
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 200.6261 * 0.985452042 = 197.7073999234962
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 200.6261 * (1 - 0.985452042) = 2.9187000765037947
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 197.7073999234962 + 2.9187000765037947 = nan
- tar_emi_inclLU
  - bl_onlyLU_refyr >= 0., so apply the reduction to the emi_bl_onlyLU_refyr part as well.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * (emi_cov_exclLU_refyr + bl_onlyLU_refyr) + emi_notcov_exclLU_taryr = 1.0 * 0.7 * (197.7073999234962 + 165.06057072938563) + 2.9187000765037947 = 256.85627953352105
- tar_emi_exclLU = ndc_value_exclLU = nan
- tar_emi_inclLU = ndc_value_inclLU = 256.85627953352105
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_exclLU is nan. So calculate it.
- lulucf_first_try, so tar_emi_exclLU = np.nansum([tar_emi_inclLU, -bl_onlyLU_taryr]) = np.nansum([256.85627953352105, - 165.06057072938563]) = 91.79570880413542.
- tar_emi_exclLU = 91.79570880413542
- tar_emi_inclLU = 256.85627953352105