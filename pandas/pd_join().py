# -*- coding: utf-8 -*-
"""
#Diving Into Pandas Join - pd.join()

* Tutorial: https://news.towardsai.net/xfr
* Github: https://github.com/towardsai/tutorials/tree/master/pandas
"""

#Import Required Libraries:

import pandas as pd
import numpy as np

#Creating first DataFrame:

data1 = {"Name":["Alan","Berta","Charlie","Danielle","Euler"],
        "Age":[32,45,35,28,30]}

df1 = pd.DataFrame(data1)
df1

#Creating second DataFrame:

data2 = {"Name":["Berta","Charlie","Danielle","Euler","Frank"],
         "Money":[5000,20000,15000,10000,5000]}

df2 = pd.DataFrame(data2)
df2

#Creating Third DataFrame:

data3 = {"Name":["Berta","Charlie","Danielle"],
         "Books":[10,20,30]}

df3 = pd.DataFrame(data3)
df3

#Creating fourth DataFrame:

data4 = {"Name":["Alan","Berta","Charlie","Danielle","Euler"],
        "Age":[32,45,35,28,30]}

df4 = pd.DataFrame(data4)
df4

#Creating fifth DataFrame:

data5 = {"Money":[5000,20000,15000,10000,5000],
         "Books":[10,20,30,40,50]}

df5 = pd.DataFrame(data5)
df5

#Creating sixth DataFrame:

data6 = {"Name":["Euler","Danielle","Charlie","Berta","Alan"],
        "Age":[30,28,35,45,32]}

df6 = pd.DataFrame(data6)
df6

#Creating seventh DataFrame:

data7 = {"Name":["Rose","Patrick","Euler","Danielle"],
        "Money":[10,20,30,40]}

df7 = pd.DataFrame(data7)
df7

#Using the join() function:

df1.join(df2)

#Using the join() function:

df1.join(df2,lsuffix="_Left",rsuffix="_Right")

#Using the join() function:

df1.join(df2,lsuffix="_Left")

#Using the join() function:

df1.join(df2,rsuffix="_Right")

#Using join() function:

df4.join(df5)

#Using the join() Function:

df1.set_index("Name").join(df2.set_index("Name"))

#Using the join() function:

df1.join(df2.set_index("Name"),on="Name")

#Using the join() function:

df1.set_index("Name").join([df2.set_index("Name"),df3.set_index("Name")])

#Creating a Series:

s = pd.Series(["A","B","C","D"],name="Initial")
s

#Using the join() Function:

df1.join(s)

#Using the join() Function:

df1.set_index("Name").join(df2.set_index("Name"),how="left")

#Using the join() Function:

df1.set_index("Name").join(df2.set_index("Name"),how="right")

#Using join() function:

df1.set_index("Name").join(df2.set_index("Name"), how="outer")

#Using join() function:

df1.set_index("Name").join(df2.set_index("Name"), how="inner")

#Default how = left:
#how=left
#sort=False

df6.set_index("Name").join(other=df7.set_index("Name"),how="left",sort=False)

#Default how = left:
#how=left
#sort=True

df6.set_index("Name").join(other=df7.set_index("Name"),how="left",sort=True)

#how=right
#sort=False

df6.set_index("Name").join(other=df7.set_index("Name"),how="right",sort=False)

#how=right
#sort=True

df6.set_index("Name").join(other=df7.set_index("Name"),how="right",sort=True)

#how=outer
#sort=False

df6.set_index("Name").join(other=df7.set_index("Name"),how="outer",sort=False)

#how=outer
#sort=True

df6.set_index("Name").join(other=df7.set_index("Name"),how="outer",sort=True)

#how=inner
#sort=False

df6.set_index("Name").join(other=df7.set_index("Name"),how="inner",sort=False)

#how=inner
#sort=True

df6.set_index("Name").join(other=df7.set_index("Name"),how="inner",sort=True)
