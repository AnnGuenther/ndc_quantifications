# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
def get_table(path_to_file):
    
    gwp = 'AR4'
    unit = 'MtCO2eq'
    
    # Get table and convert the units.
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        path_to_file)
    
    table.ent = (table.ent if hasattr(table, 'ent') else table.entity.replace('AR4', ''))
    table.cat = (table.cat if hasattr(table, 'cat') else table.category)
    table.__convert_unit__(unit, entity=table.ent, gwp=gwp)
    
    return table

# %%
import pandas as pd
from pathlib import Path
from setup_metadata import setup_metadata
import helpers_functions as hpf

# %%
meta = setup_metadata()

# %%
# Covered part of emissions: globally.
# Pay attention to the countries that do not have (I)NDCs.
ndcs = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0).reindex(index=meta.isos.EARTH)
countries_without_indc = [xx for xx in meta.isos.EARTH if (type(ndcs.loc[xx, 'NDC_INDC']) != str or ndcs.loc[xx, 'NDC_INDC'] not in ['NDC', 'INDC'])]
countries_with_indc = [xx for xx in meta.isos.EARTH if (type(ndcs.loc[xx, 'NDC_INDC']) == str and ndcs.loc[xx, 'NDC_INDC'] in ['NDC', 'INDC'])]

years_cov = [1990, 2000, 2010, 2017, 2020, 2030]

# Gg (therefore including 1e-3).
emi_cov = 1e-3 * hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.pc_cov,
    'KYOTOGHG_IPCM0EL_COV_EMI_SSP2BLMESGBFILLED_CORR.csv')).__reindex__(isos=meta.isos.EARTH, years=years_cov). \
    data.loc[countries_with_indc, :].sum()
emi_tot = kyotoghg_ipcm0el = 1e-3 * get_table(Path(meta.path.preprocess, 'tables', 
    'KYOTOGHG_IPCM0EL_TOTAL_NET_SSP2BLMESGB_PMSSPBIE.csv')).__reindex__(isos=meta.isos.EARTH, years=years_cov). \
    data.sum()
pc_cov = 100. * emi_cov.div(emi_tot)

# Create latex table with emi_tot, emi_cov and pc_cov.
txt = 'Year & ' + ' & '.join([str(xx) for xx in years_cov]) + " \\\\"
txt += '\nTotal emissions (Gg CO$_2$eq AR4) & ' + ' & '.join(['{:.1f}'.format(xx) for xx in emi_tot]) + " \\\\"
txt += '\nCovered emissions (Gg CO$_2$eq AR4) & ' + ' & '.join(['{:.1f}'.format(xx) for xx in emi_cov]) + " \\\\"
txt += '\nShare of covered emissions (\%) & ' + ' & '.join(['{:.1f}'.format(xx) for xx in pc_cov])

hpf.write_text_to_file(txt, Path(meta.path.main, 'data', 'other', 'covered_emissions_table_latex.csv'))

# %%
# More data (coverage_orig, coverage_calc, coverage_used).
cov_orig = pd.read_csv(
    Path(meta.path.preprocess, 'coverage_orig_per_gas_and_per_sector_and_combi.csv'), index_col=0)
cov_orig = cov_orig.reindex(columns=[xx for xx in cov_orig.columns if ('_' not in xx and 'LULUCF' not in xx)]). \
    reindex(index=countries_with_indc)
cov_calc = pd.read_csv(
    Path(meta.path.preprocess, 'coverage_calc_per_gas_and_per_sector_and_combi.csv'), index_col=0)
cov_calc = cov_calc.reindex(columns=[xx for xx in cov_calc.columns if ('_' not in xx and 'LULUCF' not in xx)]). \
    reindex(index=countries_with_indc)
cov_used = pd.read_csv(
    Path(meta.path.preprocess, 'coverage_used_per_gas_and_per_sector_and_combi.csv'), index_col=0). \
    reindex(index=countries_with_indc)

