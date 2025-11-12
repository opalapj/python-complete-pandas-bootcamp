import pandas as pd


# Simple import and convert datetime column to datetime dtype column.
temp0 = pd.read_csv("data/temp.csv")
temp0["datetime"] = pd.to_datetime(temp0["datetime"])
temp0.info()

# Import with datetime column as datetime dtype column.
temp1 = pd.read_csv("data/temp.csv", parse_dates=["datetime"])
temp1.info()

# Import with datetime column as datetime dtype column and new label.
temp2 = pd.read_csv("data/temp.csv", parse_dates={"datetime_new": ["datetime"]})
temp2.info()

# Import with datetime column as datetime dtype index.
temp3 = pd.read_csv("data/temp.csv", parse_dates=True, index_col="datetime")
temp3.info()

# Import with datetime column as datetime dtype index and new label.
temp4 = pd.read_csv(
    "data/temp.csv",
    parse_dates={"datetime_new": ["datetime"]},
    index_col="datetime_new",
)
temp4.info()

pd.to_datetime("20201206")  # Timestamp('2020-12-06 00:00:00')
pd.to_datetime("2020/12/06")  # Timestamp('2020-12-06 00:00:00')
pd.to_datetime("2020-12-06")  # Timestamp('2020-12-06 00:00:00')

pd.to_datetime("201206")  # Timestamp('2006-12-20 00:00:00')
pd.to_datetime("20/12/06")  # Timestamp('2006-12-20 00:00:00')
pd.to_datetime("20-12-06")  # Timestamp('2006-12-20 00:00:00')

pd.to_datetime("06-12-24")  # Timestamp('2024-06-12 00:00:00')
pd.to_datetime("12-24-06")  # Timestamp('2006-12-24 00:00:00')
pd.to_datetime("24-06-12")  # Timestamp('2012-06-24 00:00:00')
