from dbfread import DBF
from pandas import DataFrame
import pandas as pd
import re

#Name of the files from the statewide database
file_name_1 = 'c001_g16_sov_data_by_g16_svprec.dbf'
file_name_2 = 'c003_g16_sov_data_by_g16_svprec.dbf'

#Reads DBF file
# df = DataFrame(iter(DBF('state_g16_sov_data_by_g16_svprec.dbf')))
df1 = DataFrame(iter(DBF(file_name_1)))
df2 = DataFrame(iter(DBF(file_name_2)))


# #Transfers to csv file
# df.to_csv("Test_1.csv")
# df2.to_csv("Test_2.csv")
# df1.to_csv("Test_3.csv")



#This function gets the FIP code from the file name.
#File name must follow the standard format
def fip(file_name):

    try:
        found = re.search('c(.+?)_', file_name).group(1)
        return found
    except AttributeError:
        found = "File name is not in the proper format Exp: 'c001_g16_sov_data_by_g16_svprec.dbf' "
        return found


y = fip(file_name_1)



#This function concatenates fip and the svprec
#Adds the new column to the end of the existing DataFrame
def svprec_key(fip_key,dataframe):

    dataframe.insert(1, "Svprec_Key", fip_key + dataframe['svprec'])





z = svprec_key(y, df1)


print(df1.head())