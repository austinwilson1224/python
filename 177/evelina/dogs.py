import pandas as pd 
import numpy as np
import sklearn.feature_extraction.text as sk_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report


# do we need this?
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score



dogs = pd.read_csv('dogs.csv')

le = LabelEncoder()
y = le.fit_transform(dogs.QorS)

stop_words = ["the","of","to","a","in",""]

# tf-idf vectorizer 
corpus = dogs.Phrase
vectorizer = sk_text.TfidfVectorizer(max_features= 100, min_df = 5, stop_words=stop_words)
# vectorizer = sk_text.TfidfVectorizer()
matrix = vectorizer.fit_transform(corpus)
tfidf_array = matrix.toarray()

# check out the data
# tfidf_array.shape
# tfidf_array[0]




# train test split 


## first split the data into questions and statements
x_q = tfidf_array[:20]
y_q = y[:20]
x_s = tfidf_array[20:]
y_s = y[20:]

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


x_train = np.vstack([x_q_train, x_s_train])
x_test = np.vstack([x_q_test, x_s_test])


y_train = np.hstack([y_q_train, y_s_train])
y_test = np.hstack([y_q_test, y_s_test])







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

x = confusion_matrix(y_test, pred)
print(x)

f1 = f1_score(y_test,pred)
f1


report = classification_report(y_test, pred)
print(report)