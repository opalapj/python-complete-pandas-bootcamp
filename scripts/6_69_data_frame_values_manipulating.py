# https://pandas.pydata.org/docs/user_guide/copy_on_write.html#migrating-to-copy-on-write

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.head()

# Changing single value with iloc.
titanic.iloc[2, 3] = 9

# Changing single value with loc.
titanic.loc[2, "age"] = 7

# Changing multiple value in column with iloc.
titanic.iloc[:2, 3] = 27
titanic.iloc[[0, 2, 4], 3] = 69
index_babies = titanic.iloc[
    (titanic.iloc[:, 3] < 1).to_list(), 3
].index  # Mask for for data selecting with iloc cannot be a series (must be converted to list).
titanic.iloc[titanic.iloc[:, 3] < 1, 3] = (
    1  # Mask for data manipulating with iloc can be a series.
)
titanic.iloc[index_babies]

# Changing multiple value in column with loc.
titanic.loc[3:4, "age"] = 18
titanic.loc[[1, 3], "age"] = 44
index_babies = titanic.loc[
    titanic["age"] < 1, "age"
].index  # Check for next line operation.
titanic.loc[titanic["age"] < 1, "age"] = 1
titanic.iloc[index_babies]

# Changing multiple value in row with iloc.
titanic.iloc[2, 0:3] = [0, 1, "male"]

# Changing multiple value in row with loc.
titanic.loc[2, "survived":"sex"] = [1, 0, "female"]

# Changing multiple value in multiple rows/columns with replace.
titanic.replace(0, "zero")
