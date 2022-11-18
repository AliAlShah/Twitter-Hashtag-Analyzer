import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
import pickle

#Loading data form csv file and setting the max number of rows to 1000000
df = pd.read_csv("Twitter_Data.csv", nrows=1000000)
#Data has 3 catagorical values 0, 1, -1, while SVM only works with two, so deleting all rows with value of 0
df.drop(df[df['category'] == 0].index, inplace=True)

#Balancing out the dataset so the number of rows with 1 equals the number of rows with -1
g = df.groupby('category')
g = pd.DataFrame(g.apply(lambda x: x.sample(g.size().min()).reset_index(drop=True)))
df = g

#Converting text data into numeric form using TfidfVectorizer object
X = df['clean_text'].values.astype('U')
tfidf = TfidfVectorizer(max_features=100000, ngram_range=(1,2))
X = tfidf.fit_transform(X)
Y = df['category']

#Splitting data into test and train
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

#Creating calssification model
clf = LinearSVC()
clf.fit(X_train, Y_train)

#Evaluating model through sklearns classification report funciton
y_pred = clf.predict(X_test)
print(classification_report(Y_test, y_pred))

#storring model using the pickle library
pickle.dump(clf, open('model', 'wb'))