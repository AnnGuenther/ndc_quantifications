# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
def setup_metadata():
    """
    **Set up the general metadata.**
    
    If you want/need to *change the folder for the preprocessed data*, do it here.
    
    Returns:
        *meta : class with meta data needed in the quantifications and plotting routines.*
    """
    
    # %%
    from pathlib import Path
    from copy import deepcopy
    import pandas as pd
    
    import helpers_functions as hpf
    
    # %%
    # Store general information in class meta.
    meta = hpf.create_class(name='meta')
    
    # %%
    """
    This part can be modified.
    """
    
    submission_until = 20201231 # yyyymmdd
    # For the first paper submission: 20200417
    # For paper revision: 20201231
    
    # Which version of the file infos_from_ndcs.xlsx to be used.
    # For the first paper submission: infos_from_ndcs_xlsx = 'infos_from_ndcs__paper_first_submission_202011.xlsx'
    # For the paper revision. infos_from_ndcs_xlsx = 'infos_from_ndcs__paper_revision_202104.xlsx'
    infos_from_ndcs_xlsx = 'infos_from_ndcs__paper_revision_202104.xlsx'
    
    # Current PRIMAP-hist
    current_primap = 'PMH21'
    current_primap_srcs = {
        'emi': 'PRIMAPHIST21', 'pop': 'PMHSOCIOECO21', 'gdp': 'PMHSOCIOECO21'}
    current_primap_last_year = 2017
    
    # pc_cov made on yyyymmdd_hhss, smd submissions up to date yyyymmdd, pmh21 PRIMAP-hist v2.1
    ############################################################################
    # !!!!! TO BE MODIFIED AFTER RUNNING preprocessing_current_pc_cov.py !!!!! #
    ############################################################################
    # For the first paper submission: path_preprocess = 'pc_cov_20210428_0834_SMD20200417_PMH21'
    # For the paper revision: path_preprocess = 'pc_cov_20210428_1130_SMD20201231_PMH21'
    path_preprocess = 'pc_cov_20210428_1130_SMD20201231_PMH21'
    
    # How many years should be used when calculating the mean over the last available years.
    meta.average_nrvalues = 6

    # %%
    """
    *meta.path*: paths to different folders.
    """
    
    # Paths
    meta.path = hpf.create_class(name='path')
    # Path to model-folder:
    meta.path.main = hpf.get_path_to_main_folder()
    # Path to output-folder:
    meta.path.output = Path(meta.path.main, 'data', 'output')
    # Path to folder where the tables from PRIMAPDB are stored as single csv-files.
    meta.path.matlab = Path(meta.path.main, 'data', 'matlab_tables')
    # Path to py_files.
    meta.path.py_files = Path(meta.path.main, 'py_files')
    # Path to preprocessed data (from preprocessing_general.py)
    meta.path.preprocess = Path(meta.path.main, 'data', 'preprocess')
    
    # Path to pc/emi_cov data.
    meta.path.pc_cov = Path(meta.path.preprocess, path_preprocess)
    
    # %%
    """
    *meta.isos*: iso3 codes of EARTH, EU, and conversion from iso3 to short country names.
    """
    
    # ISO3s of EARTH and EU28.
    meta.isos = hpf.create_class(name='isos')
    meta.isos.EARTH = hpf.get_isos_earth_only_independent()
    meta.isos.EARTH_EU28 = sorted(meta.isos.EARTH + ['EU28'])
    meta.isos.EU28 = hpf.get_isos_for_groups('EU28', 'ISO3')
    
    meta.isos.EARTH_EU27 = sorted(meta.isos.EARTH + ['EU27'])
    meta.isos.EU27 = hpf.get_isos_for_groups('EU27', 'ISO3')
    
    isos_EARTH_EU28_EU27 = sorted(meta.isos.EARTH + ['EU28', 'EU27'])
    meta.isos.iso3_to_shortname = pd.Series(
        hpf.convert_isos_and_country_names(isos_EARTH_EU28_EU27, 'ISO3', 'ShortName'), 
        index=isos_EARTH_EU28_EU27).to_dict()
    
    """
    *meta.EU*: current EU (e.g., EU28, or EU27)
    
    Submission date of GBR NDC a bit earlier (20201212)!
    Problem in between 20201212 and 20201218?!
    Not really a problem, as in get_infos_from_ndcs.py, the EU28 info is used for
    all EU28 countries if meta.EU == EU28, which is the case if the submission was
    before 20201218. So for the few days, the GBR NDC is neglected, and therefore
    the data is not double counting anything.
    """
    
    if submission_until < 20201218: # Sumbission date of EU27 NDC.
        
        meta.EU = 'EU28'
        meta.isos.EU = meta.isos.EU28 # former name: meta.EU_isos
        meta.isos.EARTH_EU = meta.isos.EARTH_EU28 # former name: meta.EU_EARTH
    
    else:
        
        meta.EU = 'EU27'
        meta.isos.EU = meta.isos.EU27
        meta.isos.EARTH_EU = meta.isos.EARTH_EU27
    
    meta.EUs = ['EU27', 'EU28']
    
    # %%
    """
    *meta.ssps*: Shared Socioeconomic Pathways; info on available marker scenarios.
    """
    
    # Available SSP scenarios.
    meta.ssps = hpf.create_class(name='ssps')
    meta.ssps.scens = hpf.create_class(name='scens', 
        long=['SSP1BLIMAGE', 'SSP2BLMESGB', 'SSP3BLAIMCGE', 'SSP4BLGCAM4', 'SSP5BLREMMP'])
    meta.ssps.scens.short = [xx[:4] for xx in meta.ssps.scens.long]
    meta.ssps.scens.long_to_short = {
        'SSP1BLIMAGE': 'SSP1', 'SSP2BLMESGB': 'SSP2', 'SSP3BLAIMCGE': 'SSP3', 
        'SSP4BLGCAM4': 'SSP4', 'SSP5BLREMMP': 'SSP5'}
    meta.ssps.scens.short_to_long = {
        'SSP1': 'SSP1BLIMAGE', 'SSP2': 'SSP2BLMESGB', 'SSP3': 'SSP3BLAIMCGE', 
        'SSP4': 'SSP4BLGCAM4', 'SSP5': 'SSP5BLREMMP'}
    meta.ssps.emi = {
        'ent': 'KYOTOGHG', 'cat': 'IPCM0EL', 'clss': 'TOTAL', 'tpe': 'NET', 
        'scen': meta.ssps.scens, 'srce': 'PMSSPBIE', 'srcepmh': f'{current_primap}SSPBIE'}
    meta.ssps.pop = {
        'ent': 'POP', 'cat': 'DEMOGR', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': meta.ssps.scens, 'srce': 'PMSSPBIEMISC', 'srcepmh': f'{current_primap}SSPBIE'}
    meta.ssps.gdp = {
        'ent': 'GDPPPP', 'cat': 'ECO', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': meta.ssps.scens, 'srce': 'PMSSPBIEMISC', 'srcepmh': f'{current_primap}SSPBIE'}
    
    # %%
    """
    *meta.nomenclature*: table meta-data nomenclature.
    """
    
    # Nomenclature of PRIMAPDB tables & of the classes in database.
    meta.nomenclature = hpf.create_class(name='nomenclature',
        tablename_from = ['ent', 'cat', 'clss', 'tpe', 'scen', 'srce'],
        attrs = [
            'cat', 'clss', 'data', 'ent', 'gwp', 'note', 'scen', 
            'srce', 'tablename', 'tpe', 'unit', 'family'])
    # PRIMAP nomenclature to 'new' nomenclature.
    meta.nomenclature.oldname_to_attr = {
        'category': 'cat', 'class': 'clss', 'data': 'data', 'entity': 'ent', 
        'gwp': 'gwp', 'note': 'note', 'scenario': 'scen', 'source': 'srce', 
        'tablename': 'tablename', 'type': 'tpe', 'unit': 'unit', 'family': 'family'}
    
    # %%
    # ###
    """
    *meta.primap*: PRIMAP-hist: info on sources and scenarios (emi, pop, gdp).
    """
    
    # Info on sources / scenarios.
    meta.primap = hpf.create_class(name='primap')
    meta.primap.current_primap = current_primap
    meta.primap.current_version = current_primap_srcs
    meta.primap.last_year = current_primap_last_year
    meta.primap.emi = {
        'ent': 'KYOTOGHG', 'cat': 'IPCM0EL', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': 'HISTCR', 'srce': current_primap_srcs['emi'], 'srcepmh': current_primap}
    meta.primap.pop = {
        'ent': 'POP', 'cat': 'DEMOGR', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': 'HISTORY', 'srce': current_primap_srcs['pop'], 'srcepmh': current_primap}
    meta.primap.gdp = {
        'ent': 'GDPPPP', 'cat': 'ECO', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': 'HISTORY', 'srce': current_primap_srcs['gdp'], 'srcepmh': current_primap}
    
    # %%
    """
    *meta.units*: default-units
    """

    # Preferred units.
    meta.units = hpf.create_class(name='units')
    meta.units.default = {'emi': 'MtCO2eq', 'pop': 'Pers', 'gdp': '2011GKD'}
    
    # %%
    """
    *meta.gwps*: GWPs
    """
    
    meta.gwps = hpf.create_class(name='gwps')
    meta.gwps.default = 'AR4'
    meta.gwps.all = ['SAR', 'AR2', 'AR4', 'AR5', 'AR5CCF']
    
    # %%
    """
    *meta.lulucf*: LULUCF source-priorisation
    """
    
    meta.lulucf = hpf.create_class(name='lulucf',
        source_prioritisation = [
            'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I',
            'UNFCCC2019BI', 'FAO2019BI'],
        nr_available_values = 3)
    
    # %%
    """
    *meta.gases*: basket-members, labels.
    """
    
    meta.gases = hpf.create_class(name='gases', main=['CO2', 'CH4', 'N2O'])
    meta.gases.fgases = ['HFCS', 'PFCS', 'SF6', 'NF3']
    meta.gases.kyotoghg = meta.gases.main + meta.gases.fgases
    meta.gases.hfcs = hpf.get_members_of_basket('HFCS')
    meta.gases.pfcs = hpf.get_members_of_basket('PFCS')
    meta.gases.lulucf = deepcopy(meta.gases.main)
    meta.gases.gas_to_label = {
        'CO2': 'CO$_2$', 'CH4': 'CH$_4$', 'N2O': 'N$_2$O', 'HFCS': 'HFCs',
        'PFCS': 'PFCs', 'SF6': 'SF$_6$', 'NF3': 'NF$_3$', 'KYOTOGHG': 'Kyoto GHG', 'FGASES': 'F-gases'}
    
    # %%
    """
    *meta.sectors*: main sectors, labels.
    """
    
    meta.sectors = hpf.create_class(name='sectors')
    meta.sectors.main = hpf.create_class(name='main')
    meta.sectors.main.exclLU = ['ENERGY', 'IPPU', 'AGRICULTURE', 'WASTE', 'OTHER']
    meta.sectors.main.inclLU = ['ENERGY', 'IPPU', 'AGRICULTURE', 'WASTE', 'OTHER', 'LULUCF']
    meta.sectors.main.sec_to_cat = {
        'ENERGY': 'IPC1', 'IPPU': 'IPC2', 'AGRICULTURE': 'IPCMAG', 
        'WASTE': 'IPC4', 'OTHER': 'IPC5', 'LULUCF': 'IPCMLULUCF'}
    meta.sectors.main.sec_to_label = {
        'ENERGY': 'Energy', 'IPPU': 'IPPU', 'AGRICULTURE': 'Agriculture', 
        'WASTE': 'Waste', 'OTHER': 'Other', 'LULUCF': 'LULUCF'}
    
    # %%
    """
    *meta.categories*: main categories, labels.
    """
    
    meta.categories = hpf.create_class(name='categories')
    meta.categories.main = hpf.create_class(name='main')
    meta.categories.main.exclLU = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5']
    meta.categories.main.inclLU = ['IPC1', 'IPC2', 'IPCMAG', 'IPC4', 'IPC5', 'IPCMLULUCF']
    meta.categories.main.cat_to_sec = {
        'IPC1': 'ENERGY', 'IPC2': 'IPPU', 'IPCMAG': 'AGRICULTURE', 
        'IPC4': 'WASTE', 'IPC5': 'OTHER', 'IPCMLULUCF': 'LULUCF'}
    meta.categories.main.cat_to_label = {
        'IPC1': 'Energy', 'IPC2': 'IPPU', 'IPCMAG': 'Agriculture', 'IPC4': 'Waste', 
        'IPC5': 'Other', 'IPCMLULUCF': 'LULUCF',
        'IPCM0EL': 'Total (excl. LULUCF)', 'IPC0': 'Total (incl. LULUCF)'}
    
    # %%
    """
    *meta.sources*: nice labels for sources
    """
    
    meta.sources = hpf.create_class(name='sources')
    meta.sources.srce_to_label = {
        'CRF2019': 'CRF (2019)', 'CRF2018': 'CRF (2018)', 
        'BUR3IPCC2006I': 'BUR (3$^{rd}$)', 'BUR2IPCC2006I': 'BUR (2$^{nd}$)', 'BUR1IPCC2006I': 'BUR (1$^{st}$)',
        'UNFCCC2019BI': 'UNFCCC (2019)', 'FAO2019BI': 'FAO (2019)', 
        'PRIMAPHIST22': 'PRIMAP-hist v2.2', 'PRIMAPHIST21': 'PRIMAP-hist v2.1', 'PRIMAPHIST20': 'PRIMAP-hist v2.0',
        'PMH22': 'PRIMAP-hist v2.2', 'PMH21': 'PRIMAP-hist v2.1', 'PMH20': 'PRIMAP-hist v2.0'}
    
    # %%
    """
    *meta.ndcs*: NDC types & last submission data to be considered.
    """
    
    meta.ndcs = hpf.create_class(name = 'ndcs')
    meta.ndcs.submissions_until = submission_until # For the first paper submission: 20200417, yyyymmdd
    meta.ndcs.types = ['ABS', 'RBY', 'RBU', 'ABU', 'REI', 'AEI', 'NGT']
    
    meta.ndcs.path_to_infos_from_ndcs = Path(meta.path.main, 'data', 'input', infos_from_ndcs_xlsx) # File with NDC infos
    
    meta.ndcs.path_to_cat_targets = Path(meta.path.main, "data", "CAT", "CAT_targets_20210423.csv")
    
    # %%
    return meta

# %%