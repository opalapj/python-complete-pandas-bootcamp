import pandas as pd


titanic = pd.read_csv(
    "data/titanic.csv", usecols=["survived", "pclass", "sex", "age", "fare"]
)

titanic1 = titanic.copy()

# Joining column with mean survived value.
# 1st method - merging.
group_surv_rate = titanic.groupby(["sex", "pclass"]).survived.agg(
    group_surv_rate="mean"
)
titanic = pd.merge(
    titanic, group_surv_rate, how="left", left_on=["sex", "pclass"], right_index=True
)

# 2nd method - transform method.
group_surv_rate1 = titanic1.groupby(["sex", "pclass"]).survived.transform("mean")
titanic1["group_surv_rate"] = group_surv_rate1

titanic.equals(titanic1)

titanic["outliers"] = abs(titanic.survived - titanic.group_surv_rate)
titanic[titanic.outliers > 0.85]

# Transform method used with fillna method.
titanic.groupby(["sex", "pclass"]).age.mean()
titanic.groupby(["sex", "pclass"]).age.transform("mean")
titanic.groupby(["sex", "pclass"]).age.transform("mean").round().astype("int")
titanic.groupby(["sex", "pclass"]).age.transform(
    lambda x: round(x.mean())
)  # More effective way.

titanic["group_mean_age"] = titanic.groupby(["sex", "pclass"]).age.transform(
    lambda x: round(x.mean())
)
titanic.age.fillna(titanic.group_mean_age, inplace=True)
