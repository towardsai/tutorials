# -*- coding: utf-8 -*-
"""

# Implementation of Correlation Matrix and covariance Matrix

*   This is used with Eigenvalues and Eigenvectors of PCA

**Import Packages**
"""

import pandas as pd
import numpy as np

matrix = np.array([[0, 3, 4], [1, 2, 4], [3, 4, 5]]) 
print(matrix)

"""**Convert to covariance**"""

np.cov(matrix)

"""**Convert to Correlation Matrix**"""

matrix_a = np.array([[0.1, .32, .2,  0.4, 0.8], 
             [.23, .18, .56, .61, .12], 
             [.9,   .3,  .6,  .5,  .3],  
             [.34, .75, .91, .19, .21]])

pd.DataFrame(matrix_a).corr()

np.corrcoef(matrix_a.T)