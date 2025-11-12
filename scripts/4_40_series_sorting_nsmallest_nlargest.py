# https://pandas.pydata.org/docs/user_guide/basics.html#

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

# Sorting by index & value.
dic = {1: 10, 3: 25, 2: 6, 4: 36, 5: 2, 6: 0, 7: None}
sales = pd.Series(dic)
sales.sort_index()
sales.sort_index(ascending=True, inplace=True)
sales.sort_values(inplace=False)
sales.sort_values(ascending=False, na_position="first", inplace=True)
dic = {"Mon": 10, "Tue": 25, "Wed": 6, "Thu": 36, "Fri": 2}
sales = pd.Series(dic)
sales.sort_index(ascending=False)

# nlargest & nsmallest methods.
age = titanic.loc[:, "age"]
age.value_counts()
age.nlargest()
age.nsmallest(10)
