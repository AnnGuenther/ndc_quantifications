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

path_to_folder_100pc_reclass = 'ndcs_20200628_2122_typeReclass_SSP2_pccov100'
path_to_folder_reclass = 'ndcs_20200628_2120_SSP2_typeReclass'

tars_100_all = pd.read_csv(Path(meta.path.output, 'output_for_paper',
    path_to_folder_100pc_reclass, 'ndc_targets.csv'))
tars_not100_all = pd.read_csv(Path(meta.path.output, 'output_for_paper',
    path_to_folder_reclass, 'ndc_targets.csv'))
cols = ['tar_emi_exclLU', 'tar_emi_inclLU', 
        'emi_bl_exclLU_refyr', 'emi_bl_exclLU_taryr',
        'emi_bl_LU_refyr', 'emi_bl_LU_taryr', 
        'pc_cov_exclLU_refyr', 'pc_cov_exclLU_taryr',
        'gdp_refyr', 'gdp_taryr']

# %%
fig = plt.figure(figsize=(14, 4))
for iso3 in meta.isos.EARTH:
    
    if 'REI' in tars_100_all.loc[tars_100_all.iso3 == iso3, 'tar_type_main'].to_list():
        int_ref = tars_100_all.loc[tars_100_all.iso3 == iso3, 'int_ref'].to_list()
        if 'GDP' in int_ref:
            int_ref = 'gdp'
        else:
            int_ref = 'pop'
        
        tars_100 = tars_100_all.loc[tars_100_all.iso3 == iso3, cols].astype(float)
        
        tars_not100 = tars_not100_all.loc[tars_not100_all.iso3 == iso3, cols].astype(float)
        
        """
        Plot data. Emissions with targets (SSP1 to SSP5).
        SSP2: 100% coverage vs. 'real' coverage.
        GDP or POP for SSP1 to SSP5.
        """
        # ndc_targets_pathways_per_country.csv
        ptws_100_ssp2 = pd.read_csv(Path(meta.path.output, 
            path_to_folder_100pc_reclass, 'ndc_targets_pathways_per_country.csv'))
        ptws_100_ssp2 = ptws_100_ssp2.loc[ptws_100_ssp2.iso3 == iso3, :]
        # ndc_targets.csv
        tars_100_ssp2 = pd.read_csv(Path(meta.path.output, 
            path_to_folder_100pc_reclass, 'ndc_targets.csv'))
        tars_100_ssp2 = tars_100_ssp2.loc[tars_100_ssp2.iso3 == iso3, :]
        
        ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_NDCSSP2BLMESGB_NDCPMSSPBIE.csv'))
        
        ptws_not100 = {}
        tars_not100 = {}
        for ssp, file in \
            ['ssp1', 'ndcs_20200628_2218_SSP1_typeReclass'], \
            ['ssp2', path_to_folder_reclass], \
            ['ssp3', 'ndcs_20200628_2229_SSP3_typeReclass'], \
            ['ssp4', 'ndcs_20200628_2243_SSP4_typeReclass'], \
            ['ssp5', 'ndcs_20200628_2258_SSP5_typeReclass']:
            data = pd.read_csv(Path(meta.path.output, 
                file, 'ndc_targets_pathways_per_country.csv'))
            ptws_not100[ssp] = data.loc[data.iso3 == iso3, :]
            data = pd.read_csv(Path(meta.path.output, 
                file, 'ndc_targets.csv'))
            tars_not100[ssp] = data.loc[data.iso3 == iso3, :]
        
        colours_ssps = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 
            'colours', 'colours_ssps.csv'), index_col=0)
        colour_ssp2 = colours_ssps.loc[meta.ssps.scens.short_to_long['SSP2'], :].to_list()
        
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2)
        
        years_int = range(1990, 2031)
        years_str = [str(xx) for xx in years_int]
        
        linewdth_ssp2 = 2.5
        linewdth_notssp2 = 1.5
        
        for condi in ['unconditional', 'conditional']:
            for rge in ['best', 'worst']:
                
                # ptws
                data = ptws_100_ssp2
                ax1.plot(years_int, data.loc[(data.tar_type_used == 'REI') & (data.condi == condi) & 
                    (data.rge == rge) & (data.category == 'IPCM0EL'), years_str].values[0], ':', color=colour_ssp2,
                    linewidth=linewdth_notssp2, label='__nolabel__')
                data = ptws_not100['ssp2']
                ax1.plot(years_int, data.loc[(data.tar_type_used == 'REI') & (data.condi == condi) & 
                    (data.rge == rge) & (data.category == 'IPCM0EL'), years_str].values[0], ':', color=colour_ssp2,
                    linewidth=linewdth_notssp2, label='__nolegend__')
                
                # tars
                data = tars_100_ssp2
                try:
                    ax1.plot(2030, float(data.loc[(data.tar_type_used == 'REI') & (data.condi == condi) & 
                        (data.rge == rge), 'tar_emi_exclLU']), 'o', color=colour_ssp2, 
                        label=('SSP2 target (excl. LULUCF)\n100% coverage' if rge == 'best' else '__nolegend__'))
                    
                    for ssp in tars_not100.keys():
                        colour_act = colours_ssps.loc[meta.ssps.scens.short_to_long[ssp.upper()], :].to_list()
                        data = tars_not100[ssp]
                        ax1.plot(2030, float(data.loc[(data.tar_type_used == 'REI') & (data.condi == condi) & 
                            (data.rge == rge), 'tar_emi_exclLU']), '^', color=colour_act,
                            label=("SSP2 target (excl. LULUCF)\n'real' coverage" if (rge == 'best' and ssp == 'ssp2') else '__nolegend__'))
                        
                        data = ptws_not100[ssp]
                        ax1.plot(years_int, data.loc[(data.condi == 'emi_bau') & 
                            (data.category == 'IPCM0EL'), years_str].values[0], color=colour_act,
                            linewidth=(linewdth_ssp2 if ssp == 'ssp2' else linewdth_notssp2), label='__nolegend__')
                        
                        # GDP
                        lbl = (f'{ssp.upper()}' if rge == 'best' else '__nolegend__')
                        ax2.plot(years_int, ptws_not100[ssp].loc[(ptws_not100[ssp].condi == int_ref), years_str].values[0],
                            color=colour_act, label=lbl, linewidth=(linewdth_ssp2 if ssp == 'ssp2' else linewdth_notssp2))
                
                except:
                    pass
        
        ax1.plot(years_int, ptws_100_ssp2.loc[(ptws_100_ssp2.condi == 'emi_bau') & 
            (ptws_100_ssp2.category == 'IPCM0EL'), years_str].values[0], color=colour_ssp2, 
            label='SSP2 national totals (excl. LULUCF)', linewidth=linewdth_ssp2)
        ax1.plot(years_int, ptws_not100['ssp2'].loc[(ptws_not100['ssp2'].condi == 'emi_cov') & 
            (ptws_not100['ssp2'].category == 'IPCM0EL'), years_str].values[0], '--', color=colour_ssp2, 
            label='SSP2 covered emissions (excl. LULUCF)', linewidth=linewdth_ssp2)
        ax1.plot(years_int, ipcmlulucf.data.loc[iso3, years_int].values, '.', color=[0, .4, 0], 
            label='LULUCF', linewidth=linewdth_ssp2)
        
        ssp = 'ssp2'
        ax2.plot(years_int, ptws_not100[ssp].loc[(ptws_not100[ssp].condi == int_ref), years_str].values[0],
            color=colour_ssp2, label='__nolegend__', linewidth=linewdth_ssp2)
        
        
        ax1.legend(loc='upper center', bbox_to_anchor=(.4, 1))
        ax2.legend(loc='upper center', bbox_to_anchor=(.2, 1))
        
        XL = [years_int[0] - 2, years_int[-1] + 2]
        for axa in [ax1, ax2]:
            axa.plot(XL, [0, 0], 'k--', linewidth=.3)
        
        YL = ax1.get_ylim()
        for year in [2005, 2030]:
            ax1.plot([year, year], YL, 'k--', linewidth=.3)
        ax1.set_xlim(XL)
        ax1.set_ylim(YL)
        
        ax2.set_xlim(XL)
        YL = ax2.get_ylim()
        for year in [2005, 2030]:
            ax2.plot([year, year], YL, 'k--', linewidth=.3)
        ax2.set_ylim(YL)
        
        for axa in [ax1, ax2]:
            YL = axa.get_ylim()
            ypos = YL[0] - .12*np.diff(YL)
            for year, txt in [2005, 'base year'], [2030, 'target year']:
                axa.text(year, ypos, txt, ha='center', va='bottom')
        
        ax1.set_ylabel('emissions / Mt CO$_2$eq AR4', fontweight='bold')
        ax2.set_ylabel(('GDP (PPP) / 2011 US$' if int_ref == 'gdp' else 'POP / Pers'), fontweight='bold')
        
        hpf.put_labels_to_subplots(ax1, ax2)
        
        hpf.set_ticks_scientific_notation(ax2, 'y')
        fig.subplots_adjust(left=.1, right=.95)
        path_to_png = Path(meta.path.main, 'plots', 'ndc_quantifications', 'REI_targets', f'{iso3}_pccov_targets_gdp.png')
        plt.savefig(path_to_png, dpi=300)
        #path_to_pdf = str(path_to_png).replace('.png', '.pdf')
        #plt.savefig(path_to_pdf, dpi=300)
        #hpf.crop_pdf(path_to_pdf)
        plt.clf()

plt.close(fig)

# %%