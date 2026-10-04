import pandas as pd
import numpy as np
# from numpy import *
d ={
    "name":["bhawwani","bhuvan", np.nan,"dhruv", "dipanshu"],
    "age":[20,20,21,20,20],
    "height":[5.11,5.8,5.9,5.8,5.9],
    "weight":[65, 67,62,np.nan,70],
    "grade":["A","A", "A","A","A"],
}
dect = pd.DataFrame(d)  #dect holds the dataframe(created a dataframe)

#===function that are out of the syllabus  but are useful in pandas library====

a = dect.shape           #to get the number of rows and columns in the table
#b = dect.info()          to get all the info of the table
#c = dect.describe()      to get the mean, median , mode, min/max percentage of the values
#d = dect.isnull().sum()  to calclate or sum the total  umber of empty spaces
#e = dect.columns         to get the list of all the columns in the table
#f = dect.head(10)        to print the number of rows and columns

#====functions to finding missing data====
# print(dect.isna())           #same as isnull function
# print(dect.isna().sum())     # to find the missing value in each columns
# print(dect.isna().any())     #to get a statment if the column contain a missing value

#=== Main syllabus function of pandas===

dn = dect.notnull()   #dp finds the space that is empty (flase == null)      ===notnull
# print(dn)
di = dect.isnull()    #dj finds the space that is not empty (true == null)   ===isnull
# print(di)
df = dect.fillna(0)     # change the missing value with any value              ===fillna
# print(df)
dd = dect.dropna()      #delete the null or missing values rows from the DS    ===dropna
print(dd)
ddd= dect.duplicated()  # if there is any duplicated value (yes == true)       ===duplicated
# print(ddd)
ddrd= dect.drop_duplicates() # if there is any duplicated value (row ==delete) ===drop_duplicated
# print(ddrd)
dect["age"] = dect["age"].fillna(dect["age"]. mean())   #mean                 #===fillna
dect["age"] = dect["age"].fillna(dect["age"]. median()) #median               #===fillna
dect["age"] = dect["age"].fillna(dect["age"]. mode())   #mode                 #===fillna
# print(dect["name"])
# print(a)