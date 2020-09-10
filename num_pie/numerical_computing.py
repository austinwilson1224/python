# https://www.youtube.com/watch?v=ZB7BZMhfPgk

a = [1,2,3,4,5]
b = [10,11,12,13,14]

a + b

result = []

for first, second in zip(a,b):
    result.append(first,second)
print(result)


import numpy as np
a = np.array([1,2,3,4], dtype="float64")

a

b = a.astype('int16')
b
a.dtype

f = np.array([1.2,2.3,4.5,5.6])

a.dtype
a = a.astype('int32')
a.dtype

a.ndim

a.shape


# number of elements in the array, not the size
a.size

a + f

a / f

a ** f

a * 10

# Universal Functions (ufuncs) 
np.sin(a)


# Multi-dimensional Arrays 

a = np.array([10,11,12,13,14])
a[1:3]
a[1:-2]
a[-4:3]

# ommitting indicies
a[:3] # grab first 3 elements
a[-2:] # grab last 2 elements
a[::2] # every other element 

# array slicing
test = list(range(0,6))
test2 = list(range(10,16))
test
a = np.array([test,test2])
a

a = np.array([list(range(0,6)),list(range(10, 16)), list(range(20,26)), list(range(30,36)), list(range(40,46)), list(range(50,56))])
a

# array slicing
# row is the first dimension
a[0, 3:5]
a[:,2]
a[2::2, ::2]

a = np.arange(25).reshape(5,5)
red = a[:,1::2]
red
red = a[:, [1,3]]
red

yellow = a[-1,:]
yellow
yellow = a[4,:]
yellow
yellow = a[4]
yellow

blue = a[1::2,0:3:2]
blue
blue = a[1::2, :3:2]
blue
blue = a[1::2, :-1:2]
blue


a = np.array([1,2,3,4])
b = a[:2]
a
b
b[0] = -1
a 
b 

b = a.copy()
c = np.copy(a)
b == c

a[-2:] = [-1,-2]
a
a[-2:] = 99
a


a.__setitem__(0,100)
a
a.__getitem__(0)

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

import numpy as np

# fancy indexing
a = np.arange(0, 80, 10)
indicies = [1, 2, -3]
y = a[indicies]
y
a[indicies] = 99
a

# indexing with booleans 
mask = np.array([0,1,1,0,0,1,0,0], dtype=bool)
y = a[mask]
y




a = np.array([-1,-3,1,4,-6,9,3])
a<0

negative = a < 0

a[negative]
a[negative] = 0

a = np.arange(25).reshape(5,5)

# blue elements
a[[0,2,3,3],[2,3,1,4]]



# all elements divisible by 3
mask = a % 3 == 0
mask
a[mask]

# nan

np.nan

# 
a = np.arange(15).reshape(5,3)
b = np.arange(3)

a+b

a = np.arange(3)
b = np.arange(5).reshape(5,1)
b

a+b



# sum
a = np.array([[1,2,3],[4,5,6]])
a.sum()
a.sum(axis=0)
a.sum(axis=-1)
a.shape
a.sum(axis=0).shape
a.sum(axis=-1).shape
np.sum(a, axis=0)
np.min(a)
np.max(a)
a.min()
a.max()

# agrmin / argmax gives you the index of the element 
import numpy as np
a = np.array([-1,1,5,5])
a == a.max()
np.where(a==a.max())

from numpy  import loadtxt
data = loadtxt('/Users/austinwilson/downloads/Numpy-Tutorial-SciPyConf-2019-master/exercises/wind_statistics/wind.data')
data