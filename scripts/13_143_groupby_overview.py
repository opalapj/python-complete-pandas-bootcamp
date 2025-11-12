import matplotlib.pyplot as plt
import pandas as pd


plt.style.use("seaborn-v0_8")

titanic = pd.read_csv("data/titanic.csv")

titanic_slice = titanic.iloc[:10, [2, 3]]
split = titanic_slice.groupby("sex")
split.get_group("male")
split.mean()

split = titanic.groupby("sex")[["fare", "age"]]
split.max()
split.all()

split = titanic.groupby("sex")
df_mean = split.mean(numeric_only=True)
df_mean.plot(kind="bar", subplots=True, figsize=(8, 15))
plt.show()

titanic.describe()

titanic.fare.mean()
titanic.groupby("pclass").fare.mean()

titanic.survived.mean()
titanic.groupby("sex").survived.mean()
titanic.groupby("pclass").survived.mean()
titanic.groupby(["sex", "pclass"]).survived.mean()

titanic["ad_ch"] = "adult"
titanic.loc[titanic.age < 18, "ad_ch"] = "child"
titanic.ad_ch.value_counts()
titanic.groupby(["sex", "ad_ch"]).survived.count()
titanic.groupby(["sex", "ad_ch"]).survived.mean()
titanic.groupby(["sex", "ad_ch"]).survived.mean().sort_values(ascending=False)

w_and_c_first = (
    titanic.groupby(["sex", "ad_ch"]).survived.mean().sort_values(ascending=False)
)
w_and_c_first.plot(kind="bar", figsize=(14, 8), fontsize=14)
plt.xlabel("Groups", fontsize=13)
plt.ylabel("Survival Rate", fontsize=13)
plt.title("Titanic Survival Rate by Sex/Age-Groups", fontsize=16)
plt.show()
