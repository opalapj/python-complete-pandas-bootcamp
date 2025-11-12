import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

t = titanic.iloc[:50]
t.set_index("pclass")
t.set_index(["pclass", "sex"])
t.set_index("pclass", append=True)

t.set_index(["pclass", "sex"], inplace=True)
titanic.head(50)
t.head(50)
t.sort_index()
t.sort_index(ascending=[True, False])
t.sort_index(level=["pclass", "sex"], ascending=[True, False])
t.sort_index(level=[0, 1], ascending=[True, False])
t.sort_index(level=[1, 0], ascending=[True, False])
t.sort_index(level=[1, 0], ascending=[True, False], inplace=True)

t.swaplevel()
t.reset_index()

t.loc[1]
t.loc["male"]  # Illegal for second level
t.swaplevel().loc["male"]
t.loc[:2]
t.loc[(1, "male")]
t.loc[(1, "male"), "age"]
t.loc[([1, 2], "male"), "age"]
t.loc[([1, 2], "male"), ["age", "fare"]]
t.loc[([1, 2], "male")]  # Illegal without ':' for multiple indexing.
t.loc[([1, 2], "male"), :]
t.loc[(slice(None), "female"), :]  # Instead of swapping levels.
