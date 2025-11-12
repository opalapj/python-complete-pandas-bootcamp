import pandas as pd


titanic = pd.read_csv(
    "data/titanic.csv", usecols=["survived", "pclass", "sex", "age", "fare"]
)

titanic.groupby("sex").mean()
titanic.groupby("sex").sum()
titanic.groupby("sex").agg(["mean", "sum", "min", "max"])
titanic.groupby("sex").agg(
    {
        "survived": ["sum", "mean"],
        "pclass": "mean",
        "age": ["mean", "median"],
        "fare": "max",
    }
)
titanic.groupby("sex").agg(
    survived_total=("survived", "sum"),
    survival_rate=("survived", "mean"),
    mean_age=("age", "mean"),
)
