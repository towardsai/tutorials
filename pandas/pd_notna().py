# -*- coding: utf-8 -*-
"""
#Handling Missing Values in Pandas

* Tutorial: https://news.towardsai.net/hmv
* Github
"""

#Import Required Libraries:

import numpy as np
import pandas as pd

#Scalar arguments:
#Numerical value

pd.notna(28)

#Scalar arguments:
#String value

pd.notna("Pratik")

#Scalar arguments:
#Empty strings are not considered as NA values

pd.notna("")

#Scalar arguments:
#Infinite values are not considered as NA values

pd.notna(np.inf)

#Scalar arguments:
#NaN: Not a Number

pd.notna(np.NaN)

#Scalar arguments:
#None

pd.notna(None)

#Scalar arguments:
#NA: Not Available

pd.notna(pd.NA)

#Scalar arguments:
#NaT: Not a Timestamp

pd.notna(pd.NaT)

#nd-arrays:

arr = np.array([1,2,"Blue"])
print(arr)
print("\n")
pd.notna(arr)

#nd-arrays:
#Empty strings are not considered as NA values

arr = np.array([[1,2,None],
                [3,4,pd.NA],
                [5,np.NaN,6],
                ["",7,8],
                ["Blue",pd.NaT,"Red"]])

print(arr)
print("\n")
pd.notna(arr)

#For index values:

id = pd.Index([1,2,np.NaN,"Blue"])
print(id)
print("\n")
pd.notna(id)

#For index values:

id = pd.DatetimeIndex([pd.Timestamp("2020-10-28"),
                      pd.Timestamp(""),
                      None,
                      np.NaN,
                      pd.NA,
                      pd.NaT])

print(id)
print("\n")
pd.notna(id)

#Series:

s = pd.Series([1,2,3,None,4,np.NaN,pd.NA,pd.NaT,"Blue"])
print(s)
print("\n")
pd.notna(s)

#DataFrame:

df = pd.DataFrame({"Name":["Alan","Berta","Charlie",None],
                   "Age":[32,45,np.NaN,28],
                   "Birthday":[pd.NaT,None,pd.Timestamp("1975-10-28"),np.NaN],
                   "Country":["USA","","USA","Canada"]
                   })

print(df)
print("\n")
pd.notna(df)

pd.isnull

pd.notnull
