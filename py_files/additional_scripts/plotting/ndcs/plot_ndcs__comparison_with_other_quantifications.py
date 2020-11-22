# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020
"""
# %%
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

ndcs_emi_exclLU = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_exclLU.csv'), index_col=0)
ndcs_emi_inclLU = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_inclLU.csv'), index_col=0)
ndcs_emi_onlyLU = pd.read_csv(
    Path(meta.path.preprocess, 'infos_from_ndcs_emi_onlyLU.csv'), index_col=0)

folder_ext = Path(meta.path.main, 'data', 'other', 'data_from_others')
folder_mine_SSP2 = Path(meta.path.output, 'ndcs_20200628_2122_SSP2_typeCalc_pccov100')
years_int = range(1990, 2031)
years_str = [str(xx) for xx in years_int]
ndcs_info = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0)

# %%
"""
Comparison of EARTH pathway with CAT quantifications.
"""

"""
cat_ptws = pd.read_csv(Path(folder_ext, 'CAT_2019-12-10_PublicData_EmissionsGaps_Dec2019_MtCO2eq.csv'), index_col=0)
cat_ptws.columns = [int(xx) for xx in cat_ptws.columns]

my_ptws = pd.read_csv(Path(folder_mine_SSP2, 'ndc_targets_pathways_per_group.csv'))
my_ptws = my_ptws.loc[my_ptws.group == 'EARTH', :]
kyotoghgar4_ipcm0el = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.matlab, 'KYOTOGHGAR4_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')).\
    data.loc['EARTH', :].reindex(index=years_int)
kyotoghgar4_ipcmlulucf = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.matlab, 'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')).\
    data.loc['EARTH', :].reindex(index=years_int)

fig = plt.figure(figsize=(7, 7))
axa = fig.add_subplot(1, 1, 1)

for ind in cat_ptws.index:
    plt.plot(cat_ptws.columns, cat_ptws.loc[ind, :], 'r')

for condi in ['unconditional', 'conditional']:
    for rge in ['best', 'worst']:
        
        lbl_ipc0 = '__nolegend__'
        lbl_ipcm0el = '__nolegend__'
        if ((condi == 'unconditional') & (rge == 'best')):
            lbl_ipc0 = 'NDCs IPC0'
            lbl_ipcm0el = 'NDCs IPCM0EL'
        
        data = my_ptws.loc[(my_ptws.condi == condi) & (my_ptws.rge == rge) & (my_ptws.category == 'IPC0'), years_str]
        plt.plot(years_int, data.loc[:, years_str].values[0], 'k', label=lbl_ipc0)
        data = my_ptws.loc[(my_ptws.condi == condi) & (my_ptws.rge == rge) & (my_ptws.category == 'IPCM0EL'), years_str]
        plt.plot(years_int, data.loc[:, years_str].values[0], 'b', label=lbl_ipcm0el)

plt.plot(kyotoghgar4_ipcm0el.index, kyotoghgar4_ipcm0el, 'c', label='PRIMAP-hist v2.1 EARTH\nIPCM0EL')
plt.plot(kyotoghgar4_ipcmlulucf.index, kyotoghgar4_ipcmlulucf.add(kyotoghgar4_ipcm0el, fill_value=0), 'g', label='PRIMAP-hist v2.1 EARTH\nIPCM0EL + IPCMLULUCF')
plt.plot(plt.xlim(), [0, 0], 'k:', label='__nolegend__')

plt.ylabel('emissions / MtCO2eq AR4', fontweight='bold')
plt.legend(loc='lower right')
plt.text(years_int[0], -7000, "red from https://climateactiontracker.org/global/cat-emissions-gaps/" +
         "\nHistorical values (incl. LULUCF) & pledge high & pledge low" +
         "\nJG: CAT includes bunkers.", ha='left', va='top')

XL = plt.xlim()
YL = plt.ylim()

fig.subplots_adjust(bottom=.2)
plt.savefig(Path(meta.path.main, 'plots', 'comparisons_with_other_data', 'comparisons_cat', 
    'EARTH.png'), dpi=300)
plt.clf()
plt.close(fig)
"""

"""
Comparison of EARTH pathway with CAT quantifications.
Add CDIAC international bunkers, as CAT includes Bunkers.
CDIAC only has data for historical years...
"""

"""
# Add CDIAC CATM1 (as CAT includes bunkers - information from J. Guetschow).

