import pandas as pd


topfive_2004 = pd.read_csv("data/topfive_2004.csv", index_col="Athlete")
topfive_2008 = pd.read_csv("data/topfive_2008.csv", index_col="Athlete")

topfive_2004 + topfive_2008

topfive_2004.add(topfive_2008)
topfive_2004.add(topfive_2008, axis=0)
topfive_2004.add(topfive_2008, fill_value=0)

topfive_2008.rename(columns={"bronze": "Bronze"}, inplace=True)
topfive_2004.add(topfive_2008, fill_value=0)
topfive_2004.add(topfive_2008, fill_value=0).sort_values(
    by=topfive_2004.columns.tolist(), ascending=False
)

topfive_2004.sub(topfive_2008, fill_value=0)
