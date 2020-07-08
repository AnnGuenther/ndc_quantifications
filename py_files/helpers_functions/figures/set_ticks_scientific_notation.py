# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last updated in 02/2020
"""

# %%
def set_ticks_scientific_notation(axa, which_axis, **kwargs):
    """
    Get scientific notation in steps of 3 (-6, -3, +3, +6, +9, etc.).
    
    INPUT:
        axa is current plot
        which_axis is 'y' or 'x' or 'xy'
        kwargs:
            power_limit: int
                When abs(max(power)) <= power_limit will not be converted.
    """
    
    # %%
    axis = []
    if 'x' in which_axis:
        axis.append('x')
    
    if 'y' in which_axis:
        axis.append('y')
    
    XL = axa.get_xlim()
    YL = axa.get_ylim()
    info = {'x': {'ticks': axa.get_xticks(), 'ticklabels': axa.get_xticklabels(), 'lims': XL},
            'y': {'ticks': axa.get_yticks(), 'ticklabels': axa.get_yticklabels(), 'lims': YL}}
    
    for ax in axis:
        # Only use the ones > xlim[0] and < xlim[-1]
        ticks = info[ax]['ticks']
        lims = info[ax]['lims']
        ticks_valid = [xx for xx in range(len(ticks)) if (ticks[xx] >= lims[0]) and (ticks[xx] <= lims[-1])]
        ticks = ticks[ticks_valid]
        ticklabels = list(info[ax]['ticklabels'])
        ticklabels = [ticklabels[xx] for xx in ticks_valid]
        # Get info on min and max.
        lowest = ticks[0]
        highest = ticks[-1]
        get_pot_lowest = [float(xx) for xx in '{:.2e}'.format(lowest).split('e')]
        get_pot_lowest = get_pot_lowest[1] - get_pot_lowest[1] % 3
        get_pot_highest = [float(xx) for xx in '{:.2e}'.format(highest).split('e')]
        get_pot_highest = get_pot_highest[1] - get_pot_highest[1] % 3
        # Don't use 0.
        get_pot = [xx for xx in [get_pot_lowest, get_pot_highest] if xx != 0.]
        # Only change the ticklabels if needed.
        if len(get_pot) > 0:
            get_pot = max(get_pot)
        else:
            get_pot = 0
        
        if abs(get_pot) > abs((kwargs['power_limit'] if 'power_limit' in kwargs.keys() else 0)):
            
            ticklabels = []
            for tick in ticks:
                tick_str = '{:.2e}'.format(tick)
                tick_str_components = tick_str.split('e')
                tick_num_components = [float(xx) for xx in tick_str_components]
                tick_num_components[0] = tick_num_components[0]*(10**(tick_num_components[1]-get_pot))
                tick_num_components[1] = get_pot
                rest = tick_num_components[1] % 3
                new_str = '{:.1f}'.format(tick_num_components[0] * 10**rest)
                ticklabels.append(new_str)
            
            if all([True if xx[-1] == '0' else False for xx in ticklabels]):
                ticklabels = [xx[:-2] for xx in ticklabels]
            
            if ax == 'x':
                axa.set_xticks(ticks)
                axa.set_xticklabels(ticklabels)
                axa.text(XL[1], YL[0], '1e' + '{:+}'.format(int(get_pot)), ha='left', va='top',
                         fontsize=axa.xaxis.get_major_ticks()[0].label.get_fontsize()*.8)
            
            if ax == 'y':
                axa.set_yticks(ticks)
                axa.set_yticklabels(ticklabels)
                axa.text(XL[0], YL[1], '1e' + '{:+}'.format(int(get_pot)), ha='left', va='bottom',
                         fontsize=axa.yaxis.get_major_ticks()[0].label.get_fontsize())
    
    return axa

# %%