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