# https://pandas.pydata.org/docs/user_guide/indexing.html

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")
summer = pd.read_csv("data/summer.csv", index_col="Athlete")

age = titanic.loc[:, "age"]
age.index
age[0]
age[2]
age[-1]  # Series does not know how to select across RangeIndex with negative index.
age.iloc[-1]
age.iloc[:3]  # Right boundary excluded (iloc).
age.loc[:3]  # Right boundary included (loc).
age.iloc[[3, 4]]

event = summer.loc[:, "Event"]
event.index
event[0]
event[2]
event[-1]  # But Series does know how to select across Index with negative index.
event.iloc[:3]
event["ALEKSANYAN, Artur"]
event[:"ALEKSANYAN, Artur"]
event["PHELPS, Michael"]
event.loc["PHELPS, Michael"]
event["PHELPS, Michael"].equals(event.loc["PHELPS, Michael"])
event.loc[["PHELPS, Michael", "LEWIS, Carl"]]
