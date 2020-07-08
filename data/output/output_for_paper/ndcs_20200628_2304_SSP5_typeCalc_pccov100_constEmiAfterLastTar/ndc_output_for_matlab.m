
%%
% Matlab file with the information from NDC quantifications to be read in.
% (ndc_quantifications_in_python/ndc_quantifications/output/ndc_quantification_xxx/pathways_for_matlab/ndc_output_for_matlab.m)
%%
NDCISIPEDIA = struct;
    
%%
% BAU emissions for SSP5 (1990:2030) used during NDC target calculations (CATM0EL).
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_BAU_NDCISIPEDIA = struct;
data_act = NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_BAU_NDCISIPEDIA;
data_act.sheet_code = 'KYOTOGHGAR4_CATM0EL_TOTAL_NET_BAU_NDCISIPEDIA' ;
data_act.sheet_entity = 'KYOTOGHGAR4';
data_act.sheet_category = 'CATM0EL';
data_act.sheet_class = 'TOTAL';
data_act.sheet_type = 'NET';
data_act.sheet_scenario = 'BAU';
data_act.sheet_source = 'NDCISIPEDIA';
data_act.sheet_unit = 'MtCO2eq';
data_act.sheet_gwp = 'AR4';
data_act.sheet_datatype = 'CountryYearMatrix';
data_act.sheet_firstdatarow = 18;
data_act.sheet_name_category = 'NationalTotalExclLULUCF';
data_act.sheet_descr = '';
data_act.sheet_note = '';
data_act.sheet_subsource = {''};
data_act.path = 'C:\Users\annikag\primap\ndcs\ndc_quantifications_in_python\data\output\ndc_quantifications_20200628_2304_SSP5_pccov100ForAllCountries_typeCalcForAllCountries_constantEmissionsAfterLastTarget\pathways_for_matlab_CATM0EL\KYOTOGHGAR4_CATM0EL_TOTAL_NET_BAU_NDCISIPEDIA.csv';
data_act.sheet_tablekind = '';
data_load = readtable(data_act.path, 'ReadRowNames', true);
data_act.colcodes_years = cellfun(@str2num, erase(data_load.Properties.VariableNames, 'Y'));
data_act.rowcodes_countries = data_load.Properties.RowNames;
data_act.data = data_load{:, :};
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_BAU_NDCISIPEDIA = data_act;
    
%%
% NDC target pathways for SSP5 (1990:2030), for unconditional worst targets (CATM0EL).
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCW_NDCISIPEDIA = struct;
data_act = NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCW_NDCISIPEDIA;
data_act.sheet_code = 'KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCW_NDCISIPEDIA' ;
data_act.sheet_entity = 'KYOTOGHGAR4';
data_act.sheet_category = 'CATM0EL';
data_act.sheet_class = 'TOTAL';
data_act.sheet_type = 'NET';
data_act.sheet_scenario = 'NDCUCW';
data_act.sheet_source = 'NDCISIPEDIA';
data_act.sheet_unit = 'MtCO2eq';
data_act.sheet_gwp = 'AR4';
data_act.sheet_datatype = 'CountryYearMatrix';
data_act.sheet_firstdatarow = 18;
data_act.sheet_name_category = 'NationalTotalExclLULUCF';
data_act.sheet_descr = '';
data_act.sheet_note = '';
data_act.sheet_subsource = {''};
data_act.path = 'C:\Users\annikag\primap\ndcs\ndc_quantifications_in_python\data\output\ndc_quantifications_20200628_2304_SSP5_pccov100ForAllCountries_typeCalcForAllCountries_constantEmissionsAfterLastTarget\pathways_for_matlab_CATM0EL\KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCW_NDCISIPEDIA.csv';
data_act.sheet_tablekind = '';
data_load = readtable(data_act.path, 'ReadRowNames', true);
data_act.colcodes_years = cellfun(@str2num, erase(data_load.Properties.VariableNames, 'Y'));
data_act.rowcodes_countries = data_load.Properties.RowNames;
data_act.data = data_load{:, :};
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCW_NDCISIPEDIA = data_act;
    
