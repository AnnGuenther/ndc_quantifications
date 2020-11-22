# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from setup_metadata import setup_metadata
import helpers_functions as hpf

# %%
meta = setup_metadata()

path_to_folder_100pc_reclass = 'ndcs_20200628_2122_SSP2_typeReclass_pccov100'
path_to_folder_reclass = 'ndcs_20200628_2120_SSP2_typeReclass'

path_to_folder_100pc_main = 'ndcs_20200702_0830_SSP2_typeMain_pccov100'
path_to_folder_main = 'ndcs_20200702_0829_SSP2_typeMain'

tars_100_all = pd.read_csv(Path(meta.path.output, 'output_for_paper',
    path_to_folder_100pc_reclass, 'ndc_targets.csv'))

tars_100_all_main = pd.read_csv(Path(meta.path.output, 'output_for_paper',
    path_to_folder_100pc_main, 'ndc_targets.csv'))

ptws_100_ssp2_all = pd.read_csv(Path(meta.path.output, 'output_for_paper',
    path_to_folder_100pc_reclass, 'ndc_targets_pathways_per_country.csv'))
tars_100_ssp2_all = pd.read_csv(Path(meta.path.output, 
    path_to_folder_100pc_reclass, 'ndc_targets.csv'))

ptws_100_ssp2_main_all = pd.read_csv(Path(meta.path.output, 'output_for_paper',
    path_to_folder_100pc_main, 'ndc_targets_pathways_per_country.csv'))
tars_100_ssp2_main_all = pd.read_csv(Path(meta.path.output, 
    path_to_folder_100pc_main, 'ndc_targets.csv'))

cols = ['tar_emi_exclLU', 'tar_emi_inclLU', 
        'emi_bl_exclLU_refyr', 'emi_bl_exclLU_taryr',
        'emi_bl_LU_refyr', 'emi_bl_LU_taryr', 
        'pc_cov_exclLU_refyr', 'pc_cov_exclLU_taryr',
        'gdp_refyr', 'gdp_taryr']

ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_NDCSSP2BLMESGB_NDCPMSSPBIE.csv'))

ptws_not100_all = {}
tars_not100_all = {}
for ssp, file in \
    ['ssp1', 'ndcs_20200628_2218_SSP1_typeReclass'], \
    ['ssp2', path_to_folder_reclass], \
    ['ssp3', 'ndcs_20200628_2229_SSP3_typeReclass'], \
    ['ssp4', 'ndcs_20200628_2243_SSP4_typeReclass'], \
    ['ssp5', 'ndcs_20200628_2258_SSP5_typeReclass']:
    ptws_not100_all[ssp] = pd.read_csv(Path(meta.path.output, 'output_for_paper',
        file, 'ndc_targets_pathways_per_country.csv'))
    tars_not100_all[ssp] = pd.read_csv(Path(meta.path.output, 'output_for_paper',
        file, 'ndc_targets.csv'))

ptws_not100_all_main = {}
tars_not100_all_main = {}
for ssp, file in \
    ['ssp1', 'ndcs_20200702_0834_SSP1_typeMain'], \
    ['ssp2', path_to_folder_main], \
    ['ssp3', 'ndcs_20200702_0839_SSP3_typeMain'], \
    ['ssp4', 'ndcs_20200702_0844_SSP4_typeMain'], \
    ['ssp5', 'ndcs_20200702_0848_SSP5_typeMain']:
    ptws_not100_all_main[ssp] = pd.read_csv(Path(meta.path.output, 'output_for_paper',
        file, 'ndc_targets_pathways_per_country.csv'))
    tars_not100_all_main[ssp] = pd.read_csv(Path(meta.path.output, 'output_for_paper',
        file, 'ndc_targets.csv'))

# %%
fig = plt.figure(figsize=(15, 5))

