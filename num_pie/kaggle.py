'''
problems selected from: https://www.kaggle.com/python10pm/learn-numpy-the-hard-way-70-exercises-solutions
'''

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

# 5. replace all items that safisfy a condition 
array = np.arange(10)
array[array % 2 != 0] = -1
array

# 6. replace all odd number in  array without changing arr
array = np.arange(10)
copy = array.copy()
copy[copy % 2 != 0] = -1
copy
array

# 7. reshape an array -- convert 1D array to 2D array with 2 rows
array = np.arange(10)
array
array.reshape(2,-1)

# 8. stack to arrays vertically
a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)
a
b
c = np.vstack((a,b)) # v is for vertical stack 
c

# 9. stack to arrays horizontally
c = np.hstack((a,b))
c

# 10. custom sequences
# [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
a = np.array([1,2,3])

np.repeat(a,3, axis=0)
np.hstack((np.repeat(a,3),a,a,a))

# 11. get common items between two arrays
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.unique(a[a==b])
a[a==b]

# 12. from array a remove items present in array b
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
a[~np.isin(a,b)]

# 13. Get the positions where elements of a and b match

# Input
print("Input")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
a
b

# Desired Output
# > (array([1, 3, 5, 7]),)
np.where(a==b)


# 14. # Q. Get all items between 5 and 10 from a.

# Input
print("Input")
a = np.array([2, 6, 1, 9, 10, 3, 27])
a

# Desired Output
# (array([6, 9, 10]),)
((a > 6) & (a  < 11))
a[(a >= 6) & (a <  11)]

# 15. # Q. Convert the function maxx that works on two scalars, to work on two arrays.

# Input

def maxx(x, y):
    """
    Get the maximum of two items
    """
    
    if x >= y:
        return x
    else:
        return y
print("Result of the maxx function")
maxx(1, 5)

print("Input")
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
a
b

# Desired Output
# pair_max(a, b)
#> array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])


# 16 
arr = np.arange(9).reshape(3,3)
arr

# swap rows
temp = arr[0,].copy()
arr[0] = arr[1].copy()
arr[1] = temp
arr

# swap columns 
arr = np.arange(9).reshape(3,3)
temp = arr[:,0].copy()
arr[:,0] = arr[:,1].copy()
arr[:,1] = temp
arr 

# 17 
# swap rows
arr = np.arange(9).reshape(3,3)
temp = arr[0,:].copy()
temp
arr[0,:], arr[1,:] = arr[1,:], temp
arr

# 18. reverse rows of 2d array
array = np.arange(9).reshape(3,3)
# rows
array[::-1,:]
np.flip(array, axis = 0)


# 29. reverse columns of a 2d array
array[:,::-1]
np.flip(array, axis = 2)


# 20. create a 2d array of random floats between  5 and 10 shape 5X3

np.random.random_integers(5,10,15) 

random_floats = np.random.uniform(5,11,15).reshape(5,3)

# 21. how to print only 3 decimal places in a python numpy array 
a = np.array([1.23455,121.111111], dtype=np.float)
a.round(decimals=3)
b = np.random.uniform(5, 10, 15).reshape(5,3)
b = b.round(3)

# set print options instead of rounding 
np.set_printoptions(precision=3)
np.random.uniform(0,10,3)

# default print options 
np.set_printoptions(edgeitems=3,infstr='inf', linewidth=75, nanstr='nan', precision=8, suppress=False, threshold=1000, formatter=None)


# 22. how to supress scientific notation

random_array = np.random.random([3,3])/1e3
random_array
np.set_printoptions(suppress=True)
random_array


# 23. how to limit the number of options printed
array = np.arange(15)
array
np.set_printoptions(threshold=10)
array


# 24. print full array without truncating 
a = np.arange(20)
np.set_printoptions(threshold=6)

a
np.set_printoptions(threshold=len(a))
a



