import matplotlib.pyplot as plt
import pandas as pd


plt.style.use("seaborn")

titanic = pd.read_csv("data/titanic.csv")

titanic.plot(
    kind="scatter",
    figsize=(15, 8),
    x="age",
    y="fare",
    # c='r',
    c="pclass",
    colormap="viridis",
    marker="x",
    # s=30,
    s="fare",
)
