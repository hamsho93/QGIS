from dbfread import DBF
from pandas import DataFrame
import pandas as pd
import re
import os


#This function gets the FIP code from the file name.
#File name must follow the standard format
def fip(file_name):

    try:
        found = re.search('c(.+?)_', file_name).group(1)
        return found
    except AttributeError:
        found = "File name is not in the proper format Exp: 'c001_g16_sov_data_by_g16_svprec.dbf' "
        return found



#This function concatenates fip and the svprec
#Adds the new column "Svprec_Key" to the end of the existing DataFrame
#Adds "FIPS" column
def svprec_key(fip_key,dataframe):

    dataframe.insert(0, "FIPS", "6"+ fip(fip_key))
    dataframe.insert(1, "Svprec_Key", "6" + fip(fip_key) + dataframe['svprec'])





PATH = r'C:\GIT\QGIS\PycharmProjects\untitled\Census_Data'
arr = os.listdir(PATH)

print(arr)
dicts = {}
i = 0
for file_name in arr:
    print(file_name)
    df = DataFrame(iter(DBF(file_name)))
    fip(file_name)
    svprec_key(file_name, df)

    dicts[i] = df
    i += 1

result = pd.concat(dicts.values(), ignore_index=True)
result.insert(0,"Election","g16")
result.insert(1,"Type", "sov")
result.to_csv("Result.csv")