# !!!!!!!!!!!!!!!!!!!!!!!!
# CDIAC CATM1 are only CO2 emissions!!! Add better Bunkers total!!!
# !!!!!!!!!!!!!!!!!!!!!!!!

years_cdiac_int = range(1990, 2015)
years_cdiac_str = [str(xx) for xx in years_cdiac_int]
cdiac = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(meta.path.matlab, 'CO2AR4_CATM1_TOTAL_NET_HISTORY_CDIAC2017P.csv')).\
    data.loc['EARTH', :].reindex(index=years_cdiac_int)

fig = plt.figure(figsize=(7, 7))
axa = fig.add_subplot(1, 1, 1)

for ind in cat_ptws.index:
    plt.plot(years_cdiac_int, cat_ptws.loc[ind, years_cdiac_int], 'r')

for condi in ['unconditional', 'conditional']:
    for rge in ['best', 'worst']:
        
        lbl_ipc0 = '__nolegend__'
        lbl_ipcm0el = '__nolegend__'
        if ((condi == 'unconditional') & (rge == 'best')):
            lbl_ipc0 = 'NDCs IPC0'
            lbl_ipcm0el = 'NDCs IPCM0EL'
        
        data = cdiac.add(
            my_ptws[(my_ptws.condi == condi) & (my_ptws.rge == rge) & (my_ptws.category == 'IPC0')].reindex(columns=years_cdiac_str).values[0], 
            fill_value=0)
        plt.plot(years_cdiac_int, data, 'k', label=lbl_ipc0)
        data = cdiac.add(
            my_ptws[(my_ptws.condi == condi) & (my_ptws.rge == rge) & (my_ptws.category == 'IPCM0EL')].reindex(columns=years_cdiac_str).values[0], 
            fill_value=0)
        plt.plot(years_cdiac_int, data, 'b', label=lbl_ipcm0el)

plt.plot(years_cdiac_int, cdiac.add(kyotoghgar4_ipcm0el.reindex(index=years_cdiac_int).values, fill_value=0), 
    'c', label='PRIMAP-hist v2.1 EARTH\nIPCM0EL')
primap_ipc0 = kyotoghgar4_ipcmlulucf.add(kyotoghgar4_ipcm0el, fill_value=0)
plt.plot(years_cdiac_int, cdiac.add(primap_ipc0.reindex(index=years_cdiac_int).values, fill_value=0), 
    'g', label='PRIMAP-hist v2.1 EARTH\nIPCM0EL + IPCMLULUCF')
plt.plot(plt.xlim(), [0, 0], 'k:', label='__nolegend__')

plt.ylabel('emissions / MtCO2eq AR4', fontweight='bold')
plt.legend(loc='lower right')
plt.text(years_int[0], -7000, "red from https://climateactiontracker.org/global/cat-emissions-gaps/" +
         "\nHistorical values (incl. LULUCF) & pledge high & pledge low" +
         "\nJG: CAT includes bunkers.\nSo CO2_CATM1_CDIAC2017P was added to our data.", ha='left', va='top')

plt.xlim(XL)
plt.ylim(YL)

fig.subplots_adjust(bottom=.2)
plt.savefig(Path(meta.path.main, 'plots', 'comparisons_with_other_data', 'comparisons_cat', 
    'EARTH_cdiac.png'), dpi=300)
