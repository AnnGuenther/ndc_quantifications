# -*- coding: utf-8 -*-

# %%
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def main_ndc_quantifications(input_file, lulucf_prio):
    """
    Calculation of NDC mitigation target emissions. Main file.

    # -------------------------
    
    Input examples:

        input_file = 'input_SSP2_typeCalc' (name of input-file, stored in /MODIFY_INPUT_HERE).
        
        lulucf_prio = '' or 'UNFCCC' or 'FAO'. 
            
            - If it is '' the default LULUCF prioritisation is used (CRF, BUR, UNFCCC, FAO).
            - For 'UNFCCC': UNFCCC, CRF, BUR, FAO.
            - For 'FAO': FAO, CRF, BUR, UNFCCC.
    
    # -------------------------
    
    Per country, target year, target type, conditionality, and range, the target emissions and emissions pathways are calculated.
    The target is calculated once including, and excluding LULUCF.
    
    # -------------------------
    
    Target types
    
    ABS:
        Absolute target emissions.
        E.g., target is to reduce emissions in 2030 to 500 MtCO2eq.
    RBY: 
        Relative reduction compared to base year.
        E.g., 20% emissions reduction compared to 2010 emissions in 2030.
    RBU: 
        Relative reduction compared to BAU. 
        E.g., 20% emissions reduction compared to business-as-usual (BAU) emissions in 2030.
    ABU: 
        Absolute reduction compared to BAU.
        E.g., 350 MtCO2eq reduction compared to BAU emissions in 2030.
    REI:
        Relative emissions intensity reduction.
        Compared to base year. E.g., 20% emissions intensity reduction compared to 2010 emissions intensity in 2030.
        Or compared to BAU. This is basically a simple RRB target, but some NDCs state it as intensity targets.
    AEI: 
        Absolute emissions intensity. 
        E.g., 2.1 tCO2eq/cap in 2030.
    NGT: 
        Non-GHG targets. 
        Nothing is calculated, baseline emissions are assumed.
    
    # -------------------------
    
    Per country one target type is chosen for the aggregation to a global pathway.
    This is generally the type_orig or type_calc.

    type_orig: what is said (+/-) in the NDC, e.g., 20\% reduction compared to BAU (RBU).
        In this case the comparison emissions are prioritised (comparison runs with 'external' input data).
    
    type_calc: what seems more suitable for the pathway calculations, e.g., if for the BAU target a quantification is given in the NDC (ABS).
        In this case the emissions given in the NDCs are prioritised.

    # -------------------------
    
    Globally and regionally aggregated emissions pathways are given with the output suitable for the MATLAB PRIMAP Emissions / Climate Module.
    They can be used to derive 2100 temperature estimates corresponding to the calculated 1990-2030 pathways.
    """
    
    # %%
    import pandas as pd
    from pathlib import Path
    import importlib
    import sys
    import helpers_functions as hpf
    import main_functions as mnf
    
    # %%
    # Load input and meta data (all in 'meta' from input_file).
    print(f"input file {input_file}")
    meta = importlib.import_module('MODIFY_INPUT_HERE.' + input_file).meta
    
    # Check if output folder exists. If so, exit the calculations.
    meta.path.output_ndcs = Path(meta.path.main, 'data', 'output', meta.output_folder + 
        ('_' + lulucf_prio if lulucf_prio!= '' else ''))
    if meta.path.output_ndcs.exists():
        sys.exit("main_ndc_quantifications.py: the output folder already exists. Nothing is calculated.")
        
    # Create output folder.
    Path(meta.path.output_ndcs).mkdir(parents=True, exist_ok=True)
    print("output path '" + str(meta.path.output_ndcs) + "' ...")
    
    # %%
    # Add some information to meta.
    
    # Target types.
    meta.target_types = ['ABS', 'RBY', 'RBU', 'ABU', 'REI', 'AEI', 'NGT']
    
    # NDCs.
    meta.path.ndcs_info = Path(meta.path.preprocess, 'infos_from_ndcs.csv')
    meta.ndcs_info = pd.read_csv(meta.path.ndcs_info, index_col='ISO3')
    
    # Units
    # All emissions have to be given in MtCO2eq, pop in Pers, and gdp in 2011GKD: info already in meta.units.
    meta.units.default['pccov'] = meta.units.default['emi'] + '/' + meta.units.default['emi']
    
    # Years (all: 1990 to 2050, pathways: 2020 to 2050)
    meta.years = hpf.create_class()
    meta.years.all = range(1990, 2051)
    meta.years.pathways = range(2020, 2051)
                    
    # %%        
    
    """
    Read input time series 1990-2050. For all countries in meta.isos.EARTH.
    For the EU28 countries, the targets are calculated separately (using the EU28 NDC info for each of the countries).
    In the end, a pathway is calculated for EU28.
    
    Read tables:
        'KYOTOGHG_IPCM0EL_TOTAL_NET_' + meta.ssps.chosen + 'FILLED_PMSSPBIE'
        'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTEREXTRAPOL_VARIOUS{lulucf_prio}'
        'KYOTOGHG_IPCM0EL_COV_PC_' + meta.ssps.chosen + 'FILLED_COVERAGE'
        'KYOTOGHG_IPCMLULUCF_COV_EMI_HISFUT_COVERAGE'
        'POP_DEMOGR_TOTAL_NET_' + meta.ssps.chosen + 'FILLED_PMSSPBIEMISC'
        'GDPPPP_ECO_TOTAL_NET_' + meta.ssps.chosen + 'FILLED_PMSSPBIEMISC'
    
    In principle one can also provide other tables (same type of data, but from other sources / with other values), 
    as long as they have the same structure and names.
    """
    
    tablenames = {
        'emi_bl_LU':
            {'table': f'KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_VARIOUS{lulucf_prio}.csv', 
            'unit': meta.units.default['emi']},
        'pc_cov_exclLU':
            {'table': 'KYOTOGHG_IPCM0EL_COV_PC_' + meta.ssps.chosen + 'FILLED_CORR.csv', 
             'unit': meta.units.default['pccov']},
        'pop':
            {'table': 'POP_DEMOGR_TOTAL_NET_' + meta.ssps.chosen + 'FILLED_PMSSPBIEMISC.csv', 
             'unit': meta.units.default['pop']},
        'gdp':
            {'table': 'GDPPPP_ECO_TOTAL_NET_' + meta.ssps.chosen + 'FILLED_PMSSPBIEMISC.csv', 
             'unit': meta.units.default['gdp']}}

    """
    If it is type_calc: use the ndc-emissions if available.
    For type_orig: use the comparison data.
    """
    if meta.use_ndc_emissions_if_available:
        tablenames['emi_bl_exclLU'] = \
            {'table': 'KYOTOGHG_IPCM0EL_TOTAL_NET_NDC' + meta.ssps.chosen + f'_NDCPMSSPBIE{lulucf_prio}.csv', 
            'unit': meta.units.default['emi']}
    else:
        tablenames['emi_bl_exclLU'] = \
            {'table': 'KYOTOGHG_IPCM0EL_TOTAL_NET_' + meta.ssps.chosen + 'FILLED_PMSSPBIE.csv', 
            'unit': meta.units.default['emi']}        
    
    database = hpf.create_class()
    
    for table_to_add in tablenames.keys():
        
        if 'cov' not in table_to_add:
            path_to_file = Path(meta.path.preprocess, 'tables', tablenames[table_to_add]['table'])
        else:
            path_to_file = Path(meta.path.pc_cov, tablenames[table_to_add]['table'])
        
        table = hpf.import_table_to_class_metadata_country_year_matrix(path_to_file). \
            __reindex__(isos=meta.isos.EARTH)
        
        if table.unit != tablenames[table_to_add]['unit']:
            sys.exit("main_ndc_quantifications.py: the unit of table " + table.tablename +
                " (" + table.unit + ") is not supported. The unit has to be " + 
                tablenames[table_to_add]['unit'] + ".")
        
        else:
            setattr(database, table_to_add, table)
    
    # Test if the input data seems ok.
    mnf.ndcs_some_initial_testing(database, meta)
    
    # %%
    """
    Additionally calculate and add the following tables to the database:
        'KYOTOGHG_IPCM0EL_NOTCOV_PC_' + meta.ssps.chosen + 'FILLED_COVERAGE'
        'KYOTOGHG_IPCM0EL_COV_EMI_' + meta.ssps.chosen + 'FILLED_COVERAGE'
        'KYOTOGHG_IPCM0EL_NOTCOV_EMI_' + meta.ssps.chosen + 'FILLED_COVERAGE'
        'KYOTOGHG_IPC0_TOTAL_NET_' + meta.ssps.chosen + '_VARIOUS{lulucf_prio}'
    """
    
    # 'KYOTOGHG_IPCM0EL_NOTCOV_PC_' + meta.ssps.chosen + 'FILLED_COVERAGE'
    
    table = hpf.copy_table(getattr(database, 'pc_cov_exclLU'))
    table.data = 1. - table.data
    table.clss = 'NOTCOV'
    table.__tablename_to_standard__()
    
    setattr(database, 'pc_ncov_exclLU', table)
    
    # 'KYOTOGHG_IPCM0EL_COV_EMI_' + meta.ssps.chosen + 'FILLED_COVERAGE'
    
    table = hpf.copy_table(getattr(database, 'emi_bl_exclLU'))
    table.data = table.data.multiply(getattr(database, 'pc_cov_exclLU').data)
    table.clss = 'COV'
    table.tpe = 'EMI'
    table.srce = 'COVERAGE'
    table.__tablename_to_standard__()
    
    setattr(database, 'emi_cov_exclLU', table)
    
    # 'KYOTOGHG_IPCM0EL_NOTCOV_EMI_' + meta.ssps.chosen + 'FILLED_COVERAGE'
    
    table = hpf.copy_table(getattr(database, 'emi_bl_exclLU'))
    table.data = table.data.multiply(getattr(database, 'pc_ncov_exclLU').data)
    table.clss = 'NOTCOV'
    table.tpe = 'EMI'
    table.srce = 'COVERAGE'
    table.__tablename_to_standard__()
    
    setattr(database, 'emi_ncov_exclLU', table)
    
    # 'KYOTOGHG_IPC0_TOTAL_NET_' + meta.ssps.chosen + '_VARIOUS'
    
    table = hpf.copy_table(getattr(database, 'emi_bl_exclLU'))
    table.data = table.data.add(getattr(database, 'emi_bl_LU').data, fill_value=0)
    table.note = "Sum over KYOTOGHG_IPCM0EL_TOTAL_NET_" + meta.ssps.chosen + "FILLED_PMSSPBIE and " + \
        "KYOTOGHG_IPCMLULUCF_COV_EMI_HISFUT_COVERAGE."
    table.cat = 'IPC0'
    table.srce = f'VARIOUS{lulucf_prio}'
    table.__tablename_to_standard__()
    
    setattr(database, 'emi_bl_inclLU', table)
    
    # %%
    # Read in the coverage_used. Needed for output and LULUCF check in ndcs_calculate_targets.py.
    
    path_to_coverage = Path(meta.path.preprocess, 'coverage_used_per_gas_and_per_sector_and_combi.csv')
    meta.coverage = pd.read_csv(path_to_coverage, index_col=0)
    
    # Read in the emissions (exclLU/inclLU/onlyLU) retrieved from the NDCs.
    for case in ['exclLU', 'inclLU', 'onlyLU']:
        table = pd.read_csv(Path(meta.path.preprocess, f'infos_from_ndcs_emi_{case}.csv'), index_col=0). \
            reindex(index=meta.isos.EARTH)
        table.columns = [int(xx) for xx in table.columns]
        setattr(database, f"emi_bl_{case}_ndcs", table)
        
    # %%
    """
    Write relevant input-info to log_file.md in the output-folder.
    In this file one will find the necessary information to re-run the calculations with the same setup.
    """
    
    fid = open(Path(meta.path.output_ndcs, 'log_file.md'), 'w')
    fid.write("### Setup for NDC quantifications\n")
    fid.write(f"- **input file:** {input_file}\n")
    fid.write(f"- **folder output:** {str(meta.path.output_ndcs)}\n")
    fid.write(f"- **folder preprocessing:** {str(meta.path.preprocess)}\n")
    fid.write(f"- **scenario:** {meta.ssps.chosen}\n")
    fid.write(f"- **gwp:** {meta.gwps.default}\n")
    fid.write("- **time series:**\n")
    [fid.write(f"  - **{xx}:** {str(Path(meta.path.preprocess, 'tables', tablenames[xx]['table']))}\n")
        for xx in tablenames]
    fid.write(f"- **ndcs general info** {str(meta.path.ndcs_info)}\n")
    fid.write(f"- **ndcs coverage_used**: {str(path_to_coverage)}\n")
    fid.write(f"- **method_pathways:** " + meta.method_pathways + "\n")
    fid.write("- **calculate_targets_for:**\n")
    [fid.write(f"  - **{xx}:** {str(meta.calculate_targets_for[xx])}\n")
        for xx in meta.calculate_targets_for]
    fid.write("- **ndcs_type_prioritisations:**\n")
    [fid.write(f"  - **{xx}:** {str(meta.ndcs_type_prioritisations[xx])}\n")
        for xx in meta.ndcs_type_prioritisations]
    fid.write("- **set_pccov_to_100:**\n")
    [fid.write(f"  - **{xx}:** {str(meta.set_pccov_to_100[xx])}\n")
        for xx in meta.set_pccov_to_100]
    fid.write("- **strengthen_targets:**\n")
    [fid.write(f"  - **{xx}:** {str(meta.strengthen_targets[xx])}\n")
        for xx in meta.strengthen_targets]
    fid.close()
            
    # %%
    """
    Correct or modify the calculation options given in input_file if necessary.
    ndcs_check_options_for_target_calculations(meta).
    """
    
    meta = mnf.ndcs_check_options_for_target_calculations(meta)
    
    """
    TARGETS
    Calculate the target emissions per country and un/conditional & best/worst & year.
    ndcs_calculate_targets(database, meta).
    """
    
    calculated_targets = mnf.ndcs_calculate_targets(database, meta)
    
    """
    PATHWAYS
    Country-pathways.
    
    Calculate the emissions pathways for un/conditional_best/worst targets, per country.
    For countries without targets use the baseline emissions (if available).
    ndcs_calculate_pathways_per_country(database, calculated_targets, meta)
    """
    
    pathways_per_country = mnf.ndcs_calculate_pathways_per_country(
        database, calculated_targets, meta)
    
    """
    PATHWAYS
    Group-pathways.
    
    Calculate the emissions pathways for un/conditional_best/worst targets, per group of countries.
    ndcs_calculate_pathways_per_group(pathways_per_country, meta)
    """
    
    pathways_groups, pathways_countries = mnf.ndcs_calculate_pathways_per_group(
            pathways_per_country, meta)
    
    # Write out the pathways to csv-files to be used in the Matlab PRIMAP Emissions Module and Climate Module
    # to calculate temperatures that correspond to the NDC emissions pathways.
    # Used are the pathways for 'EARTH'.
    
    mnf.ndcs_get_pathways_for_matlab(
        pathways_countries, pathways_groups, meta)
    
    # %%
    print('final testing ...')
    mnf.ndcs_some_final_testing(database, meta)
    
    # %%
    print("... and over it is!")
    
    # %%

