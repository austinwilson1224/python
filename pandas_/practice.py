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

df.drop(["continent", "country"], axis=1, inplace=True)
df