# %%
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import helpers_functions as hpf
from setup_metadata import setup_metadata
meta = setup_metadata()

# %%
pth_matlab = Path(meta.path.main, 'data', 'matlab_tables')
pth_test = Path(meta.path.main, 'data', 'test_lulucf')

files = hpf.get_all_files_and_or_folders_in_dir(pth_matlab)

# %%
# Recalculate the LULUCF data (from Matlab files, linear interpolation plus extrapolation)
for file in files:
    #file = 'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_BUR2IPCC2006I.csv'
    
    if ('LULUCF' in file and 'PRIMAP' not in file):
        
        table = hpf.import_table_to_class_metadata_country_year_matrix(Path(pth_matlab, file))
        data = table.data.reindex(columns=range(1990, 2051))
        
        for iso3 in data.index:
            
            #iso3 = 'IDN'
            data_i = data.loc[iso3]
            data_nan = [xx for xx in data_i.index if np.isnan(data_i[xx])]
            data_notnan = [xx for xx in data_i.index if not np.isnan(data_i[xx])]
            first_yr = data_notnan[0]
            last_yr = data_notnan[-1]
            
            if not data_i.isnull().all():
                
                if len(data_notnan) < 3:
                    print(file, iso3, "less than three data points available -> dismissed")
                    data_i.loc[:] = np.nan
                
                else:
                    
                    if len(data_nan) > 0:
                        
                        data_i.interpolate(method='linear', inplace=True, limit_area='inside')
                        
                        if first_yr > 1997:
                            print(file, iso3, "no data from 1990-1997")
                            fill_val = data_i.loc[first_yr]
                        else:
                            fill_val = data_i.loc[np.arange(1990, 1998)].mean()
                        data_i.loc[np.arange(1990, first_yr)] = fill_val
                        
                        if last_yr < 2010:
                            print(file, iso3, "no data after 2010")
                            fill_val = data_i.loc[last_yr]
                        else:
                            fill_val = data_i.loc[np.arange(2010, 2018)].mean()
                        data_i.loc[np.arange(last_yr+1, data_i.index[-1]+1)] = fill_val
            
            data.loc[iso3] = data_i
        
        table.data = data
        hpf.write_table_from_class_metadata_country_year_matrix(table, Path(pth_test, file))

# %%
# FAO: sum up CO2 + CH4 + N2O
table_kyoto = hpf.import_table_to_class_metadata_country_year_matrix(Path(pth_test, 'CO2AR4_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2019BI.csv'))
table_kyoto.ent = "KYOTOGHG"
table_kyoto.__tablename_to_standard__()
table_kyoto.__name_to_standard__()
table_kyoto.data = table_kyoto.data.reindex(columns=range(1990, 2051), index=meta.isos.EARTH)
table_kyoto.data.loc[:, :] = np.nan

for ent in ['CO2', 'CH4', 'N2O']:
    table_act = hpf.import_table_to_class_metadata_country_year_matrix(Path(pth_test, f'{ent}AR4_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2019BI.csv'))
    table_kyoto.data = table_kyoto.data.add(table_act.data, fill_value=0)

hpf.write_table_from_class_metadata_country_year_matrix(table_kyoto, 
    Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2019BI.csv'))

# %%
# Check for differences between new values and paper version
for srce in ['BUR1IPCC2006I', 'BUR2IPCC2006I', 'BUR3IPCC2006I', 'CRF2018', 'CRF2019', 'UNFCCC2019BI', 'FAO2019BI']:
    
    new = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_{srce}.csv')). \
        data.reindex(index=meta.isos.EARTH)
    old = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(f'C:/Users/annikag/primap/ndc_quantifications-v1.0.0/ndc_quantifications/data/preprocess/tables/KYOTOGHG_IPCMLULUCF_TOTAL_NET_INTERLIN_{srce}.csv')). \
        data.reindex(index=meta.isos.EARTH)
    
    for iso3 in meta.isos.EARTH:
        
        new_i = new.loc[iso3]
        old_i = old.loc[iso3]
        
        if (not (new_i.isnull().all() and old_i.isnull().all()) and (new_i != old_i).any()):
            
            diff = [xx for xx in new_i.index if new_i[xx] != old_i[xx]]
            
            if (abs(new_i-old_i) > 1e-13).any():
                
                print("\n\n", srce, iso3, "something is different!")
                print("\n", ", ".join([str(xx) for xx in diff]))
                print("\n", ", ".join([str(old_i.loc[xx]-new_i.loc[xx]) for xx in diff]))

# For BUR there is a difference, as the 1990-1999 values for three countries were nan by mistake.
# Had used the mean over 1990-1996, but these countries only have values later on.

# %%
# Check all permutations and the range of possible outcomes.
# Instead of only the three given in the paper.

# Use 1990, 2010, 2017, and 2030.

from itertools import permutations

srces = meta.lulucf.source_prioritisation

lu_data = {}

for srce in srces:
    
    lu_data[srce] = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_{srce}.csv')).data

