import pandas as pd 
import numpy as np 

path = '/Users/austinwilson/coding/scipy-2019-pandas/data/'

df = pd.read_csv(path+'gapminder.tsv', sep="\t")

df.head()

df

type(df)

df.shape
len(df)
df.info()
df.tail()

df.columns
df.index

df.values
df.values[1]
df.values[[0]]
df.dtypes

country = df["country"] # returns a list
country = df[["country"]] # returns a dataframe
country
type(country)

df["country"].unique()

# df.drop(["continent", "country"], axis=1, inplace=True)


# subset rows
# loc is a string match to the index so df.loc[0] is matching 0 to the value of the index 
df.loc[0]
df.loc[[0,1]] # more than one rows 


# iloc will give you the acual position in the dataframe... this is the actual index 
df.iloc[0]
df.iloc[[0,-1]]

# subsets
subset = df.loc[:,['year','pop']]
subset.shape
subset.head()
type(subset)

subset2 = df.iloc[:,[2,4]]
subset2

# boolean conditions
df.columns
df.country.unique()
us = df[df.country == 'United States']
us = df.loc[df['country'] == 'United States']
us = df.loc[df['country'] == 'United States',:] # same thing as previous 
us

# if you're subsetting rows and columns use loc
# if you don't use loc then it will only subset by columns 



a = True
b = False

a & b
a | b

# multiple selectors use & in pandas 
us_1982 = df.loc[(df["country"] == "United States") & (df["year"] == 1982)]
us_1982

x1 = df.groupby(['year']).mean()
x1['lifeExp']

df.groupby(['year'])['lifeExp'].agg(np.mean)
df.groupby(['year'])['lifeExp'].agg(np.std)

df.groupby(['year','continent'])[['lifeExp','gdpPercap']].agg(np.mean)
df.groupby(['continent','year'])[['lifeExp','gdpPercap']].agg(np.mean)


df.groupby(['year','continent'])[['lifeExp','gdpPercap']].agg(np.mean).reset_index()
df.groupby(['continent','year'])[['lifeExp','gdpPercap']].agg(np.mean).reset_index()

## tips exercise
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()


# filter rows by smoker == 'No' and total_bill >= 10
filter1 = tips[(tips['smoker'] == 'No') & (tips['total_bill'] >= 10)]

test = tips[(tips.smoker == 'No') & (tips.total_bill >= 20)]
test

# average total_bill for each value of smoker, day and time 
tips.groupby(['smoker']).agg(np.mean)
tips.groupby(['day']).mean()
tips.groupby(['time']).mean()
tips.groupby(['smoker', 'day', 'time'])['total_bill'].mean()