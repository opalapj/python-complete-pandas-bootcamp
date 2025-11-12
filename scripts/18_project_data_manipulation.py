import numpy as np
import pandas as pd


# Input data. Aggregation of summer DataFrame to match wik_1976 and wik_1996 DataFrames.
summer = pd.read_csv("data/summer.csv")
wik_1976 = pd.read_csv("data/wik_1976.csv")
wik_1996 = pd.read_csv("data/wik_1996.csv")

badminton_mixed = [
    21773,
    21782,
    21776,
    21785,
    21770,
    21779,
    23703,
    23712,
    23706,
    23715,
    23709,
    23700,
    25720,
    25729,
    25723,
    25732,
    25726,
    25717,
    27727,
    27736,
    27730,
    27739,
    27724,
    27733,
    29784,
    29785,
    29786,
    29787,
    29788,
    29789,
]
pd.options.display.width = None

# TODO (1) Inspecting DataFrames.
summer.head()
summer.tail()
summer.describe()
summer.describe(exclude=[np.number])  # 4 nulls for Country column.
summer.info()
summer.columns[summer.isna().any()]
summer.loc[summer.isna().any(axis=1), :]

# What is important at the beginning are the columns with the country code and medals.
wik_1976 = wik_1976.iloc[:-1, 1:5]
wik_1976["Country"] = (
    wik_1976["NOC"].str.split("(", expand=True).iloc[:, 1].apply(lambda x: x[:3])
)
wik_1976 = wik_1976.drop(columns=["NOC"]).set_index("Country")
wik_1996 = wik_1996.iloc[:-1, 1:5]
wik_1996["Country"] = (
    wik_1996["Nation"].str.split("(", expand=True).iloc[:, 1].apply(lambda x: x[:3])
)
wik_1996 = wik_1996.drop(columns=["Nation"]).set_index("Country")

# TODO (2) Identifying event gender.
# Assume that the following medals have been awarded in Mixed Events:
summer["Event_Gender"] = summer["Gender"]
# 1. the Event is marked with "mixed" or "pairs",
mask_1 = summer["Event"].str.contains("mixed|pairs", case=False)
# 2. all "Equestrian" Events,
mask_2 = summer["Sport"].str.contains("equestrian", case=False)
# 3. all "Sailing" Events before 1988 (until and including 1984),
mask_3 = (summer["Sport"].str.contains("sailing", case=False)) & (summer["Year"] < 1988)
# 4. medals (index labels) were awarded in Badminton mixed Double Events:
mask_4 = pd.Series(summer.index.isin(badminton_mixed))
summer.loc[mask_1 | mask_2 | mask_3 | mask_4, "Event_Gender"] = "Mix"
summer["Event_Gender"].value_counts()

# TODO (3) Counting medals for each unique event.
summer["Event_Medals"] = summer.groupby(
    ["Year", "Sport", "Discipline", "Event", "Event_Gender"]
)["Medal"].transform("count")
summer["Event_Medals"].value_counts().sort_index()

# TODO (4) Identifying team events.
summer["Event_Category"] = pd.Series(
    np.where(summer["Event_Medals"] > 5, "Team", "Individual")
)
summer["Event_Category"].value_counts()
# summer.loc[(summer['Event_Gender'] == 'Mix') & (summer['Event_Category'] == 'Individual')]  # There is still error.

# TODO (5) Removing duplications in team events.

individual = summer.loc[summer["Event_Category"] == "Individual"].copy()
team = summer.loc[summer["Event_Category"] == "Team"].copy()
team.drop_duplicates(
    ["Year", "Sport", "Discipline", "Country", "Event", "Medal", "Event_Gender"],
    inplace=True,
)
summer_new = pd.concat([individual, team])

# TODO (6) Aggregation.
sort_columns = ["Year", "Gold", "Silver", "Bronze", "Country"]
sort_logic = [True, False, False, False, True]
medal_table = summer_new.pivot_table(
    values="Sport",
    index=["Year", "Country"],
    columns="Medal",
    aggfunc="count",
    fill_value=0,
)[sort_columns[1:-1]]
medal_table.sort_values(sort_columns, ascending=sort_logic, inplace=True)

# TODO (7) Testing for 1976 & 1996.

medal_table.loc[1976].sub(
    wik_1976
)  # Subtraction ignores row and column order. Operates on index and header.
medal_table.loc[1976].sub(wik_1976).abs().sum()
medal_table.loc[1976].sub(wik_1976).abs().sum().sum()
medal_table.loc[1976].equals(
    wik_1976
)  # Equals does not ignore row and column order. Furthermore, compare axes' names.

t2 = wik_1976.rename_axis(columns="Medal").sort_values(
    sort_columns[1:], ascending=sort_logic[1:]
)
medal_table.loc[1976].equals(t2)

medal_table.loc[1996].sub(wik_1996).abs().sum().sum()
