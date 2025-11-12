import matplotlib.pyplot as plt
import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

# Data frame plotting.
titanic.plot(subplots=True, figsize=(12, 8), sharex=False)
titanic["age"].plot(figsize=(12, 8))
plt.show()

plt.style.available  # Predefined available styles
plt.style.use("classic")  # Style selection.

xticks = range(0, 901, 50)
yticks = range(0, 81, 5)

# Series plotting.
titanic["age"].plot(
    figsize=(12, 8),
    fontsize=13,
    c="r",
    ls="--",
    xlim=[0, 900],
    ylim=[0, 80],
    xticks=xticks,
    yticks=yticks,
    rot=30,
)
plt.title(label="Titanic - Ages", fontsize=15)
plt.legend(loc="best", fontsize=15)
plt.xlabel(xlabel="Passenger No", fontsize=13)
plt.ylabel(ylabel="Age", fontsize=13)
plt.grid()
plt.show()  # Necessary during running. Unnecessary during executing with console or debbuging.
