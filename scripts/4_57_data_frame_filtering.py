# https://pandas.pydata.org/docs/user_guide/indexing.html#

import pandas as pd


summer = pd.read_csv("data/summer.csv")
pd.set_option("expand_frame_repr", False)

summer.head()
summer.loc[:, "Year"]
mask = summer.loc[:, "Year"].between(1990, 2000)
summer.loc[mask]
summer.iloc[mask]  # Erroneous operation.
favorite_years = [1992, 1996]
mask = summer.loc[:, "Year"].isin(favorite_years)
summer.loc[mask]

pol = summer.loc[summer["Country"] == "POL"]
cnt = pol.value_counts("Athlete")

(summer["Country"] == "POL").any()
(summer["Country"] == "POL").all()
(pol["Country"] == "POL").all()
