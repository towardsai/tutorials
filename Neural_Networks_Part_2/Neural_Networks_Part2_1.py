# Import required libraries :
import numpy as np

# Define input features :
input_features = np.array([[0,0],[0,1],[1,0],[1,1]])
print (input_features.shape)
print (input_features)

# Define target output :
target_output = np.array([[0,1,1,1]])

# Reshaping our target output into vector :
target_output = target_output.reshape(4,1)
print(target_output.shape)
print (target_output)

# Define weights :
# 6 for hidden layer
# 3 for output layer
# 9 total
weight_hidden = np.array([[0.1,0.2,0.3],
                         [0.4,0.5,0.6]])
weight_output = np.array([[0.7],[0.8],[0.9]])

# Learning Rate :
lr = 0.05

# Sigmoid function :
def sigmoid(x):
 return 1/(1+np.exp(-x))
 
# Derivative of sigmoid function :
def sigmoid_der(x):
 return sigmoid(x)*(1-sigmoid(x))
 
for epoch in range(200000):
 # Input for hidden layer :
 input_hidden = np.dot(input_features, weight_hidden)
 
 # Output from hidden layer :
 output_hidden = sigmoid(input_hidden)
 
 # Input for output layer :
 input_op = np.dot(output_hidden, weight_output)
 
 # Output from output layer :
 output_op = sigmoid(input_op)
 
#========================================================

 # Phase1
 
 # Calculating Mean Squared Error :
 error_out = ((1 / 2) * (np.power((output_op - target_output), 2)))
 print(error_out.sum())
 
 # Derivatives for phase 1 :
 derror_douto = output_op - target_output
 douto_dino = sigmoid_der(input_op) 
 dino_dwo = output_hidden
 derror_dwo = np.dot(dino_dwo.T, derror_douto * douto_dino)
 
#===========================================================
 
 # Phase 2 
 # derror_w1 = derror_douth * douth_dinh * dinh_dw1
 # derror_douth = derror_dino * dino_outh
 
 # Derivatives for phase 2 :
 derror_dino = derror_douto * douto_dino
 dino_douth = weight_output
 derror_douth = np.dot(derror_dino , dino_douth.T)
 douth_dinh = sigmoid_der(input_hidden) 
 dinh_dwh = input_features
 derror_wh = np.dot(dinh_dwh.T, douth_dinh * derror_douth)
  
 # Update Weights
 weight_hidden -= lr * derror_wh
 weight_output -= lr * derror_dwo 
 
# Final hidden layer weight values :
print (weight_hidden)

# Final output layer weight values :
print (weight_output)

# Predictions :
#Taking inputs :
single_point = np.array([1,1])

#1st step :
result1 = np.dot(single_point, weight_hidden) 

#2nd step :
result2 = sigmoid(result1)

#3rd step :
result3 = np.dot(result2,weight_output)

#4th step :
result4 = sigmoid(result3)
print(result4)

#=================================================

#Taking inputs :
single_point = np.array([0,0])

#1st step :
result1 = np.dot(single_point, weight_hidden) 

#2nd step :
result2 = sigmoid(result1)

#3rd step :
result3 = np.dot(result2,weight_output)

#4th step :
result4 = sigmoid(result3)
print(result4)

#=====================================================

#Taking inputs :
single_point = np.array([1,0])

#1st step :
result1 = np.dot(single_point, weight_hidden) 

#2nd step :
result2 = sigmoid(result1)

#3rd step :
result3 = np.dot(result2,weight_output)

#4th step :
result4 = sigmoid(result3)
print(result4)
