import pandas as pd


temp = pd.read_csv("data/temp.csv", parse_dates=True, index_col="datetime")

temp.info()

resample = temp.resample("D")
resample = temp.resample("D", closed="right", label="right")
list(resample)[0]

resample = temp.resample("M")
resample = temp.resample("MS")
list(resample)[0]
list(resample)[1]
resample.mean()

resample = temp.resample("Q")
list(resample)[0]
list(resample)[1]
resample.mean()

resample = temp.resample("Y")
list(resample)[0]
list(resample)[1]
resample.mean()

resample = temp.resample("M", offset="14D")
list(resample)[0]
list(resample)[1]
resample.mean()

# Much more with better explanation in resample_poland_2023.py.

# Converting result index to PeriodIndex.
temp.resample("M", kind="period").mean()
temp.resample("W", kind="period").mean()
temp.resample("Q", kind="period").mean()
temp.resample("A", kind="period").mean()

temp_m = temp.resample("M", kind="period").mean()
temp.info()  # DatetimeIndex
temp_m.info()  # PeriodIndex
temp.plot()
temp_m.plot()
