# https://pandas.pydata.org/docs/user_guide/advanced.html

import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

titanic.head()
titanic.columns
titanic.columns[0]
titanic.columns[0] = "alive"  # Erroneous for Index., immutable.
titanic.columns = [
    "Alive",
    "Class",
    "Sex",
    "Age",
    "SibSp",
    "ParChi",
    "Fare",
    "Emb",
    "Deck",
]
# Column and index names are equal to None.
titanic.head()
titanic.columns.name
titanic.index.name
titanic.columns.name = "Pass_Charact"
titanic.index.name = "Pass_Number"
titanic.head()

summer = pd.read_csv("data/summer.csv", index_col="Athlete")

summer.head()
summer.index[0]
summer.index[0] = "MALYSZ, Adam"  # Illegal operation.
summer.info()
summer.dtypes

# Renaming index or column labels,
summer.rename(mapper={"HAJOS, Alfred": "MALYSZ, Adam"}, axis="index")
summer.rename(
    mapper={"Year": "Edition"}, axis="columns"
)  # Axis must be specifed if want to rename column labels.

# Alternative way, simpler.
summer.rename(
    index={"HAJOS, Alfred": "MALYSZ, Adam", "HERSCHMANN, Otto": "MATEJA, Robert"},
    inplace=True,
)  # Parameter 'index' instead of pair 'mapper' & 'axis'.
summer.rename(
    columns={"Year": "Edition", "City": "Town"}, inplace=True
)  # Parameter 'columns' instead of pair 'mapper' & 'axis'.
