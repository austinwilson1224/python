import pandas as pd 
import sklearn.feature_extraction.text as sk_text
from sklearn.model_selection import train_test_split


# do we need this?
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score



dogs = pd.read_csv('dogs.csv')
dogs.shape 

dogs.Phrase.iloc[0] # 'Why do dogs eat grass'



# tf-idf vectorizer 
corpus = dogs.Phrase
vectorizer = sk_text.TfidfVectorizer(max_features= ) # no stop words buddy 