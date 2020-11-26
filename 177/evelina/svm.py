import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from matplotlib import pyplot as plt

path = "/Users/austinwilson/Downloads/weather.csv"

weather = pd.read_csv(path)
weather.dropna()


################################# trash 4 lyfe 
weather.head()

columns = weather.columns
columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine','WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm','WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm','Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am','Temp3pm', 'RainToday', 'RISK_MM', 'RainTomorrow']



################################ NOT TRASH?
'''WindGustDir'''
wind_gust_direction = pd.get_dummies(weather['WindGustDir'], prefix="wind_gust_direction")

# checking 
wind_gust_direction.shape
wind_gust_direction.columns 
# now drop the other shit and join back nigguh 
weather.shape
weather.drop(['WindGustDir'], axis=1, inplace=True)
weather.shape
weather = weather.join(wind_gust_direction)
weather.columns



'''WindDir9am'''
wind_dir_9am = pd.get_dummies(weather['WindDir9am'])

# checking
wind_dir_9am.shape
wind_dir_9am.columns

'''WindDir3pm'''

'''RainToday'''

weather.columns


columns = ['Rainfall','Sunshine']

X = weather[columns]
y = weather['RainTomorrow']

plt.plot(X,y)



X.shape
y.shape

# MY NAME IS EVELINA AND I'M TRASH 

# TRAIN TEST SPLIT 

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 42)

# these should have some shit in common
X_train.shape
y_train.shape

# same size
X_test.shape
y_test.shape