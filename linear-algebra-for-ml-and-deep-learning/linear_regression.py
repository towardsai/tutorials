# import important libraries

import pandas as pd
import numpy as np

df = pd.read_csv('house_price.csv')

print(df.head())

def get_mean(value):
    total = sum(value)
    length = len(value)
    mean = total/length
    return mean

def get_variance(value):
    mean = get_mean(value)
    mean_difference_square = [pow((item - mean), 2) for item in value]
    variance = sum(mean_difference_square)/float(len(value)-1)
    return variance

def get_covariance(value1, value2):
    value1_mean = get_mean(value1)
    value2_mean = get_mean(value2)
    values_size = len(value1)
    covariance = 0.0
    for i in range(0, values_size):
        covariance += (value1[i] - value1_mean) * (value2[i] - value2_mean)
        
    return covariance / float(values_size - 1)

def linear_regression(df):

    X = df['square_feet']
    Y = df['price']
    m = len(X)

    square_feet_mean = get_mean(X)
    price_mean = get_mean(Y)
    
    #variance of X
    square_feet_variance = get_variance(X)
    price_variance = get_variance(Y)
    
    covariance_of_price_and_square_feet = get_covariance(X, Y)
    w1 = covariance_of_price_and_square_feet / float(square_feet_variance)
    w0 = price_mean - w1 * square_feet_mean
    
    # prediction --> Linear Equation
    prediction = w0 + w1 * X
    
    df['price (prediction)'] = prediction
    return df['price (prediction)']


    predicted = linear_regression(df)

    print(predicted)
    
