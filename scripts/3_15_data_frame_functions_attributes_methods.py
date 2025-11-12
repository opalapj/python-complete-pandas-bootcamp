# https://pandas.pydata.org/docs/user_guide/basics.html#attributes-and-underlying-data

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

# Python built-in functions on DataFrame.
type(titanic)
len(titanic)
round(titanic, 0)

# Data frame attributes.
titanic.shape
titanic.size
titanic.index
col_arr = titanic.columns.array
c = list(col_arr)
col_val = titanic.columns.values

# DataFrame methods.
titanic.head(n=2)
titanic.info()
titanic.min()
titanic.min(numeric_only=True)

# Methods chaining.
tmp = titanic.mean(numeric_only=True)
tmp = tmp.sort_values()
tmp = tmp.head(n=2)
titanic.mean(numeric_only=True).sort_values().head(n=2)
