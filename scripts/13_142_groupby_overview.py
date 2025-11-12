import pandas as pd


titanic = pd.read_csv("data/titanic.csv")
titanic_slice = titanic.iloc[:10, [2, 3]]

# Very interesting thing: mean aggregation is erroneous after groupby copy of column.
column_view = titanic_slice["sex"]
column_copy = titanic_slice["sex"].copy()
titanic_slice.groupby(column_view).mean()
titanic_slice.groupby(column_copy).mean()  # Illegal.
titanic_slice.groupby(column_copy).mean(numeric_only=True)

# Splitting by column as a single key.
gb0 = titanic_slice.groupby("sex")
gb0.groups
gb0.mean()

for name, subsetted_object in gb0:
    print(name)
    print(subsetted_object)

# Splitting by function as a single key (called on each value of the object’s index).
gb1 = titanic_slice.groupby(by=lambda i: i % 2)
for name, subsetted_object in gb1:
    print(name)
    print(subsetted_object)

# Splitting by column and function as a multiple key.
gb2 = titanic_slice.groupby(by=["sex", lambda i: i % 2])
for name, subsetted_object in gb2:
    print(name)
    print(subsetted_object)

# Splitting whole titanic data set.
gb3 = titanic.groupby("sex")
for name, subsetted_object in gb3:
    print(name)
    print(subsetted_object)

# Splitting only selected columns from whole titanic data set.
gb4 = titanic.groupby("sex")[["age", "fare"]]
for name, subsetted_object in gb4:
    print(name)
    print(subsetted_object)

# Splitting by multiple keys.
summer = pd.read_csv("data/summer.csv")
split = summer.groupby(by=["Country", "Gender"])
split.get_group(("POL", "Men"))
list(split.groups.keys())
