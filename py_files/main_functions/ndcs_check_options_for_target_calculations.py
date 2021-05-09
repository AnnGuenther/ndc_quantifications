# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 11/2020.
"""

# %%
def ndcs_check_options_for_target_calculations(meta):
    """
    Check whether the values for attributes of classes meta.calculate_targets_for, meta.ndcs_type_prioritisations,
    meta.set_pccov_to_100, meta.strengthen_targets, etc. -- given in input_file -- are ok.
    If nothing is given, or the given values are not ok, set them to default values or exit.
    """
    
    # %%
    import sys
    import helpers_functions as hpf
    
    # %%
    """
    calculate_targets_for
    If it is not to be used, use the default for all countries (excl. USA).
    Make new entry meta.calculate_targets_for_ctr with the final ISO3s for which targets should be calculated.
    """
    if 'calculate_targets_for' not in hpf.get_all_attributes_of_class(meta):
        
        meta.calculate_targets_for = {
            'use_it': True,
            'countries': sorted(set(set(meta.isos.EARTH) - set(['USA'])))}
        print("\nmeta.calculate_targets_for set to default!")
    
    else:
        
        """
        If it is not to be used, use it for all countries (excl. USA).
        """
        
        if not meta.calculate_targets_for['use_it']:
            
            meta.calculate_targets_for_ctr = sorted(set(set(meta.isos.EARTH) - set(['USA'])))
        
        else:
            
            meta.calculate_targets_for_ctr = check_countries(meta.calculate_targets_for['countries'], meta)
    
    # %%
    """
    ndcs_type_prioritisations
    If it is not to be used, use the default for all countries.
    """
    if 'ndcs_type_prioritisations' not in hpf.get_all_attributes_of_class(meta):
        
        meta.ndcs_type_prioritisations = {
            'use_it': True, 
            'ndcs_type_prioritisations': ['TYPE_RECLASS'], 
            'countries': 'all'}
        print("\nmeta.ndcs_type_prioritisations set to default!")
    
    else:
        
        # If it is not to be used, use the default for all countries.
        if not meta.ndcs_type_prioritisations['use_it']:
            
            meta.ndcs_type_prioritisations = {
                'use_it': True, 
                'ndc_type_prios': ['TYPE_RECLASS'], 
                'countries': 'all'}
        
        # Only chose valid values for target types. If no valid values are given it is set to default.
        ndcs_type_prioritisations_val = [xx for xx in meta.ndcs_type_prioritisations['ndcs_type_prioritisations']
            if xx in ['TYPE_RECLASS', 'TYPE_MAIN'] + meta.target_types]
        
        if len(ndcs_type_prioritisations_val) == 0:
            
            print("\nNon-valid target types given, they are set to the default.")
            meta.ndcs_type_prioritisations['ndcs_type_prioritisations'] = ['TYPE_RECLASS']
        
        else:
            
            # If something is given, which contains neither 'TYPE_RECLASS' nor 'TYPE_MAIN', add 'TYPE_RECLASS' to the list.
            # Not really needed, as TYPE_RECLASS is used either way, when no other prioritisation has values.
            
            if ('TYPE_MAIN' not in ndcs_type_prioritisations_val) \
                and ('TYPE_RECLASS' not in ndcs_type_prioritisations_val):
                
                    ndcs_type_prioritisations_val += ['TYPE_RECLASS']
                
            meta.ndcs_type_prioritisations['ndcs_type_prioritisations'] = ndcs_type_prioritisations_val
        
        # If it is not to be used, use it for all countries.
        if not meta.ndcs_type_prioritisations['use_it']:
            
            meta.ndcs_type_prioritisations['countries'] = meta.isos.EARTH
            
        else:
            
            meta.ndcs_type_prioritisations['countries'] = check_countries(meta.ndcs_type_prioritisations['countries'], meta)
    
    #%%
    """
    use_ndc_emissions_if_available
    """
    
    if 'use_ndc_emissions_if_available' not in hpf.get_all_attributes_of_class(meta):
        
        if meta.ndcs_type_prioritisations['ndcs_type_prioritisations'][0] == 'TYPE_RECLASS':
            
            meta.use_ndc_emissions_if_available = True
            print("\nmeta.use_ndc_emissions_if_available set to True as type_prio is TYPE_RECLASS!")
        
        elif meta.ndcs_type_prioritisations['ndcs_type_prioritisations'][0] == 'TYPE_MAIN':
            
            meta.use_ndc_emissions_if_available = False
            print("\nmeta.use_ndc_emissions_if_available set to False as type_prio is TYPE_MAIN!")
        
        else:
            
            sys.exit("meta.use_ndc_emissions_if_available is not set!")
    
    else:
        
        if (meta.use_ndc_emissions_if_available == True and
            
            meta.ndcs_type_prioritisations['ndcs_type_prioritisations'][0] != 'TYPE_RECLASS'):
            print("\ntype_prio is not type_reclass, but use_ndc_emissions_if_available is True. Check that!")
        
        elif (meta.use_ndc_emissions_if_available == False and
            meta.ndcs_type_prioritisations['ndcs_type_prioritisations'][0] != 'TYPE_MAIN'):
            
            print("\ntype_prio is not type_main, but use_ndc_emissions_if_available is False. Check that!")
            
        elif meta.use_ndc_emissions_if_available not in [True, False]:
            
            if meta.ndcs_type_prioritisations['ndcs_type_prioritisations'][0] == 'TYPE_RECLASS':
                
                meta.use_ndc_emissions_if_available = True
                print(f"\nmeta.use_ndc_emissions_if_available set to True " + 
                    "as given value could not be used and type_prio is type_reclass.")
            
            elif meta.ndcs_type_prioritisations['ndcs_type_prioritisations'][0] == 'TYPE_MAIN':
                
                meta.use_ndc_emissions_if_available = False
                print(f"\nmeta.use_ndc_emissions_if_available set to False " + 
                    "as given value could not be used and type_prio is type_main.")
            
            else:
                
                meta.use_ndc_emissions_if_available = True
                print(f"\nmeta.use_ndc_emissions_if_available set to True " + 
                    "as given value could not be used.")
        
    # %%
    """
    set_pccov_to_100
    """
    
    if 'set_pccov_to_100' not in hpf.get_all_attributes_of_class(meta):
        
        meta.set_pccov_to_100 = {'use_it': False}
        print("\nmeta.set_pccov_to_100 not used, as it is not given!")
    
    else:
        
        if meta.set_pccov_to_100['use_it']:
            
            if ((type(meta.set_pccov_to_100['countries']) == str 
                and meta.set_pccov_to_100['countries'].lower == 'all') 
                or meta.set_pccov_to_100['countries'] == ['all']):
                
                meta.set_pccov_to_100['countries'] = sorted(meta.isos.EARTH)
            
            meta.set_pccov_to_100['countries'] = check_countries(meta.set_pccov_to_100['countries'], meta)
    
    # %%
    if 'method_pathways' not in hpf.get_all_attributes_of_class(meta):
        
        meta.method_pathways = 'constant_percentages'
        print("\nmeta.method_pathways set to constant_percentages as nothing was given!")
    
    else:
        
        if meta.method_pathways not in ['constant_percentages', 'constant_difference', 'constant_emissions']:
            
            sys.exit("A non-valid value given for method_pathways (input file).")
    
    # %%
    """
    For countries without unconditional target: use the baseline emissions for the unconditional 
    pathway even if the conditional target is worse than the baseline (in 2030)?
    """
    
    if 'use_baseline_for_uncondi_even_if_baseline_is_better_than_condi' not in \
        hpf.get_all_attributes_of_class(meta):
        
        meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = False
        print("\nmeta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi not used, as nothing was given!")
    
    else:
        
        if meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi not in [True, False]:
            
            meta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi = False
            print("\nmeta.use_baseline_for_uncondi_even_if_baseline_is_better_than_condi was set to False, " +
                 "as the given input is not supported.")
    
    # %%
    """
    For countries that have a target (2030 value of pathway) above baseline:
    use the baseline emissions.
    """
    
    if 'use_baseline_if_target_above_bl' not in \
        hpf.get_all_attributes_of_class(meta):
        
        meta.use_baseline_if_target_above_bl = False
        print("\nmeta.use_baseline_if_target_above_bl not used, as nothing was given!")
    
    else:
        
        if meta.use_baseline_if_target_above_bl not in [True, False]:
            
            meta.use_baseline_if_target_above_bl = False
            print("\nmeta.use_baseline_if_target_above_bl was set to False, " +
                 "as the given input is not supported.")
    
    # %%
    """
    strengthen_targets
    """
    
    if 'strengthen_targets' not in hpf.get_all_attributes_of_class(meta):
        
        meta.strengthen_targets = {'use_it': False}
        print("\nmeta.strengthen_targets not used, as nothing was given!")
    
    else:
        
        if meta.strengthen_targets['use_it']:
            
            if (meta.strengthen_targets['pc'] < 0) or (meta.strengthen_targets['pc'] > 100):
                
                # If meta.strengthen_targets['pc'] is not inbetween 0 and 100 (%), give out warning and do not use it.
                print("\nError in input for meta.strengthen_targets['pc']. " +
                      "Values exceed limits. The option strengthen_targets not used.")
                meta.strengthen_targets['use_it'] = False
            
            elif meta.strengthen_targets['how_to'] not in ['add', 'multiply']:
                
                # If how_to is not add or multiply do not use it.
                print("\nError in input for meta.strengthen_targets['how_to']. " +
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
    
    # %%
    """
    groups_for_which_to_calculate_pathways (not checking for correct input here...)
    """
    
    if 'groups_for_which_to_calculate_pathways' not in hpf.get_all_attributes_of_class(meta):
        
        meta.groups_for_which_to_calculate_pathways = []
        print("\nmeta.groups_for_which_to_calculate_pathways set to [], as nothing was given!")
    
    # %%
    """
    use_CAT_targets
    """
    
    if 'use_CAT_targets' not in hpf.get_all_attributes_of_class(meta):
        
        meta.use_CAT_targets = {'use_it': False}
        print("\nmeta.use_CAT_targets not used, as it is not given!")
    
    else:
        
        if meta.use_CAT_targets['use_it']:
            
            if ((type(meta.use_CAT_targets['countries']) == str 
                and meta.use_CAT_targets['countries'].lower == 'all') 
                or meta.use_CAT_targets['countries'] == ['all']):
                
                meta.use_CAT_targets['countries'] = sorted(meta.isos.EARTH)
            
            meta.use_CAT_targets['countries'] = check_countries(meta.use_CAT_targets['countries'], meta)
    
    # %%
    return meta

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
    countries = [xx for xx in countries if xx in meta.isos.EARTH + [meta.EU]]
    
    # If meta.EU is in countries replace it by the single EU countries and remove it from list.
    if meta.EU in countries:
        
        countries = sorted(list(set(countries + meta.EU_isos) - set([meta.EU])))
    
    # If no ISO3s are left for which targets should be calculated exit the program.
    if len(countries) == 0:
        
        sys.exit("No valid countries given.")
    
    # Check which ISO3s were in the list but are not valid.
    if len(countries) != len(countries_save):
        
        txt = "Some countries were removed from given list (" + \
            ', '.join(sorted(list(set(set(countries_save) - set(countries))))) + ")."
        
        if meta.EU in countries_save:
            
            print(txt + f" {meta.EU} was replaced by single countries.")
        
        else:
            
            print(txt)
    
    # %%
    return countries
    
# %%