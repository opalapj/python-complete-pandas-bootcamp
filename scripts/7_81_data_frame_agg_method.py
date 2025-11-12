import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.agg("mean")
titanic.agg(["mean", "std"])
titanic.agg({"survived": "mean", "age": ["min", "max"]})
