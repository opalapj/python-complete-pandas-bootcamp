import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


titanic = pd.read_csv("data/titanic.csv")


sns.jointplot(data=titanic, x="age", y="fare")
sns.jointplot(data=titanic, x="age", y="fare", kind="kde")
sns.jointplot(data=titanic, x="age", y="fare", kind="hist")
sns.jointplot(data=titanic, x="age", y="fare", kind="hex")
sns.jointplot(data=titanic, x="age", y="fare", kind="reg")
sns.jointplot(data=titanic, x="age", y="fare", kind="resid")

plt.show()
