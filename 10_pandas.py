#Pandas is a Python library used for working with data sets.
#It has functions for analyzing, cleaning, exploring, and manipulating data.
#The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.
import pandas as pd

cars = {
    "make": ["2007","2008","2009"],
    "model": ["Toyota","Hyundai","Honda"]
}

print (cars)

mycars = pd.DataFrame(cars)
print(mycars)
print(pd.__version__)

#What is a Series?
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.

a= [1,5,7]
aseries = pd.Series(a)
print(aseries)

#Label a series
b = [7,8,9]
bseries = pd.Series(b, index = ["x","y","z"])
print(bseries)
#Return the value of "y":
print(bseries["y"])

#Read csv file
df = pd.read_csv("csv/aes_pv.csv")
print(df)