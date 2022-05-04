import pandas as pd
#Create dataframe that has few rows with null cells
df = pd.read_excel("excel/SampleData1.xlsx","SalesOrders")
print(df)

#drop rows with emply cells. i.e. row 1 and row 5 will be dropped.
df1 = df.dropna()
print(df1)

#drop in place instead of creating new dataframe
#df.dropna(inplace = True)
#sprint(df)

#Replace Empty Values
df1 = df.fillna(0)
print(df1)

#Replace only specific columns
df["Units"].fillna(0,inplace=True)
print(df)

#Replace Using Mean, Median, or Mode
x = df["Unit Cost"].mean()
df["Unit Cost"].fillna(x,inplace=True)
print(df)

#Fix date format
#df["OrderDate"]=pd.to_datetime(df["OrderDate"],format="yyyyMMMdd")
#print(df)

#Loop through all values in Units column
for x in df.index:
    #if units are >50 then apply flat Unit Cost of 5.00
    if(df.loc[x,"Units"]>50):
        df.loc[x,"Unit Cost"]=5

print(df)

#Fix Total column by re-calculating it
df["Total"]=df["Units"]*df["Unit Cost"]
print(df)

