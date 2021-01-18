# -*- coding: utf-8 -*-
"""
Author: Annika Günther, annika.guenther@pik-potsdam.de
Last update in 01/2021
"""

def get_all_files_and_or_folders_in_dir(path_to_dir, **kwargs):
    """
    Get list of all files and folders in directory.
    
    path_to_dir: path to directory
    kwargs:
        what = 'files' or 'folders' # to only get files or folders
        how = 'long' or 'short' # to get the total path or only the file/folder name
        contains = a string it has to contain
    default:
        what = 'both'
        how = 'short'
        contains = ''
    """
    
    # %%
    import os
    from pathlib import Path
    
    # %%
    if 'what' in kwargs.keys():
        what = kwargs['what']
    else:
        what = 'both'
    
    if 'how' in kwargs.keys():
        how = kwargs['how']
    else:
        how = 'short'
    
    if 'contains' in kwargs.keys():
        contains = kwargs['contains']
    else:
        contains = ''
    
    if what == 'both':
        if how == 'short':
            directories = [ x for x in os.listdir(path_to_dir) if (not x.startswith('.') and contains in x) ]
        else:
            directories = [ Path(path_to_dir, x) for x in os.listdir(path_to_dir) if (not x.startswith('.') and contains in x) ]
    
    elif what == 'files':
        if how == 'short':
            directories = [ x for x in os.listdir(path_to_dir) if (not x.startswith('.') and contains in x and os.path.isfile(Path(path_to_dir, x))) ]
        else:
            directories = [ Path(path_to_dir, x) for x in os.listdir(path_to_dir) if (not x.startswith('.') and contains in x and os.path.isfile(Path(path_to_dir, x))) ]
    
    elif what == 'folders':
        if how == 'short':
            directories = [ x for x in os.listdir(path_to_dir) if (not x.startswith('.') and contains in x and os.path.isdir(Path(path_to_dir, x))) ]
        else:
            directories = [ Path(path_to_dir, x) for x in os.listdir(path_to_dir) if (not x.startswith('.') and contains in x and os.path.isdir(Path(path_to_dir, x))) ]
    
    return sorted(directories)