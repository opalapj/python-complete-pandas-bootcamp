import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.head()

# Sorting by single and multiple columns.
titanic.sort_values(by="age")
titanic.sort_values(by="age", ascending=False, inplace=True)
titanic.sort_values(by=["sex", "age"], ascending=[True, False])
titanic.sort_values(by=["sex", "age"], ascending=[True, False], inplace=True)
titanic.sort_index(inplace=True)

# Sorting and reseting index.
srtd1 = titanic.sort_values(by=["sex", "age"], ascending=[True, False])
srtd1.reset_index(drop=True, inplace=True)
srtd1.head()

srtd2 = titanic.sort_values(
    by=["sex", "age"], ascending=[True, False], ignore_index=True
)  # Simpler way.
srtd2.head()

srtd2.equals(srtd1)
