import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# .csv file inspection.
# 1. Data set does not contain column names.  # TODO (1) Add column names.
# 2. Data set starts from 3rd row.  # TODO (2) Skip first 3 rows.
# 3. Last 2 rows are unnecessary.  # TODO (3) Skip last 2 rows.

col_names = [
    "Survived",
    "Class",
    "Gender",
    "Age",
    "SipSp",
    "ParCh",
    "Fare",
    "Emb",
    "Deck",
]  # (1)
titanic = pd.read_csv(
    filepath_or_buffer="data/titanic.csv",
    skiprows=3,  # (2)
    skipfooter=2,  # (3)
    header=None,  # (3)
    names=col_names,  # (1)
)
pd.set_option("display.width", None)

# Check the first rows.
titanic.head()
# Looks good, but column 'Fare' has a dollar prefix. # TODO (4) Delete prefix and change dtype.
# Check the last rows.
titanic.tail()
# Looks good.
# Check data types and compare them with our expectations.
titanic.info()
# Column's dtypes ['Survived', 'Age', 'Fare'] do not meet our expectations.  # TODO (5) Change.
# Check reason-ability of numerical columns.
titanic.describe()
# Numerical columns look reasonable.
# Check reason-ability of nonnumerical columns.
titanic.describe(exclude=[np.number])
# 'Survived' column contains 4 unique value,
# expected 2 [0, 1] - inconsistency.  # TODO (6) Replace.
# Detection of missing values.
titanic.columns[titanic.isna().any()]
# Missing values in columns ['Age', 'Emb', 'Deck'].  # TODO (7) Check and decide what to do (a. leave, b. drop, c. replace).


titanic.Fare = titanic.Fare.str.replace(pat="$", repl="")  # (4.1) 1st method.
# titanic.Fare = titanic.Fare.str.removeprefix(prefix='$')  # (4.1) 2nd method.
# titanic.Fare = titanic.Fare.str.lstrip(to_strip='$')  # (4.1) 3rd method.

titanic.Fare = pd.to_numeric(titanic.Fare)  # (4.2) 1st method.
# titanic.Fare.astype(dtype='float')  # (4.2) 2nd method.

titanic.Survived.value_counts()  # (6)
titanic.Survived.replace(to_replace={"yes": 1, "no": 0}, inplace=True)  # (6)
titanic.Survived = pd.to_numeric(titanic.Survived)  # (5)

titanic.Age.value_counts(dropna=False)  # (5)
titanic.Age.replace(to_replace={"Missing Data": np.nan}, inplace=True)  # (5)
titanic.Age.describe()  # (5)
titanic.Age = pd.to_numeric(titanic.Age)  # (5)
titanic.Age.nlargest()  # (5) After the change, values that are suspicious are exposed. TODO (8) Check and decide what to do.

titanic.drop(
    columns="Deck", inplace=True
)  # (7) That column might not be really helpful, only 203 non-null values.

nan_ages_idx = titanic.loc[
    titanic.Age.isna()
].index  # (7) Catch idx for rows to replace.
titanic.loc[nan_ages_idx]  # (7) Display.
titanic.Age.fillna(
    value=round(titanic.Age.mean(), 1), inplace=True
)  # (7) Replace with mean or median.

# Duplicates handling.
titanic.duplicated(keep="first").sum()
titanic[titanic.duplicated(keep="first")]
# There is no chance to find duplicates based on present columns.
# But it is known that last three rows are duplicated (based on deeper research). TODO (9) Remove last 3 rows.
titanic.drop(index=titanic.index[-3:], inplace=True)  # (9)

idx_outl = titanic.loc[titanic.Age > 90].index  # (8)
titanic.loc[idx_outl, "Age"] = titanic.loc[titanic.Age > 90, "Age"] / 10  # (8)
titanic.loc[idx_outl]  # (8)
titanic.loc[217, "Age"] = 42  # (8)

titanic.boxplot("Age")  # (8)
plt.show()  # (8)

titanic.Age.plot()  # (8)
plt.show()  # (8)

# Check if there are column to categorize.
ctg = titanic.dtypes.to_frame(name="type").join(
    titanic.nunique().rename(index="nuniq", inplace=True)
)
col_to_ctg = ctg.loc[
    (ctg.type == "object") & (ctg.nuniq < 100)
].index  # TODO (10) Change dtypes to 'category'.
titanic.loc[:, col_to_ctg] = titanic.loc[:, col_to_ctg].astype("category")  # (10)
titanic.info()

# Back to start and repeat first steps...
