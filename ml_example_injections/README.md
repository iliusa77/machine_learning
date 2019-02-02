Purpose: learn the model to determine the presence of SQL injections in the text string

0. need to generate data and insert in trainingSet.csv

1. module load_data.py get data from dataset trainingSet.csv (3 types data: clear emails - label 0, clear injections - label 1, and mix email + injection - label 2)

2. in main.py the cross_validation.train_test_split() function, which shuffles the records and returns four data sets to us - two training and two test data for features and labels;
joblib will save the model for future use.