# https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.loc[:, "age"]
type(titanic.loc[:, "age"])
age = titanic.loc[:, "age"]

titanic.dtypes
age.dtype
age.dtypes
age.index
age.info()
f = age.to_frame()

age.describe()
age.count()
age.size
age.sum()
sum(age)  # Don't know how to avoid NaN values.
age.min()
age.mean()
age.unique()
len(age.unique())
age.nunique()
age.nunique(dropna=False)
age.value_counts()
age.value_counts(sort=False)
age.value_counts(dropna=False)
age.value_counts(ascending=True)
age.value_counts(normalize=True)
age.value_counts(bins=5)
age.value_counts(normalize=True, bins=5)

b = titanic["fare"]
b = titanic["fare"].value_counts()
b = titanic["fare"].value_counts().index[0]  # Most common ticket price.
