from sklearn import ensemble
from sklearn import feature_extraction
from sklearn import linear_model
from sklearn import pipeline
from sklearn import cross_validation
from sklearn import metrics
from sklearn.externals import joblib

import load_data
import pickle

# Load the dataset from the csv file. Handled by load_data.py. Each email is split in characters and each one has label assigned
X, y, label_names = load_data.get_dataset()

# Split the dataset on training and testing sets
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2,random_state=0)

#Setting up vectorizer that will convert dataset into vectors using n-gram
vectorizer = feature_extraction.text.TfidfVectorizer(ngram_range=(1, 4), analyzer='char')

#Setting up pipeline to flow data though vectorizer to the liner model implementation
pipe = pipeline.Pipeline([('vectorizer', vectorizer), ('clf', linear_model.LogisticRegression())])

#Pass training set of features and labels though pipe.
pipe.fit(X_train, y_train)

#Test model accuracy by running feature test set
y_predicted = pipe.predict(X_test)

print(metrics.classification_report(y_test, y_predicted,target_names=label_names))

#Save model into pickle. Built in serializing tool
joblib.dump(pipe, 'injection_model.pkl')