sum_earth = pd.DataFrame(columns=[1990, 2010, 2017, 2030])

#combis = [
#    ['CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'UNFCCC2019BI', 'FAO2019BI'],
#    ['UNFCCC2019BI', 'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'FAO2019BI'],
#    ['FAO2019BI', 'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'UNFCCC2019BI']]
combis = list(permutations(srces))

for combi in combis:
    
    cmb = "_".join(combi)
    df_combi = pd.DataFrame(index=meta.isos.EARTH, columns=sum_earth.columns)
    
    for iso3 in df_combi.index:
        
        which_srce = []
        no_data = []
        
        for srce in combi:
            
            if (iso3 in lu_data[srce].index and not lu_data[srce].loc[iso3].isnull().all()):
                
                which_srce += [srce]
        
        if len(which_srce) > 0:
            df_combi.loc[iso3] = lu_data[which_srce[0]].loc[iso3]
        
        else:
            no_data += [iso3]
    
    #df_combi.to_csv(Path(pth_test, f'test_KYOTOGHGAR4_{cmb}.csv'))
    
    print(f"{cmb}: no data for countries " + (", ".join(no_data) if len(no_data) > 0 else "NaN"))
    
    sum_earth.loc[cmb] = df_combi.sum() / 1000

sum_earth.to_csv(Path(pth_test, 'test_combis_perYear.csv'))

# %%
for combi in combis:
    print([hpf.rnd(xx, 1) for xx in sum_earth.loc["_".join(combi)]])

# %%
# Use ranges for 1990-1999, 2000-2009, 2010-2017, 2030.

sum_earth = pd.DataFrame(columns=['1990_1999', '2000_2009', '2010_2017', '2030'])

#combis = [
#    ['CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'UNFCCC2019BI', 'FAO2019BI'],
#    ['UNFCCC2019BI', 'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'FAO2019BI'],
#    ['FAO2019BI', 'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'UNFCCC2019BI']]
combis = list(permutations(srces))

for combi in combis:
    
    cmb = "_".join(combi)
    df_combi = pd.DataFrame(index=meta.isos.EARTH, columns=sum_earth.columns)
    df_combi_net_srces = pd.DataFrame(index=meta.isos.EARTH, columns=sum_earth.columns)
    df_combi_net_sinks = pd.DataFrame(index=meta.isos.EARTH, columns=sum_earth.columns)
    
    for iso3 in meta.isos.EARTH:
        
        which_srce = []
        no_data = []
        
        for srce in combi:
            
            if (iso3 in lu_data[srce].index and not lu_data[srce].loc[iso3].isnull().all()):
                
                which_srce += [srce]
        
        if len(which_srce) > 0:
            df_combi.loc[iso3, '1990_1999'] = lu_data[which_srce[0]].loc[iso3, range(1990, 2000)].mean()
            df_combi.loc[iso3, '2000_2009'] = lu_data[which_srce[0]].loc[iso3, range(2000, 2010)].mean()
            df_combi.loc[iso3, '2010_2017'] = lu_data[which_srce[0]].loc[iso3, range(2010, 2018)].mean()
            df_combi.loc[iso3, '2030'] = lu_data[which_srce[0]].loc[iso3, 2030].mean()
            
            df_combi.loc[iso3, '1990_1999'] = lu_data[which_srce[0]].loc[iso3, range(1990, 2000)].mean()
            df_combi.loc[iso3, '2000_2009'] = lu_data[which_srce[0]].loc[iso3, range(2000, 2010)].mean()
            df_combi.loc[iso3, '2010_2017'] = lu_data[which_srce[0]].loc[iso3, range(2010, 2018)].mean()
            df_combi.loc[iso3, '2030'] = lu_data[which_srce[0]].loc[iso3, 2030].mean()
            
            df_combi.loc[iso3, '1990_1999'] = lu_data[which_srce[0]].loc[iso3, range(1990, 2000)].mean()
            df_combi.loc[iso3, '2000_2009'] = lu_data[which_srce[0]].loc[iso3, range(2000, 2010)].mean()
            df_combi.loc[iso3, '2010_2017'] = lu_data[which_srce[0]].loc[iso3, range(2010, 2018)].mean()
            df_combi.loc[iso3, '2030'] = lu_data[which_srce[0]].loc[iso3, 2030].mean()
        
        else:
            no_data += [iso3]
    
    #df_combi.to_csv(Path(pth_test, f'test_KYOTOGHGAR4_{cmb}.csv'))
    
    print(f"{cmb}: no data for countries " + (", ".join(no_data) if len(no_data) > 0 else "NaN"))
    
    sum_earth.loc[cmb] = df_combi.sum() / 1000

sum_earth.to_csv(Path(pth_test, 'test_combis_perRange.csv'))