%%
% NDC target pathways for SSP5 (1990:2030), for unconditional best targets (CATM0EL).
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCB_NDCISIPEDIA = struct;
data_act = NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCB_NDCISIPEDIA;
data_act.sheet_code = 'KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCB_NDCISIPEDIA' ;
data_act.sheet_entity = 'KYOTOGHGAR4';
data_act.sheet_category = 'CATM0EL';
data_act.sheet_class = 'TOTAL';
data_act.sheet_type = 'NET';
data_act.sheet_scenario = 'NDCUCB';
data_act.sheet_source = 'NDCISIPEDIA';
data_act.sheet_unit = 'MtCO2eq';
data_act.sheet_gwp = 'AR4';
data_act.sheet_datatype = 'CountryYearMatrix';
data_act.sheet_firstdatarow = 18;
data_act.sheet_name_category = 'NationalTotalExclLULUCF';
data_act.sheet_descr = '';
data_act.sheet_note = '';
data_act.sheet_subsource = {''};
data_act.path = 'C:\Users\annikag\primap\ndcs\ndc_quantifications_in_python\data\output\ndc_quantifications_20200628_2304_SSP5_pccov100ForAllCountries_typeCalcForAllCountries_constantEmissionsAfterLastTarget\pathways_for_matlab_CATM0EL\KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCB_NDCISIPEDIA.csv';
data_act.sheet_tablekind = '';
data_load = readtable(data_act.path, 'ReadRowNames', true);
data_act.colcodes_years = cellfun(@str2num, erase(data_load.Properties.VariableNames, 'Y'));
data_act.rowcodes_countries = data_load.Properties.RowNames;
data_act.data = data_load{:, :};
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCUCB_NDCISIPEDIA = data_act;
    
%%
% NDC target pathways for SSP5 (1990:2030), for conditional worst targets (CATM0EL).
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCW_NDCISIPEDIA = struct;
data_act = NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCW_NDCISIPEDIA;
data_act.sheet_code = 'KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCW_NDCISIPEDIA' ;
data_act.sheet_entity = 'KYOTOGHGAR4';
data_act.sheet_category = 'CATM0EL';
data_act.sheet_class = 'TOTAL';
data_act.sheet_type = 'NET';
data_act.sheet_scenario = 'NDCCW';
data_act.sheet_source = 'NDCISIPEDIA';
data_act.sheet_unit = 'MtCO2eq';
data_act.sheet_gwp = 'AR4';
data_act.sheet_datatype = 'CountryYearMatrix';
data_act.sheet_firstdatarow = 18;
data_act.sheet_name_category = 'NationalTotalExclLULUCF';
data_act.sheet_descr = '';
data_act.sheet_note = '';
data_act.sheet_subsource = {''};
data_act.path = 'C:\Users\annikag\primap\ndcs\ndc_quantifications_in_python\data\output\ndc_quantifications_20200628_2304_SSP5_pccov100ForAllCountries_typeCalcForAllCountries_constantEmissionsAfterLastTarget\pathways_for_matlab_CATM0EL\KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCW_NDCISIPEDIA.csv';
data_act.sheet_tablekind = '';
data_load = readtable(data_act.path, 'ReadRowNames', true);
data_act.colcodes_years = cellfun(@str2num, erase(data_load.Properties.VariableNames, 'Y'));
data_act.rowcodes_countries = data_load.Properties.RowNames;
data_act.data = data_load{:, :};
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCW_NDCISIPEDIA = data_act;
    
%%
% NDC target pathways for SSP5 (1990:2030), for conditional best targets (CATM0EL).
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCB_NDCISIPEDIA = struct;
data_act = NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCB_NDCISIPEDIA;
data_act.sheet_code = 'KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCB_NDCISIPEDIA' ;
data_act.sheet_entity = 'KYOTOGHGAR4';
data_act.sheet_category = 'CATM0EL';
data_act.sheet_class = 'TOTAL';
data_act.sheet_type = 'NET';
data_act.sheet_scenario = 'NDCCB';
data_act.sheet_source = 'NDCISIPEDIA';
data_act.sheet_unit = 'MtCO2eq';
data_act.sheet_gwp = 'AR4';
data_act.sheet_datatype = 'CountryYearMatrix';
data_act.sheet_firstdatarow = 18;
data_act.sheet_name_category = 'NationalTotalExclLULUCF';
data_act.sheet_descr = '';
data_act.sheet_note = '';
data_act.sheet_subsource = {''};
data_act.path = 'C:\Users\annikag\primap\ndcs\ndc_quantifications_in_python\data\output\ndc_quantifications_20200628_2304_SSP5_pccov100ForAllCountries_typeCalcForAllCountries_constantEmissionsAfterLastTarget\pathways_for_matlab_CATM0EL\KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCB_NDCISIPEDIA.csv';
data_act.sheet_tablekind = '';
data_load = readtable(data_act.path, 'ReadRowNames', true);
data_act.colcodes_years = cellfun(@str2num, erase(data_load.Properties.VariableNames, 'Y'));
data_act.rowcodes_countries = data_load.Properties.RowNames;
data_act.data = data_load{:, :};
NDCISIPEDIA.KYOTOGHGAR4_CATM0EL_TOTAL_NET_NDCCB_NDCISIPEDIA = data_act;
    
%%
clear data_act data_load