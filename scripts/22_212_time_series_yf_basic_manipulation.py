import pandas as pd
import yfinance as yf


ticker = ["AAPL", "BA", "KO", "IBM", "DIS", "MSFT"]
yf.download("AAPL", start="2010-01-01", end="2019-02-06")
stocks = yf.download(ticker, start="2010-01-01", end="2019-02-06")
stocks.info()
stocks.to_csv("data/stocks.csv")
pd.read_csv("data/stocks.csv")  # Very messy data with any additional parameters.
stocks = pd.read_csv(
    "data/stocks.csv",
    header=[0, 1],
    parse_dates=True,
    index_col=0,
)
# MultiIndex -> Index.
stocks.columns.to_flat_index()
stocks.columns = stocks.columns.to_flat_index()
# Index -> MultiIndex.
pd.MultiIndex.from_tuples(stocks.columns)
stocks.columns = pd.MultiIndex.from_tuples(stocks.columns)
# Levels swapping.
stocks.swaplevel(axis=1)
stocks.swaplevel(axis=1).sort_index(axis=1)
stocks = stocks.swaplevel(axis=1).sort_index(axis=1)
