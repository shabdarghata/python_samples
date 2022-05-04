import pandas as pd
#Read excel file
df = pd.read_excel("excel/SampleData.xlsx",sheet_name="SalesOrders")
print(df)

#Locate a specific row
print(df.loc[[0,1,3]])