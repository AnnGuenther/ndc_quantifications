# %%
import pandas as pd
import numpy as np
from pathlib import Path
from copy import deepcopy
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata
meta = setup_metadata()

# %%
folders_old = [
'ndcs_20201121_2156_SSP1_typeReclass', 
'ndcs_20201121_2202_SSP1_typeReclass_pccov100', 
'ndcs_20201121_2143_SSP1_typeMain', 
'ndcs_20201121_2150_SSP1_typeMain_pccov100', 
'ndcs_20201121_2201_SSP1_typeReclass_constEmiAfterLastTar', 
'ndcs_20201121_2207_SSP1_typeReclass_pccov100_constEmiAfterLastTar', 
'ndcs_20201121_2149_SSP1_typeMain_constEmiAfterLastTar', 
'ndcs_20201121_2155_SSP1_typeMain_pccov100_constEmiAfterLastTar', 
'ndcs_20201121_2159_SSP1_typeReclass_BLForUCAboveBL', 
'ndcs_20201121_2205_SSP1_typeReclass_pccov100_BLForUCAboveBL', 
'ndcs_20201121_2147_SSP1_typeMain_BLForUCAboveBL', 
'ndcs_20201121_2153_SSP1_typeMain_pccov100_BLForUCAboveBL', 
'ndcs_20201121_2156_SSP1_typeReclass_FAO', 
'ndcs_20201121_2202_SSP1_typeReclass_pccov100_FAO', 
'ndcs_20201121_2143_SSP1_typeMain_FAO', 
'ndcs_20201121_2150_SSP1_typeMain_pccov100_FAO']
folders_new = [
'ndcs_20201122_1037_SSP1_typeReclass', 
'ndcs_20201122_1044_SSP1_typeReclass_pccov100', 
'ndcs_20201122_1013_SSP1_typeMain', 
'ndcs_20201122_1029_SSP1_typeMain_pccov100', 
'ndcs_20201122_1043_SSP1_typeReclass_constEmiAfterLastTar', 
'ndcs_20201122_1052_SSP1_typeReclass_pccov100_constEmiAfterLastTar', 
'ndcs_20201122_1028_SSP1_typeMain_constEmiAfterLastTar', 
'ndcs_20201122_1035_SSP1_typeMain_pccov100_constEmiAfterLastTar', 
'ndcs_20201122_1041_SSP1_typeReclass_BLForUCAboveBL', 
'ndcs_20201122_1050_SSP1_typeReclass_pccov100_BLForUCAboveBL', 
'ndcs_20201122_1026_SSP1_typeMain_BLForUCAboveBL', 
'ndcs_20201122_1033_SSP1_typeMain_pccov100_BLForUCAboveBL', 
'ndcs_20201122_1037_SSP1_typeReclass_FAO', 
'ndcs_20201122_1044_SSP1_typeReclass_pccov100_FAO', 
'ndcs_20201122_1013_SSP1_typeMain_FAO', 
'ndcs_20201122_1029_SSP1_typeMain_pccov100_FAO']

for fold, fnew in zip(folders_old, folders_new):
    
    print(fold)
    
    oldp = 'C:/Users/annikag/primap/save_newcode_newpreprocess_OK/ndc_quantifications/data/output/' + \
        fold
    newp =  'C:/Users/annikag/primap/save_newcode_newpreprocess/ndc_quantifications/data/output/' + \
        fnew
    
    oldd = pd.read_csv(Path(oldp, 'ndc_targets_pathways_per_group.csv'))
    newd = pd.read_csv(Path(newp, 'ndc_targets_pathways_per_group.csv'))
    
    for ind in oldd.index[1:]:
        
        olda = oldd.loc[ind, :]
        newa = newd.loc[(newd.group == olda.group) & (newd.condi == olda.condi) & (newd.rge == olda.rge)]
        diff = [xx for xx in olda.index if ((olda[xx] != newa.loc[:, xx].values[0]) and xx != 'ndc_types_used' and str(olda[xx]) != 'nan')]
        
        if len(diff) > 0:
            print(ind, diff)