# %%
combis = [
    ['CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'UNFCCC2019BI', 'FAO2019BI'],
    ['UNFCCC2019BI', 'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'FAO2019BI'],
    ['FAO2019BI', 'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'UNFCCC2019BI']]

for combi in combis:
    cmb = "_".join(combi)
    print(sum_earth.loc[cmb])

# Is the same as in paper (but: 1990 value changed due to error in implementation)

# %%
# Give out the min, max, and 10., 50., 90. percentiles.

for case in ['Year', 'Range']:
    
    sum_earth = pd.read_csv(Path(pth_test, f'test_combis_per{case}.csv'), index_col=0)
    print("\n", case)
    print("min", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.min()]))
    print("15th", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.quantile(.15)]))
    print("50th", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.quantile(.5)]))
    print("85th", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.quantile(.85)]))
    print("max", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.max()]))


# %%
for case in ['Year', 'Range']:
    
    sum_earth = pd.read_csv(Path(pth_test, f'test_combis_per{case}.csv'), index_col=0)
    print("\n", case)
    print("min", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.min()]))
    print("15th", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.quantile(.15)]))
    print("50th", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.quantile(.5)]))
    print("85th", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.quantile(.85)]))
    print("max", ", ".join([hpf.rnd(xx, 1) for xx in sum_earth.max()]))

# %%
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot(1,1,1)

YL = [-5, 5]
XL = [-8, 128]
ax.set_ylim(YL)
ax.set_xlim(XL)
ax.plot([50, 50], YL, 'k:', linewidth=.5)
ax.plot(XL, [0, 0], 'k:', linewidth=.5)
ax.plot([104, 104], YL, 'k:', linewidth=.5)
ax.plot([112, 112], YL, 'k:', linewidth=.5)
ax.plot([120, 120], YL, 'k:', linewidth=.5)

colours = {
    '1990_1999': [1, 0, 0],
    '2000_2009': [.5, .5, 1],
    '2010_2017': [0, 1, 1],
    '2030': [0, 0, 0]}

