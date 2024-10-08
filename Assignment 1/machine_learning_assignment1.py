# -*- coding: utf-8 -*-
"""Machine Learning Assignment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w4FeyoSaI7R0MYGhzGypc_XLW1sJIla2
"""



"""       **AGABA LUCKY**
     **2024/HD05/21913U **
**RIGOROUS EXPLORATORY DATA ANALYSIS OF DATA CONCERNING HEALTHCARE, AND HEALTH POLICY ISSUES AFFECTING AMERICANS AGED 50 AND OLDER UTILIZING PYTHON LIBRARIES INCLUDING PANDAS, MATPLOTLIB, AND SEABORN**
"""



#import the necessary python libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the csv file
df = pd.read_csv('/content/NPHA-doctor-visits.csv')

#check for the first five rows of the dataset
df.head()

#check for the last five rows of the dataset
df.tail()

#check for the number of rows and columns in the dataset
df.shape

#check for the columns together with their datatypes
df.info()

#check for the number of unique elements in the dataset
df.nunique()

#obtain a summary of the dataset/ descriptive statistics
df.describe().T

df.describe()

#checking for missing values
df.isnull().sum()

#checking for missing values
df.isnull().sum()/df.shape[0]*100

#checking for duplicates in the dataset
df.duplicated().sum()

#dropping or eliminating the duplicated values
df.drop_duplicates()

#checking for garbage values
for i in df.select_dtypes(include='object').columns:
  print(df[i].value_counts())
  print("***"*10)

"""**Exploratory Data Analysis (EDA)**"""

#understanding the distribution of the data for each numerical column using a histogram
for i in df.select_dtypes(include='number').columns:
  sns.histplot(data=df, x=i, kde=True)
  plt.ylabel('Frequency')
  plt.title('Data distribution')
  plt.show()

#identifying outliers in the dataset
for i in df.select_dtypes(include='number').columns:
  sns.boxplot(data=df, x=i)
  plt.show()

#dealing with the outliers
#def out_liers(col):
#  q1,q3=np.percentile(col,[25,75])
#  iqr=q3-q1
 # upper_bound=q3+(1.5*iqr)
  #lower_bound=q1-(1.5*iqr)
  #return upper_bound,lower_bound

#for i in ['Phyiscal Health', 'Employment', 'Stress Keeps Patient from Sleeping', 'Medication Keeps Patient from Sleeping',
 #         'Pain Keeps Patient from Sleeping', 'Trouble Sleeping', 'Prescription Sleep Medication', 'Race']:
  #upper_bound,lower_bound=out_liers(df[i])
  #df[i]=np.where(df[i]>upper_bound,upper_bound,df[i])
  #df[i]=np.where(df[i]<lower_bound,lower_bound,df[i])

#for i in ['Phyiscal Health', 'Employment', 'Stress Keeps Patient from Sleeping', 'Medication Keeps Patient from Sleeping',
    #      'Pain Keeps Patient from Sleeping', 'Trouble Sleeping', 'Prescription Sleep Medication', 'Race']:
    #      sns.boxplot(df[i])
     #     plt.show()

df.select_dtypes(include='number').columns

#scatter plot to understand the relationship between my target variable and other variables
for i in ['Age', 'Phyiscal Health', 'Mental Health',
       'Dental Health', 'Employment', 'Stress Keeps Patient from Sleeping',
       'Medication Keeps Patient from Sleeping',
       'Pain Keeps Patient from Sleeping',
       'Bathroom Needs Keeps Patient from Sleeping',
       'Uknown Keeps Patient from Sleeping', 'Trouble Sleeping',
       'Prescription Sleep Medication', 'Race', 'Gender']:
       sns.scatterplot(data=df, x=i, y='Number of Doctors Visited')
       plt.show()

#checking for the correlation with heatmap to interpret the relation and multicollinearity
df.select_dtypes(include='number').corr()

plt.figure(figsize=(10,10))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)

for i in df.select_dtypes(include='number').columns:
  plt.figure(figsize=(10,10))
  sns.kdeplot(data=df, x=i)
  plt.show()

