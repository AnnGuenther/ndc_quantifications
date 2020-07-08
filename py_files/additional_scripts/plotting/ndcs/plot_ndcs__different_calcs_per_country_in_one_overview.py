# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020
"""

# %%
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

# %%
def plotting():
    
    # ndc_targets.csv: only the countries with target values, not the ones for which the baseline is used.
    
    tar = 'tar_emi_exclLU'
    
    colours = {'unconditional': (.5, .8, .5), 'conditional': (.8, .5, .5)}
    
    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)
    
    isos_to_plot = pd.Series(sorted([xx for xx in list(quantis[list(quantis.keys())[0]].iso3.unique()) if type(xx) == str]))
    isos_per_plot = int(np.ceil(len(isos_to_plot)/3))
    isos_plots = {ax1: isos_to_plot[0:isos_per_plot], 
        ax2: isos_to_plot[isos_per_plot:2*isos_per_plot], 
        ax3: isos_to_plot[2*isos_per_plot:len(isos_to_plot)]}
    
    for what, count in zip(quantis.keys(), np.arange(.2, .8, .6/(len(quantis.keys())-1))):
        
        data = quantis[what]
        case = ('calc' if 'calc' in what else 'orig')
        
        for axa in isos_plots.keys():
            
            for iso3, count_iso in zip(isos_plots[axa], range(len(isos_plots[axa]))):
                
                data_iso3 = data.loc[data.iso3 == iso3, :]
                
                if len(data_iso3) > 0:
                    
                    data_iso3 = data_iso3.loc[(data_iso3.tar_type_used == data_iso3.loc[:, f'tar_type_{case}'].unique()[0])]
                    
                    for ind in data_iso3.index:
                        
                        data_act = data_iso3.loc[ind, :]
                        axa.scatter(count_iso + count, float(data_act[tar]), color=colours[data_act.condi])
    
    for axa in isos_plots.keys():
        axa.set_yscale('log')
        YL = [1e-3, 1e5]
        axa.set_ylim(YL)
        for count_iso in range(len(isos_plots[axa])):
            axa.plot([count_iso, count_iso], YL, color=(.5, .5, .5))
            axa.plot([count_iso+.5, count_iso+.5], YL, color=(.8, .8, .8))
        
        axa.set_xticks([.5 + xx for xx in range(len(isos_plots[axa]))])
        axa.set_xticklabels(isos_plots[axa], rotation=90)

    plt.savefig(path_to_file, dpi=300)
    #path_to_pdf = str(path_to_file).replace('.png', '.pdf')
    #plt.savefig(path_to_pdf, dpi=300)
    #hpf.crop_pdf(path_to_pdf)
    plt.clf()
    plt.close(fig)

# %%
ssp_calc100 = 'ndcs_20200628_2122_SSP2_typeCalc_pccov100'
ssp_orig100 = 'ndcs_20200702_0830_SSP2_typeOrig_pccov100'
ssp_calc = 'ndc_quantifications_20200610_1720_SSP2_typeCalc'
ssp_orig = 'ndc_quantifications_20200610_1721_SSP2_typeOrig'
ssp = 'SSP2'

# %%
quantis = {}
for what, folder in \
    ['ssp2_calc', ssp_calc100], \
    ['ssp2_orig', ssp_orig100]:
    quantis[what] = pd.read_csv(Path(meta.path.main, 'data', 'output', folder, 'ndc_targets.csv'))

path_to_file = Path(meta.path.main, 'plots', 'ndc_quantifications', 'ssp2_calc100pc_vs_orig100pc.png')
plotting()

# %%
quantis = {}
for what, folder in \
    ['ssp2_calc', ssp_calc], \
    ['ssp2_calc_100%', ssp_calc100]:
    quantis[what] = pd.read_csv(Path(meta.path.main, 'data', 'output', folder, 'ndc_targets.csv'))

path_to_file = Path(meta.path.main, 'plots', 'ndc_quantifications', 'ssp2_calcRealCov_vs_calc100pc.png')
plotting()

# %%
quantis = {}
for what, folder in \
    ['ssp2_orig', ssp_orig], \
    ['ssp2_orig_100%', ssp_orig100]:
    quantis[what] = pd.read_csv(Path(meta.path.main, 'data', 'output', folder, 'ndc_targets.csv'))

path_to_file = Path(meta.path.main, 'plots', 'ndc_quantifications', 'ssp2_origRealCov_vs_orig100pc.png')
plotting()

# %%
def plotting2():
    
    data_exclLU = pd.DataFrame(index=meta.isos.EARTH)
    tar_types = pd.DataFrame(index=meta.isos.EARTH)
    
    year = '2030'
    
    for what, folder in \
        [f'calc', folder_calc], \
        [f'orig', folder_orig]:
        
        quantis = pd.read_csv(Path(meta.path.main, 'data', 'output', folder, 
            'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
        
        # BL emissions.
        if what == f'calc':
            emi_bau = quantis.loc[(quantis.condi == 'emi_bau') & (quantis.category == cat), :]
            emi_bau.index = emi_bau.iso3
            data_exclLU.loc[:, 'bl'] = emi_bau.loc[:, year].reindex(index=data_exclLU.index)
        
        # Target emissions.
        emi_tar = quantis.loc[(quantis.condi == condi) & (quantis.rge == rge) &
            (quantis.category == cat), :]
        emi_tar.index = emi_tar.iso3
        data_exclLU.loc[:, f"tars_{what}"] = emi_tar.loc[:, year].reindex(index=data_exclLU.index)
        # Percentage difference to BL.
        # Negative: target pathway below BL.
        data_exclLU.loc[:, f"{what}"] = (data_exclLU.loc[:, f"tars_{what}"].div(
            data_exclLU.loc[:, 'bl']))*100. - 100.
        # Target types.
        tar_types.loc[:, what] = emi_tar.loc[:, 'tar_type_used'].reindex(index=data_exclLU.index)
    
    # Check if calc differs from orig.
    data_exclLU.loc[:, 'calc_vs_orig'] = data_exclLU.loc[:, 'calc'].add(-data_exclLU.loc[:, 'orig'], fill_value=0)
    # Drop the ones where it does not differ.
    data_exclLU.drop(index=data_exclLU.index[data_exclLU.loc[:, 'calc_vs_orig'] == 0.], inplace=True)
    data_exclLU.drop(index=data_exclLU.index[data_exclLU.loc[:, 'calc_vs_orig'].isnull()], inplace=True)
    data_exclLU.sort_values(by='bl', ascending=False, inplace=True)
    
    data_exclLU.to_csv(
        Path(meta.path.main, 'data', 'other', 
        f'comparison_between_quantifications_{ssp}_{cat}_{year}_{condi}_{rge}.csv'))
    
    # Plot those countries.
    fig = plt.figure(figsize=(17, 7))
    ax1 = fig.add_subplot(1, 1, 1)
    
    ax1.scatter(data_exclLU.index, data_exclLU.bl, marker='s', color='k', label=f'baseline ({ssp})')
    ax1.scatter(data_exclLU.index, data_exclLU.tars_calc, marker='o', color='b', label=label_calc)
    ax1.scatter(data_exclLU.index, data_exclLU.tars_orig, marker='*', color='c', label=label_orig)
    ax1.set_ylabel('emissions / Mt CO$_2$eq (AR4)', fontweight='bold')
    ax1.legend(loc='upper right')
    if xtick_orig:
        xticklabels = [f"{xx}, {tar_types.loc[xx, 'calc']}, {tar_types.loc[xx, 'orig']}" for xx in data_exclLU.index]
        xticklabels = [xx.replace('baseline_emissions', 'BL') if 'baseline' in xx else xx for xx in xticklabels]
    else:
        xticklabels = [f"{xx}, {tar_types.loc[xx, 'calc']}" for xx in data_exclLU.index]
        xticklabels = [xx.replace('baseline_emissions', 'BL') if 'baseline' in xx else xx for xx in xticklabels]
    
    ax1.set_xticklabels(xticklabels, rotation=90, fontweight='bold')
    XL = ax1.get_xlim()
    YL = ax1.get_ylim()
    for grid in range(int(XL[0]), int(XL[-1])):
        ax1.plot([grid+.5, grid+.5], YL, color=(.5, .5, .5), linewidth=.5)
    
    ax1.plot(XL, [0, 0], color=(.5, .5, .5), linewidth=.5)
    
    ax1.set_xlim(XL)
    ax1.set_ylim(YL)
    ax1.set_title(title + f'\n{year} {ssp} {cat} {condi} {rge}', fontweight='bold')
    
    fig.subplots_adjust(hspace=.3, bottom=.3)
    path_to_file = Path(meta.path.main, 'plots', 'ndc_quantifications', 'ssp2_difference_calc_orig_pc100', file)
    plt.savefig(path_to_file, dpi=300)
    #path_to_pdf = str(path_to_file).replace('.png', '.pdf')
    #plt.savefig(path_to_pdf, dpi=300)
    #hpf.crop_pdf(path_to_pdf)
    plt.clf()
    plt.close(fig)

# %%
for cat in ['IPCM0EL', 'IPC0']:
    
    for condi, rge in ['unconditional', 'worst'], ['conditional', 'best']:
        
        folder_calc = ssp_calc100
        folder_orig = ssp_orig100
        label_calc = 'type_calc'
        label_orig = 'type_orig'
        xtick_orig = True
        title = 'Countries for which the target emissions for type_calc and type_orig differ'
        file = f'check_where_differences_between_type_calc_and_orig_come_from_ssp2_{cat}_{condi}_{rge}.png'
        plotting2()
        
        folder_calc = ssp_calc100
        folder_orig = ssp_calc
        label_calc = 'calc'
        label_orig = 'calc100%'
        xtick_orig = False
        title = 'Countries for which the target emissions for type_calc and type_calc100% differ'
        file = f'check_where_differences_between_type_calc_and_calc100pc_come_from_ssp2_{cat}_{condi}_{rge}.png'
        plotting2()
        
        folder_calc = ssp_orig100
        folder_orig = ssp_orig
        label_calc = 'orig'
        label_orig = 'orig100%'
        xtick_orig = False
        title = 'Countries for which the target emissions for type_orig and type_orig100% differ'
        file = f'check_where_differences_between_type_orig_and_orig100pc_come_from_ssp2_{cat}_{condi}_{rge}.png'
        plotting2()

# %%
"""
Check countries which have values for type_calc but not for type_orig (NGT should be the only ones).
And get the mitigation pathway and baseline emissions for 2030.
"""

plot_diff = True
if plot_diff:
    fig = plt.figure(figsize=(7, 4))

ndcs_info = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0)

years_ptw_int = range(1990, 2051)
years_ptw_str = [str(xx) for xx in years_ptw_int]

condi = 'conditional'
rge = 'best'

for cat, cat_LU in ['IPCM0EL', 'exclLU'], ['IPC0', 'inclLU']:
    ndcs_emi = pd.read_csv(
        Path(meta.path.preprocess, f'infos_from_ndcs_emi_{cat_LU}.csv'), index_col=0)
    
    quantis_calc = pd.read_csv(Path(meta.path.main, 'data', 'output', ssp_calc, 
        'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
    quantis_orig = pd.read_csv(Path(meta.path.main, 'data', 'output', ssp_orig, 
        'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
    
    year = '2030'
    txt_all = 'iso3,type_calc,type_orig,bl,bl_global_share,diff,tar_calc,tar_calc_ndc,tar_orig,tar_orig_ndc'
    txt_all += ',refyr_emi_ssp,refyr_emi_ndc,diff_emi_refyr'
    
    bau = pd.read_csv(Path(meta.path.main, 'data', 'output', ssp_calc100, 
        'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
    bau = bau.loc[(bau.condi == 'emi_bau') & (bau.category == cat), :]
    bau.index = bau.iso3
    bau = bau.sort_values(by=year, ascending=False)
    bau_tot_2017 = bau.loc[:, year].reindex(index=meta.isos.EARTH).sum()
    
    folders = [ssp_calc100, ssp_orig100]
    
    for iso3 in bau.index:
        
        txt = '\n' + iso3
        
        refyr = f"{ndcs_info.loc[iso3, 'BASEYEAR'] :.0f}"
        
        emi_tars = []
        
        for folder in folders:
            
            quantis = pd.read_csv(Path(meta.path.main, 'data', 'output', folder, 
                'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
            
            try:
                emi_tar = quantis.loc[(quantis.iso3 == iso3) & (quantis.condi == condi) &
                    (quantis.rge == rge) & (quantis.category == cat), year].values[0]
                txt += ',' + "{:.0f}".format(emi_tar)
                emi_tars += [emi_tar]
            except:
                emi_tar = np.nan
                txt += ','
                emi_tars += [emi_tar]
            
            # Baseline emissions.
            if folder == folders[-1]:
                try:
                    bau_act = quantis.loc[(quantis.iso3 == iso3) & (quantis.condi == 'emi_bau') &
                        (quantis.category == cat), year].values[0]
                    txt += ',' + "{:.0f}".format(bau_act)
                    txt += ',' + "{:.1f}".format(bau_act/bau_tot_2017*100.)
                except:
                    txt += ',,'
                
                try:
                    emi_refyr_ssp = f"{quantis.loc[(quantis.iso3 == iso3) & (quantis.condi == 'emi_bau') & (quantis.category == cat), refyr].values[0] :.1f}"
                except:
                    emi_refyr_ssp = ""
        
        txt += f",{np.diff(emi_tars)[0]}"
        
        neg_emi = (True if quantis.loc[(quantis.iso3 == iso3) & (quantis.condi == condi) &
            (quantis.rge == rge) & (quantis.category == cat), year].values[0] < 0 else False)
        
        if ((plot_diff and np.diff(emi_tars)[0] != 0) or (plot_diff and neg_emi)):
            
            ax1 = fig.add_subplot(1, 1, 1)
            ax1.plot([1990, 2050], [0, 0], 'k:', linewidth=.3)
            # Plot baseline emissions and target emissions.
            for folder in folders:
                
                if 'typeCalc' in folder:
                    colour_target = (1, 0, 0)
                    linestyle = '--'
                    which_type = 'calc'
                elif 'typeOrig' in folder:
                    colour_target = (1, .5, .5)
                    linestyle = '-.'
                    which_type = 'orig'
                
                colour_bau = (0, 0, 1)
                colour_emi_ndc = (0, .5, 0)
                
                # SSP data and target.
                quantis = pd.read_csv(Path(meta.path.main, 'data', 'output', folder, 
                    'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
                quantis_LU = quantis.loc[(quantis.iso3 == iso3) & (quantis.category == 'IPCMLULUCF'), :]
                quantis = quantis.loc[(quantis.iso3 == iso3) & (quantis.category == cat), :]
                bau_ptw = quantis.loc[(quantis.condi == 'emi_bau'), years_ptw_str]
                bau_ptw_LU = quantis_LU.loc[(quantis_LU.condi == 'emi_bau'), years_ptw_str]
                target_ptw = quantis.loc[(quantis.condi == condi) & (quantis.rge == rge), years_ptw_str]
                
                ax1.plot(years_ptw_int, bau_ptw.loc[bau_ptw.index[0], :], color=colour_bau, label=('Emi. SSP2' if which_type == 'calc' else '__nolegend__'))
                ax1.plot(years_ptw_int, bau_ptw_LU.loc[bau_ptw_LU.index[0], :], color=(0, 1, 0), label=('Emi. LU' if which_type == 'calc' else '__nolegend__'))
                
                if 'typeCalc' in folder:
                    tar_type = ndcs_info.loc[iso3, 'TYPE_CALC']
                elif 'typeOrig' in folder:
                    tar_type = ndcs_info.loc[iso3, 'TYPE_ORIG']
                
                ax1.plot(years_ptw_int, target_ptw.loc[target_ptw.index[0], :], linestyle=linestyle, color=colour_target, label=f'{which_type} ({tar_type})')
                
                # Emissions data from NDC.
                ax1.scatter(years_ptw_int, ndcs_emi.loc[iso3, years_ptw_str], color=colour_emi_ndc, label=('Emi. NDC' if which_type == 'calc' else '__nolegend__'))
                
                # Vertical lines to show differences.
                baseyear = ndcs_info.loc[iso3, 'BASEYEAR']
                if not np.isnan(baseyear):
                    ax1.plot([baseyear, baseyear], [ndcs_emi.loc[iso3, str(int(baseyear))], 
                        bau_ptw.loc[bau_ptw.index, str(int(baseyear))]], 'k:', linewidth=.5)
                else:
                    if (type(tar_type) == str and tar_type != 'NGT'):
                        target_info = hpf.get_targets_from_json(ndcs_info.loc[iso3, tar_type], tar_type, iso3)
                        for taryr in target_info.taryr.unique():
                            ax1.plot([int(taryr), int(taryr)], 
                                [ndcs_emi.loc[iso3, taryr], bau_ptw.loc[bau_ptw.index, taryr].values], 'k:', linewidth=.5)
            
            ax1.legend(loc='center right', bbox_to_anchor=(1.35, .5))
            ax1.set_ylabel('emissions / Mt CO$_2$eq', fontweight='bold')
            ax1.set_title(f"{iso3}: {cat_LU} (global share in 2017: {bau_ptw.loc[bau_ptw.index[0], '2017']/bau_tot_2017*100 :.1f}%)" +
                          f"{(', negative emissions' if neg_emi else '')}")
            fig.subplots_adjust(right=.75)
            path_to_png = Path(meta.path.main, 'plots', 'ndc_quantifications', 
                'comparison_type_calc_orig', f'comparison_type_calc_orig_{iso3}_{cat_LU}_{condi}_{rge}.png')
            plt.savefig(path_to_png, dpi=300)
            plt.clf()
        
        # Target types.
        calc_act = quantis_calc.loc[(quantis_calc.iso3 == iso3) & (quantis_calc.category == cat), :]
        orig_act = quantis_orig.loc[(quantis_orig.iso3 == iso3) & (quantis_orig.category == cat), :]
        try:
            tar_calc = calc_act.loc[(calc_act.condi == condi) & (calc_act.rge == rge), 'tar_type_used'].values[0]
        except:
            tar_calc = ''
        try:
            tar_orig = orig_act.loc[(orig_act.condi == condi) & (orig_act.rge == rge), 'tar_type_used'].values[0]
        except:
            tar_orig = ''
        tar_calc_ndc = ndcs_info.loc[iso3, 'TYPE_CALC']
        tar_orig_ndc = ndcs_info.loc[iso3, 'TYPE_ORIG']
        txt += f",{tar_calc},{tar_calc_ndc},{tar_orig},{tar_orig_ndc}"
        
        txt += f",{emi_refyr_ssp}"
        try:
            emi_refyr_ndc = ndcs_emi.loc[iso3, refyr]
            if not np.isnan(emi_refyr_ndc):
                txt += f",{emi_refyr_ndc :.1f},{emi_refyr_ndc-emi_refyr_ssp :.1f}"
        except:
            txt += ","
        
        txt_all += txt
    
    hpf.write_text_to_file(txt_all, 
        Path(meta.path.main, 'data', 'other', f'comparison_type_calc_orig_100pc_{cat_LU}_{year}_{ssp}_{condi}_{rge}.csv'))

if plot_diff:
    plt.close(fig)

# %%
"""
Plot the emissions from the NDCs and the SSP2 baseline, both inclLU and exclLU.
"""

ndcs_emi_inclLU = pd.read_csv(Path(meta.path.preprocess, f'infos_from_ndcs_emi_inclLU.csv'), index_col=0)
ndcs_emi_exclLU = pd.read_csv(Path(meta.path.preprocess, f'infos_from_ndcs_emi_exclLU.csv'), index_col=0)
ssp2_ipcm0el = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCM0EL_TOTAL_NET_SSP2BLMESGBFILLED_PMSSPBIE.csv')).data
ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.preprocess, 'tables', 'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS.csv')).data
ssp2_ipc0 = ssp2_ipcm0el.add(ipcmlulucf, fill_value=0)

fig = plt.figure(figsize=(7, 5))
for iso3 in meta.isos.EARTH:
    if (ndcs_emi_inclLU.loc[iso3, :].any() or ndcs_emi_exclLU.loc[iso3, :].any()):
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.plot([1990, 2050], [0, 0], 'k:', linewidth=.3)
        ax1.plot(years_ptw_int, ssp2_ipcm0el.loc[iso3, years_ptw_int], 'k', label='SSP2 exclLU')
        ax1.scatter(years_ptw_int, ndcs_emi_exclLU.loc[iso3, years_ptw_str], color='k', label='NDC exclLU')
        ax1.plot(years_ptw_int, ssp2_ipc0.loc[iso3, years_ptw_int], 'g:', label='SSP2 inclLU')
        ax1.scatter(years_ptw_int, ndcs_emi_inclLU.loc[iso3, years_ptw_str], marker='*', color='g', label='NDC inclLU')
        YL = ax1.get_ylim()
        XL = ax1.get_xlim()
        ax1.plot([2017.5, 2017.5], YL, 'k:', linewidth=.3)
        ax1.legend(loc='center right', bbox_to_anchor=(1.35, .5))
        ax1.set_ylabel('emissions / Mt CO$_2$eq', fontweight='bold')
        neg_exclLU = ('\nNegative exclLU NDC emissions so probably it is inclLU!!!' 
            if any(ndcs_emi_exclLU.loc[iso3, years_ptw_str] < 0) else '')
        neg_inclLU = ('\nNegative inclLU NDC emissions so it actually is inclLU!!!' 
            if any(ndcs_emi_inclLU.loc[iso3, years_ptw_str] < 0) else '')
        ax1.set_title(f"{iso3}{neg_exclLU}{neg_inclLU}")
        fig.subplots_adjust(right=.75)
        path_to_png = Path(meta.path.main, 'plots', 'ndc_quantifications', 
            f'comparison_emi_ndcs_{ssp}', f'comparison_emi_ndc_{ssp}_{iso3}.png')
        plt.savefig(path_to_png, dpi=300)
        plt.clf()
    
plt.close(fig)

# %%