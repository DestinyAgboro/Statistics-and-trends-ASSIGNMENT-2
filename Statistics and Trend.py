# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:48:08 2022

@author: USER
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
Creating my function which accepts a filename as an input, 
reads a dataframe in Worldbank format, and outputs two dataframes:
one with years as columns, the other with nations.
"""
def ClimateChangeData(filename,nations_name,fields,indicator):
    DataFrame = pd.read_csv(filename,skiprows=4)
    DataFrame = DataFrame[DataFrame['Indicator Name'] == indicator]
    DataFrame = DataFrame[fields]
    DataFrame.set_index('Country Name', inplace = True)
    DataFrame = DataFrame.loc[nations_name]
    return DataFrame,DataFrame.transpose()
filename = 'API_19_DS2_en_csv_v2_4700503.csv'
nations_name = ['India','China','Ghana','Nigeria','Argentina']
fields = ['Country Name', '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000']
indicators = ['Urban population', 'CO2 emissions (metric tons per capita)', 'Electric power consumption (kWh per capita)']

"""
Below is the dataframe of Urban population indicator for 
India,China,Ghana,Nigeria and Argentina with its transpose with
nations as columns from 1990 to 2000.
"""
uban_pops,transpose_uban_pops = ClimateChangeData(filename,nations_name,fields,indicators[0])
print(uban_pops)
print()
print(uban_pops.describe())
print()
print(transpose_uban_pops)
print()

"""
Below is the dataframe of CO2 emissions (metric tons per capita) indicator for 
India,China,Ghana,Nigeria and Argentina with its transpose with
nations as columns from 1990 to 2000.
"""
Eachcountry_CO2Emi,transpose_Eachcountry_CO2emi = ClimateChangeData(filename,nations_name,fields,indicators[1])
print(Eachcountry_CO2Emi)
print()
print(Eachcountry_CO2Emi.describe())
print()
print(transpose_Eachcountry_CO2emi)
print()

