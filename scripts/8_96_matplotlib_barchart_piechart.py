import matplotlib.pyplot as plt
import pandas as pd


plt.style.use("seaborn")

summer_2012 = pd.read_csv("data/summer_2012.csv")
summer_2012.set_index("Country", inplace=True)

summer_2012["Medal"].plot(kind="bar", figsize=(12, 8), fontsize=12, rot=45)

summer_2012["Medal"].plot(kind="pie", figsize=(12, 8), fontsize=12, rot=45)
