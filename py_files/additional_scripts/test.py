# %%
def text_to_latex_file():
    
    # %%
    def df_to_table(table_body, caption, label, columns, hlines, **kwargs):
        
        table = \
            "\n\n \\begin{table}[H]" + \
            (kwargs['fontsize'] if 'fontsize' in kwargs.keys() else '') + \
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
            "\n\n \\begin{figure}[H]" + \
            "\n \\centering" + \
            f"\n \\includegraphics[width={width}]" + \
            "{" f"{path_to_figure}" "}" + \
            "\n \\caption{" f"{caption}" "}" + \
            "\n \\label{" f"{label}" "}" + \
            "\n \\end{figure}"
        
        return figure
    
    # %%
    def plot_ts_nonLULUCF():
        
        fig = plt.figure(figsize=(12, 6))
        
        ax_sec = fig.add_subplot(1, 2, 1)
        ax_gas = fig.add_subplot(1, 2, 2)
        
        yrs_to_plot = range(1990, 2051)
        
        yrs_to_plot_cats = range(1990, 2018)
        cats_to_plot = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5']
        data_cats = pd.DataFrame(index=cats_to_plot, columns=yrs_to_plot_cats)
        
        for cat in cats_to_plot:
            data_cats.loc[cat, :] = getattr(tables_iso, f"KYOTOGHG_{cat}").data.reindex(index=[iso3]).reindex(columns=yrs_to_plot_cats).values[0]
        
        lower_lim = [0] * len(yrs_to_plot_cats)
        for cat in cats_to_plot:
            upper_lim = list(lower_lim + data_cats.loc[cat, :].values)
            ax_sec.fill_between(yrs_to_plot_cats, lower_lim, upper_lim, color=colours['cats'].loc[cat, :].values,
                                label=meta.categories.main.cat_to_sec[cat])
            lower_lim = upper_lim
                
        for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
            data_ssp = getattr(tables_iso, f"{ssp_short}_emi")
            ax_sec.plot(yrs_to_plot, data_ssp.data.loc[iso3, yrs_to_plot], ssps_linestyle[ssp_short],
                        color=colours['ssps'].loc[ssp_long, :].to_list(), label=f"dm{ssp_short}",
                        linewidth=linewdth)
        
        gases_to_plot = meta.gases.kyotoghg
        data_gases = pd.DataFrame(index=gases_to_plot, columns=yrs_to_plot)
        
        for gas in gases_to_plot:
            data_gases.loc[gas, :] = getattr(tables_iso, f"SSP2_{gas}").data.reindex(index=[iso3]).reindex(columns=yrs_to_plot).values[0]
        
        lower_lim = [0] * len(yrs_to_plot)
        for gas in gases_to_plot:
            upper_lim = list(lower_lim + data_gases.loc[gas, :].values)
            ax_gas.fill_between(yrs_to_plot, lower_lim, upper_lim, color=colours['gases'].loc[gas, :].values,
                                label=meta.gases.gas_to_label[gas])
            lower_lim = upper_lim
        
        # SSP2
        data_ssp = getattr(tables_iso, "SSP2_emi")
        ax_gas.plot(yrs_to_plot, data_ssp.data.loc[iso3, yrs_to_plot], ssps_linestyle['SSP2'],
                    color=colours['ssps'].loc[meta.ssps.scens.long[1], :].to_list(), label='dmSSP2',
                    linewidth=linewdth)
        
        YL = [0, ax_sec.get_ylim()[1]]
        XL = [yrs_to_plot[0], yrs_to_plot[-1]]
        
        for axa, label in zip([ax_sec, ax_gas], ['(a) Per main sector', '(b) Per Kyoto GHG']):
            axa.set_xlim(XL)
            axa.set_ylim(YL)
            axa.text(XL[0] + .05 * np.diff(XL), YL[1] - .05 * np.diff(YL), label,
                fontweight='bold', ha='left', va='top')
            axa.set_xlabel('year', fontweight='bold')
        
        ax_sec.set_ylabel("national emissions (exclLU)" f"\n{units_iso['emi']['label']}",
            fontweight='bold')
        
        ax_sec.legend(loc='center', bbox_to_anchor=(.5, -.25), ncol=4)
        ax_gas.legend(loc='center', bbox_to_anchor=(.5, -.25), ncol=4)
        
        fig.subplots_adjust(left=.1, bottom=.25, right=.95, top=.95)
        path_to_png = Path(path_to_tex_files, f'ts_emi_exclLU_{iso3}.png')
        plt.savefig(path_to_png, dpi=300)
        plt.clf()
        plt.close(fig)
    
    # %%
    def plot_ts_gdp_pop():
        
        fig = plt.figure(figsize=(12, 9))
        
        ax_gdp = fig.add_subplot(2, 2, 1)
        ax_emi_gdp = fig.add_subplot(2, 2, 2)
        ax_pop = fig.add_subplot(2, 2, 3)
        ax_emi_pop = fig.add_subplot(2, 2, 4)
        
        yrs_to_plot = range(1990, 2051)
        
        for axa in [ax_gdp, ax_emi_gdp, ax_pop, ax_emi_pop]:
            axa.plot(yrs_to_plot, [0]*len(yrs_to_plot), 'k:', linewidth=.5)
        
        for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
            
            for axa, what in zip([ax_gdp, ax_emi_gdp, ax_pop, ax_emi_pop], ['gdp', 'emi_gdp', 'pop', 'emi_pop']):
                axa.plot(yrs_to_plot, getattr(tables_iso, f"{ssp_short}_{what}").data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
                            linestyle=ssps_linestyle[ssp_short], color=colours['ssps'].loc[ssp_long, :].to_list(),
                            label=f"dm{ssp_short}", linewidth=linewdth)
        
        ax_emi_gdp.plot(yrs_to_plot, getattr(tables_iso, f"CO2_IPC1_emi_gdp").data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
                'k-.', label=f"Energy CO$_2$", linewidth=linewdth)
        ax_emi_pop.plot(yrs_to_plot, getattr(tables_iso, f"CO2_IPC1_emi_pop").data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
                'k-.', label=f"Energy CO$_2$", linewidth=linewdth)
        
        XL = [yrs_to_plot[0], yrs_to_plot[-1]]
        for axa, what, label in \
            zip([ax_gdp, ax_emi_gdp, ax_pop, ax_emi_pop], 
                ['gdp', 'emi_gdp', 'pop', 'emi_pop'],
                ['GDP', 'Emissions per GDP', 'Population', 'Emissions per capita']):
            axa.set_xlim(XL)
            ylabel = units_iso[what]['label']
            axa.set_ylabel(f"{label}" f"\n{ylabel}", fontweight='bold')
            axa.set_xlabel("year", fontweight='bold')
        
        ax_emi_pop.legend(loc='center', bbox_to_anchor=(-.11, -.28), ncol=6)
        
        hpf.put_labels_to_subplots(ax_gdp, ax_emi_gdp, ax_pop, ax_emi_pop)
        
        fig.subplots_adjust(left=.1, bottom=.14, right=.95, top=.95, hspace=.2, wspace=.3)
        path_to_png = Path(path_to_tex_files, f'ts_gdp_pop_{iso3}.png')
        plt.savefig(path_to_png, dpi=300)
        plt.clf()
        plt.close(fig)
    
    # %%
    def plot_ts_LULUCF():
        
        fig = plt.figure(figsize=(12, 5))
        ax_lu = fig.add_subplot(1, 1, 1)
        
        yrs_to_plot = range(1990, 2021)
        
        ax_lu.plot(yrs_to_plot, [0]*len(yrs_to_plot), 'k:', linewidth=.5)
        
        for srce in meta.lulucf.source_prioritisation:
            
            mark = '<'
            if 'CRF' in srce:
                mark = '*'
            elif 'FAO' in srce:
                mark = 's'
            elif 'EDGAR' in srce:
                mark = 'v'
            elif 'BUR' in srce:
                mark = 'p'
            
            ax_lu.plot(yrs_to_plot, getattr(tables_iso, f'LULUCF_{srce}').data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
                       marker=mark, markersize=markersze, linestyle=':', color=colours['lulucf'].loc[srce, :],
                       label=meta.sources.srce_to_label[srce], linewidth=linewdth)
        
        ax_lu.plot(yrs_to_plot, getattr(tables_iso, 'LULUCF_CHOSEN').data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
                   marker='o', markersize=.5*markersze, linestyle='', color=colours['lulucf'].loc['CHOSEN', :],
                   label='Chosen data', linewidth=linewdth)
        
        ax_lu.set_xlim([yrs_to_plot[0], yrs_to_plot[-1]])
        ax_lu.set_ylabel("emissions (onylLU)" f"\n{units_iso['emi']['label']}", fontweight='bold')
        ax_lu.set_xlabel('year', fontweight='bold')
        ax_lu.legend(loc='center', bbox_to_anchor=(1.13, .5))
        
        fig.subplots_adjust(left=.1, bottom=.1, right=.8, top=.95)
        path_to_png = Path(path_to_tex_files, f'ts_emi_onlyLU_{iso3}.png')
        plt.savefig(path_to_png, dpi=300)
        plt.clf()
        plt.close(fig)
    
    # %%
    def plot_ts_pc_cov():
        
        fig = plt.figure(figsize=(12, 4))
        
        ax_ts = fig.add_subplot(1, 2, 1)
        ax_corr = fig.add_subplot(1, 2, 2)
        
        yrs_to_plot = range(1990, 2031)
        yrs_corr = range(2010, 2018)
        
        ax_ts.set_xlim([yrs_to_plot[0], yrs_to_plot[-1]])
        ax_ts.set_ylim([-1, 101])
        
        for ssp_short, ssp_long in zip(meta.ssps.scens.short, meta.ssps.scens.long):
            
            ax_ts.plot(yrs_to_plot, 100. * getattr(tables_iso, f"{ssp_short}_pc_cov").data.reindex(index=[iso3], columns=yrs_to_plot).values[0],
                linestyle=ssps_linestyle[ssp_short], color=colours['ssps'].loc[ssp_long, :].to_list(),
                label=f"dm{ssp_short}", linewidth=linewdth)
            
            for markersize, marker, yrs in zip([.5*markersze, markersze], ['o', 's'], [yrs_to_plot, yrs_corr]):
                ax_corr.scatter(
                    getattr(tables_iso, f"{ssp_short}_emi").data.reindex(index=[iso3], columns=yrs).values[0],
                    getattr(tables_iso, f"{ssp_short}_emi_cov").data.reindex(index=[iso3], columns=yrs).values[0],
                    markersize, marker=marker, facecolor=colours['ssps'].loc[ssp_long, :].to_list())
        
        YL = [0, ax_corr.get_xlim()[-1]]
        ax_corr.set_xlim(YL)
        ax_corr.set_ylim(YL)
        
        ax_ts.set_xlabel("year", fontweight='bold')
        ax_ts.set_ylabel("%cov" "\n%", fontweight='bold')
        ax_corr.set_xlabel("national emissions" f"\n{units_iso['emi']['label']}", fontweight='bold')
        ax_corr.set_ylabel("covered emissions" f"\n{units_iso['emi']['label']}", fontweight='bold')
        
        ax_ts.legend(loc='center', bbox_to_anchor=(2.5, .5))
        hpf.put_labels_to_subplots(ax_ts, ax_corr)
        
        fig.subplots_adjust(left=.1, bottom=.15, right=.85, top=.95, wspace=.25)
        path_to_png = Path(path_to_tex_files, f'ts_pc_cov_{iso3}.png')
        plt.savefig(path_to_png, dpi=300)
        plt.clf()
        plt.close(fig)
    
    # %%
    def plot_ndcs():
        
        yrs_to_plot = range(1990, 2031)
        yrs_to_plot_str = [str(xx) for xx in yrs_to_plot]
        
        fig = plt.figure(figsize=(12, 4))
        
        ax_ts = fig.add_subplot(1, 2, 1)
        ax_vert = fig.add_subplot(1, 2, 2)
        
        ax_ts.plot(yrs_to_plot, [0]*len(yrs_to_plot), 'k:', linewidth=.5)
        
        for prio, line in \
            ['prio_NDCs', '--'], \
            ['prio_SSPs', ':']:
            
            what = 'coverage_100'
            ssp = 'SSP2'
            color_ssp = colours['ssps'].loc[ssp2_long, :]
            
            data_act = ndc_quantis_ptws[prio][what][ssp]
            data_act = data_act.loc[
                (data_act.iso3 == iso3) &
                (data_act.rge.isin(['best', 'worst'])), yrs_to_plot_str]
            if len(data_act.index) != 4:
                print(f"Warning for {iso3}: the length of data_act in plot_ndcs() is "
                      f"{len(data_act.index)} instead of 4!")
            ax_ts.plot(yrs_to_plot, data_act.min(), linestyle=line, color=color_ssp)
            ax_ts.plot(yrs_to_plot, data_act.max(), linestyle=line, color=color_ssp)
            ax_ts.fill_between(
                yrs_to_plot, data_act.min(), data_act.max(), color=color_ssp, alpha=.2)
        
        count = 0
        vert_lines = []
        
        for ssp_short, ssp_long in \
            zip(meta.ssps.scens.short, meta.ssps.scens.long):
                    
            color_ssp = colours['ssps'].loc[ssp_long, :]
            
            for prio in ['prio_NDCs', 'prio_SSPs']:
            
                for what in ndc_quantis_ptws['prio_SSPs'].keys():
                    
                    data_act = ndc_quantis_ptws[prio][what][ssp_short]
                    data_act = data_act.loc[
                        (data_act.iso3 == iso3) & (data_act.rge.isin(['best', 'worst'])), '2030']
                    if len(data_act.index) != 4:
                        print(f"Warning for {iso3}: the length of data_act in plot_ndcs() is "
                              f"{len(data_act.index)} instead of 4!")
                    ax_vert.plot([count] * 4, data_act, marker='.', markersize=3, color=color_ssp)
                    
                    count += 1
                    
                    if what == list(ndc_quantis_ptws['prio_SSPs'].keys())[-1]:
                        count += 1
                        vert_lines += [count]
        
        ax_vert.plot(ax_vert.get_xlim(), [0, 0], 'k:', linewidth=.5)
        
        YL = [min(ax_ts.get_ylim()[0], ax_vert.get_ylim()[0]),
              max(ax_ts.get_ylim()[1], ax_vert.get_ylim()[1])]
        ax_ts.set_ylim(YL)
        ax_vert.set_ylim(YL)
        
        for vert_line in vert_lines[:-1]:
            ax_vert.plot([vert_line-1, vert_line-1], YL, 'k:', linewidth=.5)
        
        ax_vert.set_xticks([])
        
        ax_ts.set_xlabel('year', fontweight='bold')
        ax_ts.set_ylabel('emissions' f"\nMt CO$_2$eq AR4", fontweight='bold')
        ax_vert.set_ylabel('emissions' f"\nMt CO$_2$eq AR4", fontweight='bold')
        
        fig.subplots_adjust(left=.1, bottom=.1, right=.95, top=.95, wspace=.25)
        path_to_png = Path(path_to_tex_files, f'ts_ndcs_quantis_{iso3}.png')
        plt.savefig(path_to_png, dpi=300)
        plt.clf()
        plt.close(fig)
    
    # %%
    #path_to_pdf = str(path_to_png).replace('.png', '.pdf')
    #plt.savefig(path_to_pdf, dpi=300)
    #hpf.crop_pdf(path_to_pdf)
    #hpf.set_ticks_scientific_notation(ax2, 'y')
    #hpf.put_labels_to_subplots(ax1, ax2)
    
    # %%
    ctr = meta.isos.iso3_to_shortname[iso3].replace("&", "\&")
    
    path_to_tex_files = Path(path_out, iso3)
    Path(path_to_tex_files).mkdir(parents=True, exist_ok=True)
    
    # %%
    # Get the tables for iso3 and change the units to 'nice looking units'.
    
    # Get highest emissions in SSPs_emi.
    emi_min, emi_max = 0, 0
    for tablename in [f"{xx}_emi" for xx in meta.ssps.scens.short]:
        data = getattr(tables, tablename).__subset__(isos=[iso3]).data
        emi_min = min([emi_min, data.min(axis=1).values[0]])
        emi_max = max([emi_max, data.max(axis=1).values[0]])
    
    units_iso = {}
    units_iso['emi'] = {}
    units_iso['emi']['unit'], units_iso['emi']['multiplier'] = hpf.get_conversion_to_nice_unit([emi_min, emi_max], 
        getattr(tables, 'SSP1_emi').unit) # Have all the same unit.
    
    for tablename in ['SSP2_emi_gdp', 'SSP2_emi_pop', 'SSP2_gdp', 'SSP2_pop']:
        table = getattr(tables, tablename).__subset__(isos=[iso3])
        tpe = tablename.replace('SSP2_', '')
        units_iso[tpe] = {}
        units_iso[tpe]['unit'], units_iso[tpe]['multiplier'] = \
            hpf.get_conversion_to_nice_unit(table.data, table.unit)
    
    # %%
    # Get the table entries for iso3 and convert the units.
    tables_iso = hpf.create_class(name='tables_iso')
    tables_iso_df = pd.DataFrame()
    
    for tablename in hpf.get_all_attributes_of_class(tables):
        
        table = getattr(tables, tablename).__subset__(isos=[iso3])
        
        if ('share' not in tablename) and ('pc_cov' not in tablename):
            
            if table.family == 'emi/gdp':
                unit_act = units_iso['emi_gdp']
            
            elif table.family == 'emi/pop':
                unit_act = units_iso['emi_pop']
            
            else:
                unit_act = units_iso[table.family]
            
            table.data = table.data * unit_act['multiplier']
            table.unit = unit_act['unit']
        
        setattr(tables_iso, tablename, table)
        
        # TODO: not efficient.
        if tablename != 'emi_his_all':
            
            for attr in hpf.get_all_attributes_of_class(table):
                if attr == 'data':
                    for yr in table.data.columns:
                        tables_iso_df.loc[table.tablename, yr] = table.data.loc[iso3, yr]
                else:
                    tables_iso_df.loc[table.tablename, attr] = getattr(table, attr)
    
    # Write data to csv-file.
    tables_iso_df_cols_yrs = [xx for xx in tables_iso_df.columns if type(xx) == int]
    tables_iso_df_cols_attrs = [xx for xx in tables_iso_df.columns if type(xx) == str]
    tables_iso_df.loc[:, tables_iso_df_cols_attrs + tables_iso_df_cols_yrs]. \
        to_csv(Path(path_to_tex_files, f'data_{iso3}.csv'))
    
    if not tables_iso_df.loc['KYOTOGHG_IPCM0EL_TOTAL_NET_HISTCR_PRIMAPHIST21', range(1990, 2018)].isnull().all():
        
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
            
            txt_emi_trend = f"\n The trend in total emissions is mostly driven by "
            
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
            txt_emi_trend += \
                "\\footnote{" + \
                "Analysis based on the correlations between total national emissions (exclLU) " + \
                "versus the emissions of the combinations of main-sectors \& the gases " + \
                "CO$_2$, CH$_4$, N$_2$O and F-gases. " + \
                f"\n Only data from {yrs_corr[0]} to {yrs_corr[-1]} are assessed. " + \
                "\n The (up to) three gas \& sector combinations are chosen for which the slope of the " + \
                f"regression line to the correlated values exceeds {lim_slope}." + \
                "}"
        
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
                    getattr(tables_iso, 'SSP2_' + tpe).data.loc[iso3, yr]
                overview_table.loc[tpe, 'share_' + when] = \
                    getattr(tables_iso, 'SSP2_' + tpe + '_share').data.loc[iso3, yr] * 100.
                overview_table.loc[tpe, 'rank_' + when] = \
                    '{:.0f}'.format(getattr(tables, 'SSP2_' + tpe + '_share').data.reindex(index=meta.isos.EARTH).reindex(columns=[yr]). \
                        rank(method='dense', ascending=False).loc[iso3, yr])
            
            # Put in the units.
            unit_act = getattr(tables_iso, 'SSP2_' + tpe).unit
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
            gases_table.loc[gas, 'emi'] = getattr(tables_iso, f"{gas}_IPCM0EL").data.loc[iso3, yr_his]
            gases_table.loc[gas, 'share'] = 100. * gases_table.loc[gas, 'emi'] / gases_table.loc['KYOTOGHG', 'emi']
        
        cats_table = pd.DataFrame(index=['IPCM0EL'] + meta.categories.main.exclLU, columns=['emi', 'share'])
        for cat in cats_table.index:
            cats_table.loc[cat, 'emi'] = getattr(tables_iso, f"KYOTOGHG_{cat}").data.loc[iso3, yr_his]
            cats_table.loc[cat, 'share'] = 100. * cats_table.loc[cat, 'emi'] / cats_table.loc['IPCM0EL', 'emi']
        
        ssps_table = pd.DataFrame(index=meta.ssps.scens.short, columns=[2017, 2030, 2050])
        for yr in ssps_table.columns:
            for ssp in ssps_table.index:
                ssps_table.loc[ssp, yr] = getattr(tables_iso, f"{ssp}_emi").data.loc[iso3, yr]
        
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
            ssps_table.loc[ssp2_short, 2030])
        ssp2_2030_pc = hpf.num_to_str_one_non_zero_decimal(
            100. * (ssps_table.loc[ssp2_short, 2030] / ssps_table.loc[ssp2_short, 2017] - 1))
        
        # %%
        # Share of CO2 in 2030 (SSP2).
        
        yr = 2030
        number = hpf.num_to_str_one_non_zero_decimal(
            100. * getattr(tables, 'SSP2_CO2').data.loc[iso3, yr] / getattr(tables, 'SSP2_emi').data.loc[iso3, yr])
        share_co2_2030 = f"{number}\%"
        yr = 2050
        number = hpf.num_to_str_one_non_zero_decimal(
            100. * getattr(tables, 'SSP2_CO2').data.loc[iso3, yr] / getattr(tables, 'SSP2_emi').data.loc[iso3, yr])
        share_co2_2050 = f"{number}\%"
        
        # %%
        # Calculate the linear regressions for gdp, pop and emi/gdp and emi/pop for 2010 to most recent value.
        # SSP2.
        
        yrs_linreg = range(2010, 2018)
        _, _, gdp_linreg = hpf.linear_regression(yrs_linreg, tables_iso.SSP2_gdp.data.loc[iso3, yrs_linreg])
        _, _, emi_gdp_linreg = hpf.linear_regression(yrs_linreg, tables_iso.SSP2_emi_gdp.data.loc[iso3, yrs_linreg])
        _, _, pop_linreg = hpf.linear_regression(yrs_linreg, tables_iso.SSP2_pop.data.loc[iso3, yrs_linreg])
        _, _, emi_pop_linreg = hpf.linear_regression(yrs_linreg, tables_iso.SSP2_emi_pop.data.loc[iso3, yrs_linreg])
        
        # %%
        # Table with covered sectors and gases.
        
        cats = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5']
        table_combis = pd.DataFrame(index=['NDCs', 'Adap.'] + cats,
            columns=['NDCs', 'Adap.'] + meta.gases.kyotoghg)
        
        for case in [xx for xx in cov_used.columns if '_' in xx]:
            if 'LULUCF' not in case:
                
                ent, cat = case.split('_')
                table_combis.loc[cat, ent] = cov_used.loc[iso3, case]
        
        table_combis.loc[cats, 'NDCs'] = \
            cov_ndcs.loc[iso3, cats].values
        table_combis.loc[cats, 'Adap.'] = \
            cov_used.loc[iso3, cats].values
        table_combis.loc['NDCs', meta.gases.kyotoghg] = \
            cov_ndcs.loc[iso3, :].reindex(index=list(meta.gases.kyotoghg)).values
        table_combis.loc['Adap.', meta.gases.kyotoghg] = \
            cov_used.loc[iso3, :].reindex(index=list(meta.gases.kyotoghg)).values
        
        # Add the information on emissions per sector / gas / combi, and print the covered ones as bold.
        # Print the emissions and the share in national emissions (exclLU).
        
        table_combis_emis = pd.DataFrame(index=cats + ['Total'], columns=meta.gases.kyotoghg + ['Total'])
        table_combis_emis.loc['Total', 'Total'] = getattr(tables_iso, 'KYOTOGHG_IPCM0EL').data.loc[iso3, yr_his]
        
        for cat in cats:
            # Total emissions.
            table_combis_emis.loc[cat, 'Total'] = getattr(tables_iso, f'KYOTOGHG_{cat}').data.loc[iso3, yr_his]
            for gas in meta.gases.main:
                # Per gas-sector combi.
                table_combis_emis.loc[cat, gas] = getattr(tables_iso, f'{gas}_{cat}').data.loc[iso3, yr_his]
        
        for gas in meta.gases.fgases:
            table_combis_emis.loc['IPC2', gas] = getattr(tables_iso, f'{gas}_IPCM0EL').data.loc[iso3, yr_his]
        
        for gas in meta.gases.kyotoghg:
            table_combis_emis.loc['Total', gas] = getattr(tables_iso, f'{gas}_IPCM0EL').data.loc[iso3, yr_his]
        
        table_combis_shares = 100. * table_combis_emis / table_combis_emis.loc['Total', 'Total']
        
        # Put data together (1 decimal).
        table_combis_str = table_combis.loc[['NDCs', 'Adap.'], :]
        for row in table_combis_emis.index:
            
            if row != 'Total':
                table_combis_str.loc[row, 'NDCs'] = table_combis.loc[row, 'NDCs']
                table_combis_str.loc[row, 'Adap.'] = table_combis.loc[row, 'Adap.']
            
            for col in table_combis_emis.columns:
                
                fontweight = ''
                if (row != 'Total' and col != 'Total'):                
                    if table_combis.loc[row, col] == '+':
                        fontweight = '\\bfseries '
                
                share = hpf.num_to_str_one_non_zero_decimal(table_combis_shares.loc[row, col], maximal=2)
                table_combis_str.loc[row, col] = f"{fontweight}{share}\%"
        
        table_combis_str[table_combis_str == '\\bfseries nan\%'] = '\\bfseries /'
        table_combis_str[table_combis_str == 'nan\%'] = '/'
        
        table_combis_str[table_combis_str == '+'] = '\\bfseries +'
        
        table_combis_str[table_combis_str.isnull()] = ''
        table_combis_str.index = [sec_to_label[meta.categories.main.cat_to_sec[xx]] 
            if xx in meta.categories.main.cat_to_sec.keys() else xx
            for xx in table_combis_str.index]
        table_combis_str.insert(0, '', table_combis_str.index.values)
        table_combis_str.columns = table_combis_str.columns.to_list()[:3] + \
            [meta.gases.gas_to_label[xx] for xx in table_combis_str.columns.to_list()[3:-1]] + ['Total']
        
        # %%
        ndc_iso3 = infos_from_ndcs.loc[iso3, :]
        has_ndc = ndc_iso3['NDC_INDC']
        type_main = ndc_iso3['TYPE_ORIG']
        type_reclass = ndc_iso3['TYPE_CALC']
        
        # %%
        linewdth = 2
        markersze = 10
        
        plot_ts_nonLULUCF()
        plot_ts_LULUCF()
        plot_ts_gdp_pop()
        
        # %%
        txt = \
            "\\documentclass[12pt]{article}" + \
            "\n\n %%%" + \
            "\n \\usepackage[utf8]{inputenc}" + \
            "\n \\usepackage{graphicx}" + \
            "\n \\usepackage{xcolor}" + \
            "\n \\usepackage{hyperref}" + \
            "\n \\hypersetup{colorlinks, linkcolor = black, citecolor = black, filecolor = black, " + \
            "urlcolor = [RGB]{227, 114, 34}}" + \
            "\n \\usepackage{float}" + \
            "\n \\usepackage{geometry}\geometry{a4paper, total={170mm,257mm}, left=20mm, top=20mm}" + \
            "\n\n \\definecolor{PIKorange}{RGB}{227, 114, 34}" + \
            "\n \\definecolor{PIKgray}{RGB}{142, 144, 143}"
        
        # %%
        txt += \
            "\n\n \\title{" " \\bfseries \\color{PIKorange} " + \
            f"{ctr}: information on national emissions, population and GDP, and mitigation targets" "}"
    
        txt += \
            "\n\n %%%" + \
            "\n\n \\begin{document}"
        
        txt += \
            "\n\n \\maketitle" + \
            "\n\n %%%" + \
            "\n \\noindent \\textbf{Authors:} \\newline" + \
            "\n \\indent Annika Guenther$^{1}$ \\newline" + \
            "\n \\indent Johannes Guetschow$^{1}$ \\newline" + \
            "\n \\noindent \\textbf{Affiliations:} \\newline" + \
            "\n \\indent 1. Potsdam Institute for Climate Impact Research, Germany \\newline" + \
            "\n \\noindent \\textbf{DOI:} [to be added] \\newline"
        
        # %%
        txt += \
            "\n\n \\textbf{TODO}" + \
            "\n \\begin{itemize}" + \
            "\n \\item Table with info on target (main and reclass; emissions from NDC; target quantis + plot)." + \
            "\n \\item GWP: NDC emissions coverted from AR2 to AR4 by national conversion factor (2010--2017, PRIMAP-hist v2.1)." + \
            "\n \\item References!" + \
            "\n \\end{itemize}"
        
        # %% Non-LULUCF emissions and socio-economic data.
        txt += \
            "\n\n \\newpage %%%" + \
            "\n \\section{Emissions and socio-economic data}" + \
            "\n \\label{sec:nonLULUCFSocioEco}"
        
        number1 = hpf.num_to_str_one_non_zero_decimal(
            overview_table.loc['emi', 'share_his'])
        number2 = hpf.num_to_str_one_non_zero_decimal(
            overview_table.loc['emi', 'share_fut'])
        
        if number1 == number2:
            txt_act1, txt_act2 = "and", "stay at a similar level"
        else:
            txt_act1, txt_act2 = "while", \
                ("increase to" if float(number2) > float(number1) else "decrease to") + f" {number2}\%"
        
        txt += \
            f"\n With national emissions of {tot_emi_his}~{units_iso['emi']['label']}, {ctr} contributed " + \
            f"{number1}\% to global emissions in {yr_his}, " + \
            f"{txt_act1} in {yr_fut} its share is estimated to {txt_act2} " "(Table~\\ref{tab:overview})." + \
            f"\n The estimates for {yr_fut} are based on the downscaled {ssp2_short}" + \
            f" Middle of the Road marker scenario (dm{ssp2_short}), in which {ctr} is estimated to emit " + \
            f"{ssp2_2030}~{units_iso['emi']['label']} in {yr_fut}." + \
            f"\n That change in emissions would constitute "
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
            f"\n The pathways dmSSP1--5 show a range of {number1}" + \
            f"--{number2}~{units_iso['emi']['label']} in 2030, and " + \
            f"{number3}--{number4}~{units_iso['emi']['label']} in 2050."
        ##
        if ((f"{overview_table.loc['emi_gdp', 'rank_his']}" != "nan")
            and (f"{overview_table.loc['emi_pop', 'rank_his']}" != "nan")):
            txt_act = \
                "\n The country's global rank in terms of total emissions per unit of GDP was " + \
                    f"{overview_table.loc['emi_gdp', 'rank_his']} in {yr_his}, and " + \
                    f"{overview_table.loc['emi_pop', 'rank_his']} regarding the per-capita emissions"
            txt_act += \
                (f" ({overview_table.loc['emi_gdp', 'rank_fut']} and {overview_table.loc['emi_pop', 'rank_fut']} in {yr_fut})."
                 if f"{overview_table.loc['emi_gdp', 'rank_fut']}" != "nan" else ".")
        elif f"{overview_table.loc['emi_gdp', 'rank_his']}" != "nan":
            txt_act = \
                "\n The country's global rank in terms of total emissions per unit of GDP was " + \
                    f"{overview_table.loc['emi_gdp', 'rank_his']} in {yr_his}"
            txt_act += \
                (f" ({overview_table.loc['emi_gdp', 'rank_fut']} in {yr_fut})."
                 if f"{overview_table.loc['emi_gdp', 'rank_fut']}" != "nan" else ".")
        elif f"{overview_table.loc['emi_pop', 'rank_his']}" != "nan":
            txt_act = \
                "\n The country's global rank in terms of total per-capita emissions was " + \
                    f"{overview_table.loc['emi_pop', 'rank_his']} in {yr_his}"
            txt_act += \
                (f" ({overview_table.loc['emi_pop', 'rank_fut']} in {yr_fut})."
                 if f"{overview_table.loc['emi_pop', 'rank_fut']}" != "nan" else ".")
        else:
            txt_act = ""
        
        txt += txt_act
        
        ##
        # Historical share.
        number = hpf.num_to_str_one_non_zero_decimal(sum_start1850_share_iso)
        txt += \
            f"\n In terms of accumulated historical emissions, {ctr}" + \
            f" contributed to the global {yr_sum_start1850}--{yr_his} emissions by {number}\%. "
        number1 = hpf.num_to_str_one_non_zero_decimal(sum_start1990_share_iso)
        #number2 = hpf.num_to_str_one_non_zero_decimal(sum_start1850_iso)
        #number3 = hpf.num_to_str_one_non_zero_decimal(sum_start1990_iso)
        txt += \
            ("\n However, when " if abs(sum_start1990_share_iso - sum_start1850_share_iso) > 5 else "\n When ") + \
            f"only accounting for the years {yr_sum_start1990}--{yr_his}, its contribution " + \
            ("stays the same " if number1 == number 
             else ("increases " if float(number1) > float(number) else "decreases ")) + \
            f"to {number1}\%."
            # " ({yr_sum_start1850} to {yr_his}: " + \
            # f"{number2}~{units_iso['emi']['label']}, and {yr_sum_start1990} to {yr_his}: " + \
            # f"{number3}~{units_iso['emi']['label']})."
        
        txt += \
            f"\n All of the emissions are presented following GWP~{meta.gwps.default}" + \
            ", and exclude emissions from LULUCF (exclLU)," + \
            " and bunkers fuels emissions (exclBunkers)."
        ##
        # Table {tab:overview}.
        label = "tab:overview"
        columns = "l || l r l r r"
        hlines = [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
        caption = \
            f"National emissions (dm{ssp2_short}), GDP and population for {ctr}, together with the emissions per unit of GDP " + \
            f"and per capita emissions (all for {yr_his} and {yr_fut}). " + \
            "\n Additionally, the global share and its rank are displayed."
        table_body = pd.DataFrame(index=range(len(hlines)), columns=range(6))
        table_body.loc[0, :] = [f"\\bfseries {xx}" for xx in overview_table_str.columns.to_list()]
        table_body.loc[1:, :] = overview_table_str.values
        table_body.loc[1:, 0] = [f"\\bfseries {xx}" for xx in table_body.loc[1:, 0].to_list()]
        table_body[table_body.isin(['nan', 'nan\%'])] = '--'
        txt += df_to_table(table_body, caption, label, columns, hlines)
        ##
        txt += \
            f"\n\n For {ctr}, in {yr_his} the main emissions share on sectoral level " + \
            "(Fig.~\\ref{fig:tsEmi}) came from " + \
            f"the {highest_sec_his_1st} sector ({highest_sec_his_share_1st}\%)" + \
            (f", followed by {highest_sec_his_2nd} ({highest_sec_his_share_2nd}\%)"
             if f"{highest_sec_his_share_2nd}" != "nan" else 
             (f", and {highest_sec_his_3rd} ({highest_sec_his_share_3rd}\%). "
              if f"{highest_sec_his_share_3rd}" != "nan" else "."))
            
        ##
        txt += \
            f"\n The Kyoto~GHG" + \
            f" with the highest emissions in {yr_his} was " + \
            f"{highest_gas_his_1st}, constituting " + \
            ("as much as " if float(highest_gas_his_share_1st) > 70 else " ") + \
            f"{highest_gas_his_share_1st}\% of the national emissions. "
        ##
        if f"{highest_gas_his_share_2nd}" != "nan":
            txt += \
                (f"\n Second largest contributor was {highest_gas_his_2nd} ({highest_gas_his_share_2nd}\%)"
                 if f"{highest_gas_his_share_2nd}" != "nan" else 
                 (f", followed by {highest_gas_his_3rd} ({highest_gas_his_share_3rd}\%)."
                  if f"{highest_gas_his_share_3rd}" != "nan" else "."))
        
        ##
        txt += \
            "\n The total of F-gases" + \
            ("only " if float(share_fgases_his) < 7 else "") + f"represented {share_fgases_his}\%."
        
        # TODO: If CO2 is the highest share, don't repeat the pc share.
        
        # TODO: Something about NDC and target.
        
        txt += txt_emi_trend
        
        txt += \
            f"\n The total CO$_2$ emissions are expected to be {share_co2_2030} " + \
            f"of the national Kyoto~GHG emissions in 2030 (dmSSP2)."
            
        # TODO: Check the correlations and the slope of regressions between emi_tot and emi_gas_sec.
        
        # Check if the ratios per gas are constant in the future and if they are the same for the different SSPs:
        # They are not constant and are not the same for the SSPs.
            
        # Historical emissions.
        path_to_figure = Path(path_to_tex_files, f'ts_emi_exclLU_{iso3}.png')
        caption = \
            "'Stacked' timeseries of national emissions (exclLU) per main-sector (a) and Kyoto~GHG (b). " + \
            f"\n No information available on the sectoral contributions after {yr_his}."
        txt += include_graphics(path_to_figure, caption, "fig:tsEmi", "\\textwidth")
            
        # TODO: Maybe get the linear regressions of the different emissions time series (and share)
        # and check which ones increase/decrease most strongly.
        
        # TODO: The total emissions are most notably influenced by the emissions from sector + gas (see correlation emitot & emisec or emigas).
        # TODO: Johannes includes the following in his plots (1850 to now):
        #sectors = {'IPC1A', 'IPC1B', 'IPC2', 'IPC3A', 'IPCMAGELV', 'IPC4', 'IPC5'};
        #gases = {'CO2', 'CH4', 'N2O', 'FGASESAR4'};
        
        gdp_linreg_nan = np.isnan(gdp_linreg.slope)
        pop_linreg_nan = np.isnan(pop_linreg.slope)
            
        if not (gdp_linreg_nan and pop_linreg_nan):
            path_to_figure = Path(path_to_tex_files, f'ts_gdp_pop_{iso3}.png')
            caption = \
                "Timeseries of national GDP (a) and population (c), " + \
                "and Kyoto~GHG emissions (exclLU, exclBunkers) per unit of GDP (b) or per capita (d)."
            txt += include_graphics(path_to_figure, caption, "fig:tsSocioEco", "\\textwidth")
        
        # Historical data.
        gdp_trend = ('positive' if gdp_linreg.slope > 0. else 'negative')
        emi_gdp_trend = ('positive' if emi_gdp_linreg.slope > 0. else 'negative')
        pop_trend = ('positive' if pop_linreg.slope > 0. else 'negative')
        emi_pop_trend = ('positive' if emi_pop_linreg.slope > 0. else 'negative')
        if not gdp_linreg_nan:
            txt += \
                f"\n\n The national GDP " + \
                ('increased ' if gdp_trend == 'positive' else 'decreased ') + \
                "in recent years, and the emissions per unit of GDP had " + \
                ("a similar trend " if emi_gdp_trend == 'positive' else "an opposite trend ") + \
                "(Fig.~\\ref{fig:tsSocioEco})."
        if not pop_linreg_nan:
            txt += \
                "\n The population " + \
                ("increased, " if pop_trend == 'positive' else "decreased, ") + \
                ("and " if (pop_trend == 'positive' and emi_pop_trend == 'positive') else "while ") + \
                "the per capita emissions " + ("were on the rise. " if emi_gdp_linreg.slope > 0 else "dropped. ")
        
        # Future data.
        # EMI per GDP: de-coupled?
        yrs_fut = range(2017, 2051)
        yrs_fut_str = [str(xx) for xx in yrs_fut]
        if not tables_iso.SSP2_gdp.data.loc[iso3, yrs_fut].isnull().all():
            yr_of_max = tables_iso.SSP2_gdp.data.loc[iso3, yrs_fut].idxmax()
            txt += f"\n Following dm{ssp2_short}, the GDP is projected to "
            txt += \
                (f"increase after {yrs_fut_str[0]} but to drop again before {yrs_fut_str[-1]}. " 
                if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
                (f"increase towards {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[-1] else "") + \
                (f"drop towards {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[0] else "")
            yr_of_max = tables_iso.SSP2_emi_gdp.data.loc[iso3, yrs_fut].idxmax()
            txt += \
                "\n The emissions per GDP are estimated to " + \
                (f"rise after {yrs_fut_str[0]} but to decrease again before {yrs_fut_str[-1]}. " 
                if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
                (f"rise towards {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[-1] else "") + \
                (f"decrease towars {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[0] else "")
            
            no_gdp_data = False
        
        else:
            no_gdp_data = True
        
        if not tables_iso.SSP2_pop.data.loc[iso3, yrs_fut].isnull().all():
            yr_of_max = tables_iso.SSP2_pop.data.loc[iso3, yrs_fut].idxmax()
            txt += \
                f"\n {ctr}'s population is assumed to " + \
                (f"grow after {yrs_fut_str[0]} but to diminish again before {yrs_fut_str[-1]}" 
                if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
                (f"grow towards {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[-1] else "") + \
                (f"diminish towars {yrs_fut_str[-1]}" if yr_of_max == yrs_fut[0] else "")
            yr_of_max = tables_iso.SSP2_emi_pop.data.loc[iso3, yrs_fut].idxmax()
            txt += \
                ", and the per capita emissions are expected to " + \
                (f"increase after {yrs_fut_str[0]} but to decline again before {yrs_fut_str[-1]}. " 
                if (yr_of_max > yrs_fut[0] and yr_of_max < yrs_fut[-1]) else "") + \
                (f"increase towards {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[-1] else "") + \
                (f"decline towars {yrs_fut_str[-1]}. " if yr_of_max == yrs_fut[0] else "")
            
            no_pop_data = False
        
        else:
            no_pop_data = True
        
        if (no_gdp_data and no_pop_data):
            txt += f"\n For {ctr}, no GDP and population data are available from dmSSPs."
        elif no_gdp_data:
            txt += f"\n For {ctr}, no GDP data are available from dmSSPs."
        elif no_pop_data:
            txt += f"\n For {ctr}, no population data are available from dmSSPs."
        
        # TODO: Maybe include some 'nice' words.
        
        # %% LULUCF emissions
        lu_srces = []
        for lu_srce in meta.lulucf.source_prioritisation:
            lu_data = getattr(tables_iso, f"LULUCF_{lu_srce}").data.loc[iso3, :]. \
                reindex(index=range(1990, yr_his+1))
            lu_srces_data = int(sum([1 for xx in lu_data if not np.isnan(xx)]))
            if lu_srces_data > 0:
                lu_srces += [f"{meta.sources.srce_to_label[lu_srce]}~/ {lu_srces_data}"]
        
        lu_srces = ", ".join(lu_srces)
        if len(lu_srces) > 0:
            lu_chosen = tables_iso.LULUCF_CHOSEN.data.loc[iso3, range(1990, yr_his+1)]
            lu_chosen_srce = meta.sources.srce_to_label[info_lulucf_chosen.loc[iso3]]
            emi_onlyLU_yrHis = lu_chosen[yr_his]
            emi_onlyLU_yrHis_str = hpf.num_to_str_one_non_zero_decimal(emi_onlyLU_yrHis)
            emi_exclLU_yrHis = tables_iso.KYOTOGHG_IPCM0EL.data.loc[iso3, yr_his]
            emi_exclLU_yrHis_str = hpf.num_to_str_one_non_zero_decimal(emi_exclLU_yrHis)
            ratio_lu = 100.*emi_onlyLU_yrHis/emi_exclLU_yrHis
            emi_onlyLU_min = lu_chosen.min()
            emi_onlyLU_min_str = hpf.num_to_str_one_non_zero_decimal(emi_onlyLU_min)
            emi_onlyLU_max = lu_chosen.max()
            emi_onlyLU_max_str = hpf.num_to_str_one_non_zero_decimal(emi_onlyLU_max)
            emi_onlyLU_mean = lu_chosen.mean()
            txt += \
                f"\n\n LULUCF emissions data for {ctr} are available from the following sources " + \
                "(Fig.~\\ref{fig:tsLULUCF}): " f"{lu_srces}, with the number of available data points in " + \
                f"1990--{yr_his} displayed additionally." + \
                f"\n Based on data from {lu_chosen_srce}, " + \
                f"for the year {yr_his}, LULUCF is estimated to be a net " + \
                ("sink" if emi_onlyLU_yrHis < 0. else "source") + \
                f" of {emi_onlyLU_yrHis_str}~{units_iso['emi']['label']}, which in absolute terms is " + \
                ("in the range of" if 85 < ratio_lu < 115 else 
                ("higher than" if ratio_lu > 115 else "lower than")) + \
                f" the non-LULUCF emissions of {emi_exclLU_yrHis_str}~{units_iso['emi']['label']}." + \
                f"\n The " + ("large "
                 if (emi_onlyLU_min/emi_onlyLU_mean < .5 or emi_onlyLU_max/emi_onlyLU_mean > 1.5) 
                 else "") + f"emissions range for {lu_chosen_srce} and 1990--{yr_his} is " + \
                f"{emi_onlyLU_min_str}--{emi_onlyLU_max_str}~{units_iso['emi']['label']}."
                
                # High fluctuations?
                # Difference between sources?
            
            path_to_figure = Path(path_to_tex_files, f'ts_emi_onlyLU_{iso3}.png')
            caption = \
                "Timeseries of emissions from LULUCF (CO$_2$ plus CH$_4$ and N$_2$O) " + \
                "as available from different data-sources. " + \
                f"\n Indicated in pink are the 'chosen' data, as used in our assessment of {ctr}'s NDC (if needed). " + \
                "\n The pink timeseries was inter- and~/ or extrapolated (interpolation: linear, extrapolation: constant)."
            txt += include_graphics(path_to_figure, caption, "fig:tsLULUCF", "\\textwidth")
        
        else:
            lu_srces = ", ".join([meta.sources.srce_to_label[xx] for xx in meta.lulucf.source_prioritisation])
            txt += \
                f"\n No LULUCF data are available for {ctr} from the following sources: {lu_srces}."
        
        # TODO: Only plot it for historical years, as it is kept constant afterwards there is nothing to see.
        # TODO: FAO2019 does not have circles but only a line, as the KYOTOGHG is the sum over CO2, CH4 and N2O ...
        
        # %% Mitigation targets
        txt += \
            "\n\n \\newpage %%%" + \
            "\n \\section{Mitigation targets (NDC)}" + \
            "\n \\label{sec:mitiTars}"
        
        txt += \
            "\n\n \\textbf{ " + \
            "\n Give the \%cov for the base and target year (and 2017). \\newline" + \
            "\n Global share for 2030 for the mitigated pathways and \% reduction relative to 1990 and 2017. \\newline" + \
            "\n Table with the 'input' data and the resulting targets (like ndcs\_targets.csv). \\newline" + \
            "}"
        
        # %%
        if iso3 == 'USA':
            txt += \
                "Even though the USA has submitted an NDC to the UNFCCC, " + \
                "due to the initiated withdrawal from the Paris Agreement, " + \
                "the USA is no longer assessed as country with NDC."
        
        if has_ndc not in ['NDC', 'INDC']:
            txt += \
                f"\n {ctr} does not have an (I)NDC." + \
                "\n Therefore the assumed 'mitigated' emissions pathways used for global aggregates equal " +\
                "the baseline emissions (dmSSP1--5)."
        
        else:
            plot_ts_pc_cov()
            plot_ndcs()
            
            txt += \
                f"\n {ctr} has an {has_ndc}, with a GHG mitigation target of the type " + \
                f"{type_main} ({tar_to_long[type_main]}; main target type)." + \
                f"\n The reclassified target type " + \
                ("equals the main target type." if type_main == type_reclass
                 else f"is {type_reclass} ({tar_to_long[type_reclass]}).")
            
            cols = ['type', 'condi', 'rge', 'val', 'refYr', 'tarYr', 'peakYr', 'intRef', 'LU']
            tars_df = pd.DataFrame(columns=cols)
            tars_df.loc[0, :] = ['type',  'condi.', 'range', 'value', 'refYr', 'tarYr', 'peakYr', 'intensRef', 'LU']
            count = 1
            types = ([type_main, type_reclass] if type_main != type_reclass else [type_main])
            for tar_tpe in types:
                if tar_tpe in ndc_iso3.index:
                    tars_json = json.loads(ndc_iso3[tar_tpe])
                    for lu in tars_json[tar_tpe].keys():
                        for condi in ['unconditional', 'conditional']:
                            for rge in ['worst', 'best']:
                                try:
                                    for yr in sorted(tars_json[tar_tpe][lu][condi][rge].keys()):
                                        tars_df.loc[count, 'type'] = tar_tpe
                                        tars_df.loc[count, 'condi'] = condi.replace('tional', '.')
                                        tars_df.loc[count, 'rge'] = rge
                                        tars_df.loc[count, 'tarYr'] = yr
                                        tars_df.loc[count, 'LU'] = lu
                                        val = tars_json[tar_tpe][lu][condi][rge][yr]. \
                                            replace('_', ' ').replace('%', '\%'). \
                                            replace('MtCO2', 'Mt~CO$_2$').replace('tCO2', 't~CO$_2$')
                                        # Delete decimals if necessary.
                                        point = [xx for xx in range(len(val)) if val[xx] == '.']
                                        if (len(point) > 0 and '%' not in val):
                                            space = [xx for xx in range(len(val)) if val[xx] == ' ']
                                            if len(space) > 0:
                                                val_nr = val[:space[0]]
                                                unit = val[space[0]:]
                                                val = hpf.num_to_str_one_non_zero_decimal(
                                                    float(val_nr), nr_non_zero=2) + unit
                                        
                                        tars_df.loc[count, 'val'] = val
                                        count += 1
                                except:
                                    pass
            
            if len(tars_df.index) > 1:
                tars_df.loc[1:, 'refYr'] = f"{ndc_iso3['BASEYEAR'] :.0f}"
                tars_df.loc[1:, 'peakYr'] = f"{ndc_iso3['DECLINE_AFTER_YEAR'] :.0f}"
                tars_df.loc[1:, 'intRef'] = ndc_iso3['INTENSITY_PERCAP_GDP']
                tars_df[tars_df == 'nan'] = ''
                tars_df[tars_df.isnull()] = ''
                for col in tars_df.columns:
                    if (tars_df.loc[1:, col] == '').values.all():
                        tars_df.drop(columns=[col], inplace=True)
                
                tars_df.loc[0, :] = [f"\\bfseries {xx}" for xx in tars_df.loc[0, :]]
                
                tars_df.loc[1:, :] = tars_df.loc[1:, :].sort_values(
                    ['type', 'LU', 'tarYr']).values
                
                caption = f"Information on {ctr}'s GHG mitigation target(s)."
                if len(types) == 1:
                    hlines = [2] + [0] * (len(tars_df.index)-1)
                else:
                    hlines = [2] + [0] * (len(tars_df.type[tars_df.type == type_main]) - 1) + [1] + \
                        [0] * (len(tars_df.type[tars_df.type == type_reclass]))
                
                txt += df_to_table(tars_df, caption, "tab:mitiTars", 
                    "".join(["l "] * len(tars_df.columns)), hlines) #, fontsize="\\small"
            
            else:
                txt += \
                    f"\n As the target has been assessed to be NGT, the assumed 'mitigated' " + \
                    "emissions pathways used for global aggregates equal the baseline emissions (dmSSP1--5)."
            
            # %%
            # TODO
            
            #txt += f"\n\n{ctr} has a " + infos_from_ndcs
            #tar_to_long
            
            # %%
            # Covered share of emissions.
            
            # TODO: Rules for pccov.
            # TODO: Only include the coverage stuff if it has an (I)NDC.
            txt += \
                (f"\n\n As {ctr} is part of the NDC by the European Union (28), " + \
                 "the coverage of the EU28 NDC is used." if iso3 in meta.isos.EU28 else "")
            
            path_to_figure = Path(path_to_tex_files, f'ts_pc_cov_{iso3}.png')
            caption = \
                f"Timeseries of {ctr}'s national emissions (exclLU) and the share of " + \
                f"emissions that is assumed to be covered by {ctr}'s mitigation target."
            txt += include_graphics(path_to_figure, caption, "fig:tsPcCov", "\\textwidth")
            
            # Tables with coverage.
            label = "tab:coveredSectorsGases"
            emi_iso3_exclLU = hpf.num_to_str_one_non_zero_decimal(
                table_combis_emis.loc['Total', 'Total'])
            emi_iso3_onlyLU = hpf.num_to_str_one_non_zero_decimal(
                tables_iso.LULUCF_CHOSEN.data.loc[iso3, yr_his])
            caption = \
                f"Information on covered sectors and gases as retrieved from {has_ndc} and adapted " + \
                f"('Adap.': used to calculate \%cov), and their shares in {ctr}'s {yr_his} emissions " + \
                f"(exclLU, exclBunkers; total {emi_iso3_exclLU}~{units_iso['emi']['label']})." + \
                "\n If either the sector or gas is assessed as 'not-covered', the emissions from this " + \
                "sector-gas combination are counted as not-covered (--). " + \
                "\n Else the emissions are counted as covered (+; covered shares given in bold)." + \
                "\n (/) means that no information is available." + \
                f"\n LULUCF: {has_ndc} '{cov_ndcs.loc[iso3, 'IPCMLULUCF']}' and " + \
                f"adapted '{cov_used.loc[iso3, 'IPCMLULUCF']}' " + \
                f"(estimated as a " + ("net sink" if float(emi_iso3_onlyLU) < 0. else "net source") + \
                f" of {emi_iso3_onlyLU}~{units_iso['emi']['label']} in {yr_his}; based on the 'chosen' LULUCF emissions)."
            columns = "l || c c || c c c c c c c | c"
            hlines = [2, 0, 2, 0, 0, 0, 0, 1, 0]
            table_body = pd.DataFrame(index=range(len(hlines)), columns=range(11))
            table_body.loc[0, :] = [f"\\bfseries {xx}" for xx in table_combis_str.columns.to_list()]
            table_body.loc[1:, :] = table_combis_str.values
            table_body.loc[1:, 0] = [f"\\bfseries {xx}" for xx in table_body.loc[1:, 0].to_list()]
            table_body.loc[:, 0] = [xx.replace('Agriculture', 'Agri.') if 'Agriculture' in xx else xx
                                     for xx in table_body.loc[:, 0]]
            txt += df_to_table(table_body, caption, label, columns, hlines, fontsize='\\small')
            
            # TODO: in brackets include the share of total emissions that combi stands for (2017).
            # TODO: Table with emissions per main-sector and per gas, and per combi?
            
            # TODO: Emissions target. Table with assumptions. All target years, etc.
            # TODO: Targets: plots like in UBA.
            path_to_figure = Path(path_to_tex_files, f'ts_ndcs_quantis_{iso3}.png')
            caption = \
                "Quantified mitigation targets (based on different input data and calculation options)." + \
                "\n Vertical lines: conditionality~/ range;" + \
                "\n colour coded: dmSSP1--5;" + \
                "\n first~/ second set of six: prio NDCs~/ SSPs;" + \
                f"\n set of six: {', '.join([xx.replace('_', ' ') for xx in ndc_quantis['prio_NDCs'].keys()])}."
            txt += include_graphics(path_to_figure, caption, "fig:miti", "\\textwidth")
            
        # %% Data sources and references
        txt += \
            "\n\n \\newpage %%%" + \
            "\n \\section{Data sources, additional information and references}" + \
            "\n \\label{sec:dataSourcesRefs}"
        
        primap_link = "https://dataservices.gfz-potsdam.de/pik/showshort.php?id=escidoc:4736895"
        primap_link_text = f"{meta.sources.srce_to_label[meta.primap.current_version['emi']]}"
        txt += \
            "\n\n \\noindent \\href{" f"{primap_link}" "}{" f"{primap_link_text}" "}: " + \
            "emissions from PRIMAP-hist are data from the country reported data priority scenario (HISTCR)."
        
        dmSSPs_link = "https://zenodo.org/record/3638137#.X2syXouxU2w"
        dmSSPs_link_text = "dmSSPs"
        txt += \
            "\n\n \\noindent \\href{" f"{dmSSPs_link}" "}{" f"{dmSSPs_link_text}" "}: " + \
            "emissions, population and GDP data are PMSSPBIE data for the five marker scenarios."
        
        # TODO: which data are needed in for the quantification of that country, and are they available.
        
        # %% Footnotes
        add_info = {
            "SSPs":
                "Shared Socio-economic Pathways. \\newline" +
                "\n Narratives and challenges to mitigation and adaptation: \\newline" +
                "\n \\textit{SSP1}: Sustainability, Taking the Green Road (low~/ low); \\newline" +
                "\n \\textit{SSP2}: Middle of the Road (medium~/ medium); \\newline" +
                "\n \\textit{SSP3}: Regional Rivalry, A Rocky Road (high~/ high); \\newline"+
                "\n \\textit{SSP4}: Inequality, A Road Divided (low~/ high); and \\newline" +
                "\n \\textit{SSP5}: Fossil-fuelled Development, Taking the Highway (high~/ low).",
            "GDP":
                "Gross Domestic Product. \\newline" +
                "\n Throughout this document the GDP is given as GDP~PPP, with PPP being the Purchasing Power Parity.",
            "GWP":
                "Global Warming Potential. \\newline" +
                "\n We use GWP values from the IPCC " +
                ("4$^{th}$ Assessment Report (AR4). " if meta.gwps.default == 'AR4' else "") +
                ("2$^{nd}$ Assessment Report (SAR). " if meta.gwps.default in ['SAR', 'AR2'] else "") +
                "\n They reflect the forcing potential of one kilogram of a gas' emissions in comparison " +
                "to one kilogram of CO$_2$ (GWP$_{CO2}$ = 1). " +
                "\n The GWPs correspond to a 100-yr period and are " +
                f"for CH$_4$:~{gwps['CH4'] :.0f}, for N$_2$O:~{gwps['N2O'] :.0f}" +
                f", for SF$_6$:~{gwps['SF6'] :.0f}, and for NF$_3$:~{gwps['NF3'] :.0f}. " +
                f"\n For the basket of HFC-gases the GWPs from AR4 are in the range {gwps[hfcs].min() :.0f}--{gwps[hfcs].max() :.0f}, " +
                f"and for PFCs {gwps.reindex(index=pfcs).min() :.0f}--{gwps.reindex(index=pfcs).max() :.0f}. " +
                "\n To assess emissions of several GHGs, their emissions are weighted by their respective GWPs " +
                "and presented in CO$_2$ equivalents (CO$_2$eq).",
            "LULUCF":
                "Land Use, Land-Use Change and Forestry. \\newline" +
                "\n Emissions from LULUCF are excluded throughout the document, unless stated otherwise.",
            "Bunkers fuels":
                "Emissions from international aviation and shipping.",
            "Kyoto~GHG":
                "Kyoto~GHG (Greenhouse Gas) basket. \\newline" +
                "\n Carbon dioxide (CO$_2$), methane (CH$_4$), nitrous oxide (N$_2$O), " +
                "hydrofluorocarbons (HFCs), perfluorocarbons (PFCs), " +
                "sulfur hexafluoride (SF$_6$), and nitrogen trifluoride (NF$_3$).",
            "F-gases":
                "Fluorinated gases. \\newline" +
                "\n Basket of HFCs, PFCs, and the gases SF$_6$ and NF$_3$. " +
                "\n Some F-gases have very long atmospheric lifetimes and high Global Warming Potentials.",
            "Target reclassification":
                f"When a country has, e.g., an RBU target ({tar_to_long['RBU']}), and the BAU emissions are provided, " +
                "it can be quantified based on the given emissions, and is reclassified from type\_main~RBU to " +
                f"type\_reclass~ABS ({tar_to_long['ABS']})." +
                f"\n Additionally, 'NGT' targets can be reclassified as 'ABU' ({tar_to_long['ABU']}) if " +
                "absolute mitigation effects due to planned policies and measures are provided.",
            "Quantification options":
                "Different quantification options were tested. \\newline" +
                "\n \\textit{dmSSP1--5}: down-scaled SSP marker scenarios; \\newline" +
                "\n \\textit{type\_reclass}: external data prioritised (PRIMAP-hist, dmSSPs); \\newline" +
                "\n \\textit{type\_main}: emissions data from within NDCs were prioritised; \\newline" +
                "\n \\textit{100\% coverage \& estimated coverage}; \\newline" +
                "\n \\textit{constant~emi}: constant emissions after last target year (instead of constant relative difference to baseline); \\newline" +
                "\n \\textit{baseline uncondi}: baseline emissions as uncond. pathways for Parties without uncond. targets, " +
                "even if baseline is better than cond. targets (instead of cond. pathway as uncond. pathways in these cases)."
                }
        
        txt += \
            "\n\n \\begin{description}" + \
            "".join(["\n \\item [" + xx + "] " + add_info[xx] for xx in add_info.keys()]) + \
            "\n \\end{description}"
        
        # %% Links
        isos_links = [iso3, 'EARTH']
        isos_links = (isos_links if iso3 not in meta.isos.EU28 else isos_links + ['EU28'])
        links_iso = links.loc[links.iso3.isin(isos_links), :].sort_values('text')
        txt += \
            "\n\n \\noindent \\textbf{Links to additional information:}" + \
            "\n \\begin{itemize}" + \
            "\n \\item " + \
            "\n \\vspace{-.2cm} \\item ".join([
                "\\href{" +
                f"{links_iso.loc[xx, 'link']}" "}{" +
                f"{links_iso.loc[xx, 'text']}" "} " +
                (f"({links_iso.loc[xx, 'date']})" if type(links_iso.loc[xx, 'date']) == str else "")
                for xx in links_iso.index]) + \
            "\n \\end{itemize}"
        
        # %%
        txt += \
            "\n\n %%%" + \
            "\n \\end{document}"
        
        # %%
        # Write text to .tex file.
        path_tex_file = Path(path_to_tex_files, f"factsheet_{iso3}.tex")
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
        # TODO: Come up with rules to be able to use expressions such as "differs strongly", 
        # "increase/decrease substantially",
        # "major share/contributions", etc.
        # TODO: Do not include empty plots.
        # TODO: Global page: include the graphics I had done on the data needed.
    
# %%
for iso3 in ['IDN']:# meta.isos.EARTH[110:]:
    print(iso3)
    text_to_latex_file()

# %%
