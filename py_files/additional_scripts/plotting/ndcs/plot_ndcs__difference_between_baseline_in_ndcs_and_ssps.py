# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
"""
Plot the sum over the baseline emissions (historical and future) in NDCs and
'our PRIMAP-hist & SSP baselines'.
Per base and target year calculate the sum over all available NDC values, 
and our corresponding sum (only for the countries with values in that year).
"""

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

# %%
# Get the NDC emissions data.
# Only for years which are needed for the type_orig.
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
    tar_type = ndc_tar_info['TYPE_ORIG']
    
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
# Scaled.
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

YL = [-.3, 1.4]
#XL = [1989, 2031]

fig = plt.figure(figsize=(12, 4))
ax_exclLU = fig.add_subplot(1, 2, 1)
ax_inclLU = fig.add_subplot(1, 2, 2)

XL = [-.7, 1.9]
#XL = [1989, 2031]

share = pd.DataFrame(columns=['exclLU', 'inclLU'], index=years)
diff = pd.DataFrame(columns=['exclLU', 'inclLU'], index=years)

for year in number_of_values.index:
    for case, axa in ['exclLU', ax_exclLU], ['inclLU', ax_inclLU]:
        data_act = sums_per_year.loc[year, [xx for xx in sums_per_year.columns if case in xx]]
        # Scale the data to 0 to 1.
        data_min = data_act.min()
        data_max = data_act.max()
        for ind in [f"{case}_{xx}" for xx in meta.ssps.scens.long + ['ndc']]:
            marker = ('o' if 'ndc' not in ind else '*')
            color = ((0, .4, 0) if 'ndc' in ind else colours_ssps.loc[ind.split('_')[1]])
            facecolor = ((1, 1, 1) if 'ndc' in ind else color)
            if year == 1990:
                if 'SSP1' in ind:
                    lgd = 'SSP1'
                elif 'SSP2' in ind:
                    lgd = 'SSP2'
                elif 'SSP3' in ind:
                    lgd = 'SSP3'
                elif 'SSP4' in ind:
                    lgd = 'SSP4'
                elif 'SSP5' in ind:
                    lgd = 'SSP5'
                elif 'ndc' in ind:
                    lgd = 'NDCs'
            else:
                lgd = '__nolegend__'
            
            axa.scatter((data_act[ind]-data_min)/(data_max-data_min), str(year), marker=marker,
                        color=color, facecolor=facecolor, label=lgd)
        
        # SSP2.
        axa.scatter((data_act[f"{case}_{ssp2}"]-data_min)/(data_max-data_min), str(year), marker='o',
                    color=colours_ssps.loc[ssp2, :].to_list(), label='__nolegend__')
        # Share of emissions with available NDC emissions data (compared to total SSP2).
        emi_ssp2 = emi_ssps[case][ssp].loc[:, year]
        diff_ssp2 = data_act[f"{case}_ndc"] - data_act[f"{case}_{ssp2}"]
        share_ssp2 = data_act[f"{case}_{ssp2}"]/emi_ssp2.reindex(index=meta.isos.EARTH).sum(axis=0)*100
        if not np.isnan(data_min):
            number_of_values.loc[year, case] = f"{number_of_values.loc[year, case]}"
            share.loc[year, case] = f"{share_ssp2 :.1f}%"
            diff.loc[year, case] = f"{diff_ssp2 :+.1f}"
        
        if not np.isnan(data_min):
            axa.text(0, str(year), f"{data_min :.1f}   ", ha='right', va='center')
            axa.text(1, str(year), f"   {data_max :.1f}", ha='left', va='center')

ax_exclLU.legend(loc='center', bbox_to_anchor=(1.6, 1.1), ncol=6)

ax_exclLU.set_ylabel('year', fontweight='bold')

YL = ax_exclLU.get_ylim()
YL = [YL[0]*0.9, YL[1]*1.1]
for axa, txt, case in zip([ax_exclLU, ax_inclLU], ['(a) excluding LULUCF', '(b) including LULUCF'], ['exclLU', 'inclLU']):
    axa.plot([-.08, -.08], ['1990', '2030'], 'k:', linewidth=.3)
    axa.plot([1.08, 1.08], ['1990', '2030'], 'k:', linewidth=.3)
    axa.plot(XL, [6.5, 6.5], 'k:', linewidth=.3) # HIS vs. FUT.
    axa.set_ylim(YL)
    axa.set_ylim(YL)
    axa.set_xlim(XL)
    axa.text(XL[0] + .01*np.diff(XL), YL[1] - .02*np.diff(YL), txt, fontweight='bold', ha='left', va='top')
    axa.set_xticks([])
    
    for year in number_of_values.index:
        if type(number_of_values.loc[year, case]) == str:
            axa.text(XL[1] + np.diff(XL)*.27, str(year), f"{diff.loc[year, case]} |", 
                ha='right', va='center', fontweight='bold')
            axa.text(XL[1] + np.diff(XL)*.5, str(year), f"{share.loc[year, case]} |", 
                ha='right', va='center', fontweight='bold')
            axa.text(XL[1] + np.diff(XL)*.58, str(year), f"{number_of_values.loc[year, case]}", 
                ha='right', va='center', fontweight='bold')
    
    axa.set_yticklabels(number_of_values.index)
    axa.set_xlabel('emissions / Mt CO$_2$eq', fontweight='bold')

ax_exclLU.text(XL[0] + np.diff(XL)*1.7, YL[0] - np.diff(YL)*.1, 
    'Values on the right of each plot: difference between sum over available emissions in NDCs and SSP2 baseline (marker scenario) |' +
    '\nshare of global SSP2 emissions (excl. bunkers) | number of countries with emissions data available.', 
    ha='center', va='top')

fig.subplots_adjust(wspace=.85, right=.8, bottom=.2)
path_to_png = Path(meta.path.main, 'plots', 'ndc_quantifications', 'comparison_emi_ndcs_vs_ssp_scaled.png')
plt.savefig(path_to_png, dpi=300)
path_to_pdf = str(path_to_png).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%