# %%
import pandas as pd
import numpy as np
from pathlib import Path
import os
from copy import deepcopy
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata
meta = setup_metadata()

# %%
main_ndc_quantifications('input_SSP2_typeMain', '')
main_ndc_quantifications('input_SSP2_typeMain', 'FAO')
main_ndc_quantifications('input_SSP2_typeMain_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100', '')
main_ndc_quantifications('input_SSP2_typeMain_pccov100', 'FAO')
main_ndc_quantifications('input_SSP2_typeMain_pccov100_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeReclass', '')
main_ndc_quantifications('input_SSP2_typeReclass', 'FAO')
main_ndc_quantifications('input_SSP2_typeReclass_constEmiAfterLastTar', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100', '')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100', 'FAO')
main_ndc_quantifications('input_SSP2_typeReclass_pccov100_constEmiAfterLastTar', '')

# %%
energy = 159 + 91 + 686 + 102 + 639
ippu = 69 + 2 + 4 + 7
afolu = 1284 + 673 + 6 + 540 + 191 + 148 + 98
waste = 187 + 159 + 1 + 290
total = energy + ippu + afolu + waste
print(total)

# %%