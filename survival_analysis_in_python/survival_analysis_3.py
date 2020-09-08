#Import required libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter

#Read the data file:
data = pd.read_csv("lung.csv")
data =  data.drop(["Unnamed: 0"],axis=1)
data.head()

#Columns of dataset:
data.columns

#Drop rows with null values:
data= data.dropna(subset=['inst', 'time', 'status', 'age', 'sex','ph.ecog','ph.karno', 'pat.karno', 'meal.cal', 'wt.loss'])
data.head()

#Create an object:
kmf = KaplanMeierFitter() 

#Organize the data:
data.loc[data.status == 1, 'dead'] = 0
data.loc[data.status == 2, 'dead'] = 1
data.head()

#Fit data into our object:
kmf.fit(durations =  data["time"], event_observed = data["dead"])

#Get the event table:
kmf.event_table

#Get required columns from the data:
data = data[[ 'time', 'age', 'sex', 'ph.ecog','ph.karno','pat.karno', 'meal.cal', 'wt.loss', 'dead']]
             
#Get the summary using CoxPHFitter:
cph = CoxPHFitter()
cph.fit(data,"time",event_col="dead")
cph.print_summary()

#Plot the result on graph:
cph.plot()

data.iloc[10:15,:]

#Plotting the data:
d_data = data.iloc[10:15,:]
cph.predict_survival_function(d_data).plot()
