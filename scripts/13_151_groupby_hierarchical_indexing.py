import pandas as pd


titanic = pd.read_csv(
    "data/titanic.csv", usecols=["survived", "pclass", "sex", "age", "fare"]
)

titanic.groupby(["sex", "pclass"]).mean()
summary = titanic.groupby(["sex", "pclass"]).mean()
summary  # Multiindex, where sex is 0 level, and pclass is 1 level.
summary.index.levels[0]
summary.index.levels[1]

summary.swaplevel()  # Swap without sorting.
summary.swaplevel().sort_index()  # Looks better.
