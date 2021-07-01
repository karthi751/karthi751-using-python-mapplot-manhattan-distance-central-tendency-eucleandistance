import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""from scipy.stats import skew 
import pylab as p"""

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#making a dataframe
df = pd.DataFrame(d)

#mean value
"The average value of dataset"
#print(df.mean())

#median value
"It gives middle value in the dataset"
#print(df.median())

#mode value
"It gives the most occureneces value in dataset"
moded = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46])}
dfmode = pd.DataFrame(d)
#print(dfmode.mode())

#skewness
skdata = pd.read_csv('/Users/letzconnectad3/Downloads/sample_submission.csv')
skdf = pd.DataFrame(skdata)
#print(skdf)

#mean
meansk = skdf.mean()
print(meansk)

#median
mediansk = skdf.median()
print(mediansk)

print(skdf.describe())

#sns.histplot(skdf['SalePrice'], color ="r")

plt.plot(skdf['SalePrice'])

skwne = (skdf["SalePrice"]).skew()
print(skwne)

#https://www.kaggle.com/gmailpawan/house-pricing-skew-reduction-technique/data





