import numpy as np 


# arrays challenge 1
def arrays(arr):
    result = np.array(arr, float)[::-1]
    return result




arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# reshape 

input2 = input().strip().split(' ')

my_array = np.array(input2,int).reshape(3,3)
print(my_array)


# transpose 

dimension = np.array(input().strip().split(' '),int)
rows = int(dimension[0])
cols = int(dimension[1])
rows
cols

l = []
l

for i in range(rows):
    user_input = input().strip().split()
    print(user_input)
    l.append(user_input)


arr = np.array(l,int).reshape(rows,cols)
arr

arr.transpose()
arr.flatten()

# concatenate
dimension = input().strip.split(' ')
rows = int(dimension[0]) + int(dimension[1])
cols = int(dimension[2])
l = []
for i in range(rows):
    user_input = input().strip().split(' ')
    l.append(user_input)

arr = np.array(l,int).reshape(rows,cols)