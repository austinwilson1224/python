import pandas as pd 
import numpy as np 
path = '/Users/austinwilson/coding/scipy-2019-pandas/data/'


def my_function(x,y):
    pass

def my_sq(x):
    return x ** 2

my_sq(2)
my_sq(4)

# assert is the basis for unit testing in python 
assert my_sq(4) == 16

def avg_2(x,y):
    return (x+y)/2

assert avg_2(10,2) == 6

df = pd.DataFrame({
    'a': [10,20,30],
    'b': [20,30,40]
})

df['a'] ** 2
df['a'].apply(my_sq) # passing the function my_sq into the apply method 

def my_exp(x, e):
    return x ** e

my_exp(2, 10)

assert my_exp(2,2) == 4

df['a'].apply(my_exp, e=4)

def print_me(x):
    print(x)



df.apply(print_me)


def avg_3(x,y,z):
    return (x+y+z)/3

df.apply(avg_3, )

def avg_3_apply(col):
    x = col[0]
    y = col[1]
    z = col[2]
    # return np.mean(col)
    return (x+y+z) / 3

df.apply(avg_3_apply)

df['a'].mean()

df['a'] + df['b']

def avg_2_mod(x,y):
    if x == 20:
        return np.NaN
    else:
        return (x + y) / 2

avg_2_mod(df['a'],df['b'])


# how to vectorize a function in python .... use numpy vectorize
avg_2_mod_vec = np.vectorize(avg_2_mod)

avg_2_mod_vec(df['a'],df['b'])


# in order to vectorize a function use @np.vertorize
@np.vectorize
def avg_2_mod1(x,y):
    if x == 20:
        return np.NaN
    else:
        return (x + y) / 2

avg_2_mod(df['a'],df['b'])


import numba 

@numba.vectorize
def avg_2_mod_numba(x,y):
    if x == 20:
        return np.NaN
    else:
        return (x + y) / 2

avg_2_mod_numba(df['a'].values,df['b'].values)

# timeit
avg_2(df['a'], df['b'])






tbl3 = pd.read_csv(path+'table3.csv')
tbl3


tbl3.dtypes

def extract_population(rate, delim='/', position=1):
    pop = rate.split(delim)[position]
    return int(pop)

assert extract_population('123/456') == 456

pops = tbl3['rate'].apply(extract_population)

tbl3['pop'] = pops
tbl3['pop2'] = tbl3['rate'].apply(extract_population)

# stopped at 2:13:09
