import pandas as pd


temp = pd.read_csv("data/temp.csv", parse_dates=True, index_col="datetime")

temp_d = temp.resample("D").mean()

birthd = pd.date_range(start="2014-12-24", periods=3, freq=pd.DateOffset(years=1))

temp_d.loc[birthd]

birthd = pd.date_range(start="2010-12-24", periods=10, freq=pd.DateOffset(years=1))

temp_d.loc[birthd]  # Illegal for mask not in index.
temp_d.reindex(birthd)
temp_d.reindex(birthd, method="bfill")
temp_d.reindex(birthd, method="ffill")
temp_d.reindex(birthd, method="nearest")
