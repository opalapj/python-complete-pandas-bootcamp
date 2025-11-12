import pandas as pd


sales = pd.Series(
    data=[15, 32, 45, 21, 55, 15, 0],
    index=["Mo", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
)

# Ranking.
sales.sort_values(ascending=False)
sales.rank()
sales.rank(ascending=False).sort_values(ascending=True)
sales.rank(ascending=False, method="min").sort_values(ascending=True)
sales.rank(ascending=False, method="min", pct=True).sort_values(ascending=True)

titanic = pd.read_csv("data/titanic.csv")

titanic["fare"].rank(ascending=False)
titanic["fare_rank"] = titanic["fare"].rank(ascending=False, method="min")
titanic.head()
titanic.sort_values(by="fare_rank")

# Nlargesting, nsmallesting and uniquing.
titanic.nlargest(n=10, columns="fare_rank")
titanic.nsmallest(n=10, columns="fare_rank")
titanic.nunique()
titanic.nunique(axis=1)

titanic.nsmallest(n=5, columns="age")
youngest_passenger = titanic.iloc[titanic["age"].idxmin()]