# %%
folders_old = [
'ndcs_20201119_1238_SSP1_typeMain',
'ndcs_20201119_1249_SSP1_typeMain_pccov100',
'ndcs_20201119_1247_SSP1_typeMain_constEmiAfterLastTar',
'ndcs_20201119_1255_SSP1_typeMain_pccov100_constEmiAfterLastTar',
'ndcs_20201119_1246_SSP1_typeMain_BLForUCAboveBL',
'ndcs_20201119_1254_SSP1_typeMain_pccov100_BLForUCAboveBL',
'ndcs_20201119_1238_SSP1_typeMain_FAO',
'ndcs_20201119_1249_SSP1_typeMain_pccov100_FAO']
folders_new = [
'ndcs_20201122_1013_SSP1_typeMain', 
'ndcs_20201122_1029_SSP1_typeMain_pccov100', 
'ndcs_20201122_1028_SSP1_typeMain_constEmiAfterLastTar', 
'ndcs_20201122_1035_SSP1_typeMain_pccov100_constEmiAfterLastTar', 
'ndcs_20201122_1026_SSP1_typeMain_BLForUCAboveBL', 
'ndcs_20201122_1033_SSP1_typeMain_pccov100_BLForUCAboveBL', 
'ndcs_20201122_1013_SSP1_typeMain_FAO', 
'ndcs_20201122_1029_SSP1_typeMain_pccov100_FAO']

for fold, fnew in zip(folders_old, folders_new):
    
    print(fold)
    
    oldp = 'C:/Users/annikag/primap/ndc_quantifications/data/output/output_for_paper/' + \
        fold
    newp =  'C:/Users/annikag/primap/save_newcode_newpreprocess/ndc_quantifications/data/output/' + \
        fnew
    
    oldd = pd.read_csv(Path(oldp, 'ndc_targets_pathways_per_group.csv'))
    newd = pd.read_csv(Path(newp, 'ndc_targets_pathways_per_group.csv'))
    
    for ind in oldd.index[1:]:
        
        olda = oldd.loc[ind, :]
        newa = newd.loc[(newd.group == olda.group) & (newd.condi == olda.condi) & (newd.rge == olda.rge)]
        diff = []
        for xx in [str(xx) for xx in range(1990, 2051)]:
            if hpf.rnd(olda[xx], 3) != hpf.rnd(newa.loc[:, xx].values[0], 3):
                diff += [xx]
        
        if len(diff) > 0:
            print(ind)

# %%# %%
folders_old = [
'ndcs_20201119_1238_SSP1_typeMain',
'ndcs_20201119_1249_SSP1_typeMain_pccov100',
'ndcs_20201119_1247_SSP1_typeMain_constEmiAfterLastTar',
'ndcs_20201119_1255_SSP1_typeMain_pccov100_constEmiAfterLastTar',
'ndcs_20201119_1246_SSP1_typeMain_BLForUCAboveBL',
'ndcs_20201119_1254_SSP1_typeMain_pccov100_BLForUCAboveBL',
'ndcs_20201119_1238_SSP1_typeMain_FAO',
'ndcs_20201119_1249_SSP1_typeMain_pccov100_FAO']
folders_new = [
'ndcs_20201122_1013_SSP1_typeMain', 
'ndcs_20201122_1029_SSP1_typeMain_pccov100', 
'ndcs_20201122_1028_SSP1_typeMain_constEmiAfterLastTar', 
'ndcs_20201122_1035_SSP1_typeMain_pccov100_constEmiAfterLastTar', 
'ndcs_20201122_1026_SSP1_typeMain_BLForUCAboveBL', 
'ndcs_20201122_1033_SSP1_typeMain_pccov100_BLForUCAboveBL', 
'ndcs_20201122_1013_SSP1_typeMain_FAO', 
'ndcs_20201122_1029_SSP1_typeMain_pccov100_FAO']

for fold, fnew in zip(folders_old, folders_new):
    
    print(fold)
    
    oldp = 'C:/Users/annikag/primap/ndc_quantifications/data/output/output_for_paper/' + \
        fold
    newp =  'C:/Users/annikag/primap/save_newcode_newpreprocess/ndc_quantifications/data/output/' + \
        fnew
    
    oldd = pd.read_csv(Path(oldp, 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
    newd = pd.read_csv(Path(newp, 'ndc_targets_pathways_per_country_used_for_group_pathways.csv'))
    
    for ind in oldd.index:
        
        olda = oldd.loc[ind, :]
        newa = newd.loc[(newd.iso3 == olda.iso3) & (newd.condi == olda.condi) & (newd.rge == olda.rge)]
        diff = []
        for xx in olda.index:
            if str(olda[xx]) != 'nan':
                try:
                    val = float(olda[xx])
                    if hpf.rnd(olda[xx], 3) != hpf.rnd(newa.loc[:, xx].values[0], 3):
                        diff += [olda.iso3 + ', ' + xx]
                except:
                    if olda[xx] != newa.loc[:, xx].values[0]:
                        diff += [olda.iso3 + ', '+ xx]
        
        if len(diff) > 0:
            print(ind, olda.iso3, olda.condi, olda.rge)

# %%