plt.clf()
plt.close(fig)
"""

# %%
"""
Compare single countries (CAT and our calculations with 100% coverage and type_reclass).
"""

cat_tars = pd.read_csv(Path(folder_ext, 'CAT_website_data_1219_COP25.csv'))
cat_tars.columns = [xx.replace(' ', '_').replace('/', '_') for xx in cat_tars.columns]
cat_tars.columns = [xx if xx != 'Default_graph_label'
               else 'label'for xx in cat_tars.columns ]
cat_tars.columns = [xx if xx != 'Sector_Type'
               else 'st'for xx in cat_tars.columns ]
cat_countries = sorted(cat_tars.country.unique())
cat_isos = hpf.convert_country_names_to_isos(cat_countries, 'ISO3')

# %%
my_calc = pd.read_csv(Path(folder_mine_SSP2, "ndc_targets.csv"))
my_calc_ptws = pd.read_csv(Path(folder_mine_SSP2, 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))

colours = {'unconditional_worst': (1, .5, 0),
          'unconditional_best': (.7, .5, .2),
          'conditional_worst': (0, .5, 1),
          'conditional_best': (.2, .5, .7)}

fig = plt.figure(figsize=(15, 5))
for ct in range(len(cat_isos)):
    country_act = cat_countries[ct]
    iso_act = cat_isos[ct]
    if iso_act in list(my_calc.iso3):
        #
        cat_act = cat_tars.loc[cat_tars.country == country_act, :]
        cat_his = cat_act.loc[
                cat_act.label == 'Historical emissions, excl forestry', :]
        cat_lu = cat_act.loc[
                cat_act.label == 'Historical emissions/removals from forestry', :]
        cat_cpp = cat_act.loc[
                cat_act.label.isin([
                        'Current policy projections', 
                        'Implementation of national measures',
                        'Implementation of EU legislation']), :]
        cat_ndc_ref = cat_act.loc[
                cat_act.label == 'Reference for NDC', :]
        cat_ndc = cat_act.loc[
                (cat_act.label.isin(['NDC', 'NDC unconditional', 'NDC conditional'])) &
                (cat_act.st.isin(['Unconditional, Max', 'Unconditional, Min',
                                     'Conditional, Max', 'Conditional, Min'])), :]
        ax1 = fig.add_subplot(1, 2, 1)
        ax1.set_title('CAT', fontweight='bold')
        ax2 = fig.add_subplot(1, 2, 2)
        ax2.set_title('PIK (cov set to 100%)', fontweight='bold')
        #
        ax1.plot(years_int, cat_his.loc[:, years_str].values[0], 'k')
        ax2.plot(years_int, cat_his.loc[:, years_str].values[0], 'k:')
        ax1.plot(years_int, cat_lu.loc[:, years_str].values[0], 'g')
        ax2.plot(years_int, cat_lu.loc[:, years_str].values[0], 'g:')
        ax1.plot(years_int, cat_cpp.loc[:, years_str].values[0], 'r')
        ax2.plot(years_int, cat_cpp.loc[:, years_str].values[0], 'r:')
        ax1.plot(years_int, cat_ndc_ref.loc[:, years_str].values[0], 'b')
        for cd in cat_ndc.index:
            if 'UNCONDITIONAL' in cat_ndc.loc[cd, 'st'].upper():
                condi = 'unconditional'
            else:
                condi = 'conditional'
            # endif
            if 'MAX' in cat_ndc.loc[cd, 'st'].upper():
                rge = 'worst'
            else:
                rge = 'best'
            ax1.plot(years_int, cat_ndc.loc[cd, years_str].values, 's',
                     color=colours[condi + '_' + rge])
        #
        my_calc_act = my_calc.loc[my_calc.iso3 == iso_act, :]
        my_calc_ptws_act = my_calc_ptws.loc[my_calc_ptws.iso3 == iso_act, :]
        my_calc_emi = my_calc_ptws_act.loc[my_calc_ptws_act.condi == 'emi_bau', :]
        my_calc_emi_lu = my_calc_ptws_act.loc[my_calc_ptws_act.category == 'IPCMLULUCF', :]
        my_calc_pc = my_calc_ptws_act.loc[my_calc_ptws_act.rge == 'pc_cov', :]
        #
        ax2.plot(years_int, my_calc_emi.loc[:, years_str].values[0], 'r')
        ax1.plot(years_int, my_calc_emi.loc[:, years_str].values[0], 'r:')
#        ax2.plot(years_int, my_calc_emi_lu.loc[:, years_str].values[0], 'g')
#        ax1.plot(years_int, my_calc_emi_lu.loc[:, years_str].values[0], 'g:')
        my_calc_yrs_act = my_calc_act.taryr
        
        which_targets = ndcs_info.loc[iso_act, 'TYPE_RECLASS'] # set(['ABS'] + ndcs_info.loc[iso_act, ['TYPE_RECLASS', 'TYPE_MAIN']].to_list())
        for tar_yr in sorted(my_calc_yrs_act.unique()):
            if tar_yr <= 2030:
                add_x = 0
                for condi in ['unconditional', 'conditional']:
                    for rge in ['worst', 'best']:
                        add_x = add_x + .2
                        
                        my_calc_ndc_act = my_calc_act.loc[(my_calc_act.condi == condi) &
                            (my_calc_act.rge == rge) & (my_calc_act.taryr == tar_yr), 
                            'tar_emi_exclLU'].astype(float)
                        my_calc_tar_types = my_calc_act.loc[my_calc_ndc_act.index, 
                            'tar_type_used']
                        my_calc_tars_to_plot = [xx for xx in my_calc_tar_types.index if my_calc_tar_types[xx] in which_targets]
                        my_calc_ndc_act = my_calc_ndc_act.loc[my_calc_tars_to_plot]
                        if my_calc_ndc_act.any():
                            ax2.plot([tar_yr+add_x]*len(my_calc_ndc_act), my_calc_ndc_act.values, 'o',
                                     color=colours[condi + '_' + rge])
                        
                        ptw_chosen = my_calc_ptws_act.loc[(my_calc_ptws_act.condi == condi) &
                            (my_calc_ptws_act.rge == rge) & (my_calc_ptws_act.category == 'IPCM0EL'), years_str].values[0]
                        ax1.plot(years_int, ptw_chosen, 'b:')
                        ax2.plot(years_int, ptw_chosen, 'b')
        #
        ax2.scatter(range(1990, 2031), ndcs_emi_exclLU.loc[iso_act, [str(xx) for xx in range(1990, 2031)]], color='k')
        ax2.scatter(range(1990, 2031), ndcs_emi_inclLU.loc[iso_act, [str(xx) for xx in range(1990, 2031)]], color='c')
        ax2.scatter(range(1990, 2031), ndcs_emi_onlyLU.loc[iso_act, [str(xx) for xx in range(1990, 2031)]], color='g')
        #
        for axa in [ax1, ax2]:
            axa.set_xlim([1989, 2031])
            axa.plot(axa.get_xlim(), [0, 0], 'k')
        # endfor
        YL = [min([min(ax1.get_ylim()), min(ax2.get_ylim())]), 
              max([max(ax1.get_ylim()), max(ax2.get_ylim())])]
        for axa in [ax1, ax2]:
            axa.set_ylim(YL)
        # endfor
        ax1.set_ylabel('emissions / MtCO2eq (AR4)', fontweight='bold')
        fig.suptitle("Comparison CAT and PIK (SSP2), targets exclude LULUCF\n" + country_act, 
                     fontweight='bold')
        fig.subplots_adjust(top=.8, right=.87, hspace=.3)
        plt.savefig(Path(meta.path.main, 'plots', 'comparisons_with_other_data', 'comparisons_cat', 
            'comparison_cat_ssp2default_excllu_' + iso_act + '.png'), dpi=300)
        plt.clf()

plt.close(fig)

# %%
"""
Comparison of country targets to data from ndcpartnership.
https://ndcpartnership.org/countries-map
"""

ndc_partner = pd.read_csv(Path(folder_ext, 'targets_from_ndcpartnership_20200427.csv'))

my_calc = pd.read_csv(Path(folder_mine_SSP2, "ndc_targets.csv"))
my_calc_ptws = pd.read_csv(Path(folder_mine_SSP2, 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))

colours = {'unconditional_worst': (1, .5, 0),
          'unconditional_best': (.7, .5, .2),
          'conditional_worst': (0, .5, 1),
          'conditional_best': (.2, .5, .7)}

# Given baseline emissions.
ndcs_bau = hpf.get_infos_from_ndcs_emi()

fig = plt.figure(figsize=(15, 5))
for iso_act in ndc_partner.iso3.unique():
    ndc_act = ndc_partner.loc[ndc_partner.iso3 == iso_act, :]
    if not ndc_act.emi.isnull().all():
        bau_act = ndc_act.loc[ndc_act.what == 'BAU', :]
        tar_act = ndc_act.loc[ndc_act.what.isin(['Unconditional', 'Conditional']), :]
        ax1 = fig.add_subplot(1, 3, 1)
        ax1.set_title('NDC Partnership', fontweight='bold')
        ax2 = fig.add_subplot(1, 3, 2)
        ax2.set_title('PIK (cov set to 100%)\ninclLU', fontweight='bold')
        ax3 = fig.add_subplot(1, 3, 3)
        ax3.set_title('PIK (cov set to 100%)\nexclLU', fontweight='bold')
        #
        ax1.scatter(bau_act.year.values, bau_act.emi.values, color='k')
        for cd in tar_act.index:
            if 'UNCONDITIONAL' in tar_act.loc[cd, 'what'].upper():
                condi = 'unconditional'
            else:
                condi = 'conditional'
            
            ax1.plot(tar_act.loc[cd, 'year'], tar_act.loc[cd, 'emi'], 's',
                color=colours[condi + '_best'])
        #
        my_calc_act = my_calc.loc[my_calc.iso3 == iso_act, :]
        my_calc_ptws_act = my_calc_ptws.loc[my_calc_ptws.iso3 == iso_act, :]
        my_calc_emi = my_calc_ptws_act.loc[my_calc_ptws_act.condi == 'emi_bau', :]
        my_calc_emi_lu = my_calc_ptws_act.loc[my_calc_ptws_act.category == 'IPCMLULUCF', :]
        my_calc_pc = my_calc_ptws_act.loc[my_calc_ptws_act.rge == 'pc_cov', :]
        #
#        ax2.plot(years_int, my_calc_emi_lu.loc[:, years_str].values[0], 'g')
        my_calc_yrs_act = my_calc_act.taryr
        #
        ax2.scatter(ndcs_bau['onlyLU'].columns, ndcs_bau['onlyLU'].loc[iso_act, :], color='g')
        ax2.scatter(ndcs_bau['inclLU'].columns, ndcs_bau['inclLU'].loc[iso_act, :], color='k')
        ax3.scatter(ndcs_bau['exclLU'].columns, ndcs_bau['exclLU'].loc[iso_act, :], color='k')
        #
        try:
            tar_type_calc = my_calc_act.loc[:, 'tar_type_reclass'].unique()[0]
            for tar_yr in sorted(my_calc_yrs_act.unique()):
                if tar_yr <= 2030:
                    add_x = 0
                    for condi in ['unconditional', 'conditional']:
                        for rge in ['worst', 'best']:
                            add_x = add_x + .2
                            my_calc_ndc_act = my_calc_act.loc[(my_calc_act.condi == condi) &
                                (my_calc_act.rge == rge) & (my_calc_act.taryr == tar_yr) &
                                (my_calc_act.tar_type_used == tar_type_calc), 
                                'tar_emi_exclLU'].astype(float)
                            my_calc_ndc_act_inclLU = my_calc_act.loc[(my_calc_act.condi == condi) &
                                (my_calc_act.rge == rge) & (my_calc_act.taryr == tar_yr) &
                                (my_calc_act.tar_type_used == tar_type_calc), 
                                'tar_emi_inclLU'].astype(float)
                            if my_calc_ndc_act.any():
                                ax2.plot([tar_yr+add_x]*len(my_calc_ndc_act_inclLU), my_calc_ndc_act_inclLU.values, 'o',
                                         color=colours[condi + '_' + rge])
                                ax3.plot([tar_yr+add_x]*len(my_calc_ndc_act), my_calc_ndc_act.values, 'o',
                                         color=colours[condi + '_' + rge])
                            
                            try:
                                # IPC0.
                                ptw_chosen = my_calc_ptws_act.loc[(my_calc_ptws_act.condi == condi) &
                                    (my_calc_ptws_act.rge == rge) & (my_calc_ptws_act.category == 'IPC0'), years_str].values[0]
                                ax2.plot(years_int, ptw_chosen, 'c')
                                # IPCM0EL.
                                ptw_chosen = my_calc_ptws_act.loc[(my_calc_ptws_act.condi == condi) &
                                    (my_calc_ptws_act.rge == rge) & (my_calc_ptws_act.category == 'IPCM0EL'), years_str].values[0]
                                ax3.plot(years_int, ptw_chosen, 'b')
                            except:
                                pass
        except:
            tar_type_reclass = 'NAN'
        #
        # BAU exclLU
        ax3.plot(years_int, my_calc_emi.loc[:, years_str].values[0], ':r')
        for axa in [ax1, ax2, ax3]:
            axa.set_xlim([1989, 2031])
            axa.plot(axa.get_xlim(), [0, 0], 'k')
        
        YL = [min([min(ax1.get_ylim()), min(ax2.get_ylim()), min(ax3.get_ylim())]), 
              max([max(ax1.get_ylim()), max(ax2.get_ylim()), max(ax3.get_ylim())])]
        for axa in [ax1, ax2, ax3]:
            axa.set_ylim(YL)
        
        ax1.set_ylabel('emissions / MtCO2eq (AR4)', fontweight='bold')
        fig.suptitle("Comparison NDC partnership and PIK (SSP2)\n" + iso_act + ', ' + tar_type_reclass, 
                     fontweight='bold')
        fig.subplots_adjust(top=.8, right=.87, hspace=.3)
        plt.savefig(Path(meta.path.main, 'plots', 'comparisons_with_other_data', 'comparisons_ndcpartnership', 
            'comparison_ssp2default_excllu_' + iso_act + '.png'), dpi=300)
        plt.clf()

plt.close(fig)

# %%