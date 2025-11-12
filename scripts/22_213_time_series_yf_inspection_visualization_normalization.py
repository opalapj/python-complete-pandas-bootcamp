import pandas as pd


stocks = pd.read_csv("data/stocks.csv", header=[0, 1], parse_dates=True, index_col=0)

stocks.head()
stocks.tail()
stocks.info()
stocks.describe()
stocks.swaplevel(axis=1).loc[:, "BA"]
stocks.loc[:, "Close"]
close = stocks.loc[:, "Close"].copy()
close.head()
close.plot()

close.div(close.iloc[0]).mul(100)
norm = close.div(close.iloc[0]).mul(100)
norm.plot()
