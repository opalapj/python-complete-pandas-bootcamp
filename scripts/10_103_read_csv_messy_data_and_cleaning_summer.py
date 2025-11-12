import numpy as np
import pandas as pd


# .csv file inspection.
summer = pd.read_csv("data/summer_imp.csv")
pd.set_option("expand_frame_repr", False)

# Check the first rows.
summer.head()
# Looks good, but name of one column ('Athlete Name') has space,
# what is bad idea. Strings contain white spaces and some of names
# are lower case.
# TODO (1) Change column name, delete prefix and suffix (white spaces),
#  switch names to upper case.
# Check the last rows.
summer.tail()
# Looks good.
# Check data types and compare them with our expectations.
summer.info()
# Looks good.
# Check reason-ability of numerical columns.
summer.describe()
# Numerical columns look reasonable.
# Check reason-ability of nonnumerical columns.
summer.describe(exclude=[np.number])
# 4 missing values in 'Country' column.  # TODO (2) Check.
# 4 unique values in 'Medal' column.  # TODO (3) Check and replace.
# Detection of missing values.
summer.columns[summer.isna().any()]
# Missing values in column 'Country'.  # TODO (2) Check and decide what to do (a. leave, b. drop, c. replace)


summer.rename(columns={"Athlete Name": "Athlete_Name"}, inplace=True)  # (1.1)
summer.loc[
    summer.Athlete_Name.str.endswith(" ") & summer.Athlete_Name.str.startswith(" ")
]  # (1.2)
summer.Athlete_Name = summer.Athlete_Name.str.strip()  # (1.2)
summer.Athlete_Name = summer.Athlete_Name.str.title()  # (1.3) Switch all to title case.
# summer.Athlete_Name.str.split(pat=',', expand=True).iloc[:, 0].str.upper().str.cat(summer.Athlete_Name.str.split(pat=',', expand=True).iloc[:, 1], sep=',')  # (1.3) Switch last name to upper case.

summer.loc[pd.isna(summer.Country)]  # (2) Displaying rows with missing values.
summer.loc[summer.isna().any(axis=1)]  # (2) Displaying rows with missing values.
summer.dropna(
    inplace=True
)  # (2) These rows are not useful, even Athlete_Name are unknown.

summer.Medal.value_counts()  # (3)
summer.loc[summer.Medal == "Gold Medal"]  # (3)
summer.Medal.replace(to_replace={"Gold Medal": "Gold"}, inplace=True)  # (3)

# Duplicates handling.
# 1st check for all columns.
summer.loc[summer.duplicated(keep=False)]
# 7 pairs of duplicated rows are present, but only 5 are real duplicates. TODO (4) Remove unnecessary duplictaes.
summer.drop(index=[2069, 12253, 15596, 21833, 28678], inplace=True)  # (4)

# My own extra check.
subset = ["Year", "Athlete_Name", "Event"]
summer[summer.duplicated(keep=False, subset=subset)].sort_values(by=subset).tail(20)
summer[summer.duplicated(keep=False, subset=subset)].sort_values(by=subset).head(20)

# Check if there are column to categorize.
ctg = summer.dtypes.to_frame(name="type").join(
    summer.nunique().rename(index="nuniq", inplace=True)
)
col_to_ctg = ctg.loc[
    (ctg.type == "object") & (ctg.nuniq < 100)
].index  # TODO (5) Change dtypes to 'category'.
summer.loc[:, col_to_ctg] = summer.loc[:, col_to_ctg].astype("category")  # (5)
summer.info()  # (5)

# Back to start and repeat first steps...
