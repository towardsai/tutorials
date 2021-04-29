# -*- coding: utf-8 -*-
"""
#Handling Missing Values in Pandas

* Tutorial: https://news.towardsai.net/hmv
* Github: https://github.com/towardsai/tutorials/tree/master/pandas
"""

#Import Required Libraries:
import pandas as pd

#Raw data in form of dictionary:
info = {"Person":["Alan","Berta","Charlie","Danielle","Euler",pd.NA], #Name of Person.
        "Age":[32,45,35,28,30,pd.NA],                                 #Age of Person.
        "Degree":["CS","Biology","Physics",pd.NA,"Physics","CS"],     #Major.
        "Country":["USA","Mexico","USA","Canada","USA","Canada"],     #Country of study.
        "Books":[10,pd.NA,30,40,50,60],                               #Books owned.
        "Batch Size":[200,100,50,200,50,pd.NA]                        #Batch Size.
        }

#Converting the raw data into DataFrame:
data = pd.DataFrame(info)

#Printing the DataFrame:
data

#Dropping the rows where at least one element is missing.

data.dropna()

#Drop the rows where at least one element is missing.

data.dropna(axis=0)

#Drop the rows where at least one element is missing.

data.dropna(axis="rows")

#Drop the columns where at least one element is missing.

data.dropna(axis=1)

#Drop the columns where at least one element is missing.

data.dropna(axis="columns")

#Drop the rows where at least one element is missing.

data.dropna(how="any")

#Import Required Libraries:
import pandas as pd

#Raw data in form of dictionary:
info = {"Person":["Alan","Berta",pd.NA,"Charlie","Danielle","Euler"], #Name of Person.
        "Age":[32,45,pd.NA,35,28,30],                                 #Age of Person.
        "Degree":["CS","Biology",pd.NA,"Physics",pd.NA,"Physics"],    #Major.
        "Country":["USA","Mexico",pd.NA,"USA","Canada","USA"],        #Country of study.
        "Books":[10,pd.NA,pd.NA,30,40,50],                            #Books owned.
        "Batch Size":[200,100,pd.NA,50,200,50]                        #Batch Size.
        }

#Converting the raw data into DataFrame:
data = pd.DataFrame(info)

#Printing the DataFrame:
data

#Drop the rows if all elements are missing.

data.dropna(how="all")

#Keep the rows with at least 5 non missing elements.

data.dropna(thresh=5)

#Import Required Libraries:
import pandas as pd

#Raw data in form of dictionary:
info = {"Person":["Alan","Berta",pd.NA,"Charlie","Danielle","Euler"], #Name of Person.
        "Age":[32,pd.NA,pd.NA,35,pd.NA,30],                           #Age of Person.
        "Degree":["CS","Biology",pd.NA,"Physics",pd.NA,"Physics"],    #Major.
        "Country":["USA",pd.NA,pd.NA,"USA","Canada","USA"],           #Country of study.
        "Books":[10,pd.NA,pd.NA,30,40,50],                            #Books owned.
        "Batch Size":[200,100,pd.NA,50,200,50]                        #Batch Size.
        }

#Converting the raw data into DataFrame:
data = pd.DataFrame(info)

#Printing the DataFrame:
data

#Define in which columns to look for missing elements.

data.dropna(subset=["Person","Degree","Country"])

#Import Required Libraries:
import pandas as pd

#Raw data in form of dictionary:
info = {"Person":["Alan","Berta","Charlie","Danielle","Euler",pd.NA], #Name of Person.
        "Age":[32,45,35,28,30,pd.NA],                                 #Age of Person.
        "Degree":["CS","Biology","Physics",pd.NA,"Physics","CS"],     #Major.
        "Country":["USA","Mexico","USA","Canada","USA","Canada"],     #Country of study.
        "Books":[10,pd.NA,30,40,50,60],                               #Books owned.
        "Batch Size":[200,100,50,200,50,pd.NA]                        #Batch Size.
        }

#Converting the raw data into DataFrame:
data = pd.DataFrame(info)

#Printing the DataFrame:
data

#Inplace=True will make changes in the original DataFrame.
#It will return nothing.

data.dropna(inplace=True)
data
