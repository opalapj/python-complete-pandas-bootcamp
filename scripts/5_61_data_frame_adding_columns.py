# https://pandas.pydata.org/docs/user_guide/dsintro.html#column-selection-addition-deletion

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.head()
titanic.info()

# 1st way.
titanic["zeros"] = 0
titanic["zeros"]
titanic.head()
titanic["zeros"] = "zero"

titanic.ones = 1  # Direct selecting does not work (value is written to attribute).
titanic.ones
titanic.head()

# 2nd way.
titanic.insert(loc=len(titanic.columns), column="ones", value=1)
titanic["ones"]

# 3rd way - based on other existing column.
1912 - titanic.age
titanic.insert(loc=4, column="birthyear", value=1912 - titanic.age)
titanic.insert(loc=7, column="relatives", value=titanic.sibsp + titanic.parch)
