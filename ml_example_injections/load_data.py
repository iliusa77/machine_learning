import csv

def get_dataset():
   X = []
   y = []
   label_names = ["safe data","Injected email"]
   with open('trainingSet.csv') as csvfile:
       readCSV = csv.reader(csvfile, delimiter='\n')
       for row in readCSV:
           splitted = row[0].split(',')
           X.append(splitted[0])
           y.append(splitted[1])

          
        
   print("\n\nData set features {0}". format(len(X)))
   print("Data set labels   {0}\n". format(len(y)))

   print(X)

   return X, y, label_names