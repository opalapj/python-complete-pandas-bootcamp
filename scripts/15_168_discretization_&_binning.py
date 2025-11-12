import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

bins_limits = [0, 10, 18, 30, 55, 100]
bins_names = ["child", "teenager", "young_adult", "adult", "elderly"]

pd.cut(titanic["age"], bins_limits, right=False)
pd.cut(titanic["age"], bins_limits, right=False, labels=bins_names)
cats = pd.cut(titanic["age"], bins_limits, right=False, labels=bins_names)

pd.cut(titanic["age"], 5).unique().sort_values()
titanic["age"].min()
titanic["age"].max()

cats.unique()
cats.nunique()
cats.value_counts()
titanic["age_cat"] = cats


titanic["fare_cat"] = pd.cut(titanic["fare"], 5, precision=0)
titanic["fare_cat"].value_counts()

titanic["fare_cat"] = pd.qcut(titanic["fare"], 5, precision=0)
titanic["fare_cat"] = pd.qcut(titanic["fare"], [0, 0.1, 0.5, 0.95, 1], precision=0)
titanic["fare_cat"].value_counts()

titanic.groupby(["fare_cat", "age_cat"])["survived"].mean()
titanic.groupby(["fare_cat", "age_cat"])["survived"].mean().unstack()
