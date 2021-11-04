# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 08/2020.
"""

# %%
"""
Plot the sum over the baseline emissions (historical and future) in NDCs and
'our PRIMAP-hist & SSP baselines'.
Per base and target year calculate the sum over all available NDC values, 
and our corresponding sum (only for the countries with values in that year).

As table ...
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

# %%
# Get the NDC emissions data.
# Only for years which are needed for the type_main.
ndcs_all = hpf.get_infos_from_ndcs(meta, write_out_data=False)

years = range(1990, 2031)
emi_ndcs = {}
emi_ndcs['inclLU'] = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_inclLU.csv'), index_col=0)
emi_ndcs['exclLU'] = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_exclLU.csv'), index_col=0)
emi_ndcs['inclLU'].loc['USA', :] = np.nan
emi_ndcs['exclLU'].loc['USA', :] = np.nan
emi_ndcs_plot = {}
emi_ndcs_plot['inclLU'] = pd.DataFrame(index=meta.isos.EARTH, columns=years)
emi_ndcs_plot['exclLU'] = pd.DataFrame(index=meta.isos.EARTH, columns=years)

for iso3 in meta.isos.EARTH:
    
    ndc_tar_info = ndcs_all.loc[iso3, :]
    tar_type = ndc_tar_info['TYPE_MAIN']
    
    if (type(tar_type) == str and tar_type != 'NGT'):
        
        target = ndc_tar_info[tar_type]
        
        if type(target) == str:
            
            if tar_type in ['RBY', 'REI']:
                baseyear = ndc_tar_info['BASEYEAR']
                if not np.isnan(baseyear):
                    baseyear = int(ndc_tar_info['BASEYEAR'])
                else:
                    baseyear = ''
            else:
                baseyear = ''
            
            for case in ['inclLU', 'exclLU']:
                # Only use the baseyear emissions (if applicable).
                if baseyear != '':
                    emi_act = emi_ndcs[case].loc[iso3, str(baseyear)]
                    if not np.isnan(emi_act):
                        emi_ndcs_plot[case].loc[iso3, baseyear] = emi_act
                # Else use the target year emissions.
                else:
                    tars = hpf.get_targets_from_json(target, tar_type, iso3)
                    for ind in tars.index:
                        if type(tars.loc[ind, case]) == str:
                            taryr = tars.loc[ind, 'taryr']
                            emi_act = emi_ndcs[case].loc[iso3, taryr]
                            if not np.isnan(emi_act):
                                emi_ndcs_plot[case].loc[iso3, int(taryr)] = emi_act

# %%
emi_ssps = {}
emi_ssps['inclLU'] = {}
emi_ssps['exclLU'] = {}

lulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv')).data

for ssp in meta.ssps.scens.long:
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', f"KYOTOGHG_IPCM0EL_TOTAL_NET_{ssp}FILLED_PMSSPBIE.csv"))
    emi_ssps['exclLU'][ssp] = table.data
    emi_ssps['inclLU'][ssp] = hpf.copy_table(table).data.add(lulucf, fill_value=0)

