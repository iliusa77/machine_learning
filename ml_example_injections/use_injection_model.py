import numpy as np
from sklearn.externals import joblib

#Load classifier from the pickle file
clf = joblib.load('injection_model.pkl')

#Set of test data
input_data = ["aselectndwdpyrey@gmail.com",
           "andrew@microsoft.com'",
           "a.johns@deloite.com",
           "'",
           "select@mail.jp",
           "update11@nebuzar.com",
           "' OR 1=1",
           "asdasd@sick.com'",
           "andrew@mail' OR 1=1",
           "an'drew@bark.1ov111.com",
           "andrew@gmail.com'"]

predicted_attacks = clf.predict(input_data).astype(np.int)
label_names = ["Safe Data", "SQL Injection"]

for email, item in zip(input_data, predicted_attacks):
 print(u'\n{} ----> {}'.format(label_names[item], email))