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

#Delete row 13
df.drop(13,inplace=True)
print(df)

#Look at duplicate rows
print(df.duplicated())

#Remove duplicate row
df.drop_duplicates(inplace=True)
print(df)

#Find co-relation between columns
print(df.corr())

#The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
#The number varies from -1 to 1.
#1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
#0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
#-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
#0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

