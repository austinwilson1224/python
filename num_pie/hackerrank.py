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


# zeros and ones

user_input = input().strip().split(' ')
array_shape = np.array(user_input, dtype=np.int)

print(np.zeros(shape=array_shape, dtype=int))
print(np.ones(shape=array_shape, dtype=int))


# identity -- some problem with test cases where the numeric values are actually strings with leading  whitespace 
user_input = np.array(input().strip().split(' '), dtype=np.int)
array = np.eye(user_input[0],user_input[1],k=0)
array = str(np.eye(user_input[0],user_input[1],k=0)).replace('1', ' 1').replace('0', ' 0')

print(array)


# min/max
import numpy
print(numpy.max(numpy.min(numpy.array([input().split() 
     for _ in range(int(input().split()[0]))],int),axis=1)))

dimension = input().split(' ') # 4 2 so we have 4 rows and 2 columns 
rows = int(dimension[0])
cols = int(dimension[1])
rows
cols


the_list = []

for i in range(rows):
    user_input = input().split(' ')
    # print(i)
    the_list.append(user_input)
    print(the_list)




the_list

array = np.array(the_list, dtype=int).reshape(rows,cols)

min = np.min(array,axis=1)
min
max = np.max(min)
max


# 1 2 
# 3 4 



# mean, var and std 


dimension = input().split(' ') # 4 2 so we have 4 rows and 2 columns 
rows = int(dimension[0])
cols = int(dimension[1])
rows
cols


# alternative for input
rows, cols = map(int,input().split(' '))


the_list = []

for i in range(rows):
    user_input = input().split(' ')
    the_list.append(user_input)



array = np.array(the_list,int)
np.set_printoptions(legacy='1.13') # to fix error
print(np.mean(array,axis = 1))
print(np.var(array,axis = 0))
print(np.std(array))


# array mathematics

rows, cols = map(int,input().split(' '))


a = []
for i in range(rows):
    a.append(input().split(' '))


b = []
for i in range(rows):
    b.append(input().split(' '))




a = np.array(a,int).reshape(rows,cols)
b = np.array(b,int).reshape(rows,cols)

print(a + b)
print(a - b)
print( a * b)
print(a // b)
print(a % b)
print(a ** b)



  