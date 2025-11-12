import pandas as pd


# 1st way to create DatetimeIndex.
# Especially for indexes with inconstant intervals.
pd.to_datetime(["2015-02-20", "2015-03-20", "2015-05-20"])
pd.to_datetime(["2015-02-20", "20MARCH2015", "May 20 2015"])  # Illegal.
pd.to_datetime(["2015-02-20", "20MARCH2015", "May 20 2015"], format="mixed")

# 2nd way.
pd.DatetimeIndex(["2015-02-20", "2015-03-20", "2015-05-20"])
pd.DatetimeIndex(["2015-02-20", "20MARCH2015", "May 20 2015"])  # Legal.

# 3rd way.
pd.date_range(start="2023-01-01", end="2023-12-31")
pd.date_range(start="2023-01-01", end="2023-12-31", freq="M")

pd.date_range(start="2023-01-01", end="2023-12-31", freq="M", periods=5)  # Illegal.
# Feed with date boundaries and periods or frequency...
pd.date_range(start="2023-01-01", end="2023-12-31", freq="M")
pd.date_range(
    start="2023-01-01", end="2023-12-31", periods=12
)  # Not recommend, run to see.
# ...or feed with one of boundaries and periods and frequency.
pd.date_range(start="2023-01-01", freq="M", periods=12)
pd.date_range(end="2023-12-31", freq="M", periods=12)

# Weekly frequency without and with day indication.
pd.date_range(start="2023-01-01", freq="W", periods=12)
pd.date_range(start="2023-01-01", freq="W-Mon", periods=12)

# Monthly frequency with various start dates.
pd.date_range(start="2023-01-10", freq="M", periods=12)
pd.date_range(start="2023-01-10", freq="MS", periods=12)
pd.date_range(start="2023-01-10", freq=pd.DateOffset(months=1), periods=12)

# Quarterly frequency with various start dates.
pd.date_range(start="2023-01-10", freq="Q", periods=4)
pd.date_range(start="2023-01-10", freq="QS", periods=4)
pd.date_range(start="2023-01-10", freq="QS-Feb", periods=4)
pd.date_range(start="2023-01-10", freq=pd.DateOffset(months=3), periods=4)

# Aliases can be multiplied
pd.date_range(start="2023-01-10", freq="2H", periods=4)
pd.date_range(start="2023-01-10", freq="3D", periods=4)
pd.date_range(start="2023-01-10", freq="3D2H", periods=4)
