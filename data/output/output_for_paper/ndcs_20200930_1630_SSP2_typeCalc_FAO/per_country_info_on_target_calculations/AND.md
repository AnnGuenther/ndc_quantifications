

## tar_type_used: ABU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -0.19482011123162934 (-0.19373 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [0.53353538 0.53353538]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.020952571428571428).
    - bl_onlyLU_refyr = -0.020952571428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.020952571428571428).
    - bl_onlyLU_taryr = -0.020952571428571428
### tar_type_used = ABU
tar_emi is the given baseline minus the absolute reduction.
- bl_exclLU_taryr = ndcs_emi_exclLU[taryr] = 0.5335353843696946
- tar_emi_exclLU = bl_exclLU_taryr + ndc_value_exclLU = 0.5335353843696946 + -0.19482011123162934 = 0.33871527313806526 # ndc_value is negative for a reduction ...
- tar_emi_exclLU = ndc_value_exclLU = 0.33871527313806526
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.33871527313806526, -0.020952571428571428]) = 0.31776270170949383
- tar_emi_exclLU = 0.33871527313806526
- tar_emi_inclLU = 0.31776270170949383

## tar_type_used: ABS, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: 0.3387152731380653 (0.336820 MtCO2eq_SAR)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [0.53353538 0.53353538]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.020952571428571428).
    - bl_onlyLU_refyr = -0.020952571428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.020952571428571428).
    - bl_onlyLU_taryr = -0.020952571428571428
### tar_type_used = ABS
tar_emi is the given absolute emissions value.
- tar_emi_exclLU = ndc_value_exclLU = 0.3387152731380653
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.3387152731380653, -0.020952571428571428]) = 0.3177627017094939
- tar_emi_exclLU = 0.3387152731380653
- tar_emi_inclLU = 0.3177627017094939

## tar_type_used: RBU, refyr: 2030, taryr: 2030, unconditional_best
- ndc_value_exclLU: -37.0 (-37%)
- ndc_value_inclLU: nan (nan)
- lulucf_first_try: True
- Emissions values from NDCs:
  - ndcs_emi_inclLU for refyr and taryr: [nan nan]
  - ndcs_emi_exclLU for refyr and taryr: [0.53353538 0.53353538]
  - ndcs_emi_onlyLU for refyr and taryr: [nan nan]
- ndc_level_exclLU = 1. + ndc_value_exclLU / 100. = 1. + -37.0 / 100. = 0.63
- ndc_level_inclLU = 1. + ndc_value_inclLU / 100. = 1. + nan / 100. = nan
- LULUCF
  - is_LU_covered_valinfo: False
  - is_LU_covered_secinfo: False
  - Get the LULUCF data for the reference and target year (bl_onlyLU_refyr/taryr).
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.020952571428571428).
    - bl_onlyLU_refyr = -0.020952571428571428
    - emi_onlyLU 2030: external_emi_onlyLU used (-0.020952571428571428).
    - bl_onlyLU_taryr = -0.020952571428571428
### tar_type_used = RBU
- emi_cov_exclLU_refyr = ict['emi_bl_exclLU_refyr'] * ict['pc_cov_exclLU_refyr'] = 0.5335353843696946 * 0.96133757 = 0.5129076099189782
- emi_notcov_exclLU_taryr = ict['emi_bl_exclLU_taryr'] * (1 - ict['pc_cov_exclLU_taryr']) = 0.5335353843696946 * (1 - 0.96133757) = 0.020627774450716424
- intensity_growth = 1.
- tar_emi_exclLU = intensity_growth * ndc_level_exclLU * emi_cov_exclLU_refyr + emi_notcov_exclLU_taryr = 1.0 * 0.63 * 0.5129076099189782 + 0.020627774450716424 = 0.3437595686996727
- tar_emi_inclLU
  - bl_onlyLU_refyr < 0., so add emi_bl_onlyLU_refyr as is.
  - tar_emi_inclLU = intensity_growth * ndc_level_inclLU * emi_cov_exclLU_refyr + bl_onlyLU_refyr + emi_notcov_exclLU_taryr = 1.0 * nan * 0.5129076099189782 + -0.020952571428571428 + 0.020627774450716424 = nan
- tar_emi_exclLU = ndc_value_exclLU = 0.3437595686996727
- tar_emi_inclLU = ndc_value_inclLU = nan
### Function calc_targets_inclLU_exclLU()
If not both, inclLU and exclLU information are given calculate the 'other case' from the given case.
- tar_emi_inclLU is nan. So calculate tar_emi_inclLU = np.nansum([tar_emi_exclLU, bl_onlyLU_taryr]) = np.nansum([0.3437595686996727, -0.020952571428571428]) = 0.3228069972711013
- tar_emi_exclLU = 0.3437595686996727
- tar_emi_inclLU = 0.3228069972711013