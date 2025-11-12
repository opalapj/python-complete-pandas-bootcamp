import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

pd.get_dummies(titanic, columns=["sex"])
pd.get_dummies(titanic, columns=["sex"], dtype="int")
pd.get_dummies(titanic, columns=["sex", "pclass"], dtype="int")
pd.get_dummies(titanic, columns=["sex", "pclass"], dtype="int", drop_first=True)
