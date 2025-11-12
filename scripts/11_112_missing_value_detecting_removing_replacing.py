import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


titanic = pd.read_csv("data/titanic.csv")

# 1st method.
titanic.info()

# 2nd group of methods.
titanic.isna().any()
titanic.isna().all()
titanic.isna().sum()

# Displaying number of na values.
titanic.isna().any(axis=1)
titanic.loc[titanic.isna().any(axis=1)]

# Detection of columns or rows with any missing values.
titanic.columns[titanic.isna().any()]
titanic.index[titanic.isna().any(axis=1)]

# Graphical method, very useful.
plt.figure()
sns.heatmap(~titanic.isna())
plt.show()

# Removing.
titanic.dropna()
titanic.dropna(axis=1)

titanic.dropna(axis=0, how="any").shape
titanic.dropna(axis=1, how="any").shape
titanic.dropna(axis=0, how="all").shape
titanic.dropna(axis=1, how="all").shape

titanic.dropna(axis=0, thresh=8).shape
titanic.dropna(axis=1, thresh=204).shape

titanic.dropna(axis=0, subset=["sex", "age", "parch"]).shape

# Replacing.
titanic.age.fillna(value=round(titanic.age.mean(), 1), inplace=True)
