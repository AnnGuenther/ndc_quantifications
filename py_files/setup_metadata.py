# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020
"""

# %%
def setup_metadata():
    """
    Set up the general metadata.
    If you want/need to change the folder for the preprocessed data, do it here.
    Returns:
    meta : class.
        Meta data needed in the quantifications and plotting routines.
    
    """
    # %%
    from pathlib import Path
    from copy import deepcopy
    import pandas as pd
    
    import helpers_functions as hpf
    
    # %%
    """
    meta.path: paths to different folders.
    """
    
    # Store general information in class meta.
    meta = hpf.create_class(name='meta')
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
    #####################################
    ##### TO BE UPDATED WHEN NEEDED #####
    #####################################
    meta.path.pc_cov = Path(meta.path.preprocess, 'pc_cov_20200702_0825')
    
    # %%
    """
    meta.isos: iso3 codes of EARTH, EU, conversion from iso3 to short country names.
    """
    
    # ISO3s of EARTH and EU28.
    meta.isos = hpf.create_class(name='isos')
    meta.isos.EARTH = hpf.get_isos_earth_only_independent()
    meta.isos.EU28 = hpf.get_isos_for_groups('EU28', 'ISO3')
    meta.isos.EARTH_EU28 = sorted(meta.isos.EARTH + ['EU28'])
    meta.isos.iso3_to_shortname = pd.Series(
        hpf.convert_isos_and_country_names(meta.isos.EARTH_EU28, 'ISO3', 'ShortName'), 
        index=meta.isos.EARTH_EU28).to_dict()
    
    # %%
    """
    SSPs: Shared Socioeconomic Pathways; info on available marker scenarios.
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
        'scen': meta.ssps.scens, 'srce': 'PMSSPBIE'}
    meta.ssps.pop = {
        'ent': 'POP', 'cat': 'DEMOGR', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': meta.ssps.scens, 'srce': 'PMSSPBIEMISC'}
    meta.ssps.gdp = {
        'ent': 'GDPPPP', 'cat': 'ECO', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': meta.ssps.scens, 'srce': 'PMSSPBIEMISC'}
        
    # %%
    """
    Nomenclature: table meta-data nomenclature.
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
    PRIMAP-hist: info on sources and scenarios (emi, pop, gdp).
    """
    
    # Info on sources / scenarios.
    meta.primap = hpf.create_class(name='primap')
    meta.primap.current_version = {
        'emi': 'PRIMAPHIST21', 'pop': 'PMHSOCIOECO21', 'gdp': 'PMHSOCIOECO21'}
    meta.primap.last_year = 2017
    meta.primap.emi = {
        'ent': 'KYOTOGHG', 'cat': 'IPCM0EL', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': 'HISTCR', 'srce': 'PRIMAPHIST21'}
    meta.primap.pop = {
        'ent': 'POP', 'cat': 'DEMOGR', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': 'HISTORY', 'srce': 'PMHSOCIOECO21'}
    meta.primap.gdp = {
        'ent': 'GDPPPP', 'cat': 'ECO', 'clss': 'TOTAL', 'tpe': 'NET',
        'scen': 'HISTORY', 'srce': 'PMHSOCIOECO21'}
    
    # %%
    """
    Default-units
    """

    # Preferred units.
    meta.units = hpf.create_class(name='units')
    meta.units.default = {'emi': 'MtCO2eq', 'pop': 'Pers', 'gdp': '2011GKD'}
    
    # %%
    """
    GWPs
    """
    
    meta.gwps = hpf.create_class(name='gwps')
    meta.gwps.default = 'AR4'
    meta.gwps.all = ['SAR', 'AR2', 'AR4', 'AR5', 'AR5CCF']
    
    # %%
    """
    LULUCF source-priorisation
    """
    
    meta.lulucf = hpf.create_class(name='lulucf',
        source_prioritisation = [
            'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I',
            'UNFCCC2019BI', 'FAO2019BI'])
    
    # %%
    """
    Gases: basket-members, labels.
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
    Sectors: main sectors, labels.
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
    Categories: main categories, labels.
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
    Nice labels for sources
    """
    
    meta.sources = hpf.create_class(name='sources')
    meta.sources.srce_to_label = {
        'CRF2019': 'CRF (2019)', 'CRF2018': 'CRF (2018)', 
        'BUR3IPCC2006I': 'BUR (3$^{rd}$)', 'BUR2IPCC2006I': 'BUR (2$^{nd}$)', 'BUR1IPCC2006I': 'BUR (1$^{st}$)',
        'UNFCCC2019BI': 'UNFCCC (2019)', 'FAO2019BI': 'FAO (2019)', 
        'PRIMAPHIST21': 'PRIMAP-hist v2.1', 'PRIMAPHIST20': 'PRIMAP-hist v2.0'}
    
    # %%
    """
    NDC types.
    """
    
    meta.ndcs = hpf.create_class(name = 'ndcs')
    meta.ndcs.types = ['ABS', 'RBY', 'RBU', 'ABU', 'REI', 'AEI', 'NGT']
    # %%
    return meta

#enddef

# %%