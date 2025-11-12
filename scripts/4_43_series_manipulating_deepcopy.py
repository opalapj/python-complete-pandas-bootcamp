# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

import pandas as pd


sales = pd.Series(
    [10, 25, 6, 36, 2, 0, None, 5],
    index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"],
)


sales["Sun"] = 0
sales.iloc[3] = 30
r1 = (sales / 1.1).round(2)
r2 = sales.div(1.1).round(2)
r1.equals(r2)

titanic = pd.read_csv("data/titanic.csv")
age1 = titanic.loc[:, "age"]
age2 = titanic.loc[:, "age"]
age2 = titanic.loc[:, "age"].copy(deep=False)
age2 = titanic.loc[:, "age"].copy(deep=True)  # Works.

age1.iloc[1] = 30
age2.iloc[1] = 30

age1.head()
age2.head()
titanic.head()
