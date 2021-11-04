# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Modified by Mika Pflüger

Last updated in 07/2020
"""

# %%
def get_path_to_main_folder():
    """
    Returns the path to the main folder, which has to be named 'ndc_quantifications'.
    """
    
    from pathlib import Path
    
    path_cwd = Path.cwd()
    for parent in path_cwd.parents:
        if parent.name == "ndc_quantifications":
            return parent
    raise ValueError(
        "Could not find path to main folder. Make sure that your main folder is named 'ndc_quantifications'!")

# %%
