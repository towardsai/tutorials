#Import required libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

#Read the dataset:
data = pd.read_csv("lung.csv")
data.head()

#Print the column names of our data:
print(data.columns)

#Additional info about our dataset:
data.info()

#Statistical info about our dataset:
data.describe()

#Plot histogram for sex of patient:
print (data["sex"].hist())

#Create an object of KaplanMeierFitter:
kmf = KaplanMeierFitter() 

#Organize our data:
#If status = 1 , then dead = 0
#If status = 2 , then dead = 1
data.loc[data.status == 1, 'dead'] = 0
data.loc[data.status == 2, 'dead'] = 1
data.head()

#Fit the parameter values in our object:
kmf.fit(durations =  data["time"], event_observed = data["dead"])

#Print the event table:
kmf.event_table
# Removed = Observed + Censored
# Censored = Person that didn't die.(They are of no use to us!)
# Observed = Persons that died.

#Calculating the survival probability for a given time:
event_at_0 = kmf.event_table.iloc[0,:]

#Calculate the survival probability for t=0:
surv_for_0 = (event_at_0.at_risk - event_at_0.observed)/event_at_0.at_risk
surv_for_0

#Calculating the survival probability for a given time:
event_at_5 = kmf.event_table.iloc[1,:]

#Calculate the survival probability for t=5:
surv_for_5 = (event_at_5.at_risk - event_at_5.observed)/event_at_5.at_risk
surv_for_5

#Calculating the survival probability for a given time:
event_at_11 = kmf.event_table.iloc[2,:]

#Calculate the survival probability for t=11:
surv_for_11 = (event_at_11.at_risk - event_at_11.observed)/event_at_11.at_risk
surv_for_11

#Calculating the actual survival probability at a given time:

surv_after_0 = surv_for_0 
print("Survival Probability After 0 Days: ",surv_after_0)

#Calculating the actual survival probability at a given time:
surv_after_5 = surv_for_0 * surv_for_5
print("Survival Probability After 5 Days: ",surv_after_5)


#Calculating the actual survival probability at a given time:surv_after_11 = surv_for_0 * surv_for_5 * surv_for_11
print("Survival Probability After 11 Days: ",surv_after_11)

#Get the probability values the easy way!
print("Survival probability for t=0: ",kmf.predict(0))
print("Survival probability for t=5: ",kmf.predict(5))
print("Survival probability for t=11: ",kmf.predict(11))

#Predicting the surviaval probability for an array of value:
kmf.predict([0,5,11,12])

#To get the full list:
kmf.survival_function_

#Plot the graph:
kmf.plot()
plt.title("The Kaplan-Meier Estimate")
plt.xlabel("Number of days")
plt.ylabel("Probability of survival")

#The median number of days:
print("The median survival time: ",kmf.median_survival_time_)

#Survival probability with confidence interval:
kmf.confidence_interval_survival_function_

#Plot survival function with confidence interval:
confidence_surv_func = kmf.confidence_interval_survival_function_
plt.plot(confidence_surv_func["KM_estimate_lower_0.95"],label="Lower")
plt.plot(confidence_surv_func["KM_estimate_upper_0.95"],label="Upper")
plt.title("Survival Function With Confidence Interval")
plt.xlabel("Number of days")
plt.ylabel("Survival Probability")
plt.legend()

#Probabaility of a subject dying:
#p(1022) = p(0) +......+p(1022)
kmf.cumulative_density_

#Plot the cumulative density graph:
kmf.plot_cumulative_density()
plt.title("Cumulative Density Plot")
plt.xlabel("Number of days")
plt.ylabel("Probability of person's death")

#Cumulative density with confidence interval:
kmf.confidence_interval_cumulative_density_

#Plot cumulative density with confidence interval:
confidence_cumulative_density = kmf.confidence_interval_cumulative_density_
plt.plot(kmf.confidence_interval_cumulative_density_["KM_estimate_lower_0.95"],label="Lower")
plt.plot(kmf.confidence_interval_cumulative_density_["KM_estimate_upper_0.95"],label="Upper")
plt.title("Cumulative Density With Confidence Interval")
plt.xlabel("Number of days")
plt.ylabel("Cumulative Density")
plt.legend()

#Find cumulative density at a specific time:
kmf.cumulative_density_at_times(times=1022)

#Conditional median time to event of interest:
kmf.conditional_time_to_event_

#Conditional median time left for event:
median_time_to_event = kmf.conditional_time_to_event_
plt.plot(median_time_to_event,label="Median Time left")
plt.title("Medain time to event")
plt.xlabel("Total days")
plt.ylabel("Conditional median time to event")
plt.legend()

#Hazard function:
from lifelines import NelsonAalenFitter

#Create an object of NelsonAalenFitter:
naf = NelsonAalenFitter()

#Fit our data into the object:
naf.fit(data["time"], event_observed=data["dead"])

#Print the cumulative hazard:
naf.cumulative_hazard_

#Plot the cumulative hazard grpah:
naf.plot_cumulative_hazard()
plt.title("Cumulative Probability for Event of Interest")
plt.xlabel("Number of days")
plt.ylabel("Cumulative Probability of person's death")

#We can predict the value at a certain point :
print("Time = 500 days: ",naf.predict(500))
print("Time = 1022 days: ",naf.predict(1022))

#Cumulative hazard with confidence interval:
naf.confidence_interval_

#Plot cumulative hazard with confidence interval:
confidence_interval = naf.confidence_interval_
plt.plot(confidence_interval["NA_estimate_lower_0.95"],label="Lower")
plt.plot(confidence_interval["NA_estimate_upper_0.95"],label="Upper")
plt.title("Cumulative hazard With Confidence Interval")
plt.xlabel("Number of days")
plt.ylabel("Cumulative hazard")
plt.legend()

#Plot the cumulative_hazard and cumulative density:
kmf.plot_cumulative_density(label="Cumulative Hazard")
naf.plot_cumulative_hazard(label="Cumulative Density")
plt.xlabel("Number of Days")
