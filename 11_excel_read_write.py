import pandas as pd
#Read excel file
df = pd.read_excel("excel/SampleData.xlsx",sheet_name="SalesOrders")
print(df)

#Locate a specific row
print(df.loc[[0,1,2]])

#Write excel file
with pd.ExcelWriter("excel/SampleData.xlsx",mode="a",if_sheet_exists="replace") as writer:
    df.loc[[0,1,2]].to_excel(writer,sheet_name="SalesOrdersFirstThree")

