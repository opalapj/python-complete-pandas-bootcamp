import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

age = titanic.loc[:, "age"]
# Returning index and value.
age.nlargest(1)
age.nsmallest(1)
# Returning index.
age.idxmax()
age.idxmin()
# Returning value.
age.max()
age.min()

dic = {"Mon": 10, "Tue": 25, "Wed": 6, "Thu": 36, "Fri": 2, "Sat": 0, "Sun": None}
sales = pd.Series(dic)
sales.sort_values(ascending=True).index[0]
sales.idxmin()
sales.sort_values(ascending=False).index[0]
sales.idxmax()