combis = [
    ['CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'UNFCCC2019BI', 'FAO2019BI'],
    ['UNFCCC2019BI', 'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'FAO2019BI'],
    ['FAO2019BI', 'CRF2019', 'CRF2018', 'BUR3IPCC2006I', 'BUR2IPCC2006I', 'BUR1IPCC2006I', 'UNFCCC2019BI']]

sum_earth = pd.read_csv(Path(pth_test, 'test_combis_perRange.csv'), index_col=0)

for rge in sum_earth.columns:
    
    if rge != '2030':
        ax.plot(np.arange(0, 105, 10), sum_earth.loc[:, rge].quantile(np.arange(0, 1.05, .1)), color=colours[rge], linewidth=2, label=rge.replace("_", "-"))
    
    else:
        ax.plot(np.arange(0, 105, 10), sum_earth.loc[:, rge].quantile(np.arange(0, 1.05, .1)), color=colours[rge], linewidth=3, linestyle=":", label='2018-2050')

ax.legend()

for combi, xval, combiname in zip(combis, np.arange(0, len(combi)*8, 8), ['Prio\nCRF', 'Prio\nUNFCCC', 'Prio\nFAO']):
    
    cmb = "_".join(combi)
    
    for rge, sze in zip(sum_earth.columns, np.arange(40, 0, -10)):
        
        ax.scatter(108+xval, sum_earth.loc[cmb, rge], sze, color=colours[rge])
        
        yloc = YL[0]+.12*np.diff(YL)
        ax.text(108+xval, yloc, str(combiname), rotation=90, ha='center', va='center', fontweight='bold')

ax.set_xticks(np.arange(0, 101, 20))
ax.text(50, YL[0]-.14*np.diff(YL), "Percentile", fontweight='bold', ha='center')
ax.set_ylabel("Kyoto GHG LULUCF emissions\nGt CO$_2$eq AR4", fontweight='bold')

fig.subplots_adjust(bottom=.15, top=.99, left=.1, right=.99)
path_to_plot = Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_percentiles_perPeriod.png')
plt.savefig(path_to_plot, dpi=300)
path_to_pdf = str(path_to_plot).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
# FAO 2018:

# Calculate the LULUCF data (from Matlab files, linear interpolation plus extrapolation)

pth_FAO2018 = Path('C:/Users/annikag/primap/datatables_csv/proc_FAO2018_14Oct19')

for ent in ['CO2', 'CH4', 'N2O']:
    
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(pth_FAO2018, f"{ent}_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2018I.csv"))
    data = table.data.reindex(columns=range(1990, 2051))
    
    data = data * hpf.get_gwps_for_gases(ent, "AR4")
    table.gwp = "AR4"
    data = data * hpf.get_conversion_unit(table.unit, "Mt")
    table.unit = "MtCO2eq"
    table.__name_to_standard__()
    table.__tablename_to_standard__()
    
    for iso3 in data.index:
        
        data_i = data.loc[iso3]
        data_nan = [xx for xx in data_i.index if np.isnan(data_i[xx])]
        data_notnan = [xx for xx in data_i.index if not np.isnan(data_i[xx])]
        first_yr = data_notnan[0]
        last_yr = data_notnan[-1]
        
        if not data_i.isnull().all():
            
            if len(data_notnan) < 3:
                print(table.tablename, iso3, "less than three data points available -> dismissed")
                data_i.loc[:] = np.nan
            
            else:
                
                if len(data_nan) > 0:
                    
                    data_i.interpolate(method='linear', inplace=True, limit_area='inside')
                    
                    if first_yr > 1997:
                        print(table.tablename, iso3, "no data from 1990-1997")
                        fill_val = data_i.loc[first_yr]
                    else:
                        fill_val = data_i.loc[np.arange(1990, 1998)].mean()
                    data_i.loc[np.arange(1990, first_yr)] = fill_val
                    
                    if last_yr < 2010:
                        print(table.tablename, iso3, "no data after 2010")
                        fill_val = data_i.loc[last_yr]
                    else:
                        fill_val = data_i.loc[np.arange(2010, 2018)].mean()
                    data_i.loc[np.arange(last_yr+1, data_i.index[-1]+1)] = fill_val
        
        data.loc[iso3] = data_i
    
    table.data = data
    hpf.write_table_from_class_metadata_country_year_matrix(table, Path(pth_test, f"{table.tablename}.csv"))

# %%
# FAO: sum up CO2 + CH4 + N2O
table_kyoto = hpf.import_table_to_class_metadata_country_year_matrix(Path(pth_test, 'CO2AR4_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2018I.csv'))
table_kyoto.ent = "KYOTOGHG"
table_kyoto.__tablename_to_standard__()
table_kyoto.__name_to_standard__()
table_kyoto.data = table_kyoto.data.reindex(columns=range(1990, 2051), index=meta.isos.EARTH)
table_kyoto.data.loc[:, :] = np.nan

for ent in ['CO2', 'CH4', 'N2O']:
    table_act = hpf.import_table_to_class_metadata_country_year_matrix(Path(pth_test, f'{ent}AR4_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2018I.csv'))
    table_kyoto.data = table_kyoto.data.add(table_act.data, fill_value=0)

hpf.write_table_from_class_metadata_country_year_matrix(table_kyoto, 
    Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2018I.csv'))

# %%
# FAO2016
# Only available in IPCC1996er categories.

# Calculate the LULUCF data (from Matlab files, linear interpolation plus extrapolation)

pth_FAO2016 = Path('C:/Users/annikag/primap/datatables_csv/proc_FAO2016_24Jan17')

for ent in ['CO2', 'CH4', 'N2O', 'KYOTOGHGAR4']:
    
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(pth_FAO2016, f"{ent}_CAT5_TOTAL_NET_HISTORY_FAO2016P.csv"))
    data = table.data.reindex(columns=range(1990, 2051))
    
    if ent != 'KYOTOGHGAR4':
        data = data * hpf.get_gwps_for_gases(ent, "AR4")
    
    else:
        table.ent = 'KYOTOGHG'
    
    table.gwp = "AR4"
    data = data * hpf.get_conversion_unit(table.unit, "Mt")
    table.unit = "MtCO2eq"
    table.__name_to_standard__()
    table.__tablename_to_standard__()
    
    for iso3 in data.index:
        
        data_i = data.loc[iso3]
        data_nan = [xx for xx in data_i.index if np.isnan(data_i[xx])]
        data_notnan = [xx for xx in data_i.index if not np.isnan(data_i[xx])]
        first_yr = data_notnan[0]
        last_yr = data_notnan[-1]
        
        if not data_i.isnull().all():
            
            if len(data_notnan) < 3:
                print(table.tablename, iso3, "less than three data points available -> dismissed")
                data_i.loc[:] = np.nan
            
            else:
                
                if len(data_nan) > 0:
                    
                    data_i.interpolate(method='linear', inplace=True, limit_area='inside')
                    
                    if first_yr > 1997:
                        print(table.tablename, iso3, "no data from 1990-1997")
                        fill_val = data_i.loc[first_yr]
                    else:
                        fill_val = data_i.loc[np.arange(1990, 1998)].mean()
                    data_i.loc[np.arange(1990, first_yr)] = fill_val
                    
                    if last_yr < 2010:
                        print(table.tablename, iso3, "no data after 2010")
                        fill_val = data_i.loc[last_yr]
                    else:
                        fill_val = data_i.loc[np.arange(2010, 2018)].mean()
                    data_i.loc[np.arange(last_yr+1, data_i.index[-1]+1)] = fill_val
        
        data.loc[iso3] = data_i
    
    table.data = data
    hpf.write_table_from_class_metadata_country_year_matrix(table, Path(pth_test, f"{table.tablename}.csv"))

# KYOTOGHGAR4 already given.
# no need to sum up CO2 + CH4 + N2O.

# %%
# CRF2017 and 2016:

# Calculate the LULUCF data (from Matlab files, linear interpolation plus extrapolation)

for crf, folder in ['CRF2017', 'proc_CRF2017_02Oct18'], ['CRF2016', 'proc_CRF2016_23Jun17']:
    
    pth_CRF = Path('C:/Users/annikag/primap/datatables_csv', folder)
    
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(pth_CRF, f"KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_{crf}.csv"))
    data = table.data.reindex(columns=range(1990, 2051))
    
    table.ent = "KYOTOGHG"
    table.gwp = "AR4"
    data = data * hpf.get_conversion_unit(table.unit, "Mt")
    table.unit = "MtCO2eq"
    table.__name_to_standard__()
    table.__tablename_to_standard__()
    
    for iso3 in data.index:
        
        data_i = data.loc[iso3]
        data_nan = [xx for xx in data_i.index if np.isnan(data_i[xx])]
        data_notnan = [xx for xx in data_i.index if not np.isnan(data_i[xx])]
        first_yr = data_notnan[0]
        last_yr = data_notnan[-1]
        
        if not data_i.isnull().all():
            
            if len(data_notnan) < 3:
                print(table.tablename, iso3, "less than three data points available -> dismissed")
                data_i.loc[:] = np.nan
            
            else:
                
                if len(data_nan) > 0:
                    
                    data_i.interpolate(method='linear', inplace=True, limit_area='inside')
                    
                    if first_yr > 1997:
                        print(table.tablename, iso3, "no data from 1990-1997")
                        fill_val = data_i.loc[first_yr]
                    else:
                        fill_val = data_i.loc[np.arange(1990, 1998)].mean()
                    data_i.loc[np.arange(1990, first_yr)] = fill_val
                    
                    if last_yr < 2010:
                        print(table.tablename, iso3, "no data after 2010")
                        fill_val = data_i.loc[last_yr]
                    else:
                        fill_val = data_i.loc[np.arange(2010, 2018)].mean()
                    data_i.loc[np.arange(last_yr+1, data_i.index[-1]+1)] = fill_val
        
        data.loc[iso3] = data_i
    
    table.data = data
    hpf.write_table_from_class_metadata_country_year_matrix(table, Path(pth_test, f"{table.tablename}.csv"))

