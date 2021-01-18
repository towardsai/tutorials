# import numpy
import numpy as np 

# define our sigmoid function
def sigmoid(x):
  return 1/ (1 + np.exp(-x))

# craete the AN
class Neuron:
  def __init__(self, weights, bias):
    self.weights = weights
    self.bias = bias

  def feedforwards(self, inputs):
    total = np.dot(self.weights, inputs) + self.bias
    return sigmoid(total)

weights = np.array([0, 1])
bias = 4

neuron = Neuron(weights, bias)

x = np.array([2, 3])

forward = neuron.feedforwards(x)

print(forward)
