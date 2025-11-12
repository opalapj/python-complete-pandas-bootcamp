import pandas as pd


temp = pd.read_csv("data/temp.csv", parse_dates=True, index_col="datetime")

temp.loc["2013-01-01 00:00:00"]
temp.iloc[0]

temp.loc["2013-01-01"]
temp.loc["2013-01"]
temp.loc["2013"]
temp.loc["2013-01-01":"2013-12-31"]
temp.loc["2013-01-01":"2013-12-31"].equals(temp.loc["2013"])
temp.loc[:"2013-12-31"]
temp.loc["2013-01-01":]

temp.loc["20february2015"]
temp.loc["20february2015 10:00"]

two_days = ["2013-12-31", "2014-12-31"]
# two_days = pd.to_datetime(two_days)  # From course, but unnecessary.
temp.loc[two_days]

two_days = ["2013-12-31 00:00", "2014-12-31 00:00"]
temp.loc[two_days]

two_days = ["2013-12-31 00:00:00", "2014-12-31 00:00:00"]
temp.loc[two_days]