# %%
# UNFCCC2018, 2017, 2016:

# Calculate the LULUCF data (from Matlab files, linear interpolation plus extrapolation)

for unfccc, folder, cat, srce in \
    ['UNFCCC2018', 'proc_UNFCCC2018_09Nov18', 'IPCMLULUCF', 'UNFCCC2018I'], \
    ['UNFCCC2017', 'proc_UNFCCC2017B_05Dec17', 'CAT5', 'UNFCCC2017BP'], \
    ['UNFCCC2015', 'proc_UNFCCC2015_22Feb16', 'CAT5', 'UNFCCC2015P']:
    
    pth_CRF = Path('C:/Users/annikag/primap/datatables_csv', folder)
    
    table = hpf.import_table_to_class_metadata_country_year_matrix(
        Path(pth_CRF, f"KYOTOGHGAR4_{cat}_TOTAL_NET_HISTORY_{srce}.csv"))
    data = table.data.reindex(columns=range(1990, 2051))
    
    table.ent = "KYOTOGHG"
    table.gwp = "AR4"
    data = data * hpf.get_conversion_unit(table.unit, "Mt")
    table.unit = "MtCO2eq"
    table.__name_to_standard__()
    table.__tablename_to_standard__()
    
    for iso3 in data.index:
        
        data_i = data.loc[iso3]
        data_nan = [xx for xx in data_i.index if np.isnan(data_i[xx])]
        data_notnan = [xx for xx in data_i.index if not np.isnan(data_i[xx])]
        first_yr = data_notnan[0]
        last_yr = data_notnan[-1]
        
        if not data_i.isnull().all():
            
            if len(data_notnan) < 3:
                print(table.tablename, iso3, "less than three data points available -> dismissed")
                data_i.loc[:] = np.nan
            
            else:
                
                if len(data_nan) > 0:
                    
                    data_i.interpolate(method='linear', inplace=True, limit_area='inside')
                    
                    if first_yr > 1997:
                        print(table.tablename, iso3, "no data from 1990-1997")
                        fill_val = data_i.loc[first_yr]
                    else:
                        fill_val = data_i.loc[np.arange(1990, 1998)].mean()
                    data_i.loc[np.arange(1990, first_yr)] = fill_val
                    
                    if last_yr < 2010:
                        print(table.tablename, iso3, "no data after 2010")
                        fill_val = data_i.loc[last_yr]
                    else:
                        fill_val = data_i.loc[np.arange(2010, 2018)].mean()
                    data_i.loc[np.arange(last_yr+1, data_i.index[-1]+1)] = fill_val
        
        data.loc[iso3] = data_i
    
    table.data = data
    hpf.write_table_from_class_metadata_country_year_matrix(table, Path(pth_test, f"{table.tablename}.csv"))

# %%
# Compare FAO2019 and FAO2018, and FAO2016.
fao2019 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2019BI.csv')).data
fao2018 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_FAO2018I.csv')).data
fao2016 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_CAT5_TOTAL_NET_HISTORY_FAO2016P.csv')).data

