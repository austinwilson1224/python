import numpy as np
import pandas as pd
path = '/Users/austinwilson/coding/scipy-2019-pandas/data/'


# columns containing values not variables
pew = pd.read_csv(path+'pew.csv')
pew.head()
pew.shape

pew.melt(id_vars='religion')


pew.melt(id_vars='religion', var_name="income", value_name="count")


billboard = pd.read_csv(path+'billboard.csv')
billboard.head()
billboard.melt(id_vars=['year','artist','track','time','date.entered'], var_name="rank", value_name="week")

(billboard.melt(id_vars=['year','artist','track','time','date.entered'], var_name="rank", value_name="week").groupby('artist').mean())

# doesn't work idk why
(billboard.melt(id_vars=['year','artist','track','time','date.entered'], var_name="rank", value_name="week").groupby('artist')['rank'].mean())

ebola = pd.read_csv(path+'country_timeseries.csv')
ebola.head(15)
ebola.tail(15)

ebola_long = ebola.melt(id_vars = ["Date", "Day"], 
                        var_name = 'cd_country',
                        value_name = 'count')
ebola_long.head()


# to split up  a value by an underscore
'hello_world'.split('_')[0]

# take out cases or  deaths from cd_country
#  can use .str to get access to string methods
# can use .cat to access categorical things 
ebola_split = ebola_long['cd_country'].str.split('_', expand=True)
ebola_split


ebola_long[["status", "country"]] = ebola_split
ebola_long.head()


ebola_long["test"] = 1
ebola_long.head()
# ebola_long["cd_country"] = str(ebola_long["cd_country"]).split('_')[0]
ebola_long["cd_country"].unique()



# weather data set 
weather = pd.read_csv(path+'weather.csv')

weather.head()

weather_long = weather.melt(id_vars=['id','year','month','element'], var_name=['day'],value_name='temp')
weather_long.head()
weather_long.shape

(weather_long.pivot_table(index=['id','year','month','day'],columns='element',values='temp').reset_index())

1_000_000 # same as 1000000

[1,2,3,] # can have a trailing comma in lists

tbl1 = pd.read_csv(path+"table1.csv")
tbl2 = pd.read_csv(path+"table2.csv")
tbl3 = pd.read_csv(path+"table3.csv")
tbl1
tbl2

tbl2.pivot_table(index=["country","year"],columns="type",values="count").reset_index()

tbl3
tbl3['rate'].str.split('/').str.get(1)



