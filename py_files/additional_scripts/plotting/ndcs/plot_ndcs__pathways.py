# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 04/2020.
"""

# %%
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from setup_metadata import setup_metadata
import helpers_functions as hpf

# %%
meta = setup_metadata()

years_int = range(1990, 2051)
years_str = [str(xx) for xx in years_int]
years_ptw_int = range(2020, 2051)
years_ptw_str = [str(xx) for xx in years_ptw_int]
colours_condi_rge = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_condi_rge.csv'), index_col=0)
colours_tar_types = pd.read_csv(Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_ndc_types.csv'), index_col=0)
colours_tar_types.loc['baseline_emissions', :] = colours_condi_rge.loc['baseline_emissions', :]

# %%
folder = 'ndcs_20200628_2229_SSP3_typeCalc'
ssp = 'SSP3'

path_plots = Path(meta.path.main, 'plots', 'ndc_quantifications', folder)
Path(path_plots).mkdir(parents=True, exist_ok=True)

path_ndcs = Path(meta.path.output, folder)
ndc_tars = pd.read_csv(Path(path_ndcs, 'ndc_targets.csv'))
ndc_ptws_ctr = pd.read_csv(Path(path_ndcs, 'ndc_targets_pathways_per_country.csv'))
ndc_ptws_grp = pd.read_csv(Path(path_ndcs, 'ndc_targets_pathways_per_group.csv'))
ndc_ptws_chosen = pd.read_csv(Path(path_ndcs, 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
info_per_country = pd.read_csv(Path(meta.path.preprocess, 'info_per_country.csv'), index_col=0)

# %%
ptw_earth = ndc_ptws_grp.loc[
    (ndc_ptws_grp.group == 'EARTH') & 
    (ndc_ptws_grp.condi == 'emi_bau') &
    (ndc_ptws_grp.category == 'IPCM0EL'), years_str]
plt.plot(years_int, ptw_earth.values[0]/1000, color=colours_condi_rge.loc['baseline_emissions', :].to_list(), label='baseline')

for condi, rge in ['unconditional', 'worst'], ['unconditional', 'best'], \
    ['conditional', 'worst'], ['conditional', 'best']:
    
    ptw_earth = ndc_ptws_grp.loc[
        (ndc_ptws_grp.group == 'EARTH') & 
        (ndc_ptws_grp.condi == condi) &
        (ndc_ptws_grp.rge == rge) & 
        (ndc_ptws_grp.category == 'IPCM0EL'), years_ptw_str]
    plt.plot(years_ptw_int, ptw_earth.values[0]/1000, color=colours_condi_rge.loc[f'{condi}_{rge}', :].to_list(), label=f'{condi}_{rge}')

plt.plot(plt.xlim(), [0, 0], 'k', linewidth=.1)
plt.legend()
plt.ylabel('Gg CO2eq')
plt.title('Global emissions (based on national totals of Kyoto GHG)')
plt.savefig(Path(path_plots, f"{ssp}.png"), dpi=300)
plt.clf()
plt.close()

# %%
for iso3 in sorted(ndc_ptws_ctr.iso3.unique()):
    
    ptws_iso = ndc_ptws_ctr.loc[(ndc_ptws_ctr.iso3 == iso3) & (ndc_ptws_ctr.category == 'IPCM0EL'), :]
    
    for tar_type in [xx for xx in ptws_iso.tar_type_used.unique() if type(xx) == str]:
        
        ptws_tar = ptws_iso.loc[ptws_iso.tar_type_used == tar_type, :]
        
        for condi, rge in ['unconditional', 'worst'], ['unconditional', 'best'], \
            ['conditional', 'worst'], ['conditional', 'best']:
            
            lbl = '__nolabel__'
            if [condi, rge] == ['unconditional', 'worst']:
                lbl = f'{tar_type}'
            
            plt.plot(years_int, 
                ptws_tar.loc[(ptws_tar.condi == condi) & (ptws_tar.rge == rge), years_str].values[0], 
                color=colours_tar_types.loc[tar_type, :].to_list(), label=lbl)
            
        try:
            tars_single = ndc_tars.loc[(ndc_tars.iso3 == iso3) & (ndc_tars.tar_type_used == tar_type), ['taryr', 'tar_emi_exclLU']]
            for row, data in tars_single.iterrows():
                plt.plot(int(data.taryr), float(data.tar_emi_exclLU), 'o', color=colours_tar_types.loc[tar_type, :].to_list())
        except:
            pass
    
    plt.plot(plt.xlim(), [0, 0], 'k', linewidth=.1)
    plt.ylabel('Mt CO2eq')
    plt.legend()
    plt.title(f'Emissions pathways for {iso3}\n(un/conditional & best/worst)')
    plt.savefig(Path(path_plots, f"{iso3}.png"), dpi=300)
    plt.clf()

plt.close()

# %%
ptw_emi_earth = ndc_ptws_grp.loc[(ndc_ptws_grp.group == 'EARTH') & 
    (ndc_ptws_grp.condi == 'emi_bau') & (ndc_ptws_grp.category == 'IPCM0EL'), :]
ptw_pop_earth = ndc_ptws_grp.loc[(ndc_ptws_grp.group == 'EARTH') & (ndc_ptws_grp.condi == 'pop'), :]
ptw_gdp_earth = ndc_ptws_grp.loc[(ndc_ptws_grp.group == 'EARTH') & (ndc_ptws_grp.condi == 'gdp'), :]

fig = plt.figure(figsize=(7, 7))

for iso3 in sorted(ndc_ptws_ctr.iso3.unique()):
    
    axa = fig.add_subplot(1, 1, 1)
    
    for category, lnestyle in ['IPCM0EL', '-'], ['IPC0', ':']:
        
        ptws_iso = ndc_ptws_ctr.loc[(ndc_ptws_ctr.iso3 == iso3) & (ndc_ptws_ctr.category == category), :]
        
        for tar_type in [xx for xx in ptws_iso.tar_type_used.unique() if type(xx) == str]:
            
            ptws_tar = ptws_iso.loc[ptws_iso.tar_type_used == tar_type, :]
            
            for condi, rge in ['unconditional', 'worst'], ['unconditional', 'best'], \
                ['conditional', 'worst'], ['conditional', 'best']:
                
                lbl = '__nolabel__'
                if [category, condi, rge] == ['IPCM0EL', 'unconditional', 'worst']:
                    lbl = f'{tar_type}'
                
                axa.plot(years_int, 
                    ptws_tar.loc[(ptws_tar.condi == condi) & (ptws_tar.rge == rge), years_str].values[0], lnestyle,
                    color=colours_tar_types.loc[tar_type, :].to_list(), label=lbl)
                
                try:
                    axa.plot(years_int, ndc_ptws_chosen.loc[
                        (ndc_ptws_chosen.iso3 == iso3) & (ndc_ptws_chosen.category == category) &
                        (ndc_ptws_chosen.condi == condi) & (ndc_ptws_chosen.rge == rge), years_str].values[0], 'm--', linewidth=.5)
                except:
                    pass
                
            try:
                tars_single = ndc_tars.loc[(ndc_tars.iso3 == iso3) & (ndc_tars.tar_type_used == tar_type), ['taryr', 'tar_emi_exclLU', 'tar_emi_inclLU']]
                for row, data in tars_single.iterrows():
                    axa.plot(int(data.taryr), float(data.tar_emi_exclLU), 'o', color=colours_tar_types.loc[tar_type, :].to_list())
                    axa.plot(int(data.taryr), float(data.tar_emi_inclLU), '*', color=colours_tar_types.loc[tar_type, :].to_list())
            except:
                pass
    
    ptws_lu = ndc_ptws_ctr.loc[(ndc_ptws_ctr.iso3 == iso3) & (ndc_ptws_ctr.category == 'IPCMLULUCF') & 
                               (ndc_ptws_ctr.condi == 'emi_bau'), years_str]
    
    if not ptws_lu.isnull().all().all():
        lbl = 'LULUCF\n' + meta.sources.srce_to_label[info_per_country.loc[iso3, 'lulucf_source']]
    else:
        lbl = 'LULUCF'
    
    axa.plot(years_int, ptws_lu.values[0], '.', color=(0, .7, 0), label=lbl)
    
    axa.plot(plt.xlim(), [0, 0], 'k', linewidth=.1)
    
    # Mark years 2017 and 2030.
    YL = axa.get_ylim()
    XL = axa.get_xlim()
    axa.set_xlim(XL)
    axa.set_ylim(YL)
    axa.plot([2017, 2017], [YL[1] - .02*(YL[1] - YL[0]), YL[1]], 'k', linewidth=.5)
    axa.plot([2030, 2030], [YL[1] - .02*(YL[1] - YL[0]), YL[1]], 'k', linewidth=.5)
    
    axa.set_ylabel('Mt CO2eq', fontweight='bold')
    axa.set_xlabel('year', fontweight='bold')
    axa.legend(loc='center', bbox_to_anchor=(.5, -.18), ncol=3)
    axa.set_title(f'Emissions pathways for {iso3}\n(un/conditional & best/worst)\n', fontweight='bold')
    
    emi_ctr = ndc_ptws_ctr.loc[(ndc_ptws_ctr.iso3 == iso3) & (ndc_ptws_ctr.rge == 'emi_bau') &
        (ndc_ptws_ctr.category == 'IPCM0EL'), :]
    pop_ctr = ndc_ptws_ctr.loc[(ndc_ptws_ctr.iso3 == iso3) & (ndc_ptws_ctr.rge == 'pop'), :]
    gdp_ctr = ndc_ptws_ctr.loc[(ndc_ptws_ctr.iso3 == iso3) & (ndc_ptws_ctr.rge == 'gdp'), :]
    axa.text(XL[0] - .05*(XL[1] - XL[0]), YL[0] - .27*(YL[1]-YL[0]), 
        "Solid/dotted lines: national Kyoto GHG emissions excluding/including LULUCF emissions." +
        "\nDotted line in magenta: chosen pathways." + 
        "\nGlobal share in 2017 / 2030:\n    " +
        f"baseline emissions: {100*emi_ctr.loc[:, '2017'].values[0]/ptw_emi_earth.loc[:, '2017'].values[0]:.2f}% / " +
        f"{100*emi_ctr.loc[:, '2030'].values[0]/ptw_emi_earth.loc[:, '2030'].values[0]:.2f}%, " +
        f"population: {100*pop_ctr.loc[:, '2017'].values[0]/ptw_pop_earth.loc[:, '2017'].values[0]:.2f}% / " +
        f"{100*pop_ctr.loc[:, '2030'].values[0]/ptw_pop_earth.loc[:, '2030'].values[0]:.2f}%, " +
        f"GDP (PPP): {100*gdp_ctr.loc[:, '2017'].values[0]/ptw_gdp_earth.loc[:, '2017'].values[0]:.2f}% / " +
        f"{100*gdp_ctr.loc[:, '2030'].values[0]/ptw_gdp_earth.loc[:, '2030'].values[0]:.2f}%.", 
        fontsize=9, ha='left', va='top')
    
    fig.subplots_adjust(bottom=.27, left=.15)
    fig.savefig(Path(path_plots, f"{iso3}_inclLU.png"), dpi=300)
    fig.clf()

plt.close(fig)

# %%# %%