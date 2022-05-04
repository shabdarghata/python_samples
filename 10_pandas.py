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

#Create a simple Pandas Series from a dictionary:
mydict = {
    "day1" : "420",
    "day2" : "500",
    "day3" : "600"
}

s=pd.Series(mydict);
print(s)

#Create a DataFrame from two Series:
s2 = {
    "calories": [1,2,3],
    "names": ["a","b","c"]
}
d2 = pd.DataFrame(s2)
print(d2)

#Locate Row
print(d2.loc[0])

#Return row 0 and 1:
print(d2.loc[[0,1]])

#Add a list of names to give each row a name:
d3 = pd.DataFrame(s2,index=["x","y","z"])
print(d3)

#Locate row using index name
print(d3.loc["z"])
print(d3.loc[["y","z"]])

#You can check your system's maximum rows with the pd.options.display.max_rows statement.
print(pd.options.display.max_rows)

#Change default value of max rows
pd.options.display.max_rows=100
print(df)
#df.head()

#Read JSON
df2=pd.read_json("json/sample1.json", typ='series')
#df2.head()
print(df2)

#Analyzing data
print(df.head(10))
print(df.info())