import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


titanic = pd.read_csv("data/titanic.csv")
titanic["pclass"] = titanic["pclass"].astype(str)  # Due to error.

plt.figure(figsize=(12, 8))

# sns.stripplot(data=titanic, x='sex', y='age', jitter=False)
# sns.stripplot(data=titanic, x='sex', y='age', jitter=True)
# sns.stripplot(data=titanic, x='sex', y='age', jitter=True, hue='pclass')
# sns.stripplot(data=titanic, x='sex', y='age', jitter=True, hue='pclass', dodge=True)

# sns.swarmplot(data=titanic, x='sex', y='age', hue='pclass', dodge=True)

# sns.barplot(data=titanic, x='sex', y='age', hue='pclass', dodge=True)

sns.pointplot(data=titanic, x="sex", y="age", hue="pclass", dodge=True)

plt.show()