colours_ssps = pd.read_csv(
    Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_ssps.csv'), index_col=0)

ssp2 = 'SSP2BLMESGB'

# %%
number_of_values = pd.DataFrame(columns=['exclLU', 'inclLU'], index=years)
sums_per_year = pd.DataFrame(index=years)
for year in years:
    for case in ['exclLU', 'inclLU']:
        # NDC data.
        data_ndcs = emi_ndcs_plot[case].loc[:, year]
        isos_with_data = data_ndcs.index[~data_ndcs.isnull()]
        data_ndcs = data_ndcs[isos_with_data].sum()
        if data_ndcs != 0:
            sums_per_year.loc[year, f"{case}_ndc"] = data_ndcs
            
            if len(isos_with_data) > 0:
                # SSP data.
                for ssp in meta.ssps.scens.long:
                    if f"{case}_{ssp}" not in sums_per_year.columns:
                        sums_per_year.loc[:, f"{case}_{ssp}"] = [np.nan]*len(sums_per_year.index)
                    sums_per_year.loc[year, f"{case}_{ssp}"] = np.nansum([sums_per_year.loc[year, f"{case}_{ssp}"],
                        emi_ssps[case][ssp].loc[isos_with_data, year].sum()])
                
    #            if f"{case}_ndc" not in sums_per_year.columns:
    #                sums_per_year.loc[:, f"{case}_ndc"] = [np.nan]*len(sums_per_year.index)
    #            sums_per_year.loc[year, f"{case}_ndc"] = data_ndcs.sum()
                
                ndcs_vs_ssp2 = pd.Series(index=isos_with_data, dtype='float64')
                ndcs_vs_ssp2.loc[:] = 100*emi_ndcs_plot[case].loc[isos_with_data, year]/emi_ssps[case][ssp2].loc[isos_with_data, year]-100
                ndcs_vs_ssp2 = ndcs_vs_ssp2.sort_values(axis=0, ascending=False)
                print(f"% {year} for {case}: " + 
                    ', '.join([f"{xx} ({ndcs_vs_ssp2.loc[xx] :.1f}%)" for xx in ndcs_vs_ssp2.index]) + '.')
                # Negative value: NDC is lower.
                number_of_values.loc[year, case] = len(isos_with_data)

number_of_values.drop(index=number_of_values.index[number_of_values.isnull().all(axis=1)], inplace=True)
sums_per_year.drop(index=sums_per_year.index[sums_per_year.isnull().all(axis=1)], inplace=True)

share = pd.DataFrame(columns=['exclLU', 'inclLU'], index=years)
diff = pd.DataFrame(columns=['exclLU', 'inclLU'], index=years)

df_exclLU = pd.DataFrame()
df_inclLU = pd.DataFrame()
for year in number_of_values.index:
    for case, df in ['exclLU', df_exclLU], ['inclLU', df_inclLU]:
        
        data_act = sums_per_year.loc[year, [xx for xx in sums_per_year.columns if case in xx]]
        
        for ind in meta.ssps.scens.long + ['ndc']:
            sum_act = data_act[f"{case}_{ind}"]
            if not np.isnan(sum_act):
                sum_act = f"{sum_act :.1f}"
                sum_act = (sum_act if len(sum_act) < 6 else sum_act[:-5] + '~' + sum_act[-5:]) # Separate thousands.
                if ('SSP3' in ind) or ('ndc' in ind) or (year >= 2025):
                    sum_act = sum_act
                else:
                    sum_act = ''
            else:
                sum_act = ''
            
            df.loc[(meta.ssps.scens.long_to_short[ind] + " (*)" if ind != 'ndc' else 'NDCs (*)'), year] = sum_act
        
        # Share of emissions with available NDC emissions data (compared to total SSP2).
        emi_ssp2 = emi_ssps[case][ssp].loc[:, year]
        diff_ssp2 = data_act[f"{case}_ndc"] - data_act[f"{case}_{ssp2}"]
        share_ssp2 = data_act[f"{case}_{ssp2}"]/emi_ssp2.reindex(index=meta.isos.EARTH).sum(axis=0)*100
        if not np.isnan(data_act[f"{case}_ndc"]):
            diff_pc = 100*diff_ssp2/data_act[f"{case}_{meta.ssps.scens.long[1]}"]
            df.loc['~~Difference to SSP2', year] = f"{diff_pc :+.1f}%"
            df.loc['~~Number of Parties', year] = f"{number_of_values.loc[year, case]}"
            df.loc['~~Global share (SSP2)', year] = f"{share_ssp2 :.1f}%"
        else:
            df.loc['~~Difference to SSP2', year] = ''
            df.loc['~~Number of Parties', year] = ''
            df.loc['~~Global share (SSP2)', year] = ''

# %%
# Create a latex table.
txt = " & ".join(["(*): Mt~CO$_2$eq AR4"] + ['\\textbf{' + xx + '}' for xx in df.columns.astype(str).to_list()]) + " \\\\ \hline \hline \n"
for case, df, label in ['exclLU', df_exclLU, 'Excluding LULUCF'], ['inclLU', df_inclLU, 'Including LULUCF']:
    txt += " & ".join(["\\textbf{" f"{label}" "}"] + ['']*len(df.columns)) + " \\\\ \hline \n"
    for row in df.index:
        txt += f"{row} & " + " & ".join(df.loc[row, :])
        if row == df.index[-1]:
            txt += " \\\\ \hline \hline \n"
        elif 'SSP5' in row:
            txt += " \\\\ \hline \n"
        else:
            txt += " \\\\ \n"

txt = txt[:-len(" \\\\ \hline \hline \n")]
txt = txt.replace('%', '\%')

hpf.write_text_to_file(txt, 
   Path(meta.path.main, 'data', 'other', 'ndc_emissions_vs_ssps.txt'))

# %%