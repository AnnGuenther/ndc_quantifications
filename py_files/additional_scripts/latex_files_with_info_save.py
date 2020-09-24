# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020.
"""

# %%
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
# Get general information.

meta = setup_metadata()

path_out = Path(meta.path.main, 'latex_files')
Path(path_out).mkdir(parents=True, exist_ok=True)

tables = hpf.create_class(name='tables')
units = meta.units.default

infos_from_ndcs = pd.read_csv(Path(meta.path.preprocess, 'infos_from_ndcs.csv'), index_col=0)

tar_to_long = {
    'ABS': "Absolute Target Emissions",
    'BYT': "Base Year Target",
    'RRB': "Relative Reduction compared to BAU",
    'ARB': "Absolute Reduction compared to BAU",
    'RIT_BYT': "Relative Emissions Intensity Reduction compared to Base Year",
    'RIT_BAU': "Relative Emissions Intensity Reduction compared to BAU Emissions Intensity",
    'AIT': "Absolute Emissions Intensity Target",
    'NGT': "Non-GHG Target"}

gwps = hpf.get_gwps_for_gases('all', meta.gwps.default)
hfcs = hpf.get_members_of_basket('HFCS')
pfcs = hpf.get_members_of_basket('PFCS')

colours = {}
colours['ssps'] = pd.read_csv(
    Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_ssps.csv'), index_col=0)
colours['cats'] = pd.read_csv(
    Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_categories_ipc.csv'), index_col=0)
colours['gases'] = pd.read_csv(
    Path(meta.path.py_files, 'additional_scripts', 'plotting', 'colours', 'colours_gases.csv'), index_col=0)

# %%
# Covered sectors and gases.

cov_ndcs = pd.read_csv(Path(meta.path.preprocess, 'coverage_orig_per_gas_and_per_sector_and_combi.csv'), index_col=[0]).astype(str)
cov_used = pd.read_csv(Path(meta.path.preprocess, 'coverage_used_per_gas_and_per_sector_and_combi.csv'), index_col=[0]).astype(str)

dct = {'ndcs': cov_ndcs, 'used': cov_used}

for attr in dct.keys():
    
    # Replace yes by +, no by - and nan by /.
    act = dct[attr]
    act[act.isin(['YES', 'yes', 'Yes'])] = '+'
    act[act.isin(['NO', 'no', 'No'])] = '-'
    act[act.isin(['NAN', 'nan', 'NaN'])] = '/'

# %%
# Get SSP data (historical years == PRIMAP data).

# Emissions, GDP and POP.
# SSP for overview: SSP2.
ssp_for_overview = [xx for xx in meta.ssps.scens.long if 'SSP2' in xx][0]

tables_to_add = {
    'ssp_emi': 'KYOTOGHG_IPCM0EL_TOTAL_NET_' + ssp_for_overview + 'FILLED_PMSSPBIE',
    'ssp_gdp': 'GDPPPP_ECO_TOTAL_NET_' + ssp_for_overview + 'FILLED_PMSSPBIEMISC',
    'ssp_pop': 'POP_DEMOGR_TOTAL_NET_' + ssp_for_overview + 'FILLED_PMSSPBIEMISC'}

for tpe in tables_to_add.keys():
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', tables_to_add[tpe] + '.csv')). \
                __convert_to_baseunit__().__reindex__(index=meta.isos.EARTH)
    if tpe == 'ssp_emi':
        setattr(tables, tpe, table.__change_gwp__(meta.gwps.default))
    else:
        setattr(tables, tpe, table)

# emi/GDP, emi/capita.
tables.ssp_emi_gdp = hpf.combine_tables('divide', [tables.ssp_emi, tables.ssp_gdp])
tables.ssp_emi_pop = hpf.combine_tables('divide', [tables.ssp_emi, tables.ssp_pop])

# Global share.
for case in ['ssp_emi', 'ssp_gdp', 'ssp_pop', 'ssp_emi_gdp', 'ssp_emi_pop']:
    share = hpf.copy_table(getattr(tables, case))
    share.data = share.data.div(share.data.reindex(index=meta.isos.EARTH).sum(axis=0))
    share.unit = share.unit + ' / ' + share.unit
    setattr(tables, case + '_share', share)

# %%
# Get data per gas and category.

for gas in ['KYOTOGHG'] + meta.gases.kyotoghg:
    
    setattr(tables, 'his_' + gas, hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
        gas + '_IPCM0EL_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))
    
    if gas in meta.gases.fgases:
        table_code = gas + '_IPCM0EL_TOTAL_NET_' + meta.ssps.scens.long[1] + 'FILLED_SSPSPLIT.csv'
    else:
        table_code = gas + '_IPCM0EL_TOTAL_NET_' + meta.ssps.scens.long[1] + '_' + meta.ssps.emi['srce'] + '.csv'
    
    setattr(tables, f"SSP2_{gas}", hpf.import_table_to_class_metadata_country_year_matrix(
        Path(meta.path.preprocess, 'tables', table_code)). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

for cat in ['IPCM0EL'] + meta.categories.main.inclLU:
    setattr(tables, 'his_' + cat, hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
        'KYOTOGHG_' + cat + '_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

for ssp in meta.ssps.scens.long:
    setattr(tables, 'emi_' + ssp[:4], hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
        'KYOTOGHG_IPCM0EL_TOTAL_NET_' + ssp + 'FILLED_PMSSPBIE.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# For SSP2 get CO2 emissions.
setattr(tables, 'emi_CO2_ssp2', hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
    'CO2_IPCM0EL_TOTAL_NET_' + ssp_for_overview + 'FILLED_PMSSPBIE.csv')). \
            __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# TODO: calculate rvalues for the combinations, which entity+category does have most influence on the trend in the total emissions?

combis_ent_cat = [
    'KYOTOGHG_IPCM0EL', 
    'CO2_IPC1', 'CO2_IPC2', 'CO2_IPCMAG', 'CO2_IPC4',
    'CH4_IPC1', 'CH4_IPC2', 'CH4_IPCMAG', 'CH4_IPC4',
    'N2O_IPC1', 'N2O_IPC2', 'N2O_IPCMAG', 'N2O_IPC4',
    'FGASES_IPC2']

for combi in combis_ent_cat:
    setattr(tables, combi, hpf.import_table_to_class_metadata_country_year_matrix(
            Path(meta.path.preprocess, 'tables', combi + '_TOTAL_NET_HISTCR_PRIMAPHIST21.csv')). \
            __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

# %%
# Cumulative historical emissions.

# PRIMAP-hist 1850 to 2017.
setattr(tables, 'his_emi_all', hpf.import_table_to_class_metadata_country_year_matrix(Path(meta.path.preprocess, 'tables', 
    'KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_' + meta.primap.current_version['emi'] + '__allYears.csv')). \
                __convert_to_baseunit__().__change_gwp__(meta.gwps.default).__reindex__(index=meta.isos.EARTH))

yr_his = 2017
yr_sum_start1850 = 1850
yr_sum_start1990 = 1990
sum_start1850 = hpf.copy_table(getattr(tables, 'his_emi_all')).data.reindex(columns=range(yr_sum_start1850, yr_his+1)).sum(axis=1)
sum_start1990 = hpf.copy_table(getattr(tables, 'his_emi_all')).data.reindex(columns=range(yr_sum_start1990, yr_his+1)).sum(axis=1)

# %%
def df_to_table(table_body, caption, label, columns, hlines):
    
    table = \
        "\n \\begin{table}[htbp]" + \
        "\n \\centering" + \
        "\n \\caption{" f"{caption}" "}" + \
        "\n \\label{" f"{label}" "}" + \
        "\n \\begin{tabular}{" f"{columns}" "}"
    
    for row in range(len(hlines)):
        table += \
            "\n " + \
            " & ".join(table_body.loc[row, :].to_list()) + " \\tabularnewline " + \
            " ".join(['\\hline'] * hlines[row])
    
    table += \
        "\n \\end{tabular}" + \
        "\n \\end{table}"
    
    return table

# %%
def include_graphics(path_to_figure, caption, label, width):
    
    path_to_figure = str(path_to_figure).replace("\\", "/")
    
    figure = \
        "\n \\begin{figure}[htbp]" + \
        "\n \\centering" + \
        f"\n \\includegraphics[width={width}]" + \
        "{" f"{path_to_figure}" "}" + \
        "\n \\caption{" f"{caption}" "}" + \
        "\n \\label{" f"{label}" "}" + \
        "\n \\end{figure}"
    
    return figure

# %%
ssps_linestyle = {'SSP1': '--', 'SSP2': '-', 'SSP3': '--', 'SSP4': ':', 'SSP5': ':'}

def plot_tsNonLULUCF():
    
    fig = plt.figure(figsize=(12, 6))
    
    ax_sec = fig.add_subplot(1, 2, 1)
    ax_gas = fig.add_subplot(1, 2, 2)
    
    yrs_to_plot = range(1990, 2051)
    
    yrs_to_plot_cats = range(1990, 2018)
    cats_to_plot = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5']
    data_cats = pd.DataFrame(index=cats_to_plot, columns=yrs_to_plot_cats)
    
    for cat in cats_to_plot:
        data_cats.loc[cat, :] = getattr(tables, f"his_{cat}").data.reindex(index=[iso3]).reindex(columns=yrs_to_plot_cats).values[0]
    
    lower_lim = [0] * len(yrs_to_plot_cats)
    for cat in cats_to_plot:
        upper_lim = list(lower_lim + data_cats.loc[cat, :].values)
        ax_sec.fill_between(yrs_to_plot_cats, lower_lim, upper_lim, color=colours['cats'].loc[cat, :].values,
                            label=meta.categories.main.cat_to_sec[cat])
        lower_lim = upper_lim
            
    for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
        data_ssp = getattr(tables, f"emi_{ssp_short}")
        ax_sec.plot(yrs_to_plot, data_ssp.data.loc[iso3, yrs_to_plot], ssps_linestyle[ssp_short],
                    color=colours['ssps'].loc[ssp_long, :].to_list(), label=f"dm{ssp_short}")
    
    gases_to_plot = meta.gases.kyotoghg
    data_gases = pd.DataFrame(index=gases_to_plot, columns=yrs_to_plot)
    
    for gas in gases_to_plot:
        data_gases.loc[gas, :] = getattr(tables, f"SSP2_{gas}").data.reindex(index=[iso3]).reindex(columns=yrs_to_plot).values[0]
    
    lower_lim = [0] * len(yrs_to_plot)
    for gas in gases_to_plot:
        upper_lim = list(lower_lim + data_gases.loc[gas, :].values)
        ax_gas.fill_between(yrs_to_plot, lower_lim, upper_lim, color=colours['gases'].loc[gas, :].values,
                            label=meta.gases.gas_to_label[gas])
        lower_lim = upper_lim
    
    # SSP2
    data_ssp = getattr(tables, "emi_SSP2")
    ax_gas.plot(yrs_to_plot, data_ssp.data.loc[iso3, yrs_to_plot], ssps_linestyle['SSP2'],
                color=colours['ssps'].loc[meta.ssps.scens.long[1], :].to_list(), label='dmSSP2')
    
    YL = [0, ax_sec.get_ylim()[1]]
    XL = [yrs_to_plot[0], yrs_to_plot[-1]]
    
    for axa, label in zip([ax_sec, ax_gas], ['(a) Per main sector', '(b) Per Kyoto GHG']):
        axa.set_xlim(XL)
        axa.set_ylim(YL)
        axa.text(XL[0] + .05 * np.diff(XL), YL[1] - .05 * np.diff(YL), label,
            fontweight='bold', ha='left', va='top')
        axa.set_xlabel('year', fontweight='bold')
    
    ax_sec.set_ylabel("national emission (exclLU)" f"\n{units_iso['emi']['label']}",
        fontweight='bold')
    
    ax_sec.legend()
    ax_gas.legend()
    
    path_to_png = Path(path_to_tex_files, f'ts_emi_exclLU_{iso3}.png')
    plt.savefig(path_to_png, dpi=300)
    path_to_pdf = str(path_to_png).replace('.png', '.pdf')
    plt.savefig(path_to_pdf, dpi=300)
    hpf.crop_pdf(path_to_pdf)
    plt.clf()
    plt.close(fig)

#        fig.subplots_adjust(left=.1, right=.95, bottom=.2)
#        hpf.set_ticks_scientific_notation(ax2, 'y')
#        hpf.put_labels_to_subplots(ax1, ax2)

# %%
def text_to_latex_file():
    
    # %%
    ctr = meta.isos.iso3_to_shortname[iso3]
    
    path_to_tex_files = Path(path_out, iso3)
    Path(path_to_tex_files).mkdir(parents=True, exist_ok=True)
    
    # %%
    # Get the tables for iso3 and change the units to 'nice looking units'.
    
    # Get highest emissions in emi_SSPs.
    emi_min, emi_max = 0, 0
    for tablename in ['emi_SSP1', 'emi_SSP2', 'emi_SSP3', 'emi_SSP4', 'emi_SSP5']:
        data = getattr(tables, tablename).__subset__(isos=[iso3]).data
        emi_min = min([emi_min, data.min(axis=1).values[0]])
        emi_max = max([emi_max, data.max(axis=1).values[0]])
    
    units_iso = {}
    units_iso['emi'] = {}
    units_iso['emi']['unit'], units_iso['emi']['multiplier'] = hpf.get_conversion_to_nice_unit([emi_min, emi_max], 
        getattr(tables, 'emi_SSP1').unit) # Have all the same unit.
    
    # %%
    for tablename in ['ssp_emi_gdp', 'ssp_emi_pop', 'ssp_gdp', 'ssp_pop']:
        table = getattr(tables, tablename).__subset__(isos=[iso3])
        tpe = tablename.replace('ssp_', '')
        units_iso[tpe] = {}
        units_iso[tpe]['unit'], units_iso[tpe]['multiplier'] = \
            hpf.get_conversion_to_nice_unit(table.data, table.unit)
    
    tables_iso = hpf.create_class(name='tables_iso')
    for tablename in hpf.get_all_attributes_of_class(tables):
        table = getattr(tables, tablename).__subset__(isos=[iso3])
        
        if 'share' not in tablename:
            
            if table.family == 'emi/gdp':
                unit_act = units_iso['emi_gdp']
            elif table.family == 'emi/pop':
                unit_act = units_iso['emi_pop']
            else:
                unit_act = units_iso[table.family]
            
            table.data = table.data * unit_act['multiplier']
            table.unit = unit_act['unit']
        
        setattr(tables_iso, tablename, table)
    
    # %%
    sum_start1850_iso = sum_start1850.loc[iso3] * units_iso['emi']['multiplier']
    sum_start1850_share_iso = 100. * sum_start1850.loc[iso3] / sum_start1850.reindex(index=meta.isos.EARTH).sum()
    sum_start1990_iso = sum_start1990.loc[iso3] * units_iso['emi']['multiplier']
    sum_start1990_share_iso = 100. * sum_start1990.loc[iso3] / sum_start1990.reindex(index=meta.isos.EARTH).sum()
    
    # %%
    # Which gas / sector was the driver in the recent emissions trend.
    
    # Get the historical entity + sector that has the closest slope to 1 for
    # a linear regression between KYOTOGHG_IPCM0EL and emissions per sector+gas combi.
    combi_slopes = pd.DataFrame(index=combis_ent_cat[1:], columns=['slope', 'rvalue', 'emi_yr_his', 'share_yr_his'])
    yrs_corr = list(range(2010, yr_his+1))
    
    for combi in combis_ent_cat[1:]:
        
        try:
            xx = getattr(tables, 'KYOTOGHG_IPCM0EL').data.loc[iso3, yrs_corr] * units_iso['emi']['multiplier']
            yy = getattr(tables, combi).data.loc[iso3, yrs_corr] * units_iso['emi']['multiplier']
            xx, yy, linreg = hpf.linear_regression(xx, yy)
            combi_slopes.loc[combi, 'rvalue'] = linreg.rvalue
            combi_slopes.loc[combi, 'slope'] = linreg.slope
            combi_slopes.loc[combi, 'emi_yr_his'] = yy[-1]
            combi_slopes.loc[combi, 'share_yr_his'] = 100. * yy[-1] / xx[-1]
        except:
            pass
    
    sec_to_label = meta.sectors.main.sec_to_label
    combi_for_trend = combi_slopes.slope.sort_values(ascending=False)
    lim_slope = .2
    if any(combi_for_trend > lim_slope):
        
        combi_for_trend = combi_for_trend[combi_for_trend > lim_slope]
        trend_gas, trend_sec, trend_gas_txt, trend_sec_txt = [], [], [], []
        for ind in combi_for_trend.index:
            
            gas, cat = ind.split('_')
            trend_gas += [gas]
            trend_sec += [cat]
            
            trend_gas_txt += [meta.gases.gas_to_label[gas]]
            trend_sec_txt += [sec_to_label[meta.categories.main.cat_to_sec[cat]]]
        
        txt_emi_trend = f"\nThe trend in total emissions is mostly driven by "
        
        if len(set(trend_gas)) == 1: # 1 gas
            if len(set(trend_sec)) == 1: # 1 sector
                txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, "
                nr_trend = 1
            elif len(set(trend_sec)) == 2: # 2 sectors
                txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} and " + \
                    f"{trend_sec_txt[1]} sectors, "
                nr_trend = 2
            elif len(set(trend_sec)) > 2: # 3 sectors
                txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]}, " + \
                    f"{trend_sec_txt[1]}, and {trend_sec_txt[2]} sectors, "
                nr_trend = 3
        
        elif len(set(trend_gas)) == 2: # 2 gases
            if len(set(trend_sec)) == 1: # 2 gases, 1 sector
                txt_emi_trend += f"{trend_gas_txt[0]} and {trend_gas_txt[1]} emissions from the {trend_sec_txt[0]} sector, "
                nr_trend = 2
            elif len(set(trend_sec)) == 2: # 2 gases, 2 sectors
                txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, " + \
                    f"and {trend_gas_txt[1]} emissions from the {trend_sec_txt[1]} sector, "
                nr_trend = 2
            elif len(set(trend_sec)) > 2: # 2 gases, 3 sectors.
                txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, " + \
                    f"{trend_gas_txt[1]} emissions from the {trend_sec_txt[1]} sector, " + \
                    f"and {trend_gas_txt[2]} emissions from the {trend_sec_txt[2]} sector, "
                nr_trend = 3
        
        elif len(set(trend_gas)) > 2: # 3 gases
            if len(set(trend_sec)) == 1: # 3 gases, 1 sector
                txt_emi_trend += f"{trend_gas_txt[0]}, {trend_gas_txt[1]} and {trend_gas_txt[2]} " + \
                    f"emissions from the {trend_sec_txt[0]} sector, "
                nr_trend = 3
            elif len(set(trend_sec)) == 2: # 3 gases, 2 sectors
                txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, " + \
                    f"{trend_gas_txt[1]} emissions from the {trend_sec_txt[1]} sector, " + \
                    f"and {trend_gas_txt[2]} emissions from the {trend_sec_txt[2]} sector, "
                nr_trend = 3
            elif len(set(trend_sec)) > 2: # 3 gases, 3 sectors
                txt_emi_trend += f"{trend_gas_txt[0]} emissions from the {trend_sec_txt[0]} sector, " + \
                    f"{trend_gas_txt[1]} emissions from the {trend_sec_txt[1]} sector, " + \
                    f"and {trend_gas_txt[2]} emissions from the {trend_sec_txt[2]} sector, "
                nr_trend = 3
        
        if nr_trend == 1:
            number = hpf.num_to_str_one_non_zero_decimal(
                combi_slopes.loc[trend_gas[0] + '_' + trend_sec[0], 'share_yr_his'].sum())
            txt_emi_trend += f"which contributed {number}\% "
        elif nr_trend == 2:
            number1 = hpf.num_to_str_one_non_zero_decimal(
                combi_slopes.loc[trend_gas[0] + '_' + trend_sec[0], 'share_yr_his'].sum())
            number2 = hpf.num_to_str_one_non_zero_decimal(
                combi_slopes.loc[trend_gas[1] + '_' + trend_sec[1], 'share_yr_his'].sum())
            txt_emi_trend += f"which contributed {number1}\% and {number2}\% "
        elif nr_trend == 3:
            number1 = hpf.num_to_str_one_non_zero_decimal(
                combi_slopes.loc[trend_gas[0] + '_' + trend_sec[0], 'share_yr_his'].sum())
            number2 = hpf.num_to_str_one_non_zero_decimal(
                combi_slopes.loc[trend_gas[1] + '_' + trend_sec[1], 'share_yr_his'].sum())
            number3 = hpf.num_to_str_one_non_zero_decimal(
                combi_slopes.loc[trend_gas[2] + '_' + trend_sec[2], 'share_yr_his'].sum())
            txt_emi_trend += f"which contributed {number1}\%, {number2}\%, and {number3}\% "
        
        txt_emi_trend += f"to {ctr}'s 2017 emissions."
        txt_emi_trend += "\footnote{" + \
            "Analysis based on the correlations between total national emissions (excl. LULUCF) " + \
            "versus the emissions of the combinations of main-sectors \& the gases CO$_2$, CH$_4$, N$_2$O and F-gases. " + \
            f"Only data from {yrs_corr[0]} to {yrs_corr[-1]} are assessed. " + \
            "The (up to) three gas \& sector combinations are chosen for which the slope of the " + \
            f"regression line to the correlated values exceeds {lim_slope}." + \
            "}\n"
    
    else:
        txt_emi_trend = ""

    # %%
    # Nicer unit lables.
    units_iso['emi']['label'] = units_iso['emi']['unit'].replace('CO2', 'CO$_2$')
    units_iso['gdp']['label'] = units_iso['gdp']['unit'].replace('2011GKD', ' 2011 GK\$')
    units_iso['emi_gdp']['label'] = units_iso['emi_gdp']['unit'].replace('CO2', 'CO$_2$').replace('2011GKD', ' 2011 GK\$')
    units_iso['pop']['label'] = units_iso['pop']['unit'].replace('Pers', ' Pers')
    units_iso['emi_pop']['label'] = units_iso['emi_pop']['unit'].replace('CO2', 'CO$_2$').replace('Pers', ' Pers')
    
    # %% For Overview
    
    # Table with total emissions, share of global emissions and ranking (2017 & 2030).
    # Also for GDP, population and emi/GDP, emi/capita.
    # SSP2.
    
    overview_table = pd.DataFrame(
        columns=['unit', 'tot_his', 'share_his', 'rank_his', 'tot_fut', 'share_fut', 'rank_fut'],
        index=['emi', 'gdp', 'emi_gdp', 'pop', 'emi_pop'])
    yr_fut = 2030
    
    for tpe in overview_table.index:
        for when, yr in ['his', yr_his], ['fut', yr_fut]:
            overview_table.loc[tpe, 'tot_' + when] = \
                getattr(tables_iso, 'ssp_' + tpe).data.loc[iso3, yr]
            overview_table.loc[tpe, 'share_' + when] = \
                getattr(tables_iso, 'ssp_' + tpe + '_share').data.loc[iso3, yr] * 100.
            overview_table.loc[tpe, 'rank_' + when] = \
                '{:.0f}'.format(getattr(tables, 'ssp_' + tpe + '_share').data.reindex(index=meta.isos.EARTH).reindex(columns=[yr]). \
                    rank(method='dense', ascending=False).loc[iso3, yr])
        
        # Put in the units.
        unit_act = getattr(tables_iso, 'ssp_' + tpe).unit
        unit_act = (unit_act.replace('CO2', 'CO$_2$') if 'CO2' in unit_act else unit_act)
        unit_act = (unit_act.replace('2011GKD', ' 2011~GK\$') if '2011GKD' in unit_act else unit_act)
        unit_act = (unit_act.replace('Pers', ' Pers') if 'Pers' in unit_act else unit_act)
        overview_table.loc[tpe, 'unit'] = unit_act
    
    # Table of strings.
    mapping = {'emi': 'Emissions', 'gdp': 'GDP (PPP)', 'emi_gdp': 'Emissions per GDP (PPP)',
               'pop': 'Population', 'emi_pop': 'Emissions per capita'}
    overview_table_str = pd.DataFrame()
    row = 0
    for tpe in mapping.keys():
        overview_table_str.loc[row, 'Year'] = str(yr_his)
        overview_table_str.loc[row+1, 'Year'] = str(yr_fut)
        overview_table_str.loc[row, 'Total'] = hpf.num_to_str_one_non_zero_decimal(
            overview_table.loc[tpe, 'tot_his'])
        overview_table_str.loc[row+1, 'Total'] = hpf.num_to_str_one_non_zero_decimal(
            overview_table.loc[tpe, 'tot_fut'])
        overview_table_str.loc[[row, row+1], 'Unit'] = overview_table.loc[tpe, 'unit']
        overview_table_str.loc[row, 'Glob. share'] = hpf.num_to_str_one_non_zero_decimal(
            overview_table.loc[tpe, 'share_his']) + "\%"
        overview_table_str.loc[row+1, 'Glob. share'] = hpf.num_to_str_one_non_zero_decimal(
            overview_table.loc[tpe, 'share_fut']) + "\%"
        overview_table_str.loc[row, 'Rank'] = \
            '{:}'.format(overview_table.loc[tpe, 'rank_his'])
        overview_table_str.loc[row+1, 'Rank'] = \
            '{:}'.format(overview_table.loc[tpe, 'rank_fut'])
        row += 2
    
    overview_table_str.insert(0, '', 
        ['Emissions', '', 'GDP', '', 'Emissions', 'per GDP', 'Population', '', 'Emissions', 'per capita'])
    
    # %%
    gases_table = pd.DataFrame(index=['KYOTOGHG'] + meta.gases.kyotoghg, columns=['emi', 'share'])
    for gas in gases_table.index:
        gases_table.loc[gas, 'emi'] = getattr(tables_iso, 'his_' + gas).data.loc[iso3, yr_his]
        gases_table.loc[gas, 'share'] = 100. * gases_table.loc[gas, 'emi'] / gases_table.loc['KYOTOGHG', 'emi']
    
    cats_table = pd.DataFrame(index=['IPCM0EL'] + meta.categories.main.exclLU, columns=['emi', 'share'])
    for cat in cats_table.index:
        cats_table.loc[cat, 'emi'] = getattr(tables_iso, 'his_' + cat).data.loc[iso3, yr_his]
        cats_table.loc[cat, 'share'] = 100. * cats_table.loc[cat, 'emi'] / cats_table.loc['IPCM0EL', 'emi']
    
    ssps_table = pd.DataFrame(index=meta.ssps.scens.short, columns=[2017, 2030, 2050])
    for yr in ssps_table.columns:
        for ssp in ssps_table.index:
            ssps_table.loc[ssp, yr] = getattr(tables_iso, 'emi_' + ssp).data.loc[iso3, yr]
    
    # %%
    tot_emi_his = hpf.num_to_str_one_non_zero_decimal(
        cats_table.loc['IPCM0EL', 'emi'])
    
    highest_sec_his_1st = sec_to_label[meta.categories.main.cat_to_sec[
        cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False).index[0]]]
    highest_sec_his_share_1st = hpf.num_to_str_one_non_zero_decimal(
        cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False)[0])
    highest_sec_his_2nd = sec_to_label[meta.categories.main.cat_to_sec[
        cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False).index[1]]]
    highest_sec_his_share_2nd = hpf.num_to_str_one_non_zero_decimal(
        cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False)[1])
    highest_sec_his_3rd = sec_to_label[meta.categories.main.cat_to_sec[
        cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False).index[2]]]
    highest_sec_his_share_3rd = hpf.num_to_str_one_non_zero_decimal(
        cats_table.loc[meta.categories.main.exclLU, 'share'].sort_values(ascending=False)[2])
    
    highest_gas_his_1st = meta.gases.gas_to_label[gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False).index[0]]
    highest_gas_his_share_1st = hpf.num_to_str_one_non_zero_decimal(
        gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False)[0])
    highest_gas_his_2nd = meta.gases.gas_to_label[gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False).index[1]]
    highest_gas_his_share_2nd = hpf.num_to_str_one_non_zero_decimal(
        gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False)[1])
    highest_gas_his_3rd = meta.gases.gas_to_label[gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False).index[2]]
    highest_gas_his_share_3rd = hpf.num_to_str_one_non_zero_decimal(
        gases_table.loc[meta.gases.kyotoghg, 'share'].sort_values(ascending=False)[2])
    
    share_fgases_his = hpf.num_to_str_one_non_zero_decimal(
        gases_table.loc[meta.gases.fgases, 'share'].sum())
    
    ssp2_2030 = hpf.num_to_str_one_non_zero_decimal(
        ssps_table.loc[ssp_for_overview[:4], 2030])
    ssp2_2030_pc = hpf.num_to_str_one_non_zero_decimal(
        100. * (ssps_table.loc[ssp_for_overview[:4], 2030] / ssps_table.loc[ssp_for_overview[:4], 2017] - 1))
    
    # %%
    # Share of CO2 in 2030 (SSP2).
    
    yr = 2030
    number = hpf.num_to_str_one_non_zero_decimal(
        100. * getattr(tables, 'emi_CO2_ssp2').data.loc[iso3, yr] / getattr(tables, 'ssp_emi').data.loc[iso3, yr])
    share_co2_2030 = f"{number}\%"
    yr = 2050
    number = hpf.num_to_str_one_non_zero_decimal(
        100. * getattr(tables, 'emi_CO2_ssp2').data.loc[iso3, yr] / getattr(tables, 'ssp_emi').data.loc[iso3, yr])
    share_co2_2050 = f"{number}\%"
    
    # %%
    # Calculate the linear regressions for gdp, pop and emi/gdp and emi/pop for 2010 to most recent value.
    # SSP2.
    
    yrs_linreg = range(2010, 2018)
    _, _, gdp_linreg = hpf.linear_regression(yrs_linreg, tables_iso.ssp_gdp.data.loc[iso3, yrs_linreg])
    _, _, emi_gdp_linreg = hpf.linear_regression(yrs_linreg, tables_iso.ssp_emi_gdp.data.loc[iso3, yrs_linreg])
    _, _, pop_linreg = hpf.linear_regression(yrs_linreg, tables_iso.ssp_pop.data.loc[iso3, yrs_linreg])
    _, _, emi_pop_linreg = hpf.linear_regression(yrs_linreg, tables_iso.ssp_emi_pop.data.loc[iso3, yrs_linreg])
    
    # %%
    # Table with covered sectors and gases.
    
    cats = ['IPC1', 'IPC2', 'IPCMAG', 'IPCMLULUCF', 'IPC4', 'IPC5']
    table_combis = pd.DataFrame(index=['NDCs', 'Adapted'] + cats,
        columns=['NDCs', 'Adapted'] + meta.gases.kyotoghg)
    
    for case in [xx for xx in cov_used.columns if '_' in xx]:
        
        ent, cat = case.split('_')
        table_combis.loc[cat, ent] = cov_used.loc[iso3, case]
    
    table_combis.loc[cats, 'NDCs'] = \
        cov_ndcs.loc[iso3, meta.categories.main.inclLU].values
    table_combis.loc[cats, 'Adapted'] = \
        cov_used.loc[iso3, meta.categories.main.inclLU].values
    table_combis.loc['NDCs', meta.gases.kyotoghg] = \
        cov_ndcs.loc[iso3, :].reindex(index=list(meta.gases.kyotoghg)).values
    table_combis.loc['Adapted', meta.gases.kyotoghg] = \
        cov_used.loc[iso3, :].reindex(index=list(meta.gases.kyotoghg)).values
    table_combis[table_combis.isnull()] = ''
    table_combis.index = \
        ['NDCs', 'Adapted'] + [sec_to_label[meta.categories.main.cat_to_sec[xx]] 
        for xx in table_combis.index[2:]]
    table_combis.insert(0, '', table_combis.index.values)
    
    # %%
    plot_tsNonLULUCF()
    
    # %%
    # To have the caption of Tables spanning the entire width.
    txt = \
        "\\documentclass[12pt]{article}" + \
        "\n\n %%%" + \
        "\n \\usepackage[utf8]{inputenc}" + \
        "\n \\usepackage{graphicx}" + \
        "\n \\usepackage{geometry}\geometry{a4paper, total={170mm,257mm}, left=20mm, top=20mm}"
    
    # %%
    txt += "\n\n \\title{" f"{ctr}" ": information on national emissions, population and GDP, and mitigation targets}"

    txt += \
        "\n\n %%%" + \
        "\n \\begin{document}"
    
    txt += \
        "\n\n \\maketitle" + \
        "\n\n %%%" + \
        "\n \\noindent \\textbf{Authors:} \\newline" + \
        "\n \\indent Annika Guenther$^{1}$ \\newline" + \
        "\n \\indent Johannes Guetschow$^{1}$ \\newline" + \
        "\n \\noindent \\textbf{Affiliations:} \\newline" + \
        "\n \\indent 1. Potsdam Institute for Climate Impact Research, Germany \\newline" + \
        "\n \\noindent \\textbf{DOI:} [to be added] \\newline"
    
    # %% Overview
    
    txt += \
        "\n\n %%%" + \
        "\n \\section{Overview and key messages}" + \
        "\n \\label{sec:overview}"
    ##
    txt += \
        f"\n\n In {yr_his}, the national emissions of {ctr} were {tot_emi_his}~{units_iso['emi']['label']} " + \
        f"(GWP {meta.gwps.default}" + \
        "\\footnote{" "\\textit{Global Warming Potential (GWP)}" ": we use GWP values from the IPCC " + \
        ("4$^{th}$ Assessment Report (AR4). " if meta.gwps.default == 'AR4' else "") + \
        ("2$^{nd}$ Assessment Report (SAR). " if meta.gwps.default in ['SAR', 'AR2'] else "") + \
        "\n They reflect the forcing potential of one kilogram of a gas' emissions in comparison " + \
        "to one kilogram of CO$_2$ (GWP$_{CO2}$ = 1). " + \
        "\n The GWPs used here correspond to a 100-yr period. " + \
        f"\n For CH$_4$ the AR4 GWP is {gwps['CH4'] :.0f}, for N$_2$O it is {gwps['N2O'] :.0f}" + \
        f", for SF$_6$ it is {gwps['SF6'] :.0f}, and for NF$_3$ it is {gwps['NF3'] :.0f}. " + \
        f"\n For the basket of HFC-gases it ranges between {gwps[hfcs].min() :.0f} and {gwps[hfcs].max() :.0f}" + \
        f", and for PFCs between {gwps.reindex(index=pfcs).min() :.0f} and {gwps.reindex(index=pfcs).max() :.0f}. " + \
        "\n When emissions of several GHGs are assessed, their emissions are weighted by their respective GWP " + \
        "and presented in CO$_2$ equivalents (CO$_2$eq)." "} " + \
        ", excluding LULUCF" + \
        "\\footnote{" "\\textit{LULUCF}" ": Land use, land-use change and forestry. " + \
        "\n Emissions from LULUCF are excluded throughout the document, unless stated otherwise." "} " + \
        "and emissions from bunkers fuels). "
    ##
    txt += \
        f"\n The highest share was emitted in the {highest_sec_his_1st} sector, followed by " + \
        f"{highest_sec_his_2nd} and {highest_sec_his_3rd}" + \
        f" ({highest_sec_his_share_1st}\%, {highest_sec_his_share_2nd}\%, and {highest_sec_his_share_3rd}\%, respectively). "
    ##
    txt += \
        f"\n The Kyoto GHG" + \
        "\\footnote{" "\\textit{Kyoto GHG}" " basket (GreenHouse Gas): carbon dioxide (CO$_2$), methane (CH$_4$), " + \
        "nitrous oxide (N$_2$O), hydrofluorocarbons (HFCs), perfluorocarbons (PFCs), " + \
        "sulfur hexafluoride (SF$_6$), and nitrogen trifluoride (NF$_3$)." "}" + \
        f" with the highest emissions in {yr_his} (in terms of CO$_2$ equivalent) was " + \
        f"{highest_gas_his_1st}, constituting " + ("as much as " if float(highest_gas_his_share_1st) > 70 else " ") + \
        f"{highest_gas_his_share_1st}\% of the national emissions. "
    ##
    txt += \
        f"\n Second largest contributor was {highest_gas_his_2nd}, followed by {highest_gas_his_3rd}" + \
        f" ({highest_gas_his_share_2nd}\%, and {highest_gas_his_share_3rd}\%, respectively). "
    ##
    txt += \
        "\n The total of F-gases" + \
        "\\footnote{" "\\textit{F-gases}" " (fluorinated gases): basket of HFCs, PFCs, " + \
        "SF$_6$ and NF$_3$. Some f-gases have very long atmospheric lifetimes and high Global Warming Potentials." "} " + \
        ("only " if float(share_fgases_his) < 7 else "") + f"represented {share_fgases_his}\%. " + \
        "\n Even though contributing a rather little part of GHG emissions in terms of CO$_2$ equivalents, " + \
        "F-gases are important due to their high GWPs and atmospheric lifetimes."
    ##
    txt += \
        f"\n Following the downscaled {ssp_for_overview[:4]} pathway emissions, in 2030 {ctr} is estimated to emit " + \
        f"{ssp2_2030}~{units_iso['emi']['label']}, which would constitute "
    ##
    if float(ssp2_2030_pc) > 0.:
        txt += ("an increase" if float(ssp2_2030_pc) < 10 else "a substantial increase")
    elif float(ssp2_2030_pc) < 0.:
        txt += ("a decrease" if float(ssp2_2030_pc) > -10 else "a substantial decrease")
    elif float(ssp2_2030_pc) == 0:
        txt += "no real change"
    
    txt += f" of {ssp2_2030_pc}\% compared to {yr_his}. "
    
    ##
    number1 = hpf.num_to_str_one_non_zero_decimal(
        ssps_table.loc[:, 2030].min())
    number2 = hpf.num_to_str_one_non_zero_decimal(
        ssps_table.loc[:, 2030].max())
    number3 = hpf.num_to_str_one_non_zero_decimal(
        ssps_table.loc[:, 2050].min())
    number4 = hpf.num_to_str_one_non_zero_decimal(
        ssps_table.loc[:, 2050].max())
    txt += \
        f"\n The pathways SSP1 to~5 show a range of {number1}" + \
        f"--{number2}~{units_iso['emi']['label']} in 2030, and " + \
        f"{number3}--{number4}~{units_iso['emi']['label']} in 2050."
    
    # TODO: If CO2 is the highest share, don't repeat the pc share.
    
    number1 = hpf.num_to_str_one_non_zero_decimal(
        overview_table.loc['emi', 'share_his'])
    number2 = hpf.num_to_str_one_non_zero_decimal(
        overview_table.loc['emi', 'share_fut'])
    txt += \
        "\n As to be seen in Table~\\ref{tab:overview}, the global share of " + \
        f"{ctr}'s emissions in {yr_his} was " + \
        f"{number1}\%, while in {yr_fut} the global share is estimated to " + \
        ('increase to ' if overview_table.loc['emi', 'share_fut'] > overview_table.loc['emi', 'share_his'] else 'decrease to ') + \
        f"{number2}\%."
    ##
    txt += \
        f"\n In {yr_his}, the country's global rank in terms of total emissions per GDP (PPP) was " + \
        f"{overview_table.loc['emi_gdp', 'rank_his']}, and " + \
        f"{overview_table.loc['emi_pop', 'rank_his']} regarding the per-capita emissions (" + \
        f"{overview_table.loc['emi_gdp', 'rank_fut']} and {overview_table.loc['emi_pop', 'rank_fut']} in {yr_fut})."
    ##
    # Table {tab:overview}.
    label = "tab:overview"
    columns = "l || l r l r r"
    hlines = [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
    caption = \
        "Total emissions, GDP (PPP) and population for {ctr}, together with the emissions per GDP (PPP) " + \
        f"and emissions per capita (all for {yr_his} and {yr_fut}). " + \
        "\n Additionally, the global share and its rank are displayed. " + \
        f"\n All non-historic values are from the downscaled {ssp_for_overview[:4]} pathways."
    table_body = pd.DataFrame(index=range(len(hlines)), columns=range(6))
    table_body.loc[0, :] = [f"\\bfseries {xx}" for xx in overview_table_str.columns.to_list()]
    table_body.loc[1:, :] = overview_table_str.values
    table_body.loc[1:, 0] = [f"\\bfseries {xx}" for xx in table_body.loc[1:, 0].to_list()]
    txt += df_to_table(table_body, caption, label, columns, hlines)
            
    # TODO: Something about NDC and target.
    
    # %% Emissions
    txt += \
        "\n\n %%%" + \
        "\n \\section{Emissions}" + \
        "\n \\label{sec:emissions}"
    
    # %% Non-LULUCF emissions
    txt += \
        "\n\n %%%" + \
        "\n \\section{Non-LULUCF emissions}" + \
        "\n \\label{sec:nonLULUCF}"
    
    # Historical share.
    number = hpf.num_to_str_one_non_zero_decimal(sum_start1850_share_iso)
    txt += \
        f"\n\nIn terms of accumulated historical emissions, {ctr}" + \
        f" contributed to the emissions from {yr_sum_start1850} to {yr_his} by {number}\%. "
    number1 = hpf.num_to_str_one_non_zero_decimal(sum_start1990_share_iso)
    number2 = hpf.num_to_str_one_non_zero_decimal(sum_start1850_iso)
    number3 = hpf.num_to_str_one_non_zero_decimal(sum_start1990_iso)
    txt += \
        ("However, when " if abs(sum_start1990_share_iso - sum_start1850_share_iso) > 5 else "When ") + \
        f"only accounting for the years {yr_sum_start1990} to {yr_his} its share " + \
        ("increases " if sum_start1990_share_iso > sum_start1850_share_iso else "decreases ") + \
        f"to {number1}\% ({yr_sum_start1850} to {yr_his}: " + \
        f"{number2}~{units_iso['emi']['label']}, and {yr_sum_start1990} to {yr_his}: " + \
        f"{number3}~{units_iso['emi']['label']})."
    
    txt += txt_emi_trend
    
    txt += \
        f"\nThe total CO$_2$ emissions are expected to be {share_co2_2030} " + \
        f"of Kyoto GHG emissions in 2030 ({share_co2_2050} in 2050; SSP2)."
    # Downscaled by Johannes.
    # TODO: Also show the ratio between gases for SSPs?
    
    # TODO: Check the correlations and the slope of regressions between emi_tot and emi_gas_sec.
    
    # Check if the ratios per gas are constant in the future and if they are the same for the different SSPs:
    # They are not constant and are not the same for the SSPs.
        
    # Historical emissions.
    path_to_figure = Path(meta.path.main, 'plots', 'time_series', 'emi_his_and_fut', f'emi_{iso3}_stacked.png')
    caption = \
        "'Stacked' timeseries of historical emissions per main-sector (a) and Kyoto GHG (b). " + \
        "Emissions from LULUCF are not considered."
    txt += include_graphics(path_to_figure, caption, "fig:tsEmi", "\\textwidth")
        
    # TODO: Maybe get the linear regressions of the different emissions time series (and share)
    # and check which ones increase/decrease most strongly.
    
    # TODO: The total emissions are most notably influenced by the emissions from sector + gas (see correlation emitot & emisec or emigas).
    # TODO: Johannes includes the following in his plots (1850 to now):
    #sectors = {'IPC1A', 'IPC1B', 'IPC2', 'IPC3A', 'IPCMAGELV', 'IPC4', 'IPC5'};
    #gases = {'CO2', 'CH4', 'N2O', 'FGASESAR4'};
    
    # %% LULUCF emissions
    txt += \
        "\n\n %%%" + \
        "\n \\subsection{Emissions from LULUCF}" + \
        "\n \\label{sec:emiLULUCF}"
    
    path_to_figure = Path(meta.path.main, 'plots', 'time_series', 'lulucf', f'lulucf_{iso3}.png')
    caption = \
        "Timeseries of emissions from LULUCF (sum over CO$_2$, CH$_4$ and N$_2$O) as available from different data-sources. " + \
        f"Indicated in pink is the timeseries used in our assessment of {ctr}'s NDC (if needed). " + \
        "The timeseries were inter- and extrapolated with constant values to fill data gaps. " + \
        "The not-filled data are shown as circles, while the filled timeseries are shown as solid lines."
    txt += include_graphics(path_to_figure, caption, "fig:tsLULUCF", "\\textwidth")
    
    # TODO: Only plot it for historical years, as it is kept constant afterwards there is nothing to see.
    # TODO: FAO2019 does not have circles but only a line, as the KYOTOGHG is the sum over CO2, CH4 and N2O ...
    
    # %% Socioeconomic data
    txt += \
        "\n\n %%%" + \
        "\n \\section{Socioeconomic data}" + \
        "\n \\label{sec:socioEco}"
    
    path_to_figure = Path(meta.path.main, 'plots', 'time_series', f'socioeco', f'socioeco_{iso3}.png')
    caption = \
        "Timeseries of GDP (PPP) (a \& b) and population (c \& d), and KyotoGHG\_IPCM0EL emissions " + \
        "per GDP (PPP) or per capita (b \& d)."
    txt += include_graphics(path_to_figure, caption, "fig:tsSocioEco", "\\textwidth")
    
    # Historical data.
    gdp_trend = ('positive' if gdp_linreg.slope > 0. else 'negative')
    emi_gdp_trend = ('positive' if emi_gdp_linreg.slope > 0. else 'negative')
    pop_trend = ('positive' if pop_linreg.slope > 0. else 'negative')
    emi_pop_trend = ('positive' if emi_pop_linreg.slope > 0. else 'negative')
    txt += \
        "\n\n As presented in Fig.~\\ref{fig:tsSocioEco}, " f"{ctr}'s GDP (PPP) showed " + \
        ('an increase ' if gdp_trend == 'positive' else 'a decrease ') + \
        "over the last years, and the emissions per GDP (PPP) had " + \
        ("a similar trend. " if emi_gdp_trend == 'positive' else "an opposite trend. ")
    txt += \
        "\n In recent years, the population " + \
        ("increased, " if pop_trend == 'positive' else "decreased, ") + \
        ("and " if (pop_trend == 'positive' and emi_pop_trend == 'positive') else "while ") + \
        "the per-capita emissions " + ("were on the rise. " if emi_gdp_linreg.slope > 0 else "dropped. ")
    
    # Future data.
    # EMI per GDP: de-coupled?
    yrs_fut = range(2017, 2051)
    yrs_fut_str = [str(xx) for xx in yrs_fut]
    yr_of_max = tables_iso.ssp_gdp.data.loc[iso3, yrs_fut].idxmax()
    txt += f"\n Following {ssp_for_overview[:4]}, the GDP (PPP) is projected to "
    txt += \
        (f"increase after {yrs_fut_str[0]} and to drop again before {yrs_fut_str[-1]}. " 
        if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
        (f"increase towards {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[-1] else "") + \
        (f"drop towards {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[0] else "")
    yr_of_max = tables_iso.ssp_emi_gdp.data.loc[iso3, yrs_fut].idxmax()
    txt += \
        "\n The emissions per GDP (PPP) are estimated to " + \
        (f"rise after {yrs_fut_str[0]} and to decrease again before {yrs_fut_str[-1]}. " 
        if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
        (f"rise towards {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[-1] else "") + \
        (f"decrease towars {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[0] else "")
    yr_of_max = tables_iso.ssp_pop.data.loc[iso3, yrs_fut].idxmax()
    txt += \
        f"\n {ctr}'s population is assumed to " + \
        (f"grow after {yrs_fut_str[0]} and to diminish again before {yrs_fut_str[-1]}" 
        if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
        (f"grow towards {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[-1] else "") + \
        (f"diminish towars {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[0] else "")
    yr_of_max = tables_iso.ssp_emi_pop.data.loc[iso3, yrs_fut].idxmax()
    txt += \
        ", and the per-capita emissions are expected to " + \
        (f"increase after {yrs_fut_str[0]} and to decline again before {yrs_fut_str[-1]}. " 
        if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
        (f"increase towards {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[-1] else "") + \
        ("decline towars {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[0] else "")
        
    # TODO: Maybe include some 'nice' words.
    
    # %% Mitigation targets
    txt += \
        "\n\n %%%" + \
        "\n \\section{Mitigation targets (NDCs)}" + \
        "\n \\label{sec:mitiTars}"
    
    # TODO
    
    #txt += f"\n\n{ctr} has a " + infos_from_ndcs
    #tar_to_long
    
    # %% Covered emissions
    txt += \
        "\n\n %%%" + \
        "\n \\subsection{Covered share of emissions}" + \
        "\n \\label{sec:pcCov}"
    
    # TODO: Rules for pccov.
    # TODO: Only include the coverage stuff if it has an (I)NDC.
    txt += \
        (f"\n\n As {ctr} is part of the NDC by the European Union (28), the coverage of the EU28 NDC is used." 
         if iso3 in meta.isos.EU28 else "")
    
    path_to_figure = Path(meta.path.main, 'plots', 'time_series', 
        str(meta.path.pc_cov).split('\\')[-1], f'pccov_{iso3}_CORR.png')
    caption = \
        f"Timeseries of {ctr}'s national emissions (excl. LULUCF) and the share of " + \
        f"emissions that is assumed to be covered by {ctr}'s mitigation target. " + \
        "\n Timeseries are shown for SSP1 to~5."
    txt += include_graphics(path_to_figure, caption, "fig:tsPcCov", "\\textwidth")
    
    # Tables with coverage.
    label = "tab:coveredSectorsGases"
    caption = \
        "Coverage from NDC and 'Adapted' as used to calculated \%cov. " + \
        "If either the sector or gas is not covered, the emissions from this " + \
        "sector-gas combination are counted as not-covered ('-'). " + \
        "Else the emissions are counted as covered ('+'). (/) means that no information was given."
    columns = "l || c c | c c c c c c c"
    hlines = [2, 0, 1, 0, 0, 0, 0, 0, 0]
    table_body = pd.DataFrame(index=range(len(hlines)), columns=range(10))
    table_body.loc[0, :] = [f"\\bfseries {xx}" for xx in table_combis.columns.to_list()]
    table_body.loc[1:, :] = table_combis.values
    table_body.loc[1:, 0] = [f"\\bfseries {xx}" for xx in table_body.loc[1:, 0].to_list()]
    txt += df_to_table(table_body, caption, label, columns, hlines)
    
    # TODO: in brackets include the share of total emissions that combi stands for (2017).
    # TODO: Table with emissions per main-sector and per gas, and per combi?
    
    # TODO: Emissions target. Table with assumptions. All target years, etc.
    # TODO: Targets: plots like in UBA.
    path_to_figure = 'C:/Users/annikag/primap/other_things/UBA/plots/Plot_Emissions_And_Target_NewSSPs_VNM_WithIPPU.png'
    caption = "Example Viet Nam."
    txt += include_graphics(path_to_figure, caption, "fig:miti", "\\textwidth")
    
    # %% Data sources and references
    txt += \
        "\n\n %%%" + \
        "\n \\section{Data sources and references}" + \
        "\n \\label{sec:dataSourcesRefs}"
    
    txt += \
        f"\n\n All emissions are in CO$_2$ equivalents following the Global Warming Potential from " + \
        "the IPCC 4$^{th}$ Assessment Report (GWP AR4)."
    
    txt += \
        f"\n\n {meta.sources.srce_to_label[meta.primap.current_version['emi']]}: " + \
        "emissions from PRIMAP-hist are data from the country reported data priority scenario (HISTCR)."
    
    # TODO: which data are needed in for the quantification of that country, and are they available.
    
    # %%
    txt += \
        "\n\n %%%" + \
        "\n \\end{document}"
    
    # %%
    # Write text to .tex file.
    path_tex_file = Path(path_to_tex_files, iso3 + '.tex')
    tex_file = open(path_tex_file, 'w', encoding='utf8')
    
    print(txt, file=tex_file)
    tex_file.close()
    
    # %%
    # Make a pdf.
    os.chdir(path_to_tex_files)
    os.system("pdflatex " f"{path_tex_file}")
    os.chdir(meta.path.py_files)
    
    # %%
    # TODO: Include information from info_per_country where needed.
    # TODO: Come up with rules to be able to use expressions such as "differs strongly", "increase/decrease substantially",
    # "major share/contributions", etc.
    # TODO: Do not include empty plots.
    # TODO: Global page: include the graphics I had done on the data needed.
    
    # PIK_colors = [227 114 34; 142 144 143] / 255;

# %%
for iso3 in ['ARG']:#meta.isos.EARTH:
    text_to_latex_file()

# %%