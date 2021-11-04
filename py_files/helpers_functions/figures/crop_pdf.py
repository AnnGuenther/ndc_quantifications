# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de
Last updated in 06/2020.
"""

# %%
def crop_pdf(path_to_file):
    """
    Crop the pdfs in path_to_files.
    """
    
    # %%
    import os
    
    # %%
    #path_to_file = Path(meta.path.main, 'plots', 'maps', 'global_share', 'global_share_KYOTOGHG_IPCM0EL_better_limits.pdf')
    
    current_folder = os.getcwd()
    folder, file = os.path.split(path_to_file)
    os.chdir(folder)
    
    if file.endswith('.pdf'):
        os.system(f"pdfcrop {file}")
    
    os.chdir(current_folder)
    
# %%