emi_kyoto_ipcm0el = 1e-3 * get_table(Path(meta.path.preprocess, 'tables', 
    'KYOTOGHG_IPCM0EL_TOTAL_NET_SSP2BLMESGB_PMSSPBIE.csv')).__reindex__(isos=meta.isos.EARTH, years=years_cov). \
    data
emi_countries_without_indc = emi_kyoto_ipcm0el.loc[countries_without_indc, :].sum()

# %%
years_his = [1990, 2000, 2010, 2017]
global_sums = pd.DataFrame(0,
    columns=years_his,
    index=['orig_YES_YES', 'orig_NO_NO', 'orig_NAN_NAN', 'orig_YES_NO', 'orig_YES_NAN', 'orig_NO_NAN',
           'calc_YES_YES', 'calc_NO_NO', 'calc_NAN_NAN', 'calc_YES_NO', 'calc_YES_NAN', 'calc_NO_NAN',
           'used_YES_YES', 'used_NO_NO', 'used_YES_NO'])
for cat in ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5']:
    for gas in ['CO2', 'CH4', 'N2O', 'HFCS', 'PFCS', 'SF6', 'NF3']:
        try:
            emi_act = 1e-3 * get_table(Path(meta.path.preprocess, 'tables', 
                f'{gas}_{cat}_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')).__reindex__(isos=meta.isos.EARTH, years=years_his). \
                data
            
            for combi in ['YES', 'YES'], ['NO', 'NO'], ['NAN', 'NAN'], ['YES', 'NO'], ['YES', 'NAN'], ['NO', 'NAN']:
                # orig
                isos = [xx for xx in cov_orig.index if 
                    (cov_orig.loc[xx, [cat, gas]].to_list() == combi or 
                     cov_orig.loc[xx, [cat, gas]].to_list() == [combi[1], combi[0]])]
                global_sums.loc[f"orig_{combi[0]}_{combi[1]}", :] = \
                    global_sums.loc[f"orig_{combi[0]}_{combi[1]}", :].add(
                    emi_act.loc[isos, :].sum())
                # calc
                isos = [xx for xx in cov_calc.index if 
                    (cov_calc.loc[xx, [cat, gas]].to_list() == combi or 
                     cov_calc.loc[xx, [cat, gas]].to_list() == [combi[1], combi[0]])]
                global_sums.loc[f"calc_{combi[0]}_{combi[1]}", :] = \
                    global_sums.loc[f"calc_{combi[0]}_{combi[1]}", :].add(
                    emi_act.loc[isos, :].sum())
            # used
            for combi in ['YES', 'YES'], ['NO', 'NO'], ['YES', 'NO']:
                isos = [xx for xx in cov_used.index if 
                    (cov_used.loc[xx, [cat, gas]].to_list() == combi or 
                     cov_used.loc[xx, [cat, gas]].to_list() == [combi[1], combi[0]])]
                global_sums.loc[f"used_{combi[0]}_{combi[1]}", :] = \
                    global_sums.loc[f"used_{combi[0]}_{combi[1]}", :].add(
                    emi_act.loc[isos, :].sum())
                
        except:
            pass

# %%
txt = 'Year & ' + ' & '.join([str(xx) for xx in years_cov]) + " \\\\"
txt += '\nTotal emissions & ' + ' & '.join(['{:.1f}'.format(xx) for xx in emi_tot]) + " \\\\"
txt += '\nCountries without (I)NDC & ' + ' & '.join(['{:.1f}'.format(xx) + '\%'
    for xx in emi_countries_without_indc.div(emi_tot)*100]) + " \\\\"
for ind in global_sums.index:
    txt += f'\n{ind.replace("_", " ")} & ' + ' & '.join(['{:.1f}'.format(xx) + '\%' 
        for xx in global_sums.loc[ind, :].div(emi_tot)*100]) + " \\\\"

hpf.write_text_to_file(txt[:-3].replace('nan\%', '--'), Path(meta.path.main, 'data', 'other', 'covered_emissions_table_long_latex.csv'))

# %%