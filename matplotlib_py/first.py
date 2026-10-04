from numpy import *
from pandas import *
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    "age": [18,19,19,19,18,18,20,21,22,20,19,20,19,20,19,19,20,19,20,21,100],
    "salary":[74000, 85000, 88000, 97000, 100000, 100000, 15000, 80000, 90000, 100000, 110000, 120000, 90000, 120000, 150000, 120000, 112000, 12000, 110000, 100000,100000] 
}
# #=====histogram=====# to create a histogram // 

# # xlabel = "age"              #to give a name to x axis
# # ylabel = "frequnecy"        #to give a name to y axis
df = DataFrame(data)

# f = figure(figsize= (7,4))     # to give the size in lenght and height
# h1 = hist(df["age"], bins= 6)  #to give the dict to the hist (bins==intervels)
# show()                         #to show or print the  histogram
# h2 = hist(df["salary"], bins= 4)#to give the dict to the hist (bins==intervels)
# show()

#=====Box plot===== #to create a box plot // to find the median , q1- q4 , outliar

# f = figure(figsize= (7,4))
# h1 = boxplot(df["age"]) 
# show()
# h1 = boxplot(df["salary"]) 
# show()
plt.pie(df)
