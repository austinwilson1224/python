# 1. import numpy and see vertion number
import  numpy as np 
np.__version__

#  2. create a 1D array
array = np.array([1,2,3])
array
array = np.arange(10)
array

# 3. create a boolean array
array = np.array([True,True,False])
array = np.repeat(True,  9).reshape(3,-1)
array

#  4. extract elemts that meet a certain condidion
array = np.arange(10)
array
mask = array % 2 == 1
mask
array[mask]
array[array % 2 != 0]