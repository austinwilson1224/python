import pandas as pd 
import numpy as np
import sklearn.feature_extraction.text as sk_text
from sklearn.model_selection import train_test_split


# do we need this?
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score



dogs = pd.read_csv('dogs.csv')

le = LabelEncoder()
y = le.fit_transform(dogs.QorS)
y
y.shape


dogs.shape 

dogs

dogs.Phrase.iloc[0] # 'Why do dogs eat grass'


stop_words = ['']  # should we have stop words? 



# tf-idf vectorizer 
corpus = dogs.Phrase
vectorizer = sk_text.TfidfVectorizer(max_features= 500, min_df = 5)
# vectorizer = sk_text.TfidfVectorizer()
matrix = vectorizer.fit_transform(corpus)
tfidf_array = matrix.toarray()

# check out the data
tfidf_array.shape
tfidf_array[0]




# train test split 


## first split the data into questions and statements
x_q = tfidf_array[:20]
y_q = y[:20]
#y_q = dogs.QorS[:20]
x_s = tfidf_array[20:]
y_s = y[20:]
# y_s = dogs.QorS[20:]

## double check the size is correct 
len(x_q) + len(x_s) == tfidf_array.shape[0]
len(y_q) + len(y_s) == dogs.shape[0]


## now take subsets of questions and answers for train test split (.2 split for test )

### train for questions and statements
x_q_train = x_q[:16]
y_q_train = y_q[:16]

x_s_train = x_s[:16]
y_s_train = y_s[:16]


### test for questions and statements
x_q_test = x_q[16:]
y_q_test = y_q[16:]

x_s_test = x_s[16:]
y_s_test = y_s[16:]


# type(x_s) # numpy array
# type(y_s) # pandas series 

# x_q_train.shape
# x_s_train.shape
# type(x_q_train)
# type(x_s_train)

x_train = np.vstack([x_q_train, x_s_train])
x_test = np.vstack([x_q_test, x_s_test])


y_train = np.hstack([y_q_train, y_s_train])
y_test = np.hstack([y_q_test, y_s_test])


# y_train.shape
# y_test.shape

# y_train.shape[0] == x_train.shape[0]
# y_test.shape[0] == x_test.shape[0]




# double check the size 
x_train.shape
y_train.shape

x_test.shape
y_test.shape


######## classification 


nb = GaussianNB()
nb.fit(X = x_train, y = y_train)
pred = nb.predict(X = x_test)
score = accuracy_score(y_true = y_test, y_pred = pred)
score
