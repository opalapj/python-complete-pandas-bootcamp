import matplotlib.pyplot as plt
import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

plt.figure()
titanic["fare"].plot()
plt.show()

titanic["fare"].sort_values(ascending=False).head(20)
fare_cap = 250
titanic.loc[titanic["fare"] > fare_cap, "fare"]
titanic.loc[titanic["fare"] > fare_cap, "fare"] = fare_cap

titanic["fare"].sort_values(ascending=True).head(20)
fare_floor = 5
titanic.loc[titanic["fare"] < fare_floor, "fare"]
titanic.loc[titanic["fare"] < fare_floor, "fare"] = fare_floor
