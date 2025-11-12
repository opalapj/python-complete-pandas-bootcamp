import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


titanic = pd.read_csv("data/titanic.csv")

ct = pd.crosstab(titanic["sex"], titanic["pclass"])

plt.figure()

# sns.heatmap(ct)
# sns.heatmap(ct, annot=True, fmt='d')
# sns.heatmap(ct, annot=True, fmt='d', cmap='Reds')
sns.heatmap(ct, annot=True, fmt="d", cmap="Reds", vmax=150)

plt.show()
