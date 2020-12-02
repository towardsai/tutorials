import numpy as np
import numpy.ma as ma

original_array = np.array([1, 2, 3, -1, 5])
original_array

masked = ma.masked_array(original_array, mask=[0, 0, 0, 1, 0])
masked
