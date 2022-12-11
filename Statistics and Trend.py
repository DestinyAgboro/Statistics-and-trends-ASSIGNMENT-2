# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:48:08 2022

@author: USER
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ClimateChangeData(filename,nations_name,fields,indicator):
    """
    filename: read the csv file from Worldbank into it
    Nations_name:holds all the nations nane
    fields: contains all the years
    indicator :this takes the different indicator use for the analysis such as Urban population,CO2 emissions and Electric power consumption    
    
    Creating function which accepts a filename as an input, 
    reads a dataframe in Worldbank format, and outputs two dataframes:
    one with years as columns, the other with nations.
    """
    df = pd.read_csv(filename,skiprows=4)
    df = df[df['Indicator Name'] == indicator]
    df = df[fields]
    df.set_index('Country Name', inplace = True)
    df = df.loc[nations_name]
    return df,df.transpose()

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
"""
Below is the dataframe of Electric power consumption (kWh per capita) indicator for 
India,China,Ghana,Nigeria and Argentina with its transpose with
nations as columns from 1990 to 2000.
"""
Nations_Power_consump,transpose_Nations_Power_consump= ClimateChangeData(filename,nations_name,fields,indicators[2])
print(Nations_Power_consump)
print()
print(Nations_Power_consump.describe())
print()
print(transpose_Nations_Power_consump)
print()
"""
A grouped bar of CO2 emission for various nations over years from 1990 to 2000
"""
Eachcountry_CO2Emi.plot(kind='bar')
plt.title('Grouped bar of CO2 emission for various nations over years')
plt.xlabel('Countries')
plt.ylabel('Co2 emission')
plt.rcParams["figure.dpi"] = 500
plt.show()

"""
Trend in Urban Population for These Five Nations Year-over-Year
"""
plt.figure(figsize=(10,7),dpi=500)
for i in range(len(nations_name)):
    plt.plot(transpose_uban_pops.index,transpose_uban_pops[nations_name[i]],label=nations_name[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Trend in Urban Population for These Five Nations Year-over-Year')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.show()
"""
The below are Correlation heatmap for Argentina
"""
print(transpose_uban_pops['Argentina'])
print()
Argentina = pd.DataFrame(
{'Urban Population': transpose_uban_pops['Argentina'],
'Co2 emission': transpose_Eachcountry_CO2emi['Argentina'],
'power.consumption': transpose_Nations_Power_consump['Argentina']},
['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000'])
print(Argentina.corr())
print()
plt.figure(figsize=(8,5))
sns.heatmap(Argentina.corr(),annot=True,cmap='Greens')
plt.title('Correlation heatmap Argentina')
plt.show()

"""
The below are Correlation heatmap for India
"""
print(transpose_uban_pops['India'])
print()
India = pd.DataFrame(
{'Urban Population': transpose_uban_pops['India'],
'Co2 emission': transpose_Eachcountry_CO2emi['India'],
'power.consumption': transpose_Nations_Power_consump['India']},
['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000'])
print(India.corr())
print()
plt.figure(figsize=(8,5))
sns.heatmap(India.corr(),annot=True,cmap='Oranges')
plt.title('Correlation heatmap India')
plt.show()


