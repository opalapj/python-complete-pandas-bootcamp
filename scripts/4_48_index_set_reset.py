# https://pandas.pydata.org/docs/user_guide/advanced.html

import pandas as pd


summer = pd.read_csv("data/summer.csv", index_col="Athlete")
pd.set_option("expand_frame_repr", False)

summer.head()
summer.index
summer.reset_index()
summer.reset_index(drop=True)
summer.reset_index(inplace=True)
summer.reset_index(drop=True, inplace=True)
summer.set_index("Year")
summer.set_index("Year", drop=False)
summer.set_index("Year", drop=False, inplace=True)
summer.index[0] = 1894  # Erroneus for Index.

# Index creating.
new_index = ["Medal_No_{}".format(i) for i in range(1, summer.index.size + 1)]
summer.index = new_index  # Direct works.
summer.set_index(pd.Index(new_index), inplace=True)  # Index works.
summer.set_index(pd.Series(new_index), inplace=True)  # Series works.
summer.set_index(
    ("Medal_No_{}".format(i) for i in range(1, summer.index.size + 1)), inplace=True
)  # Generator works.
summer.set_index(
    ["Medal_No_{}".format(i) for i in range(1, summer.index.size + 1)], inplace=True
)  # List does not work.

summer.index.is_unique
summer.index.name = "Medal_No"
