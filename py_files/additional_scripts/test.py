folders = ['ndc_quantifications_20200628_2122_SSP2pccov100ForAllCountries_typeCalcForAllCountries',
    'ndc_quantifications_20200706_1226_SSP2_pccov100ForAllCountries_typeCalcForAllCountries_FAO']
data = pd.read_csv(Path(meta.path.output, folders[0], 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
data_fao = pd.read_csv(Path(meta.path.output, folders[1], 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
data_tars = pd.read_csv(Path(meta.path.output, folders[0], 'ndc_targets.csv'))
data_fao_tars = pd.read_csv(Path(meta.path.output, folders[1], 'ndc_targets.csv'))

for iso3 in meta.isos.EARTH:
    if data_fao.loc[(data_fao.iso3 == iso3) & (data_fao.condi == 'conditional') & (data_fao.rge == 'best'), '2030'].values[0] \
        < data.loc[(data.iso3 == iso3) & (data.condi == 'conditional') & (data.rge == 'best'), '2030'].values[0]:
        print("\n", iso3)
        print('    non', f"{data_tars.loc[(data_tars.iso3 == iso3), ['tar_type_used', 'emi_bl_onlyLU_refyr', 'refyr']]}", 
              f"{data_tars.loc[(data_tars.iso3 == iso3), ['tar_type_used', 'emi_bl_onlyLU_taryr', 'taryr']]}")
        print('    fao', f"{data_fao_tars.loc[(data_fao_tars.iso3 == iso3), ['tar_type_used', 'emi_bl_onlyLU_refyr', 'refyr']]}", 
              f"{data_fao_tars.loc[(data_fao_tars.iso3 == iso3), ['tar_type_used', 'emi_bl_onlyLU_taryr', 'taryr']]}")

# %%


# %%