import pandas as pd


stocks = pd.read_csv("data/stocks.csv", header=[0, 1], parse_dates=True, index_col=0)

aapl = stocks.loc[:, ("Close", "AAPL")]  # Creating series...
aapl = aapl.to_frame()  # ...and converting to DataFrame...

aapl = stocks.loc[:, [("Close", "AAPL")]].droplevel(
    1, axis=1
)  # ...or using square brackets.

aapl["lag1"] = aapl.shift(periods=1)
aapl["diff1"] = aapl["Close"].sub(aapl["lag1"])
aapl["return1"] = aapl["Close"].div(aapl["lag1"]).sub(1).mul(100)
aapl["diff2"] = aapl["Close"].diff(periods=1)
aapl["return2"] = aapl["Close"].pct_change(periods=1).mul(100)
