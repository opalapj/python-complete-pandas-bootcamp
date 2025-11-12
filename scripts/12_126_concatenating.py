import pandas as pd


men2004 = pd.read_csv("data/men2004.csv")
men2008 = pd.read_csv("data/men2008.csv")

# Concatenating data frames with the same column labels.
men0408 = pd.concat(
    objs=[men2004, men2008], ignore_index=False, keys=[2004, 2008], names=["Year"]
)
men0408.reset_index().drop(columns="level_1")

# Concatenating data frames with different column labels.
men2004 = pd.read_csv("data/men2004.csv")
men2008 = pd.read_csv("data/men2008.csv")

men2004.columns = ["Name", "Medals"]
men2004["Success"] = "Yes"

pd.concat(objs=[men2004, men2008], keys=[2004, 2008], names=["Year"])

men2004.drop(columns="Success", inplace=True)  # Removing unnecessary column.
men2008.columns = men2004.columns  # Inheriting column labels from other dataframe

pd.concat(objs=[men2004, men2008], keys=[2004, 2008], names=["Year"])
