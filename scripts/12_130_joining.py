import pandas as pd


men2004 = pd.read_csv("data/men2004.csv")
men2008 = pd.read_csv("data/men2008.csv")

# Joining on columns with the same names.
men2004.merge(men2008, on="Athlete")
men2004.merge(
    men2008, on="Athlete", how="outer", indicator=True, suffixes=("_2004", "_2008")
)  # As Data Frame instance method df.merge.
pd.merge(
    men2004,
    men2008,
    on="Athlete",
    how="outer",
    indicator=True,
    suffixes=("_2004", "_2008"),
)  # As general module method pd.merge.
men2004.merge(men2008, how="cross")

men0408 = men2004.merge(
    men2008, on="Athlete", how="outer", indicator=True, suffixes=("_2004", "_2008")
)
men0408._merge.value_counts()

# Joining on columns with different names.
men2004.rename(columns={"Athlete": "Name"}, inplace=True)
men0408 = men2004.merge(
    men2008,
    left_on="Name",
    right_on="Athlete",
    how="outer",
    indicator=True,
    suffixes=("_2004", "_2008"),
)
men0408.Name.fillna(men0408.Athlete, inplace=True)
men0408.drop(columns=["Athlete", "_merge"], inplace=True)

# Joining on column and index with different names.
men2008.set_index("Athlete", inplace=True)
men0408 = men2004.merge(
    men2008,
    left_on="Name",
    right_index=True,
    how="outer",
    indicator=True,
    suffixes=("_2004", "_2008"),
)

# Joining on multiple columns with the same names.
men2004_det = pd.read_csv("data/men2004_det.csv")
men2008_det = pd.read_csv("data/men2008_det.csv")

men0408_det = men2004_det.merge(men2008_det, on="Athlete")
men0408_det.loc[men0408_det["Athlete"] == "PHELPS, Michael"]
men0408_det = men2004_det.merge(men2008_det, on=["Athlete", "Medal"])
men0408_det.loc[men0408_det["Athlete"] == "PHELPS, Michael"]