# Only use the sum over iso3s with data available in all three versions.
isos_all_fao = []
for iso3 in meta.isos.EARTH:
    
    if ((iso3 in fao2019.index and not fao2019.loc[iso3].isnull().all()) and
        (iso3 in fao2018.index and not fao2018.loc[iso3].isnull().all()) and
        (iso3 in fao2016.index and not fao2016.loc[iso3].isnull().all())):
        
        isos_all_fao += [iso3]

print(f"Data compared for {len(isos_all_fao)} countries: " + ", ".join(isos_all_fao))

colours_fao = {
    'FAO2016': [.5, .5, 1],
    'FAO2018': [0, 1, 1],
    'FAO2019': [0, 0, 0]}

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)

for fao, name, cat, sze in [fao2019, 'FAO2019', 'IPCMLULUCF', 15], [fao2018, 'FAO2018', 'IPCMLULUCF', 10], [fao2016, 'FAO2016', 'CAT5', 5]:
    
    print(f"\n{name}")
    ax.plot(range(1990, 2051), fao.loc[isos_all_fao, :].sum().values/1000, '.-', label=f"{name} ({cat})", markersize=sze, color=colours_fao[name])
    
    for rge in [np.arange(1990, 2000), np.arange(2000, 2010), np.arange(2010, 2018)]:
        print(hpf.rnd(fao.loc[isos_all_fao, rge].sum().mean()/1000, 1))

XL = [1990, 2020]
ax.set_xlim(XL)
ax.set_xlabel("year", fontweight='bold')
ax.set_ylabel("Kyoto GHG LULUCF emissions\nGt CO$_2$eq AR4", fontweight='bold')
ax.legend()

YL = ax.get_ylim()
ax.text(XL[1], YL[1]+.025*np.diff(YL), f"data for {len(isos_all_fao)} countries",
    ha='right', va='bottom')

fig.subplots_adjust(bottom=.15, top=.85, left=.15, right=.95)
path_to_plot = Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_FAO_differentVersions_perPeriod.png')
plt.savefig(path_to_plot, dpi=300)
path_to_pdf = str(path_to_plot).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
# Compare CRF2019 and CRF2018, CRF2017 and CRF2016.
crf2019 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_CRF2019.csv')).data
crf2018 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_CRF2018.csv')).data
crf2017 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_CRF2017.csv')).data
crf2016 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_CRF2016.csv')).data

# Only use the sum over iso3s with data available in all three versions.
isos_all_crf = []
for iso3 in meta.isos.EARTH:
    
    if ((iso3 in crf2019.index and not crf2019.loc[iso3].isnull().all()) and
        (iso3 in crf2018.index and not crf2018.loc[iso3].isnull().all()) and
        (iso3 in crf2017.index and not crf2017.loc[iso3].isnull().all()) and
        (iso3 in crf2016.index and not crf2016.loc[iso3].isnull().all())):
        
        isos_all_crf += [iso3]

print(f"Data compared for {len(isos_all_crf)} countries: " + ", ".join(isos_all_crf))

colours_crf = {
    'CRF2016': [1, 0, 0],
    'CRF2017': [.5, .5, 1],
    'CRF2018': [0, 1, 1],
    'CRF2019': [0, 0, 0]}

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)

for crf, name, sze in [crf2019, 'CRF2019', 20], [crf2018, 'CRF2018', 15], [crf2017, 'CRF2017', 10], [crf2016, 'CRF2016', 5]:
    
    print(f"\n{name}")
    ax.plot(range(1990, 2051), crf.loc[isos_all_crf, :].sum().values/1000, '.-', label=f"{name} (IPCMLULUCF)", markersize=sze, color=colours_crf[name])
    
    for rge in [np.arange(1990, 2000), np.arange(2000, 2010), np.arange(2010, 2018)]:
        print(hpf.rnd(crf.loc[isos_all_crf, rge].sum().mean()/1000, 1))

XL = [1990, 2020]
ax.set_xlim(XL)
ax.set_xlabel("year", fontweight='bold')
ax.set_ylabel("Kyoto GHG LULUCF emissions\nGt CO$_2$eq AR4", fontweight='bold')
ax.legend()

YL = ax.get_ylim()
ax.text(XL[1], YL[1]+.025*np.diff(YL), f"data for {len(isos_all_crf)} countries",
    ha='right', va='bottom')

fig.subplots_adjust(bottom=.15, top=.85, left=.15, right=.95)
path_to_plot = Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_CRF_differentVersions_perPeriod.png')
plt.savefig(path_to_plot, dpi=300)
path_to_pdf = str(path_to_plot).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
# Compare BUR3 BUR2, and BUR1.
bur3 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_BUR3IPCC2006I.csv')).data
bur2 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_BUR2IPCC2006I.csv')).data
bur1 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, f'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_BUR1IPCC2006I.csv')).data

