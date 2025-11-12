# https://pandas.pydata.org/docs/user_guide/advanced.html

import pandas as pd


summer = pd.read_csv("data/summer.csv")

summer.index
type(summer.index)
summer.columns
type(summer.columns)
summer.axes

summer = pd.read_csv("data/summer.csv", index_col="Athlete")

summer.index
type(summer.index)
summer.columns
type(summer.columns)
summer.axes

summer.columns[:3]
summer.index[0]
summer.index[-1]
summer.index[100:102]
summer.columns.to_list()
summer.index.is_unique
summer.index.get_loc("DRIVAS, Dimitrios")  # Result for single occured value (integer).
summer.index.get_loc(
    "FLATOW, Gustav Felix"
)  # Result for multiple occured value (boolean mask).
