import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data.groupby("Primary Fur Color").size().to_csv("squirrel_count.csv")

stat = data["Primary Fur Color"].value_counts()
print(stat)

