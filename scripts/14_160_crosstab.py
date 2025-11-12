import pandas as pd


titanic = pd.read_csv("data/titanic.csv")
summer = pd.read_csv("data/summer.csv")

pd.crosstab(titanic.sex, titanic.pclass)
pd.crosstab(titanic.sex, titanic.pclass, margins=True)
pd.crosstab(titanic.sex, titanic.pclass, margins=True, normalize=True)

pd.crosstab(titanic.pclass, titanic.sex, titanic.age, aggfunc="mean")

pd.crosstab(
    [titanic.pclass, titanic.survived], titanic.sex, titanic.age, aggfunc="mean"
)
pd.crosstab(
    [titanic.pclass, titanic.survived],
    titanic.sex,
    titanic.age,
    aggfunc="mean",
    rownames=["idx0", "idx1"],
    colnames=["col"],
)

pd.pivot_table(titanic, index=["pclass", "survived"], columns="sex", values="age")

pd.crosstab(
    index=[summer.Year, summer.Country],
    columns=summer.Medal,
    aggfunc="count",
    values=summer.Athlete,
    margins=True,
).fillna(0)
