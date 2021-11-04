# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in April 2020.
"""

# %%
def plot_maps_bins(pd_series, path_to_file, **kwargs):
    """
    Plot coloured countries with 10 (or nr_bins) equally sized 'colour-bins'.
    
    kwargs:
        title (string)
        annotation (string)
        bounds (list of boundaries for the bins)
        nr_bins (int)
        colours (pd.DataFrame with 255 rows and columns=['r', 'g', 'b']) # red, green, blue
        flipud (True if you want it to be flipped)
        val_min (int or float)
        val_max (int or float)
        nr_instances (if True, then add the information on how many countries lie in one bin to the legend)
        plot_pdf (if True the figure will additionally be plotted as pdf)
        transparent (if True plot the figure background transparent)
    """
    # %%
    import pandas as pd
    import numpy as np
    import helpers_functions as hpf
    
    # %%    
    pd_series_new = pd.Series(index=pd_series.index, dtype='object')
    
    if 'colours' not in kwargs.keys():
        from setup_metadata import setup_metadata
        from pathlib import Path
        colours = pd.read_csv(Path(setup_metadata().path.py_files, 'additional_scripts', 
            'plotting', 'colours', 'colourmap_plasma.csv'))
    else:
        colours = kwargs['colours']
    
    colours.index = range(0, colours.shape[0])
    # 'flipud' colours.
    if ('flipud' in kwargs.keys() and kwargs['flipud']):
        colours.index = np.arange(colours.index[-1], colours.index[0] - 1, -1)
    
    # 10 bins of the same size.
    val_min = (kwargs['val_min'] if 'val_min' in kwargs.keys() else pd_series.min())
    val_min = (0 if np.floor(val_min) == 0 else val_min)
    val_max = (kwargs['val_max'] if 'val_max' in kwargs.keys() else pd_series.max())
    nr_bins = (kwargs['nr_bins'] if 'nr_bins' in kwargs.keys() else 10)
    # nr_bins is only used if bounds is not given.
    bounds = (kwargs['bounds'] if 'bounds' in kwargs.keys() else 
        list(np.arange(val_min, val_max, (val_max-val_min)/nr_bins))[1:])
        
    colour_dict = {}
    
    for irange in range(len(bounds)):
        if irange == 0:
            ival = "< " + "{:.2f}".format(bounds[irange]) + "%"
            pd_series_new[pd_series < bounds[irange]] = ival
            colour_dict[ival] = colours.loc[0, :].to_list()
        
        if irange < len(bounds)-1:
            ival = "{:.2f}".format(bounds[irange]) + "% - " + "{:.2f}".format(bounds[irange+1]) + "%"
            pd_series_new[((pd_series >= bounds[irange]) & (pd_series < bounds[irange+1]))] = ival
            colour_dict[ival] = colours.loc[int(colours.shape[0]/len(bounds)*(irange+1)), :].to_list()
        
        if irange == len(bounds)-1:
            ival = "> " + "{:.2f}".format(bounds[irange]) + "%"
            pd_series_new[pd_series >= bounds[irange]] = ival
            colour_dict[ival] = colours.loc[colours.shape[0]-1, :].to_list()
        
    # Remove the countries with nans.
    pd_series_new.drop(index=pd_series.index[pd_series_new.isnull()], inplace=True)
    
    annotation = ("" if 'annotation' not in kwargs.keys() else kwargs['annotation'])
    title = ("" if 'title' not in kwargs.keys() else kwargs['title'])
    nr_instances = (True if ('nr_instances' in kwargs.keys() and kwargs['nr_instances']) else False)
    plot_pdf = (True if ('plot_pdf' in kwargs.keys() and kwargs['plot_pdf']) else False)
    transparent = (True if ('transparent' in kwargs.keys() and kwargs['transparent']) else False)
    
    hpf.plot_maps(pd_series_new, colour_dict, path_to_file, 
        annotation=annotation, title=title, nr_instances=nr_instances, plot_pdf=plot_pdf,
        transparent=transparent)

# %%