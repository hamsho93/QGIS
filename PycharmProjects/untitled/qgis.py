from dbfread import DBF
from pandas import DataFrame
import pandas as pd
import re

#Name of the files from the statewide database
file_name_1 = 'c001_g16_sov_data_by_g16_svprec.dbf'
file_name_2 = 'c003_g16_sov_data_by_g16_svprec.dbf'
file_name_3 = 'c005_g16_sov_data_by_g16_svprec.dbf'


#Reads DBF file
# df = DataFrame(iter(DBF('state_g16_sov_data_by_g16_svprec.dbf')))
df1 = DataFrame(iter(DBF(file_name_1)))
df2 = DataFrame(iter(DBF(file_name_2)))
df3 = DataFrame(iter(DBF(file_name_3)))


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


##LOCation

#This function concatenates fip and the svprec
#Adds the new column "Svprec_Key" to the end of the existing DataFrame
#Adds "FIPS" column
def svprec_key(fip_key,dataframe):

    dataframe.insert(0, "FIPS", "6"+ fip(fip_key))
    dataframe.insert(1, "Svprec_Key", "6" + fip(fip_key) + dataframe['svprec'])


svprec_key(file_name_1, df1)
svprec_key(file_name_3, df3)


# Joins the dataframes together
frames = [df1, df3]
result = pd.DataFrame(pd.concat(frames))


#Adds Election and Type column into the final dataframe
result.insert(0,"Election","g16")
result.insert(1,"Type", "sov")


result.to_csv("Result.csv")


#Next Step: Figure how to read in all the files into this program