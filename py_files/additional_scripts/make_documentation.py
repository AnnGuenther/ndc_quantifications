# -*- coding: utf-8 -*-
"""
Author: Annika Guenther, annika.guenther@pik-potsdam.de

"""

# %%
"""
Create an .rst-file with the information from the .py-files.

In Anaconda Prompt run 'make clean' and then 'make html' in /docs.
"""

# %%
from pathlib import Path
import os
import helpers_functions as hpf
from setup_metadata import setup_metadata

# %%
meta = setup_metadata()

files = [
    'setup_metadata',
    'preprocessing_general',
    'preprocessing.prep_read_in_tables',
    'preprocessing.prep_ssps_fill_gaps',
    'preprocessing.prep_ssps_split_fgases',
    'preprocessing.prep_lulucf',
    'preprocessing_current_pc_cov',
    'preprocessing.prep_coverage',
    'preprocessing.prep_covered_emissions_his',
    'preprocessing.prep_covered_emissions_fut',
    'MODIFY_INPUT_HERE.input_default',
    '_to_be_run',
    'main_ndc_quantifications',
    'main_functions.ndcs_some_initial_testing',
    'main_functions.ndcs_check_options_for_target_calculations',
    'main_functions.ndcs_calculate_targets',
    'main_functions.ndcs_calculate_pathways_per_country',
    'main_functions.ndcs_calculate_pathways_per_group',
    #'main_functions.ndcs_get_pathways_for_matlab',
    'main_functions.ndcs_some_final_testing'
    ]

# %%
def get_text(txt, path_to_file):
    
    txt_act = hpf.read_text_from_file(Path(meta.path.py_files, path_to_file.replace('.', os.path.sep) + '.py'))
    
    path_to_file = (str(path_to_file)).replace(str(meta.path.py_files), '').replace('.py', '')
    path_to_file = path_to_file.replace(os.path.sep, '.')
    
    txt_new = f"\n\n{path_to_file}\n******************************************************************************"
#    txt_new += f"\n.. automodule:: {path_to_file}\n"
    
    locs = [xx for xx in range(len(txt_act[:-2])) if ((txt_act[xx:xx+3] == '"""') or (txt_act[xx:xx+4] == 'def '))]
    
    count = 0
    
    for ind in range(len(locs)):
        
        if count <= len(locs):
            
            try:
                if txt_act[locs[count]:locs[count]+4] == 'def ':
                    # Search for the end '):'
                    txt_count = txt_act[locs[count]+4:]
                    txt_count = txt_count.split('):')[0].replace('\n', '')
                    txt_count = f"\n**{txt_count})**\n"
                    txt_new += txt_count
                    count += 1
                
                else:
                    
                    txt_count = txt_act[locs[count]+3:locs[count+1]]
                    count += 2
                    
                    if 'Author:' not in txt_count:
                        txt_new += txt_count
            
            except:
                pass
    
    return txt_new

# %%
def get_text2(txt, path_to_file):
    
    txt_act = hpf.read_text_from_file(Path(meta.path.py_files, path_to_file.replace('.', os.path.sep) + '.py'))
    
    path_to_file = (str(path_to_file)).replace(str(meta.path.py_files), '').replace('.py', '')
    path_to_file = path_to_file.replace(os.path.sep, '.')
    
    txt_new = f"\n\n{path_to_file}\n******************************************************************************"
#    txt_new += f"\n.. automodule:: {path_to_file}\n"
    
    locs = [xx for xx in range(len(txt_act[:-2])) if txt_act[xx:xx+3] == '"""']
    
    count = 0
    countries = []
    
    for ind in range(len(locs)):
        
        if count <= len(locs):
            
            try:
                txt_count = txt_act[locs[count]+3:locs[count+1]]
                count += 2
                
                if 'Author:' not in txt_count:
                    countries += [txt_count.replace('\n', '')]
            
            except:
                pass
    
    txt_new += '\nCountries for which something (some emissions based on data provided within the NDC ' + \
        f' or target emissions) was calculated in {path_to_file}:\n{", ".join(sorted(countries))}.'
    
    return txt_new

# %%
txt = '\n*Comments: in the code, use (3 times " newline text newline 3 times ") for comments.* '
txt += '*Do not forget the new lines, else it will not appear in this documentation.*'
txt += """
\n\nThis documentation of the main functions to preprocess data and quantify mitigation 
targets from within the NDCs (tool NDCmitiQ), includes information retrieved from the
different py-files of the tool.
It does not include information from all py-files in this repository.

This documentation shall be seen as an add-on to the information given in the 
manuscript describing the methodology behind NDCmitiQ.
As soon as the paper is published, its DOI will be added here.

The required pandas packages can be found in requirements.txt, 
and information on how to run the code can be found in the README in the main folder.

"""


for path_to_file in files:
    txt += get_text(txt, path_to_file)

txt += get_text2(txt, 'ndcs__target_calculations_for_input_xlsx')


hpf.write_text_to_file(txt, Path(meta.path.main, 'docs', 'source', 'code.rst'))

# %%