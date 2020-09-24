# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 03/2020.
"""

# %%
class create_table():
    
    """
    Create a table (is a class) with different attributes and functions.
    
    INPUT:
        give different attributes if wanted (e.g., create_table(ent='CO2', cat='IPCM0EL'))
    
    Attributes:
        data: pd.DataFrame with index=iso3s or regions, and columns=years as integers.
        unit
        gwp: Global warming potential is only needed for emissions.
        tablename: ent_cat_clss_tpe_scen_srce.
        ent: entity, such as CO2, POP, GDPPPP.
        cat: category, such as IPC1, DEMOGR, ECO.
        clss: class, such as TOTAL, LIQUID.
        tpe: type, such as NET, REMOV.
        scen: scenario, such as HISTCR.
        srce: source, such as CRF2019.
        family: emissions, or population, or gdp.
        note
    """
    
    # %%
    def __init__(self, **kwargs):
        
        """
        Create the class with attributes.
        kwargs: the attriutes with values (e.g., ent='CO2', cat='IPCM0EL')
        """
        
        for ind in kwargs.keys():
            
            if ind != 'name':
                setattr(self, ind, kwargs[ind])
            else:
                self.__name__ = kwargs[ind]
    
    # %%
    def __tablename_to_standard__(self):
        
        """
        Tablename from attributes in 'tablename_from'.
        """
        
        tablename_from = ['ent', 'cat', 'clss', 'tpe', 'scen', 'srce']
        
        if all([hasattr(self, xx) for xx in tablename_from]):
            self.tablename = '_'.join([getattr(self, xx) for xx in tablename_from])
        
        return self
    
    # %%
    def __name_to_standard__(self):
        
        """
        Use the tablename as the __name__.
        """
        
        tablename_from = ['ent', 'cat', 'clss', 'tpe', 'scen', 'srce']
        
        if all([hasattr(self, xx) for xx in tablename_from]):
            self.__name__ = '_'.join([getattr(self, xx) for xx in tablename_from])
        return self
    
    # %%
    def __attrs_primap_to_ndcs__(self):
        
        """
        Convert the attributes from primap-table to nomenclature used here.
        """
        
        from setup_metadata import setup_metadata
        import helpers_functions as hpf
        
        meta = setup_metadata()
        
        attrs = hpf.get_all_attributes_of_class(self)
        
        for attr in attrs:
            if (attr in meta.nomenclature.oldname_to_attr.keys()
                and attr != meta.nomenclature.oldname_to_attr[attr]):
                setattr(self, meta.nomenclature.oldname_to_attr[attr], 
                    getattr(self, attr))
                delattr(self, attr)
    
    # %%
    def __plot__(self, **kwargs):
        
        """
        Plot data.
        
        Optional:
            isos = ['BRA', 'EU28']
            years = [1990, 2000, 2010], or range(1990, 2011)
        """
        
        import matplotlib.pyplot as plt
        from setup_metadata import setup_metadata
        
        isos_earth = setup_metadata().isos.EARTH
        isos = ([xx for xx in (kwargs['isos'] if type(kwargs['isos']) == list else [kwargs['isos']]) if xx in isos_earth] 
            if 'isos' in kwargs.keys() 
            else sorted(set(self.data.index) & set(isos_earth)))
        
        years = ((kwargs['years'] if type(kwargs['years']) == list else ([kwargs['years']] if type(kwargs['years']) != range else list(kwargs['years']))) 
            if 'years' in kwargs.keys() 
            else [xx for xx in self.data.columns])
        
        ax = self.data.reindex(index=isos).reindex(columns=years).transpose().plot()
        plt.plot(ax.get_xlim(), [0, 0], ':k', linewidth=.5)
        
        return ax
    
    # %%
    def __convert_unit__(self, unitTo, **kwargs):
        
        """
        Convert the unit of the table into unitTo.
        kwargs: gwp if wanted.
        
        If the data are emissions data, pay attention to the GWP.
        For a basket: only CO2eq units are allowed, and the gwpFrom and gwpTo have to be equal.
        """
        
        import sys
        from helpers_functions.units.get_conversion_unit import get_conversion_unit
        
        unitFrom = self.unit
        entity = self.ent
        
        if hasattr(self, 'gwp'):
            gwpFrom = self.gwp
        
        if 'CO2eq' in unitTo:
            
            if 'gwpTo' in kwargs.keys():
                gwpTo = kwargs['gwpTo']
            elif 'gwp' in kwargs.keys():
                gwpTo = kwargs['gwp']
            else:
                gwpTo = gwpFrom # Produces error if unitFrom is not in CO2eq.
        
        if any([xx in entity for xx in ['HFCS', 'PFCS', 'FGASES', 'KYOTOGHG']]):
            
            if ('CO2eq' not in unitTo or gwpFrom != gwpTo):
                sys.exit("create_table.py __convert_unit__: for a basket, unitFrom and unitTo "
                          "have to be in CO2eq and the gwpFrom and gwpTo have to be equal.")
            else:
                conversion = get_conversion_unit(unitFrom, unitTo)
        
        else:
            if ('gwpFrom' in locals() and 'gwpTo' in locals()):
                conversion = get_conversion_unit(unitFrom, unitTo, entity=entity, gwpFrom=gwpFrom, gwpTo=gwpTo)
            elif ('gwpFrom' in locals() and not 'gwpTo' in locals()):
                conversion = get_conversion_unit(unitFrom, unitTo, entity=entity, gwp=gwpFrom)
            elif ('gwpFrom' not in locals() and 'gwpTo' in locals()):
                conversion = get_conversion_unit(unitFrom, unitTo, entity=entity, gwp=gwpTo)
            else:
                conversion = get_conversion_unit(unitFrom, unitTo)
        
        if 'gwpTo' in locals():
            self.gwp = gwpTo
        elif hasattr(self, 'gwp'):
            del self.gwp
        
        self.data = self.data * conversion
        self.unit = unitTo
        
        return self
    
    # %%
    def __convert_to_baseunit__(self):
        
        """
        Convert the table to the baseunit (depends on data family).
        """
        
        from helpers_functions.units.get_baseunit import get_baseunit
        
        new_unit, _ = get_baseunit(self.unit)
        self.__convert_unit__(new_unit)
        
        return self
    
    # %%
    def __convert_to_nice_unit__(self, **kwargs):
        
        """
        Convert the table to 'nice looking unit' that fits the magnitude of the data.
        Does basically only make sense for single time series, as between countries it can differ a lot.
        """
        
        from helpers_functions.units.get_conversion_to_nice_unit import get_conversion_to_nice_unit
        
        unit_new, multiplier = get_conversion_to_nice_unit(self.data, self.unit, kwargs)
        
        self.unit = unit_new
        self.data = self.data * multiplier
        
        return self
    
    # %%
    def __change_gwp__(self, gwpTo):
        
        """
        Change the GWP of emissions data.
        Only works if the family == 'emi' and 
        """
        
        import sys
        from helpers_functions.units.get_conversion_gwp import get_conversion_gwp
        
        if not self.family == 'emi':
            sys.exit("create_table __change_gwp__: changing the GWP only works for emissions data.")
        elif not hasattr(self, 'gwp'):
            sys.exit("create_table.py __change_gwp__: cannot change GWP from no-GWP to GWP.")
        elif gwpTo != self.gwp:
            
            if any([xx in self.ent for xx in ['HFCS', 'PFCS', 'FGASES', 'KYOTOGHG']]):
                sys.exit("create_table.py __change_gwp__: cannot change GWP for baskets.")
            else:
                self.data = self.data * get_conversion_gwp(self.gwp, gwpTo, self.ent)
                self.gwp = gwpTo
        
        return self
    
    # %%
    def __extrapolate__(self, method, direction, **kwargs):
        
        """
        Extrapolate all time series of the table.
        Use the given method and direction.
        Check timeseries_extrapolate.py for more information.
        """
        
        from helpers_functions.data_manipulation.timeseries_extrapolate import timeseries_extrapolate
        
        period = (kwargs['period'] if 'period' in kwargs.keys() else None)
        nrvalues = (kwargs['nrvalues'] if 'nrvalues' in kwargs.keys() else None)
        
        self.data = timeseries_extrapolate(self.data, method, direction, period=period, nrvalues=nrvalues)
        
        return self
    
    # %%
    def __interpolate__(self, method):
        
        """
        Interpolate all time series of the table.
        Use the given method.
        Check timeseries_interpolate.py for more information.
        """
        
        from helpers_functions.data_manipulation.timeseries_interpolate import timeseries_interpolate
        
        self.data = timeseries_interpolate(self.data, method)
        
        return self
    
    # %%
    def __mean_nrvalues__(self, nrvalues):
        
        """
        Use the mean over the last available years (nrvalues) and put it into the years after the last available years.
        Check timeseries_mean_nrvalues.py for more information.
        """
        
        from helpers_functions.data_manipulation.timeseries_mean_nrvalues import timeseries_mean_nrvalues
        
        self.data = timeseries_mean_nrvalues(self.data, nrvalues)
        
        return self
    
    # %%
    def __reindex__(self, **kwargs):
        
        """
        Reindex the table.data with 
            isos or index=list of isos and 
            years or columns=range of integers or list of integers.
        """
        
        from setup_metadata import setup_metadata
        
        isos_earth = setup_metadata().isos.EARTH
        isos = ([xx for xx in (kwargs['isos'] if type(kwargs['isos']) == list else [kwargs['isos']]) if xx in isos_earth] 
            if 'isos' in kwargs.keys() 
            else sorted(set(self.data.index) & set(isos_earth)))
        
        years = ((kwargs['years'] if type(kwargs['years']) == list else ([kwargs['years']] if type(kwargs['years']) != range else list(kwargs['years']))) 
            if 'years' in kwargs.keys() 
            else [xx for xx in self.data.columns])
        
        self.data = self.data.reindex(index=isos).reindex(columns=years)
        
        return self
    
    # %%
    def __subset__(self, **kwargs):
        
        """
        Create a table with a subset of the isos and years in the table.
        Optional input:
            isos = list of iso3s
            years = range of years or list of years (as integers)
        Returns a new table, not self.
        """
        
        from helpers_functions.classes_tables.copy_table import copy_table
        from setup_metadata import setup_metadata
        
        isos_earth = setup_metadata().isos.EARTH
        isos = ([xx for xx in (kwargs['isos'] if type(kwargs['isos']) == list else [kwargs['isos']]) if xx in isos_earth] 
            if 'isos' in kwargs.keys() 
            else sorted(set(self.data.index) & set(isos_earth)))
        
        years = ((kwargs['years'] if type(kwargs['years']) == list else ([kwargs['years']] if type(kwargs['years']) != range else list(kwargs['years']))) 
            if 'years' in kwargs.keys() 
            else [xx for xx in self.data.columns])
        
        table = copy_table(self)
        
        table.data = table.data.reindex(index=isos)
        table.data = table.data.reindex(columns=years)
        
        return table
    
    # %%
    def __global_share__(self, **kwargs):
        
        """
        Create a table with the global share.
        Does not check if all countries are available ...
        Neither if it does make sense to calculate a global share.
        
        Optional: give isos and years for which to calculate the global share.
        """
        
        import pandas as pd
        import numpy as np
        from setup_metadata import setup_metadata
        from helpers_functions.data_manipulation.ratios_w_zeros import ratios_w_zeros
        
        # Get all valid ISO3s.
        isos_earth = setup_metadata().isos.EARTH
        isos = ([xx for xx in (kwargs['isos'] if type(kwargs['isos']) == list else [kwargs['isos']]) if xx in isos_earth] 
            if 'isos' in kwargs.keys() 
            else sorted(set(self.data.index) & set(isos_earth)))
        
        years = ((kwargs['years'] if type(kwargs['years']) == list else ([kwargs['years']] if type(kwargs['years']) != range else list(kwargs['years']))) 
            if 'years' in kwargs.keys() 
            else [xx for xx in self.data.columns])
        
        sum_earth = self.data. \
            reindex(index=isos_earth). \
            reindex(columns=years).sum(axis=0)
        
        ratios = pd.DataFrame(ratios_w_zeros(
            np.array(self.data.reindex(index=isos).reindex(columns=years)),
            [list(sum_earth)] *  len(isos)), index=isos, columns=years)
        
        return ratios
        
# %%