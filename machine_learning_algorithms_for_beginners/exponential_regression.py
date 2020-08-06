# Import required libraries:
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
# Dataset values :
day = np.arange(0,8)
weight = np.array([251,209,157,129,103,81,66,49])

# Exponential Function :
def expo_func(x, a, b):
  return a * b ** x
 
#popt :Optimal values for the parameters
#pcov :The estimated covariance of popt

popt, pcov = curve_fit(expo_func, day, weight)
weight_pred = expo_func(day,popt[0],popt[1])

# Plotting the data
plt.plot(day, weight_pred, 'r-')
plt.scatter(day,weight,label='Day vs Weight')
plt.title("Day vs Weight a*b^x")
plt.xlabel('Day')
plt.ylabel('Weight')
plt.legend()
plt.show()

# Equation
a=popt[0].round(4)
b=popt[1].round(4)
print(f'The equation of regression line is y={a}*{b}^x')
