import pandas as pd


stocks = pd.read_csv("data/stocks.csv", header=[0, 1], parse_dates=True, index_col=0)
close = stocks.loc[:, "Close"].copy()

close.index
close.index.day  # Day of month.
close.index.dayofyear
close.index.dayofweek
close.index.day_name()
close.index.day_name(locale="Polish_Poland")  # import locale -> locale.getlocale()
close.index.month
close.index.month_name()
close.index.month_name(locale="Polish_Poland")
close.index.quarter
close.index.days_in_month
close.index.week  # AttributeError: 'DatetimeIndex' object has no attribute 'week'
close.index.isocalendar().week  # 1st method
close.index.to_period("D").week  # 2nd method
(
    close.index.to_period("D").week.to_series(index=close.index)
    == close.index.isocalendar().week
).all()
