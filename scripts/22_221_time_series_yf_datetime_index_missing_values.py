import pandas as pd


stocks = pd.read_csv("data/stocks.csv", header=[0, 1], parse_dates=True, index_col=0)
close = stocks.loc[:, "Close"].copy()
close["Day"] = close.index.day_name("Polish_Poland")
close["Quarter"] = close.index.quarter
close.head(10)
all_days = pd.date_range("2009-12-31", "2019-02-06", freq="D")

# 1st method - fillna()
close = close.reindex(all_days)
close["Day"] = close.index.day_name("Polish_Poland")
close["Quarter"] = close.index.quarter
close.fillna(method="backfill")  # FutureWarning
close.bfill()
close.ffill()

# 2nd method - during reindexing
# Filling while reindexing does not look at dataframe values, but only compares the original and desired indexes.
close.loc[:, "AAPL":"MSFT"].reindex(all_days, method="bfill")
close.loc[:, "AAPL":"MSFT"].reindex(all_days, method="ffill")
close.loc[:, "AAPL":"MSFT"].reindex(all_days, method="nearest")  #
close = close.loc[:, "AAPL":"MSFT"].reindex(all_days, method="nearest")
close["Day"] = close.index.day_name("Polish_Poland")
close["Quarter"] = close.index.quarter

# Interpolation.
temp = pd.read_csv(
    r"D:\Dane\opalapi\data\programming\study\python\udemy\complete_pandas_bootcamp\Course_Materials_ALL\Course_Materials_Part4\Video_Lecture_NBs\temp.csv",
    parse_dates=True,
    index_col="datetime",
)
temp.resample("30min")
temp.resample("30min").asfreq()  # Upsampling without aggregation.
temp.asfreq("30min")  # Upsampling.
temp.resample("30min").interpolate()
