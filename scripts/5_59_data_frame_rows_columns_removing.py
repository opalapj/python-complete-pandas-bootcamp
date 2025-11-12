# https://pandas.pydata.org/docs/user_guide/basics.html#dropping-labels-from-an-axis

import pandas as pd


summer = pd.read_csv("data/summer.csv")

summer.head()

# Removing columns.
# 1st way.
summer.pop("Year")
summer.pop(["Year", "City"])  # Illegal for multiple selection.

# 2nd way.
summer.drop(columns="Year", inplace=True)
summer.drop(columns=["Year", "City"], inplace=True)
summer.drop(columns=["Year", "City"], inplace=True, errors="ignore")

# 3rd way.
del summer["Year"]

# Removing rows.
# 1st way.
summer.drop(index=1900, inplace=True)
w1 = summer.drop(index=[1904, 2040], errors="ignore")

# 2nd way.
to_remove = summer.index.isin([1904, 2040])
w2 = summer.loc[~to_remove]

w1.equals(w2)

# Check.
w1.index.isin([1904]).any()
1904 in w1.index
