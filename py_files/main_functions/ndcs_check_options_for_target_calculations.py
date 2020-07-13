# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
def ndcs_check_options_for_target_calculations(meta):
    """
    Check whether the values for attributes of classes meta.calculate_targets_for, meta.ndcs_type_prioritisations,
    meta.set_pccov_to_100, and meta.strengthen_targets -- given in input_file -- are ok.
    """
    
    # %%
    import sys
    
    # %%
    if meta.method_pathways not in ['constant_percentages', 'constant_emissions']:
        sys.exit("No valid value given for method_pathways (input file).")
    
    # %%
    """
    calculate_targets_for
    If it is not to be used, use the default for all countries.
    Make new entry meta.calculate_targets_for_ctr with the final ISO3s for which targets should be calculated.
    """
        
    # If it is not to be used, use it for all countries.
    if not meta.calculate_targets_for['use_it']:
        meta.calculate_targets_for_ctr = meta.isos.EARTH
    else:
        meta.calculate_targets_for_ctr = check_countries(meta.calculate_targets_for['countries'], meta)
    
    # %%
    """
    ndcs_type_prioritisations
    If it is not to be used, use the default for all countries.
    """
    
    # If it is not to be used, use the default for all countries.
    if not meta.ndcs_type_prioritisations['use_it']:
        meta.ndcs_type_prioritisations = {
            'use_it': True, 
            'ndc_type_prios': ['TYPE_CALC'], 
            'countries': 'all'}
    
    # Only chose valid values for target types. If no valid values are given it is set to default.
    ndcs_type_prioritisations_val = [xx for xx in meta.ndcs_type_prioritisations['ndcs_type_prioritisations']
        if xx in ['TYPE_CALC', 'TYPE_ORIG'] + meta.target_types]
    if len(ndcs_type_prioritisations_val) == 0:
        
        print("No valid target types given, they are set to the default.")
        meta.ndcs_type_prioritisations['ndcs_type_prioritisations'] = ['TYPE_CALC']
    
    else:
        
        # If something is given, which contains neither 'TYPE_CALC' nor 'TYPE_ORIG', add 'TYPE_CALC' to the list.
        # Not really needed, as TYPE_CALC is used either way, when no other prioritisation has values.
        if ('TYPE_ORIG' not in ndcs_type_prioritisations_val) \
            and ('TYPE_CALC' not in ndcs_type_prioritisations_val):
            ndcs_type_prioritisations_val += ['TYPE_CALC']
            
        meta.ndcs_type_prioritisations['ndcs_type_prioritisations'] = ndcs_type_prioritisations_val
    
    # If it is not to be used, use it for all countries.
    if not meta.ndcs_type_prioritisations['use_it']:
        
        meta.ndcs_type_prioritisations['countries'] = meta.isos.EARTH
        
    else:
        
        meta.ndcs_type_prioritisations['countries'] = check_countries(meta.ndcs_type_prioritisations['countries'], meta)
    
    # %%
    """
    For countries without unconditional target: use the baseline emissions for the unconditional 
    pathway even if the conditional target is worse than the baseline (in 2030)?
    """
    
    if meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi not in [True, False]:
        
        meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = False
        print("meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi was set to False, " +
             "as the given input is not supported.")
    
    # %%
    """
    set_pccov_to_100
    """
    
    if meta.set_pccov_to_100['use_it']:
        if ((type(meta.set_pccov_to_100['countries']) == str 
            and meta.set_pccov_to_100['countries'].lower == 'all') 
            or meta.set_pccov_to_100['countries'] == ['all']):
            meta.set_pccov_to_100['countries'] = sorted(meta.isos.EARTH)
        
        meta.set_pccov_to_100['countries'] = check_countries(meta.set_pccov_to_100['countries'], meta)
    
    # %%
    """
    strengthen_targets
    """
    
    if meta.strengthen_targets['use_it']:
        
        if (meta.strengthen_targets['pc'] < 0) or (meta.strengthen_targets['pc'] > 100):
            # If meta.strengthen_targets['pc'] is not inbetween 0 and 100 (%), give out warning and do not use it.
            print("Error in input for meta.strengthen_targets['pc']. " +
                  "Values exceed limits. The option strengthen_targets not used.")
            meta.strengthen_targets['use_it'] = False
        
        elif meta.strengthen_targets['how_to'] not in ['add', 'multiply']:
            # If how_to is not add or multiply do not use it.
            print("Error in input for meta.strengthen_targets['how_to']. " +
                  "It must be 'add' or 'multiply'. The option strengthen_targets is not used.")
            meta.strengthen_targets['use_it'] = False
        
        else:
            # Else use it and check the countries.
            meta.strengthen_targets['use_it'] = True
            if ((type(meta.strengthen_targets['countries']) == str 
                and meta.strengthen_targets['countries'].lower == 'all') 
                or meta.strengthen_targets['countries'] == ['all']):
                meta.strengthen_targets['countries'] = sorted(meta.isos.EARTH)
            else:
                meta.strengthen_targets['countries'] = check_countries(meta.strengthen_targets['countries'], meta)
    
    #%%
    """meta.use_ndc_emissions_if_available"""
    if meta.use_ndc_emissions_if_available not in [True, False]:
        meta.use_ndc_emissions_if_available = True
        print(f"meta.use_ndc_emissions_if_available set to {meta.use_ndc_emissions_if_available} as given value could not be used.")
        
    # %%
    return meta
#enddef

# %%
def check_countries(countries, meta):
    """
    Check for valid country codes.
    """
    
    # %%
    import sys
    
    # %%
    
    # Check which ISO3s were in the list but are not valid.
    countries_save = countries
    
    # If countries are 'all', replace them by all ISO3s.
    if ((type(countries) == str 
        and countries.lower() == 'all') 
        or countries == ['all']):
        countries = sorted(meta.isos.EARTH)
        countries_save = meta.isos.EARTH
    
    # Only use ISO3s that are in meta.isos.EARTH.
    countries = [xx for xx in countries if xx in meta.isos.EARTH + ['EU28']]
    
    # If 'EU28' is in countries replace it by the single EU28 countries and remove it from list.
    if 'EU28' in countries:
        countries = sorted(list(set(countries + meta.isos.EU28) - set(['EU28'])))
    
    # If no ISO3s are left for which targets should be calculated exit the program.
    if len(countries) == 0:
        sys.exit("No valid countries given.")
    
    # Check which ISO3s were in the list but are not valid.
    if len(countries) != len(countries_save):
        txt = "Some countries were removed from given list (" + \
            ', '.join(sorted(list(set(set(countries_save) - set(countries))))) + ")."
        if 'EU28' in countries_save:
            print(txt + " EU28 was replaced by single countries.")
        else:
            print(txt)
    
    # %%
    return countries
    
# %%