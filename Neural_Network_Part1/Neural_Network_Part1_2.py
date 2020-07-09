# Import required libraries:
import numpy as np

# Define input features:
input_features = np.array([[0,0],[0,1],[1,0],[1,1]])
print (input_features.shape)
print (input_features)

# Define target output:
target_output = np.array([[0,1,1,1]])

# Reshaping our target output into vector:
target_output = target_output.reshape(4,1)
print(target_output.shape)
print (target_output)

# Define weights:
weights = np.array([[0.1],[0.2]])
print(weights.shape)
print (weights)

# Define learning rate:
lr = 0.05

# Sigmoid function:
def sigmoid(x):
  return 1/(1+np.exp(-x))
 
 # Derivative of sigmoid function:
def sigmoid_der(x):
  return sigmoid(x)*(1-sigmoid(x))
 
# Main logic for neural network:
# Running our code 10000 times:

for epoch in range(10000):
  inputs = input_features
  
  #Feedforward input:
  pred_in = np.dot(inputs, weights)
  
  #Feedforward output:
  pred_out = sigmoid(pred_in)
  
  #Backpropogation 
  #Calculating error
  error = pred_out - target_output
  x = error.sum()
 
  #Going with the formula:
  print(x)
 
  #Calculating derivative:
  dcost_dpred = error
  dpred_dz = sigmoid_der(pred_out)
 
  #Multiplying individual derivatives:
  z_delta = dcost_dpred * dpred_dz#Multiplying with the 3rd individual derivative:
  inputs = input_features.T
  weights -= lr * np.dot(inputs, z_delta)
 
 
#Taking inputs:
single_point = np.array([1,0])

#1st step:
result1 = np.dot(single_point, weights)

#2nd step:
result2 = sigmoid(result1)

#Print final result
print(result2)

#Taking inputs:
single_point = np.array([0,0])

#1st step:
result1 = np.dot(single_point, weights)

#2nd step:
result2 = sigmoid(result1)

#Print final result
print(result2)

#Taking inputs:
single_point = np.array([1,1])

#1st step:
result1 = np.dot(single_point, weights)

#2nd step:
result2 = sigmoid(result1)

#Print final result
print(result2)
