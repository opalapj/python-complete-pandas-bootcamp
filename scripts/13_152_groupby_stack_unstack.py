import matplotlib.pyplot as plt
import pandas as pd


plt.style.use("seaborn-v0_8")

summer = pd.read_csv("data/summer.csv")

medals_by_country = summer.groupby(["Country", "Medal"]).Medal.count()
medals_by_country.loc["USA"]
medals_by_country.loc[("USA", "Gold")]

# Unstacking.
medals_by_country.unstack(level=1, fill_value=0)
medals_by_country = medals_by_country.unstack(level=1, fill_value=0)
medals_by_country = medals_by_country[["Gold", "Silver", "Bronze"]]
medals_by_country.sort_values(
    by=["Gold", "Silver", "Bronze"], ascending=[False, False, False], inplace=True
)
medals_by_country

# Stacking.
medals_by_country.stack()

medals_by_country.head(10).plot(kind="bar", figsize=(12, 8), fontsize=13)
plt.xlabel("Country", fontsize=13)
plt.ylabel("Medals", fontsize=13)
plt.title("Medals per Country", fontsize=16)
plt.legend(fontsize=15)
plt.show()
