import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


stocks = pd.read_csv("data/stocks.csv", header=[0, 1], parse_dates=True, index_col=0)

stocks.swaplevel(axis=1).loc[:, "BA"]
stocks.loc[:, "Close"]
close = stocks.loc[:, "Close"].copy()
close.div(close.iloc[0]).mul(100)

norm = close.div(close.iloc[0]).mul(100)
norm.plot()

ret = close.pct_change().dropna()

summary = ret.describe().T[["mean", "std"]]
summary["mean"] = summary["mean"].mul(252)
summary["std"] = summary["std"].mul(np.sqrt(252))
fig, ax = plt.subplots()
summary.plot(kind="scatter", x="std", y="mean", ax=ax)
plt.xlabel("ann. Risk(std)")
plt.ylabel("ann. Return")
plt.title("Risk/Return")
for i in summary.index:
    plt.annotate(i, xy=(summary.loc[i, "std"] + 0.002, summary.loc[i, "mean"] + 0.002))
