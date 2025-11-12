# https://pandas.pydata.org/docs/user_guide/indexing.html

import pandas as pd


summer = pd.read_csv("data/summer.csv")
pd.set_option("expand_frame_repr", False)

summer.info()
summer.describe()
summer.describe(include="all")

summer = pd.read_csv("data/summer.csv", index_col="Athlete")

# Selecting rows with iloc method.
s = summer.iloc[0]  # Series type.
df = summer.iloc[[0]]  # Data frame type (with brackets).
summer.iloc[-1]
summer.iloc[[1, 2, 3]]
summer.iloc[1:4]
summer.iloc[:5]
summer.iloc[-5:]
summer.iloc[:6:2]

summer = pd.read_csv("data/summer.csv")
summer.iloc[lambda x: x.index % 2 == 0]  # Each second row.

# Slicing with iloc method.
summer.iloc[0, 4]
summer.iloc[0, :3]
summer.iloc[0, [2, 3, 6]]
summer.iloc[[0, -1], [2, 3, 6]]
summer.iloc[:, 4]

# 4 ways for selecting column.
a = summer.Country
b = summer["Country"]
c = summer.loc[:, "Country"]
d = summer.iloc[:, 5]
a.equals(b)
b.equals(c)
c.equals(d)