# Only use the sum over iso3s with data available in all three versions.
isos_all_bur = []
for iso3 in meta.isos.EARTH:
    
    if ((iso3 in bur3.index and not bur3.loc[iso3].isnull().all()) and
        (iso3 in bur2.index and not bur2.loc[iso3].isnull().all()) and
        (iso3 in bur1.index and not bur1.loc[iso3].isnull().all())):
        
        isos_all_bur += [iso3]

print(f"Data compared for {len(isos_all_bur)} countries: " + ", ".join(isos_all_bur))

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)

for bur, name, sze in [bur3, 'BUR3', 15], [bur2, 'BUR2', 10], [bur1, 'BUR1', 5]:
    
    print(f"\n{name}")
    ax.plot(range(1990, 2051), bur.loc[isos_all_bur, :].sum().values/1000, '.-', label=f"{name} (IPCMLULUCF)", markersize=sze)
    
    for rge in [np.arange(1990, 2000), np.arange(2000, 2010), np.arange(2010, 2018)]:
        print(hpf.rnd(bur.loc[isos_all_bur, rge].sum().mean()/1000, 1))

XL = [1990, 2020]
ax.set_xlim(XL)
ax.set_xlabel("year", fontweight='bold')
ax.set_ylabel("Kyoto GHG LULUCF emissions\nGt CO$_2$eq AR4", fontweight='bold')
ax.legend()

YL = ax.get_ylim()
ax.text(XL[1], YL[1]+.025*np.diff(YL), f"data for {len(isos_all_bur)} countries",
    ha='right', va='bottom')

fig.subplots_adjust(bottom=.15, top=.85, left=.15, right=.95)
path_to_plot = Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_BUR_differentVersions_perPeriod.png')
plt.savefig(path_to_plot, dpi=300)
path_to_pdf = str(path_to_plot).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
# Compare UNFCCC versions.
unfccc2019 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_UNFCCC2019BI.csv')).data
unfccc2018 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_TOTAL_NET_HISTORY_UNFCCC2018I.csv')).data
unfccc2017 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, 'KYOTOGHGAR4_CAT5_TOTAL_NET_HISTORY_UNFCCC2017BP.csv')).data
unfccc2015 = hpf.import_table_to_class_metadata_country_year_matrix(
    Path(pth_test, 'KYOTOGHGAR4_CAT5_TOTAL_NET_HISTORY_UNFCCC2015P.csv')).data

# Only use the sum over iso3s with data available in all three versions.
isos_all_unfccc = []
for iso3 in meta.isos.EARTH:
    
    if ((iso3 in unfccc2019.index and not unfccc2019.loc[iso3].isnull().all()) and
        (iso3 in unfccc2018.index and not unfccc2018.loc[iso3].isnull().all()) and
        (iso3 in unfccc2017.index and not unfccc2017.loc[iso3].isnull().all()) and
        (iso3 in unfccc2015.index and not unfccc2015.loc[iso3].isnull().all())):
        
        isos_all_unfccc += [iso3]

print(f"Data compared for {len(isos_all_unfccc)} countries: " + ", ".join(isos_all_unfccc))

colours_unfccc = {
    'UNFCCC2015': [1, 0, 0],
    'UNFCCC2017': [.5, .5, 1],
    'UNFCCC2018': [0, 1, 1],
    'UNFCCC2019': [0, 0, 0]}

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)

for unfccc, name, cat, sze in \
    [unfccc2019, 'UNFCCC2019', 'IPCMLULUCF', 20], \
    [unfccc2018, 'UNFCCC2018', 'IPCMLULUCF', 15], \
    [unfccc2017, 'UNFCCC2017', 'CAT5', 10], \
    [unfccc2015, 'UNFCCC2015', 'CAT5', 5]:
    
    print(f"\n{name}")
    ax.plot(range(1990, 2051), unfccc.loc[isos_all_unfccc, :].sum().values/1000, '.-', label=f"{name} ({cat})", markersize=sze, color=colours_unfccc[name])
    
    for rge in [np.arange(1990, 2000), np.arange(2000, 2010), np.arange(2010, 2018)]:
        print(hpf.rnd(unfccc.loc[isos_all_unfccc, rge].sum().mean()/1000, 1))

XL = [1990, 2020]
ax.set_xlim(XL)
ax.set_xlabel("year", fontweight='bold')
ax.set_ylabel("Kyoto GHG LULUCF emissions\nGt CO$_2$eq AR4", fontweight='bold')
ax.legend()

YL = ax.get_ylim()
ax.text(XL[1], YL[1]+.025*np.diff(YL), f"data for {len(isos_all_unfccc)} countries",
    ha='right', va='bottom')

fig.subplots_adjust(bottom=.15, top=.85, left=.15, right=.95)
path_to_plot = Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_UNFCCC_differentVersions_perPeriod.png')
plt.savefig(path_to_plot, dpi=300)
path_to_pdf = str(path_to_plot).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
# CRF, UNFCCC, FAO comparison of data versions in subplots.

