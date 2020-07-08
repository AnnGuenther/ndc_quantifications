# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
def ndcs_get_pathways_for_matlab(pathways_countries_in, pathways_groups_in, meta):
    """
    Write out data for Matlab.
    To be used in the PRIMAP Emissions Module / Climate Module to calculate temperatures 
    for the emissions pathways).
    
    Creates csv-files with the data and .m-files to be used in Matlab for reading in the csv-files.
    """
    
    # %%
    import pandas as pd
    from pathlib import Path
    from copy import deepcopy
    
    # %%
    ptws_groups_in = deepcopy(pathways_groups_in) # Else the orignal DF is modified.
    ptws_countries_in = deepcopy(pathways_countries_in)
    
    # In PRIMAPDB, the years in the tables are stored with 'Y' and as string ('Y1990').
    ptws_groups_in.columns = [xx if type(xx) == str else 'Y' + str(xx) for xx in ptws_groups_in.columns]
    ptws_countries_in.columns = [xx if type(xx) == str else 'Y' + str(xx) for xx in ptws_countries_in.columns]
    yrs_int = range(1990, 2031)
    yrs_str = ['Y' + str(xx) for xx in yrs_int]
    
    # Only write out certain groups (and all countries).
    ptws_groups_in = ptws_groups_in.loc[ptws_groups_in.group.isin(
        ['EU28', 'EARTH', 'R5ASIA', 'R5LAM', 'R5MAF', 'R5OECD', 'R5REF']), :]
    
    # Replace column name 'group' by 'iso3'.
    ptws_groups_in.columns = [xx if xx != 'group' else 'iso3' for xx in ptws_groups_in.columns]
    
    # Replace the IPCM0EL by CATM0EL, as the MATLAB code for further processing is based on CAT.
    ptws_countries_in.category = [xx if xx != 'IPCM0EL' else xx.replace('IPC', 'CAT')
        for xx in ptws_countries_in.category]
    ptws_groups_in.category = [xx if xx != 'IPCM0EL' else xx.replace('IPC', 'CAT')
        for xx in ptws_groups_in.category]
    
    columns_matlab = ['iso3', 'entity', 'category', 'unit', 'gwp'] + yrs_str
    out_mat = {
        'UCW': {'condi': 'unconditional', 'rge': 'worst'},
        'UCB': {'condi': 'unconditional', 'rge': 'best'},
        'CW': {'condi': 'conditional', 'rge': 'worst'},
        'CB': {'condi': 'conditional', 'rge': 'best'}}
    struct_main = 'NDCISIPEDIA'
    
    category, name_category = ['CATM0EL', 'NationalTotalExclLULUCF']
    
    path_output_matlab = Path(meta.path.output_ndcs)
    Path(path_output_matlab).mkdir(parents=True, exist_ok=True)
    path_main = Path(path_output_matlab, 'ndc_output_for_matlab.m')
    
    file_out = open(path_main, 'w')
    # No spaces in front of the text possible for """ text """, as they would also appear in the output.
    file_out.write("""
%%
% Matlab file with the information from NDC quantifications to be read in.
% (ndc_quantifications_in_python/ndc_quantifications/output/ndc_quantification_xxx/pathways_for_matlab/ndc_output_for_matlab.m)
%%
""" + struct_main + """ = struct;
    """)
    # BAU emissions used here (pathways per country and group).
    pathways_exclLU = pd.DataFrame(columns=columns_matlab)
    pathways_exclLU = pathways_exclLU.append(
        ptws_countries_in.loc[
            (ptws_countries_in.rge == 'emi_bau') &
            (ptws_countries_in.category == category), columns_matlab], ignore_index=True)
    pathways_exclLU = pathways_exclLU.append(
        ptws_groups_in.loc[
            (ptws_groups_in.rge == 'emi_bau') &
            (ptws_groups_in.category == category), columns_matlab], ignore_index=True)
    pathways_exclLU = pathways_exclLU.sort_values(['iso3'])
    txt = "BAU emissions for " + meta.ssps.chosen[:4] + " (1990:2030) used during NDC target calculations " + \
        "(" + category + ")."
    file_out = ndc_calc_int_pathways_for_matlab(pathways_exclLU, 'BAU', 
        yrs_str, path_output_matlab, file_out, struct_main, txt, name_category)
    
    # Target pathways (per country and group).
    for mat in out_mat.keys():
        pathways_exclLU = pd.DataFrame(columns=columns_matlab)
        pathways_exclLU = pathways_exclLU.append(
            ptws_countries_in.loc[
                (ptws_countries_in.condi == out_mat[mat]['condi']) &
                (ptws_countries_in.rge == out_mat[mat]['rge']) &
                (ptws_countries_in.category == category), columns_matlab], ignore_index=True)
        pathways_exclLU = pathways_exclLU.append(
            ptws_groups_in.loc[
                (ptws_groups_in.condi == out_mat[mat]['condi']) &
                (ptws_groups_in.rge == out_mat[mat]['rge']) &
                (ptws_groups_in.category == category), columns_matlab], ignore_index=True)
        pathways_exclLU = pathways_exclLU.sort_values(['iso3'])
        txt = "NDC target pathways for " + meta.ssps.chosen[:4] + " (1990:2030), for " + \
            out_mat[mat]['condi'] + " " + out_mat[mat]['rge'] + " targets (" + category + ")."
        file_out = ndc_calc_int_pathways_for_matlab(pathways_exclLU, 'NDC' + mat, 
            yrs_str, path_output_matlab, file_out, struct_main, txt, name_category)
    
    file_out.write(
    """
%%
clear data_act data_load""")
    file_out.close()
    
