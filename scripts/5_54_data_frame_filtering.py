# https://pandas.pydata.org/docs/user_guide/indexing.html#

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.head()
titanic.sex.head()

# Filtering with single condition.
titanic.sex == "male"  # Boolean mask based on 'sex' column.
mask = titanic.sex == "male"
filter_loc = titanic.loc[mask]
filter_iloc = titanic.iloc[mask]  # Mask for iloc cannot be a series.
filter_iloc = titanic.iloc[mask.to_list()]
filter_iloc.equals(filter_loc)
titanic[mask]  # Direct selecting.
titanic[mask]["age"]
titanic.loc[mask, "age"]  # Prefer to use loc instead of chaining selecting.
titanic_male = titanic.loc[mask]
dtypes_mask = titanic.dtypes == object
titanic.loc[:, dtypes_mask]  # Filter only object type columns.
titanic.loc[:, ~dtypes_mask]  # Filter only non-object type columns (by mask inverting).

titanic.loc[mask, ~dtypes_mask]

# Filtering with multiple conditions and AND (&) operator.
ind_mask1 = titanic.sex == "male"
ind_mask2 = titanic.age > 14
ind_mask = ind_mask1 & ind_mask2
titanic.loc[mask]

needed_columns = ["survived", "sex", "age", "fare", "deck"]
col_mask1 = titanic.columns.isin(needed_columns)
# col_mask1 = [i in needed_columns for i in titanic.columns]
col_mask2 = titanic.dtypes == object
col_mask = col_mask1 & ~col_mask2
titanic.loc[:, col_mask]

filtering_result_and = titanic.loc[ind_mask, col_mask]

# Filtering with multiple conditions and OR (|) operator.
ind_mask1 = titanic.sex == "female"
ind_mask2 = titanic.age <= 14
ind_mask = ind_mask1 | ind_mask2
titanic.loc[mask]

filtering_result_or = titanic.loc[ind_mask, col_mask]