fig = plt.figure(figsize=(15, 5))

XL = [1989, 2020]

ax = fig.add_subplot(1, 3, 1)

for crf, name, sze in [crf2019, 'CRF2019', 20], [crf2018, 'CRF2018', 15], [crf2017, 'CRF2017', 10], [crf2016, 'CRF2016', 5]:
    
    print(f"\n{name}")
    ax.plot(range(1990, 2051), crf.loc[isos_all_crf, :].sum().values/1000, '.-', label=f"{name} (IPCMLULUCF)", markersize=sze, color=colours_crf[name])
    
    for rge in [np.arange(1990, 2000), np.arange(2000, 2010), np.arange(2010, 2018)]:
        print(hpf.rnd(crf.loc[isos_all_crf, rge].sum().mean()/1000, 1))

ax.set_xlim(XL)
ax.set_xlabel("year", fontweight='bold')
ax.set_ylabel("Kyoto GHG LULUCF emissions\nGt CO$_2$eq AR4", fontweight='bold')
ax.legend()

YL = ax.get_ylim()
YL = [YL[0], (1.2*YL[1] if YL[1]>0 else .8*YL[1])]
ax.set_ylim(YL)
ax.text(XL[1], YL[1]+.025*np.diff(YL), f"data for {len(isos_all_crf)} countries",
    ha='right', va='bottom')
ax.text(XL[0]+.025*np.diff(XL), YL[1]-.025*np.diff(YL), "(a) CRF",
    ha='left', va='top', fontweight='bold')

###
ax = fig.add_subplot(1, 3, 2)

for unfccc, name, cat, sze in \
    [unfccc2019, 'UNFCCC2019', 'IPCMLULUCF', 20], \
    [unfccc2018, 'UNFCCC2018', 'IPCMLULUCF', 15], \
    [unfccc2017, 'UNFCCC2017', 'CAT5', 10], \
    [unfccc2015, 'UNFCCC2015', 'CAT5', 5]:
    
    print(f"\n{name}")
    ax.plot(range(1990, 2051), unfccc.loc[isos_all_unfccc, :].sum().values/1000, '.-', label=f"{name} ({cat})", markersize=sze, color=colours_unfccc[name])
    
    for rge in [np.arange(1990, 2000), np.arange(2000, 2010), np.arange(2010, 2018)]:
        print(hpf.rnd(unfccc.loc[isos_all_unfccc, rge].sum().mean()/1000, 1))

ax.set_xlim(XL)
ax.set_xlabel("year", fontweight='bold')
ax.legend()

YL = ax.get_ylim()
YL = [YL[0], (1.2*YL[1] if YL[1]>0 else .8*YL[1])]
ax.set_ylim(YL)
ax.text(XL[1], YL[1]+.025*np.diff(YL), f"data for {len(isos_all_unfccc)} countries",
    ha='right', va='bottom')
ax.text(XL[0]+.025*np.diff(XL), YL[1]-.025*np.diff(YL), "(b) UNFCCC",
    ha='left', va='top', fontweight='bold')

###
ax = fig.add_subplot(1, 3, 3)

for fao, name, cat, sze in [fao2019, 'FAO2019', 'IPCMLULUCF', 15], [fao2018, 'FAO2018', 'IPCMLULUCF', 10], [fao2016, 'FAO2016', 'CAT5', 5]:
    
    print(f"\n{name}")
    ax.plot(range(1990, 2051), fao.loc[isos_all_fao, :].sum().values/1000, '.-', label=f"{name} ({cat})", markersize=sze, color=colours_fao[name])
    
    for rge in [np.arange(1990, 2000), np.arange(2000, 2010), np.arange(2010, 2018)]:
        print(hpf.rnd(fao.loc[isos_all_fao, rge].sum().mean()/1000, 1))

ax.set_xlim(XL)
ax.set_xlabel("year", fontweight='bold')
ax.legend()

YL = ax.get_ylim()
YL = [YL[0], (1.2*YL[1] if YL[1]>0 else .8*YL[1])]
ax.set_ylim(YL)
ax.text(XL[1], YL[1]+.025*np.diff(YL), f"data for {len(isos_all_fao)} countries",
    ha='right', va='bottom')
ax.text(XL[0]+.025*np.diff(XL), YL[1]-.025*np.diff(YL), "(c) FAO",
    ha='left', va='top', fontweight='bold')

fig.subplots_adjust(bottom=.1, top=.9, left=.1, right=.95)
path_to_plot = Path(pth_test, 'KYOTOGHGAR4_IPCMLULUCF_CRF_FAO_UNFCCC_differentVersions_perPeriod.png')
plt.savefig(path_to_plot, dpi=300)
path_to_pdf = str(path_to_plot).replace('.png', '.pdf')
plt.savefig(path_to_pdf, dpi=300)
hpf.crop_pdf(path_to_pdf)
plt.clf()
plt.close(fig)

# %%
# Only use CO2 instead of CO2+CH4+N2O?
