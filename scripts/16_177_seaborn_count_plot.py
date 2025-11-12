import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


titanic = pd.read_csv("data/titanic.csv")
titanic["pclass"] = titanic["pclass"].astype(str)  # Due to error.

plt.figure(figsize=(12, 8))
# sns.countplot(data=titanic, x='sex')
# sns.countplot(data=titanic, y='sex')
sns.countplot(data=titanic, x="sex", hue="pclass")
plt.show()
