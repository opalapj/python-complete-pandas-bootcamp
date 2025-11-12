import pandas as pd


titanic = pd.read_csv("data/titanic.csv")

# Creating view.
age = titanic.age
age1 = titanic["age"]
age2 = titanic.iloc[:, 3]
age3 = titanic.loc[:, "age"]

age.equals(age1) & age1.equals(age2) & age2.equals(age3)

age._is_view
age1._is_view
age2._is_view
age3._is_view

age[0] = 0
age1[0] = 1
age2[0] = 2
age3[0] = 3

# Creating copy.
age = titanic.age.copy()
age1 = titanic["age"].copy()
age2 = titanic.iloc[:, 3].copy()
age3 = titanic.loc[:, "age"].copy()

age.equals(age1) & age1.equals(age2) & age2.equals(age3)

age._is_view
age1._is_view
age2._is_view
age3._is_view

age[0] = 0
age1[0] = 1
age2[0] = 2
age3[0] = 3
