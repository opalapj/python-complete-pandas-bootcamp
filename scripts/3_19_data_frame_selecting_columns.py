# https://pandas.pydata.org/docs/user_guide/indexing.html

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

# 1st way to select single/multiple columns (by labels).
titanic["age"]
type(titanic["age"])  # Result of single selection is series.
titanic[["age", "sex"]]
type(titanic[["age", "sex"]])  # Result of multiple selection in brackets is data frame.
titanic[["age"]]
type(titanic[["age"]])  # Result of single selection in brackets is also data frame.

# 2nd way to select single columns (by direct indication).
titanic.age
type(titanic.age)
titanic.age.equals(titanic["age"])  # Equality checking.
