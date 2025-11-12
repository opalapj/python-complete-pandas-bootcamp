import numpy as np
import pandas as pd


stocks = pd.read_csv("data/stocks.csv", header=[0, 1], parse_dates=True, index_col=0)

aapl = stocks.loc[:, [("Close", "AAPL")]].droplevel(
    1, axis=1
)  # ...or using square brackets.
aapl.info()

ret = aapl.pct_change().dropna()
ret.plot(kind="hist", bins=100)
ret.describe()
ret_mean_daily = ret.mean().mean()
ret_var_daily = ret.var()
ret_std_daily = ret.std()
ret_mean_annual = ret_mean_daily * 252
ret_var_annual = ret_var_daily * 252
ret_std_annual = ret_std_daily * np.sqrt(252)
