import matplotlib.pyplot as pl
import pandas as pd
df = pd.read_csv("csv/data.csv")

print(df)
pl.plot(df["Pulse"],"ro")
pl.show()

#Concat 2 columns in separate dataframe
pls=[df["Pulse"],df["Maxpulse"]]
dfpls=pd.concat(pls,axis=1)
print(dfpls)
dfpls.plot()
pl.show()
