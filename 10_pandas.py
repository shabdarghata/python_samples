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