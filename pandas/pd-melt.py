# -*- coding: utf-8 -*-
"""
#Understanding Pandas Melt - pd.melt()

* Tutorial: https://news.towardsai.net/pdm
* Github: https://github.com/towardsai/tutorials/tree/master/pandas/pd-melt.py
"""

#Import Required Libraries:
import pandas as pd

#Raw data in form of dictionary:
data = {"Person":["Alan","Berta","Charlie","Danielle"], #Name of Person
        "House":["A","B","A","C"],                      #Name of houses they live in
        "Age":[32,46,35,28],                            #Age of Person
        "Books":[100,30,20,40],                         #Number of books owned
        "Movies":[10,20,80,60]                          #Number of movie watched
        }

#Converting the raw data into pandas DataFrame:
data_wide = pd.DataFrame(data)

#Printing the pandas DataFrame:
data_wide

#Melting the DataFrame from wide to long format:
#Without specifying any parameters:

data_wide.melt()

#Melting the DataFrame from wide to long format:
#id_vars

data_wide.melt(id_vars=["Person","House"]) #Identifier columns

#Melting the DataFrame from wide to long format:
#id_vars
#value_vars

data_wide.melt(id_vars=["Person","House"],           #Identifier columns
               value_vars=["Age","Books","Movies"])  #Columns to be melted

#Melting the DataFrame from wide to long format:
#id_vars
#value_vars

data_wide.melt(id_vars=["Person"],             #Identifier columns
               value_vars=["Books","Movies"])  #Columns to be melted

#Melting the DataFrame from wide to long format:
#id_vars
#value_vars
#var_name
#value_name

data_wide.melt(id_vars=["Person","House"],          #Identifier columns
               value_vars=["Age","Books","Movies"], #Columns to be melted
               var_name="Info",                     #Renaming the variable column name
               value_name="Numerical")              #Renaming the value column name

#Melting the DataFrame from wide to long format:
#id_vars
#value_vars
#var_name
#value_name

data_wide.melt(id_vars=["Person"],            #Identifier columns
               value_vars=["Books","Movies"], #Columns to be melted
               var_name="Info",               #Renaming the variable column name
               value_name="Numerical")        #Renaming the value column name

#Melting the DataFrame from wide to long format:
#id_vars
#value_vars
#var_name
#value_name
#ignore_index

data_wide.melt(id_vars=["Person","House"],          #Identifier columns
               value_vars=["Age","Books","Movies"], #Columns to be melted
               var_name="Info",                     #Renaming the variable column name
               value_name="Numerical",              #Renaming the value column name
               ignore_index=False)                  #Using the original index

#Creating multiple indexes for columns:
data_wide.columns = [["Person","House","Age","Books","Movies"],
                     ["Name","Flat","Old","Text","Video"]]

#Printing the DataFrame:
data_wide

#Melting the DataFrame from wide to long format:
#id_vars
#value_vars
#var_name
#value_name
#col_level

data_wide.melt(id_vars=["Person","House"],          #Identifier columns
               value_vars=["Age","Books","Movies"], #Columns to be melted
               var_name="Info",                     #Renaming the variable column name
               value_name="Numerical",              #Renaming the value column name
               col_level=0)                         #Using the 0th column level index

#Melting the DataFrame from wide to long format:
#id_vars
#value_vars
#var_name
#value_name
#col_level

data_wide.melt(id_vars=["Name","Flat"],             #Identifier columns
               value_vars=["Old","Text","Video"],   #Columns to be melted
               var_name="Info",                     #Renaming the variable column name
               value_name="Numerical",              #Renaming the value column name
               col_level=1)                         #Using the 1st column level index

#Melting the DataFrame from wide to long format:
#id_vars
#value_vars
#var_name
#value_name
#col_level
#ignore_index

data_wide.melt(id_vars=["Name","Flat"],             #Identifier columns
               value_vars=["Old","Text","Video"],   #Columns to be melted
               var_name="Info",                     #Renaming the variable column name
               value_name="Numerical",              #Renaming the value column name
               ignore_index=False,                  #Using the original index
               col_level=1)                         #Using the 1st column level index
