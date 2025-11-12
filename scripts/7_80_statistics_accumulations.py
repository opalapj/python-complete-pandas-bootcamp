import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.describe()
titanic.count()
titanic.count(axis=1)
titanic.mean()
titanic.mean(numeric_only=True)
titanic.sum()
titanic.sum(numeric_only=True)
titanic["fare"].cumsum()
titanic["fare"].sort_values().cumsum()
titanic.corr(numeric_only=True)
titanic["survived"].corr(titanic["parch"])  # This method is for Series!
