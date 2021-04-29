# -*- coding: utf-8 -*-
"""
#Handling Missing Values in Pandas

* Tutorial: https://news.towardsai.net/hmv
* Github https://github.com/towardsai/tutorials/tree/master/pandas
"""

#Import Required Libraries:
import pandas as pd

#Raw data in form of dictionary:
info = {"Person":["Alan","Berta","Charlie","Danielle","Euler",pd.NA], #Name of Person.
        "Age":[32,45,35,28,30,pd.NA],                                 #Age of Person.
        "Degree":["CS",pd.NA,pd.NA,pd.NA,"Physics",pd.NA],            #Major.
        "Country":["USA","Mexico","USA",pd.NA,"USA",pd.NA],           #Country of study.
        "Books":[10,pd.NA,30,pd.NA,50,60],                            #Books owned.
        "Batch Size":[200,100,50,200,50,pd.NA]                        #Batch Size.
        }

#Converting the raw data into DataFrame:
data = pd.DataFrame(info)

#Printing the DataFrame:
data

#Replacing all missing values with 0:

data.fillna(value=0)

#Replacing values:

#Values to be used for specific column:
values = {"Person":"---", "Age":0, "Degree":"---","Books":0,"Batch Size":0}

#Replacing the values:
data.fillna(value=values)

#Using method="ffill":

data.fillna(method="ffill")

#Using method="pad":
#Same as method="ffill"

data.fillna(method="pad")

#Using method="ffill":
#Using axis=0 (Default)

data.fillna(method="ffill", axis=0)

#Using method="ffill":
#Using axis=1

data.fillna(method="ffill", axis=1)

#Using method="bfill":

data.fillna(method="bfill")

#Using method="backfill":
#Same as method="bfill"

data.fillna(method="backfill")

#Using method="bfill":
#Using axis=0 (Default)

data.fillna(method="bfill",axis=0)

#Using method="bfill":
#Using axis=1:

data.fillna(method="bfill",axis=1)

#Using method="ffill":
#Using axis=0:
#Using limit=1:

data.fillna(method="ffill",axis=0, limit=1)

#Using method="ffill":
#Using axis=1:
#Using limit=1:

data.fillna(method="ffill",axis=1, limit=1)

#Using method="bfill":
#Using axis=0:
#Using limit=1:

data.fillna(method="bfill",axis=0, limit=1)

#Using method="bfill":
#Using axis=1:
#Using limit=1:

data.fillna(method="bfill",axis=1, limit=1)

#Import Required Libraries:
import pandas as pd

#Raw data in form of dictionary:
info = {"Age":[32.0,45.0,35.0,28.0,30.0,40.0],
        "Books":[10.0,pd.NA,30.0,40.0,50.0,60.0],
        "Batch Size":[200,100,50,200,50,300]
      }

#Converting the raw data into DataFrame:
data = pd.DataFrame(info)

#Printing the DataFrame:
data

data.dtypes

a = data.fillna(0,downcast="infer")
a

a.dtypes

#Inplace=True will make changes in the original DataFrame.
#It will return nothing.

data.fillna(value=0,inplace=True)
data

#Import Required Libraries:
import pandas as pd

#Raw data in form of dictionary:
info = {"Person":["Alan","Berta","Charlie","Danielle","Euler",pd.NA], #Name of Person.
        "Age":[32,45,35,28,30,pd.NA],                                 #Age of Person.
        "Degree":["CS",pd.NA,pd.NA,pd.NA,"Physics",pd.NA],            #Major.
        "Country":["USA","Mexico","USA",pd.NA,"USA",pd.NA],           #Country of study.
        "Books":[10,pd.NA,30,pd.NA,50,60],                            #Books owned.
        "Batch Size":[200,100,50,200,50,pd.NA]                        #Batch Size.
        }

#Converting the raw data into DataFrame:
data = pd.DataFrame(info)

#Printing the DataFrame:
data

#Using pd.DataFrame.bfill():

data.bfill()

#Using pd.DataFrame.backfill():

data.backfill()

#Using pd.DataFrame.ffill():

data.ffill()

#Using pd.DataFrame.pad():

data.pad()
