#Import required libraries:
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

#Define probability of success:
p = 0.7

#Find the statisticsal values:
mean, var, skew, kurt = bernoulli.stats(p, moments='mvsk')

#Print mean:
print("Mean = ",mean)

#Print variance:
print("Variance =  ",var)

#Print skewness:
print("Skewness = ",skew)

#Print kurtosis:
print("Kurtosis = ",kurt)

#Get only mean value:
mean = bernoulli.mean(p)
print("Mean = ",mean)

#Get only median value:
median = bernoulli.median(p)
print("Median = ",median)

#Get only variance value:
var = bernoulli.var(p)
print("Variance = ",var)

#Get only standard deviation value:
std = bernoulli.std(p)
print("Standard Deviation = ",std)

#Get Probability Mass Function(PMF):
x = [0,1]
p=0.7
print("Probability Mass Function = ",bernoulli.pmf(x,p))

#Plot the graph for Probability Mass Function(PMF):
x = [0,1]
p=0.7
plt.scatter(x,bernoulli.pmf(x,p),label="PMF")
plt.title("Probability Mass Function")
plt.xlabel("Data Points")
plt.ylabel("Probability")
plt.legend()

#Get Cumulative Density Function(CDF):
x = [0,1]
p = 0.7
print("Cumulative Density Function = ",bernoulli.cdf(x,p))

#Plot the Cumulative Density Function(CDF):
x = [0,1]
p = 0.7
plt.scatter(x,bernoulli.cdf(x,p),label="CDF")
plt.title("Cumulative Density Function")
plt.xlabel("Data Points")
plt.ylabel("Probability")
plt.legend()

#Plot the bar graph for PMF:
x = [0,1]
p = 0.7
plt.bar(x,bernoulli.pmf(x,p),width=0.1,color=["r","b"])
plt.title("Probability Mass Function")
plt.xlabel("Data Points")
plt.ylabel("Probability")


#Plot the bar graph for CDF:
x = [0,1]
p = 0.7
plt.bar(x,bernoulli.cdf(x,p),width=0.1,color=["r","b"])
plt.title("Cumulative Density Function")
plt.xlabel("Data Points")
plt.ylabel("Probability")

#Generate Output for Random Bernoulli Events:
p = 0.7
r = bernoulli.rvs(p, size=100)
print(r)