# %%
def ndc_calc_int_pathways_for_matlab(
    pathways_act, sheet_scenario, yrs_str, path_output_matlab, file_out, struct_main, txt, name_category):
    
    from pathlib import Path
    
    sheet_entity = pathways_act.entity.unique()[0]
    sheet_category = pathways_act.category.unique()[0]
    sheet_class = 'TOTAL'
    sheet_type = 'NET'
    sheet_source = struct_main
    sheet_unit = pathways_act.unit.unique()[0]
    sheet_gwp = pathways_act.gwp.unique()[0]
    if sheet_gwp == 'AR4':
        sheet_entity += 'AR4'
    
    sheet_code = '_'.join([sheet_entity, sheet_category, sheet_class, sheet_type,
                           sheet_scenario, sheet_source])
    columns_file = ['iso3'] + yrs_str
    data_str_head = ', '.join(columns_file);
    data_str = '\n'.join([', '.join(list(pathways_act.loc[xx, columns_file].astype(str))) 
                          for xx in pathways_act.index])
    data_str = data_str_head + '\n' + data_str
    path_data = Path(path_output_matlab, sheet_code + '.csv')
    file_out.write(
    """
%%
% """ + txt + """
""" + struct_main + """.""" + sheet_code + """ = struct;
data_act = """ + struct_main + """.""" + sheet_code + """;
data_act.sheet_code = '""" + sheet_code + """' ;
data_act.sheet_entity = '""" + sheet_entity + """';
data_act.sheet_category = '""" + sheet_category + """';
data_act.sheet_class = '""" + sheet_class + """';
data_act.sheet_type = '""" + sheet_type + """';
data_act.sheet_scenario = '""" + sheet_scenario + """';
data_act.sheet_source = '""" + sheet_source + """';
data_act.sheet_unit = '""" + sheet_unit + """';
data_act.sheet_gwp = '""" + sheet_gwp + """';
data_act.sheet_datatype = 'CountryYearMatrix';
data_act.sheet_firstdatarow = 18;
data_act.sheet_name_category = '""" + name_category + """';
data_act.sheet_descr = '';
data_act.sheet_note = '';
data_act.sheet_subsource = {''};
data_act.path = '""" + str(path_data) + """';
data_act.sheet_tablekind = '';
data_load = readtable(data_act.path, 'ReadRowNames', true);
data_act.colcodes_years = cellfun(@str2num, erase(data_load.Properties.VariableNames, 'Y'));
data_act.rowcodes_countries = data_load.Properties.RowNames;
data_act.data = data_load{:, :};
""" + struct_main + """.""" + sheet_code + """ = data_act;
    """)
    file_out_data = open(path_data, 'w')
    file_out_data.write(data_str)
    file_out_data.close()
    
    return file_out

# %%
