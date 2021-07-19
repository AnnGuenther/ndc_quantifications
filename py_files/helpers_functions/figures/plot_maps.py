# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in April 2020.

Code adapted from https://github.com/mkudija/blog/blob/master/content/downloads/code/country-maps/cartopy_countries.py!
"""
# %%
def plot_maps(pd_series, colour_dict, path_to_file, **kwargs):
    """
    Plot a world map with coloured countries.
    
    Countries in pd_series (index=iso3s, values=some kind of 'type' for which colours are given in colour_dict).
    colour_dict: keys are the 'types', and values are tuples or (r, g, b) or other types of colour indications.
    
    Optional:
        colour_nan_countries: colour for countries that do not have a value in colour_dict. Default: (.8, .8, .8)
        annotation (text)
        title (text)
        nr_instances (if True, the number of countries with the 'type' are stated in the legend)
        plot_pdf (if True the figure will additionally be plotted as pdf)
    
    # http://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/ data need to be downloaded.
    """
    # %%
    import matplotlib.pyplot as plt
    import cartopy
    import cartopy.io.shapereader as shpreader
    import cartopy.crs as ccrs
    import matplotlib.patches as mpatches
    import pandas as pd
    import helpers_functions as hpf
    from setup_metadata import setup_metadata
    
    meta = setup_metadata()
    
    # %%
    # Store data.
    data_map = pd.DataFrame(columns=['colours', 'values'])
    data_map.loc[:, 'values'] = pd_series
    
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(1, 1, 1)
    
    ax = plt.axes(projection=ccrs.Robinson())
    ax.add_feature(cartopy.feature.OCEAN, facecolor='white')
    ax.outline_patch.set_edgecolor((1, 1, 1))
    
    # Info from shapefile.
    shpfilename = shpreader.natural_earth(resolution='110m',
        category='cultural', name='admin_0_countries')
    reader = shpreader.Reader(shpfilename)
    countries = reader.records()
    
    #pd_series.drop(pd_series.index[pd_series.isnull()], inplace=True)
    
    for country in countries:
        
        iso3 = country.attributes['ADM0_A3'] # ISO_A3 does not work well
        #iso3_2 = country.attributes['ISO_A3']
        
        # Get colour
        if iso3 in pd_series.index:
            colour = colour_dict[pd_series[iso3]]
        
        #elif iso3_2 in pd_series.index:
        #    colour = colour_dict[pd_series[iso3_2]]
        
        else:
            
            if 'colour_nan_countries' in kwargs.keys():
                colour = kwargs['colour_nan_countries']
            
            else:
                colour = (.8, .8, .8)
        
        ax.add_geometries(country.geometry, ccrs.PlateCarree(),
            facecolor=(colour), label=iso3,
            edgecolor=(1, 1, 1), linewidth=.25)
        data_map.loc[iso3, 'colours'] = colour
    
    # legend
    values = list(colour_dict.keys())
    
    # Put in the number of countries with a certain value, if wanted.
    if ('nr_instances' in kwargs.keys() and kwargs['nr_instances']):
    
        nr_instances = [len(pd_series.index[pd_series == xx]) for xx in values]
        values_print = [f"{xx[0]} ({xx[1]})" for xx in zip(list(colour_dict.keys()), nr_instances)]
    
    else:
        values_print = values
    
    handles = []
    for i in range(len(values)):
        
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colour_dict[values[i]]))
        plt.legend(handles, values_print, loc='lower left', bbox_to_anchor=(0.06, 0.05), 
            fancybox=True, frameon=False, fontsize=5)

    # annotate
    if 'annotation' in kwargs.keys():
        ax.annotate(kwargs['annotation'], xy=(0, 0),  xycoords='figure fraction',
            xytext=(0.08, -0.025), textcoords='axes fraction',
            ha='left', va='top', fontsize=4.5)
    
    if 'title' in kwargs.keys():
        plt.title(kwargs['title'], fontsize=6)
    
    fig.subplots_adjust(left=.01, right=.99, bottom=.01, top=.99)
    plt.savefig(path_to_file, bbox_inches='tight', pad_inches=.01, dpi=300,
        transparent=(True if ('transparent' in kwargs.keys() and kwargs['transparent']) else False))
    
    if ('plot_pdf' in kwargs.keys() and kwargs['plot_pdf']):
        path_to_pdf = str(path_to_file).replace('.png', '.pdf')
        plt.savefig(path_to_pdf, bbox_inches='tight', pad_inches=.2, dpi=300)
        hpf.crop_pdf(path_to_pdf)
    
    plt.close()
    
    return data_map

# %%