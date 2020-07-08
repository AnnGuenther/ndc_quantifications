# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
def crop_pdfs_in_directory(path_to_folder):
    """
    Crop the pdfs in path_to_files.
    """
    
    # %%
    import os
    
    # %%
    #path_to_folder = Path(meta.path.main, 'plots', 'tables_ndcs')
    
    current_folder = os.getcwd()
    os.chdir(path_to_folder)
    files = os.listdir(path_to_folder)
    
    for file in files:
        if file.endswith('.pdf'):
            os.system(f"pdfcrop {file}")
    
    os.chdir(current_folder)
    
# %%