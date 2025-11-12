# https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics

import pandas as pd


summer = pd.read_csv("data/summer.csv")

athlete = summer.loc[:, "Athlete"]
type(athlete)
athlete.dtype
athlete.info()
athlete.describe()
d = athlete.describe()
d[2]
d["top"]
d.iloc[2]
d.loc["top"]
athlete.min()
athlete.unique()
len(athlete.unique())
athlete.nunique()
athlete.value_counts()
