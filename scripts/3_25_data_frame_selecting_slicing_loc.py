# https://pandas.pydata.org/docs/user_guide/indexing.html

import pandas as pd


summer = pd.read_csv("data/summer.csv", index_col="Athlete")

# Selecting rows with loc method.
summer.loc["DRIVAS, Dimitrios"]
summer.loc["PHELPS, Michael"]

# Slicing rows with loc method.
summer.loc["PHELPS, Michael", "Medal"]
summer.loc["PHELPS, Michael", ["Medal", "Event"]]
summer.loc[["PHELPS, Michael", "LEWIS, Carl"], ["Medal", "Event"]]
summer.loc[:, ["Medal", "Event"]]
summer.loc[:, ["Medal", "Event"]].iloc[0]
summer.loc[:"MALOKINIS, Ioannis"]  # Right boundary included.
summer.loc[:"PHELPS, Michael"]  # Error during multiple occured index label indicating.
summer.loc["DRIVAS, Dimitrios":"CHASAPIS, Spiridon"]
summer.loc["DRIVAS, Dimitrios":"CHASAPIS, Spiridon", ["Year", "Medal"]]
