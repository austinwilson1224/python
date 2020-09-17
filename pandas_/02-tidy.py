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