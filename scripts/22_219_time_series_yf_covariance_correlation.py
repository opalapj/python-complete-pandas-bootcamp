import pandas as pd
import seaborn as sns


stocks = pd.read_csv("data/stocks.csv", header=[0, 1], parse_dates=True, index_col=0)

close = stocks.loc[:, "Close"].copy()
norm = close.div(close.iloc[0]).mul(100)
ret = close.pct_change().dropna()

ret.cov()
ret.corr()

sns.heatmap(ret.corr())
sns.heatmap(ret.corr(), cmap="Reds", annot=True, annot_kws={"size": 15}, vmax=0.6)
