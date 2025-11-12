import pandas as pd


titanic = pd.read_csv(
    "data/titanic.csv", usecols=["survived", "pclass", "sex", "age", "fare"]
)

# Simple function.
titanic.groupby("sex").mean()
titanic.groupby("sex").apply(lambda g: g.mean())

# More complex function.
titanic.groupby("sex").apply(lambda g: g.loc[g["survived"] == 1].nlargest(5, "age"))