for iso3 in meta.isos.EARTH:
        
    ax_reclass = fig.add_subplot(1, 2, 1)
    ax_main = fig.add_subplot(1, 2, 2)
    
    try:
        tar_type = tars_100_all.loc[tars_100_all.iso3 == iso3, 'tar_type_reclass'].unique()[0]
        tar_type_main = tars_100_all.loc[tars_100_all.iso3 == iso3, 'tar_type_main'].unique()[0]
        
        if any([True if float(tars_100_all.loc[xx, 'tar_emi_exclLU']) > float(tars_100_all.loc[xx, 'emi_bl_exclLU_taryr']) else False
            for xx in tars_100_all.index[(tars_100_all.iso3 == iso3) & (tars_100_all.tar_type_used == tar_type)]]):
    
            tars_100 = tars_100_all.loc[(tars_100_all.iso3 == iso3) & 
                (tars_100_all.tar_type_used == tar_type), cols].astype(float)
            
            tars_not100 = tars_not100_all['ssp2'].loc[(tars_not100_all['ssp2'].iso3 == iso3) & 
                (tars_not100_all['ssp2'].tar_type_used == tar_type), cols].astype(float)
            
            tars_100_main = tars_100_all_main.loc[(tars_100_all_main.iso3 == iso3) & 
                (tars_100_all_main.tar_type_used == tar_type_main), cols].astype(float)
            
            tars_not100_main = tars_not100_all_main['ssp2'].loc[(tars_not100_all_main['ssp2'].iso3 == iso3) & 
                (tars_not100_all_main['ssp2'].tar_type_used == tar_type_main), cols].astype(float)
            
            """
            Plot data. Emissions with targets (SSP1 to SSP5).
            SSP2: 100% coverage vs. 'real' coverage.
            """
            # ndc_targets_pathways_per_country.csv
            ptws_100_ssp2 = ptws_100_ssp2_all.loc[ptws_100_ssp2_all.iso3 == iso3, :]
            ptws_100_ssp2_main = ptws_100_ssp2_main_all.loc[ptws_100_ssp2_main_all.iso3 == iso3, :]
            # ndc_targets.csv
            tars_100_ssp2 = tars_100_ssp2_all.loc[tars_100_ssp2_all.iso3 == iso3, :]
            tars_100_ssp2_main = tars_100_ssp2_main_all.loc[tars_100_ssp2_main_all.iso3 == iso3, :]
            
            ptws_not100 = {}
            tars_not100 = {}
            ptws_not100_main = {}
            tars_not100_main = {}
            for ssp in ['ssp1', 'ssp2', 'ssp3', 'ssp4', 'ssp5']:
                ptws_not100[ssp] = ptws_not100_all[ssp].loc[ptws_not100_all[ssp].iso3 == iso3, :]
                tars_not100[ssp] = tars_not100_all[ssp].loc[tars_not100_all[ssp].iso3 == iso3, :]
                ptws_not100_main[ssp] = ptws_not100_all_main[ssp].loc[ptws_not100_all_main[ssp].iso3 == iso3, :]
                tars_not100_main[ssp] = tars_not100_all_main[ssp].loc[tars_not100_all_main[ssp].iso3 == iso3, :]
            
            colours_ssps = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
                'colours', 'colours_ssps.csv'), index_col=0)
            colour_ssp2 = colours_ssps.loc[meta.ssps.scens.short_to_long['SSP2'], :].to_list()
                        
            years_int = range(1990, 2031)
            years_str = [str(xx) for xx in years_int]
            
            linewdth_ssp2 = 2.5
            linewdth_notssp2 = 1.5
            
            for condi in ['unconditional', 'conditional']:
                for rge in ['best', 'worst']:
                    
                    # reclass
                    
                    # ptws
                    data = ptws_100_ssp2
                    ax_reclass.plot(years_int, data.loc[(data.tar_type_used == tar_type) & (data.condi == condi) & 
                        (data.rge == rge) & (data.category == 'IPCM0EL'), years_str].values[0], ':', color=colour_ssp2,
                        linewidth=linewdth_notssp2, label='__nolabel__')
                    data = ptws_not100['ssp2']
                    ax_reclass.plot(years_int, data.loc[(data.tar_type_used == tar_type) & (data.condi == condi) & 
                        (data.rge == rge) & (data.category == 'IPCM0EL'), years_str].values[0], ':', color=colour_ssp2,
                        linewidth=linewdth_notssp2, label='__nolegend__')
                    
                    # tars
                    data = tars_100_ssp2
                    try:
                        ax_reclass.plot(2030, float(data.loc[(data.tar_type_used == tar_type) & (data.condi == condi) & 
                            (data.rge == rge), 'tar_emi_exclLU']), 'o', color=colour_ssp2, 
                            label=('SSP2 target (excl. LULUCF)\n100% coverage' if rge == 'best' else '__nolegend__'))
                        
                        for ssp in tars_not100.keys():
                            colour_act = colours_ssps.loc[meta.ssps.scens.short_to_long[ssp.upper()], :].to_list()
                            data = tars_not100[ssp]
                            ax_reclass.plot(2030, float(data.loc[(data.tar_type_used == tar_type) & (data.condi == condi) & 
                                (data.rge == rge), 'tar_emi_exclLU']), '^', color=colour_act,
                                label=("SSP2 target (excl. LULUCF)\n'real' coverage" if (rge == 'best' and ssp == 'ssp2') else '__nolegend__'))
                            
                            data = ptws_not100[ssp]
                            ax_reclass.plot(years_int, data.loc[(data.condi == 'emi_bau') & 
                                (data.category == 'IPCM0EL'), years_str].values[0], color=colour_act,
                                linewidth=(linewdth_ssp2 if ssp == 'ssp2' else linewdth_notssp2), label='__nolegend__')
                    
                    except:
                        pass
                    
                    # main
                    
                    # ptws
                    data = ptws_100_ssp2_main
                    ax_main.plot(years_int, data.loc[(data.tar_type_used == tar_type_main) & (data.condi == condi) & 
                        (data.rge == rge) & (data.category == 'IPCM0EL'), years_str].values[0], ':', color=colour_ssp2,
                        linewidth=linewdth_notssp2, label='__nolabel__')
                    data = ptws_not100_main['ssp2']
                    ax_main.plot(years_int, data.loc[(data.tar_type_used == tar_type_main) & (data.condi == condi) & 
                        (data.rge == rge) & (data.category == 'IPCM0EL'), years_str].values[0], ':', color=colour_ssp2,
                        linewidth=linewdth_notssp2, label='__nolegend__')
                    
                    # tars
                    data = tars_100_ssp2_main
                    try:
                        ax_main.plot(2030, float(data.loc[(data.tar_type_used == tar_type_main) & (data.condi == condi) & 
                            (data.rge == rge), 'tar_emi_exclLU']), 'o', color=colour_ssp2, 
                            label=('SSP2 target (excl. LULUCF)\n100% coverage' if rge == 'best' else '__nolegend__'))
                        
                        for ssp in tars_not100.keys():
                            colour_act = colours_ssps.loc[meta.ssps.scens.short_to_long[ssp.upper()], :].to_list()
                            data = tars_not100_main[ssp]
                            ax_main.plot(2030, float(data.loc[(data.tar_type_used == tar_type_main) & (data.condi == condi) & 
                                (data.rge == rge), 'tar_emi_exclLU']), '^', color=colour_act,
                                label=("SSP2 target (excl. LULUCF)\n'real' coverage" if (rge == 'best' and ssp == 'ssp2') else '__nolegend__'))
                            
                            data = ptws_not100_main[ssp]
                            ax_main.plot(years_int, data.loc[(data.condi == 'emi_bau') & 
                                (data.category == 'IPCM0EL'), years_str].values[0], color=colour_act,
                                linewidth=(linewdth_ssp2 if ssp == 'ssp2' else linewdth_notssp2), label='__nolegend__')
                    
                    except:
                        pass
            
            # reclass
            ax_reclass.plot(years_int, ptws_100_ssp2.loc[(ptws_100_ssp2.condi == 'emi_bau') & 
                (ptws_100_ssp2.category == 'IPCM0EL'), years_str].values[0], color=colour_ssp2, 
                label='SSP2 national totals (excl. LULUCF)', linewidth=linewdth_ssp2)
            ax_reclass.plot(years_int, ptws_not100['ssp2'].loc[(ptws_not100['ssp2'].condi == 'emi_cov') & 
                (ptws_not100['ssp2'].category == 'IPCM0EL'), years_str].values[0], '--', color=colour_ssp2, 
                label='SSP2 covered emissions (excl. LULUCF)', linewidth=linewdth_ssp2)
            ax_reclass.plot(years_int, ipcmlulucf.data.loc[iso3, years_int].values, '.', color=[0, .4, 0], 
                label='LULUCF', linewidth=linewdth_ssp2)
            
            # main
            ax_main.plot(years_int, ptws_100_ssp2_main.loc[(ptws_100_ssp2_main.condi == 'emi_bau') & 
                (ptws_100_ssp2_main.category == 'IPCM0EL'), years_str].values[0], color=colour_ssp2, 
                label='SSP2 national totals (excl. LULUCF)', linewidth=linewdth_ssp2)
            ax_main.plot(years_int, ptws_not100_main['ssp2'].loc[(ptws_not100_main['ssp2'].condi == 'emi_cov') & 
                (ptws_not100_main['ssp2'].category == 'IPCM0EL'), years_str].values[0], '--', color=colour_ssp2, 
                label='SSP2 covered emissions (excl. LULUCF)', linewidth=linewdth_ssp2)
            ax_main.plot(years_int, ipcmlulucf.data.loc[iso3, years_int].values, '.', color=[0, .4, 0], 
                label='LULUCF', linewidth=linewdth_ssp2)
            
            ax_main.legend(loc='center right', bbox_to_anchor=(2.1, .5))
            
            XL = [years_int[0] - 2, years_int[-1] + 2]
            ax_reclass.plot(XL, [0, 0], 'k--', linewidth=.3)
            ax_main.plot(XL, [0, 0], 'k--', linewidth=.3)
            
            YL = ax_reclass.get_ylim()
            for year in [2005, 2030]:
                ax_reclass.plot([year, year], YL, 'k--', linewidth=.3)
                ax_main.plot([year, year], YL, 'k--', linewidth=.3)
            
            for axa in [ax_reclass, ax_main]:
                axa.set_xlim(XL)
                axa.set_ylim(YL)
            
            YL = ax_reclass.get_ylim()
            ypos = YL[0] - .12*np.diff(YL)
            for axa in [ax_reclass, ax_main]:
                for year, txt in [2005, 'base year'], [2030, 'target year']:
                    axa.text(year, ypos, txt, ha='center', va='bottom')
            
            ax_reclass.set_ylabel('emissions / Mt CO$_2$eq AR4', fontweight='bold')
            
            ax_reclass.set_title(f"tar_type_reclass: {tar_type}", fontweight='bold')
            ax_main.set_title(f"tar_type_main: {tar_type_main}", fontweight='bold')
            
            fig.subplots_adjust(left=.1, right=.65)
            path_to_png = Path(meta.path.main, 'plots', 'ndc_quantifications', 'ssp2_targets_above_baseline', f'{iso3}_targets.png')
            plt.savefig(path_to_png, dpi=300)
    
    except:
        pass
    
    plt.clf()

plt.close(fig)

# %%