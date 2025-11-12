import matplotlib.pyplot as plt
import pandas as pd


plt.style.use("seaborn")

titanic = pd.read_csv("data/titanic.csv")


titanic["age"].plot(
    kind="hist",
    bins=80,
    density=False,
    cumulative=False,
)
plt.ylabel(None)  # In this way ylabel 'Frequency' is created automatically.


titanic["age"].hist(
    bins=80,
    density=False,
    cumulative=False,
)


plt.hist(
    x=titanic["age"],
    bins=80,
    density=False,
    cumulative=False,
)
