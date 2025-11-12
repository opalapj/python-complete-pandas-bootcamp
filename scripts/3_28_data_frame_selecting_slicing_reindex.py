# https://pandas.pydata.org/docs/user_guide/indexing.html#reindexing

import pandas as pd


summer = pd.read_csv("data/summer.csv")

summer.loc[[0, 5, 30000], ["Athlete", "Medal"]]
summer.loc[[0, 5, 30000, 40000], ["Athlete", "Medal"]]
summer.reindex(index=[0, 5, 30000, 40000], columns=["Athlete", "Medal"])
# In reindex method declare new index by parameter labels (positional or
# keyword) or parameter index (keyword only).
a = summer.reindex(labels=[0, 5, 30000, 40000], columns=["Athlete", "Medal", "Age"])
b = summer.reindex(index=[0, 5, 30000, 40000], columns=["Athlete", "Medal", "Age"])
a.equals(b)

summer = pd.read_csv("data/summer.csv", index_col="Athlete")

# Error because duplicates in indices.
summer.reindex(index=["LEWIS, Carl"], columns=["Medal", "Age"])
