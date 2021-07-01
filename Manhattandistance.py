def distancesum (arr, n):
     
    # sorting the array.
    arr.sort()
     
    # for each point, finding
    # the distance.
    res = 0
    sum = 0
    for i in range(n):
        res += (arr[i] * i - sum)
        sum += arr[i]
     
    return res
     
def totaldistancesum( x , y , n ):
    return distancesum(x, n) + distancesum(y, n)
     
# Driven Code
x = [ -1, 1, 3, 2 ]
y = [ 5, 6, 5, 3 ]
n = len(x)
print(totaldistancesum(x, y, n) )

#knn
import numpy as np
import pandas as pd
  
# import the KNNimputer class
from sklearn.impute import KNNImputer
  
  
# create dataset for marks of a student
dict = {'Maths':[80, 90, np.nan, 95], 
        'Chemistry': [60, 65, 56, np.nan], 
        'Physics':[np.nan, 57, 80, 78],
       'Biology' : [78,83,67,np.nan]}
  
# creating a data frame from the list 
Before_imputation = pd.DataFrame(dict)
#print dataset before imputaion
print("Data Before performing imputation\n",Before_imputation)
  
# create an object for KNNImputer
imputer = KNNImputer(n_neighbors=2)
After_imputation = imputer.fit_transform(Before_imputation)
# print dataset after performing the operation
print("\n\nAfter performing imputation\n",After_imputation)